from django.contrib import admin
from .models import *

# Register your models here.
class InfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug') # отображаемые параметры модели в панеле
    list_display_links = ('id', 'title') # кликабельные парамаетры
    prepopulated_fields = {"slug" : ("title",)}

class CodesAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'code', 'ident', 'name', 'recycle', 'slug')
    list_display_links = ('id', 'type', 'code', 'ident', 'name')
    list_filter = ('type', 'recycle')
    prepopulated_fields = {"slug" : ("type", "name")}

class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('id', 'name')
    search_fields = ('name', )
    prepopulated_fields = {"slug" : ("name",)}

admin.site.register(Info, InfoAdmin)
admin.site.register(Codes, CodesAdmin)
admin.site.register(Type, TypeAdmin)
