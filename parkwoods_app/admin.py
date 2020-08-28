from django.contrib import admin

# Register your models here.
from .models import Topic, Entry, Standings, Schedule

admin.site.register(Topic)
admin.site.register(Entry)
admin.site.register(Standings)
admin.site.register(Schedule)