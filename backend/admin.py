from django.contrib import admin
from . import models


@admin.register(models.Entreprise)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'status', 'slug', 'founder')
    prepopulated_fields = {'slug': ('name',), }


admin.site.register(models.Category)
