from django.contrib import admin
from url_shortning.models import URLData , ShortURLAnalytics
# Register your models here.
class URLDataAdmin(admin.ModelAdmin):
	list_display = ['id', 'targetURL' , 'shortenURL' , 'dateCreated' , 'dateExpired' , 'status' , 'shortURLbase']	

class ShortURLAnalyticsAdmin(admin.ModelAdmin):
	list_display = ['id' ,'URLid' ,'targetURL' , 'shortenURL' , 'IPAddr' , 'count_of_hits']	

admin.site.register(URLData , URLDataAdmin)
admin.site.register(ShortURLAnalytics , ShortURLAnalyticsAdmin)