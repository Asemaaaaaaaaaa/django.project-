from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *
class BooksAdmin(admin.ModelAdmin):
    list_display = ('id','title','get_html_photo')
    list_display_links = ('id','title')
    search_fields = ('title' , 'author')
    fields = ('title','author','description','price','photo','get_html_photo')
    readonly_fields = ('get_html_photo',)
    save_on_top = True

    def get_html_photo(self,object):
        return mark_safe(f"<img src='{object.photo.url}' width=50>")
    get_html_photo.short_description = "Photo"

class Training1Admin(admin.ModelAdmin):
    list_display = ('id','title','get_html_photo')
    list_display_links = ('id','title')
    search_fields = ('title' , 'author')
    fields = ('title', 'time','place','training_manager', 'photo', 'get_html_photo')
    readonly_fields = ('get_html_photo',)
    save_on_top = True

    def get_html_photo(self,object):
        return mark_safe(f"<img src='{object.photo.url}' width=50>")
    get_html_photo.short_description = "Photo"

class Training2Admin(admin.ModelAdmin):
    list_display = ('id','title','get_html_photo')
    list_display_links = ('id','title')
    search_fields = ('title' , 'author')
    fields = ('title', 'time', 'place', 'training_manager', 'photo', 'get_html_photo')
    readonly_fields = ('get_html_photo',)
    save_on_top = True

admin.site.register(Training2)
admin.site.register(Training1)
admin.site.register(Books)

    def get_html_photo(self,object):
        return mark_safe(f"<img src='{object.photo.url}' width=50>")

    get_html_photo.short_description = "Photo"

admin.site.register(Training2,Training2Admin)
admin.site.register(Training1,Training1Admin)
admin.site.register(Books,BooksAdmin)
admin.site.register(Category)
admin.site.register(Training_manager1)
admin.site.register(Training_manager2)

# Register your models here.

admin.site.site_title = 'Админ панель сайта Supportme'
admin.site.site_header = 'Админ панель сайта SupportMe'
  10
coolsite/project/forms.py