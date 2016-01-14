from django.contrib import admin

from url_shortener.models import ShortUrl

class ShortUrlAdmin(admin.ModelAdmin):
    list_display = ('id', 'long_url')

admin.site.register(ShortUrl, ShortUrlAdmin)