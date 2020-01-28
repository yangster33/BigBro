import datetime

from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView


# Create your views here.
from costs.middleware import ArchivesMixin
from costs.models import Costs
from flows.models import WeekendCostsFlows
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
    model_fields = [
        'location', 'work', 'trans_cost',
        'hotel_cost', 'local_trans_cost',
        'meat_cost', 'local_car_cost',
        'other_cost_1',
    ]

    def get_queryset(self):
        qs = Costs.objects.all()
        return qs.filter(account=self.request.user)

    def get_context_data(self, **kargs):

        context = super().get_context_data(**kargs)

        myflows_list = []
        myflows = WeekendCostsFlows.objects.exclude(step=99).filter(
            flow__contains=self.request.user._wrapped.username)
        user = self.request.user._wrapped.username
        
        for flow in myflows:
            if flow.flow.split('-')[flow.step] == user:
                myflows_list.append(flow)
        flows_costs_list = [v.costs_set.all().reverse() for v in myflows_list]
        context.update({"myflows": myflows_list})
        context.update({"flows_costs_list": flows_costs_list})
        context.update({"locations": self.localtions})

        return context

    def post(self, requset, *arg, **kargs):
        update_post = self.request.POST
        qs = Costs.objects.filter(account=self.request.user)
        if update_post.get('flow_commit') is None:
            for i in range(1, 7):
                if update_post.get('date '+str(i)) is not None:
                    now_qs = qs.get(travel_date=update_post['date '+str(i)])
                    if update_post['work '+str(i)] != '':
                        for m in self.model_fields:
                            set_data = update_post[m+' '+str(i)]
                            if m[-4:] == 'cost' or m[-6:-2] == 'cost':
                                if set_data == '':
                                    set_data = 0
                                else:
                                    set_data = float(set_data)
                            setattr(now_qs, m, set_data)
                        now_qs.save()

        flow_id = update_post.get('flow_id')
        flow = WeekendCostsFlows.objects.get(pk=flow_id)
        if flow.step + 1 < len(flow.flow.split('-')):
            flow.step += 1
        else:
            flow.step = 99
        flow.save()

        return redirect('flows')
