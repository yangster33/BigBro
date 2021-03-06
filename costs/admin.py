from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Costs
from .adminforms import CostsAdminForm

# Register your models here.


class CostResource(resources.ModelResource):

    class Meta:
        model = Costs


@admin.register(Costs)
class CostsAdmin(ImportExportModelAdmin):

    resource_class = CostResource
    form = CostsAdminForm
    list_display = ('account', 'status', 'travel_date', 'location', 'work', 'trans_cost',
                    'hotel_cost', 'local_trans_cost', 'meat_cost', 'local_car_cost', 'other_cost_1', 'sum_cost')
    fieldsets = (
        ('差旅信息',
         {'fields': ('account', 'status', 'travel_date', 'location',
                     'work',)}
         ),
        ('成本明细',
         {'fields': ('trans_cost', 'hotel_cost', 'local_trans_cost',
                     'meat_cost', 'local_car_cost', 'other_cost_1')}
         ),
        ('流程',
         {'fields': ('flows',)}
         ),
    )


    list_filter = ['account']

    # def get_queryset(self, request):
    #     qs = super().get_queryset(request)
    #     if request.user._wrapped.username == 'admin':
    #         return qs
    #     return qs.filter(account=request.user)

    # def save_model(self, request, obj, form, change):
    #     obj.account = request.user
    #     return super().save_model(request, obj, form, change)

    def sum_cost(self, obj):
        return Costs.sum_cost(obj)

    sum_cost.short_description = '合计'
