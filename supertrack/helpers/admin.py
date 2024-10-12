from django.contrib import admin


class BaseModelAdmin(admin.ModelAdmin):
    empty_value_display = "-empty-"
