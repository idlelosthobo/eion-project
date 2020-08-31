from django.contrib import admin
from app.news import models


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(models.Subject, SubjectAdmin)
