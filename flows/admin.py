from django.contrib import admin

from .models import WeekendCostsFlows
# Register your models here.

@admin.register(WeekendCostsFlows)
class WeekendCostsFlowsAdmin(admin.ModelAdmin):
    pass