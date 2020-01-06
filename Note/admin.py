from django.contrib import admin

from Note.models import Entry, Topic

admin.site.register(Topic)
admin.site.register(Entry)
