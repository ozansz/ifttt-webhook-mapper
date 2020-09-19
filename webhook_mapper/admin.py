from django.contrib import admin

from .models import GetToPostRequestMapping

@admin.register(GetToPostRequestMapping)
class GetToPostRequestMappingAdmin(admin.ModelAdmin):
    list_display = ("id", "tag", "trigger_action")