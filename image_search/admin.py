from django.contrib import admin

from image_search.models import Search

class SearchAdmin(admin.ModelAdmin):
    list_display = ('id', 'terms')

admin.site.register(Search, SearchAdmin)