from multiprocessing import context
from django.shortcuts import redirect, render
from numpy import source
from .models import Source, Destination
# Create your views here.
import requests
import json
import requests


def main(request):
    sources = Source.objects.all()
    context = {'sources': sources}
    return render(request, 'main/index.html', context)


def selectSource(request):
    if request.method == "GET":
        source_id = request.GET['drop-select']
        return redirect('main:target', source_id)


def selectTarget(request, source_id):

    targets = Destination.objects.filter(source__source_code=source_id)
    context = {'targets': targets,
               'source_id': source_id}
    return render(request, 'main/target.html', context)


def passValue(request, source_id):
    if request.method == "GET":
        dest_id = request.GET['drop-select']
        print(source_id, dest_id)
        return redirect('main:graph', source_id, dest_id)


def showGraph(request, source_id, dest_id):
    source = Source.objects.get(source_code=source_id)
    destination = Destination.objects.filter(dest_code=dest_id)[0]
    d = {}
    for day in range(7, 13):
        url = "https://www.rajeshtransports.in/search/search-list"
        if day < 10:
            day = "0" + str(day)
        payload = "fromStationCode={}&toStationCode={}&onwardDate=2022-06-{}&returnDate=&searchType=&reschedule=0".format(
            source_id, dest_id, str(day))
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest',
            'Origin': 'https://www.rajeshtransports.in',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'Referer': 'https://www.rajeshtransports.in/search/bangalore-to-guntur?fromStationCode=STF3OEX206&toStationCode=ST378E647H&onwardDate=2022-06-07',
            'Connection': 'keep-alive',
            'Cookie': 'recent-search=%5B%22STF3OEX206%22%2C%22ST378E647H%22%2C%222022-06-07%22%5D; ci_session=tgt8ktjstp6o85s7j1g9e8o3pj45jaud; ci_session=b9747tv2al15eksqpvffoepi52b6dlqf'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        json_data = json.loads(response.text)
        try:
            if len(json_data["data"]) == 0:
                d[day] = "Not Available"
            else:
                totalCost = 0
                totalSeats = 0
                for root in json_data["data"]:
                    for seatType in root['stageFare']:
                        totalCost += int(seatType['fare']) * \
                            (int(seatType['availableSeatCount']))
                        totalSeats += int(seatType['availableSeatCount'])
                d[day] = [totalCost//totalSeats, totalSeats]
        except:
            d[day] = "Not Available"
    print(d)
    context = {"fetchData": d,
               'source': source,
               'destination': destination
               }
    return render(request, 'main/graph.html', context)
