from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import News, Category


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_at',
                    'updated_at', 'is_published', 'get_photo', 'views')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category')
    fields = ('title', 'category', 'content', 'is_published', 'photo', 'created_at',
                       'updated_at', 'get_photo', 'views')
    readonly_fields = ('created_at',
                       'updated_at', 'get_photo', 'views')

    def get_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width='75'>")
        else:
            return '-'

    get_photo.short_description = 'фото'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(News, NewsAdmin)
admin.site.register(Category)

admin.site.site_title = 'Админка'
admin.site.site_header = 'Админка'
