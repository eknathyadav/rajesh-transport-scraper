from django.contrib import admin

# Register your models here.
from .models import Source, Destination
# ...
admin.site.register(Source)
admin.site.register(Destination)
