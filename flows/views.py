import datetime

from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView


# Create your views here.
from costs.middleware import ArchivesMixin
from costs.models import Costs
from .models import WeekendCostsFlows
from costs.timetraveler import which_week


class FlowsView(ArchivesMixin, ListView):
    template_name = 'index_flows.html'
    model = Costs
    paginate_by = 20
    localtions = [
        '涪陵', '北碚', '綦江',
        '大足', '巴南', '黔江',
        '长寿', '江津', '合川',
        '永川', '南川', '壁山',
        '铜梁', '潼南', '荣昌',
        '开州', '梁平', '武隆',
        '城口', '丰都', '垫江',
        '忠县', '云阳', '奉节',
        '巫山', '巫溪', '石柱',
        '秀山', '酉阳', '彭水',
    ]

    def get_queryset(self):
        qs = Costs.objects.all()
        return qs.filter(account=self.request.user)

    def get_context_data(self, **kargs):

        context = super().get_context_data(**kargs)

        myflows = WeekendCostsFlows.objects.filter(
            flow__contains=self.request.user._wrapped.username)
        flows_costs_list = [v.costs_set.all().reverse() for v in myflows]
        
        context.update({"myflows":myflows})
        context.update({"flows_costs_list":flows_costs_list})
        context.update({"locations":self.localtions})
        
        return context

    def post(self, requset, *arg, **kargs):
    
        
        print(self.request.POST)
        print(self.request)

        return redirect('flows')

