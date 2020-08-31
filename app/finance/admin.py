from django.contrib import admin
from app.finance import models


class StockAdmin(admin.ModelAdmin):
    list_display = ('name', 'abbreviation')


admin.site.register(models.Stock, StockAdmin)
