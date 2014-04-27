from django.contrib import admin
from models import * 

class UniversityAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'introduction', 'ranking',\
        	      'studentnum', 'fee', 'image', 'apartment',\
        	      'food', 'housing', 'car', 'translink',\
        	      'shopping', 'tourist', 'sports', 'googlemaps')
    list_filter = ('name', 'url', 'introduction', 'ranking',\
        	      'studentnum', 'fee', 'image', 'apartment',\
        	      'food', 'housing', 'car', 'translink',\
        	      'shopping', 'tourist', 'sports', 'googlemaps')
    search_fields = ('name', 'url')

admin.site.register(UniversityInfo, UniversityAdmin)