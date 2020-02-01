from django.contrib import admin

from .models import WeekendCostsFlows, TempFlows
# Register your models here.

@admin.register(WeekendCostsFlows)
class WeekendCostsFlowsAdmin(admin.ModelAdmin):
    pass


@admin.register(TempFlows)
class TempFlowsAdmin(admin.ModelAdmin):
    pass