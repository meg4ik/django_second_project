from django.contrib import admin

# Register your models here.

from .models import Article

class AuthorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Article, AuthorAdmin)