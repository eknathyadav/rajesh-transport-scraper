
from django.urls import path, include
from . import views
app_name = "main"
urlpatterns = [
    path('', views.main, name="main"),
    path('select-source/', views.selectSource, name="source"),
    path('<str:source_id>/', views.selectTarget, name="target"),
    path('<str:source_id>/select-target/', views.passValue, name="query"),
    path('<str:source_id>/<str:dest_id>/', views.showGraph, name="graph"),
]
