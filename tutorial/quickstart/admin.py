from django.contrib import admin

from .models import *

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Category)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'author_name', 'email', 'is_notified')
    list_display_links = ('id',)
    search_fields = ('id', 'author_name', 'email')
    list_editable = ('author_name', 'is_notified')


admin.site.register(Author, AuthorAdmin)
