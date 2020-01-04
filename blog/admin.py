from django.contrib import admin

from .models import Blog


class BlogAdminModel(admin.ModelAdmin):
    list_display = ('__str__', 'state')


admin.site.register(Blog, BlogAdminModel)
