from django.contrib import admin

from app_one.models import Topic,WebPage,AccessRecord

admin.site.register(Topic)
admin.site.register(WebPage)
admin.site.register(AccessRecord)
