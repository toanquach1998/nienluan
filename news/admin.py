from django.contrib import admin
from .models import News


class NewAdmin(admin.ModelAdmin):
    list_display = ('new_name', 'author_name', 'date_time')


admin.site.register(News, NewAdmin)