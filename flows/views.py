import datetime

from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView


# Create your views here.
from costs.middleware import ArchivesMixin
from costs.models import Costs
from flows.models import WeekendCostsFlows
from .models import WeekendCostsFlows, TempFlows
from costs.timetraveler import which_week
from .middleware import TempFlowsCreater, CostUpdater


class FlowsView(ArchivesMixin, ListView):
    template_name = 'index_flows.html'
    model = Costs
    paginate_by = 20
    now = datetime.datetime.now()
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
        username = self.request.user._wrapped.username
        myflows = WeekendCostsFlows.objects.exclude(step=99).filter(
            flow__contains=username)

        for flow in myflows:
            if flow.flow.split('-')[flow.step] == username:
                myflows_list.append(flow)
        flows_costs_list = [v.costs_set.all().reverse() for v in myflows_list]

        mytempflows = TempFlows.objects.exclude(step=99).filter(
            flow__contains=username)

        for i in mytempflows:
            if i.flow.split('-')[i.step] == username:
                myflows_list.append(i)
                temp_dict = eval(i.data)
                temp_dict['flow_id'] = i.id
                temp_dict['step'] = i.step
                flows_costs_list.append(temp_dict)
        # print(flows_costs_list)

        context.update({"myflows": myflows_list})
        context.update({"flows_costs_list": flows_costs_list})
        context.update({"locations": self.localtions})

        return context

    def post(self, requset, *arg, **kargs):
        update_post = self.request.POST
        qs = Costs.objects.filter(account=self.request.user)
        if update_post.get('temp_flow') is None:
            if update_post.get('flow_commit') is None:
                for i in range(1, 7):
                    if update_post.get('date '+str(i)) is not None:
                        now_qs = qs.get(
                            travel_date=update_post['date '+str(i)])
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
                if flow.setp == 1:
                    flow.done_time = self.now
            else:
                flow.step = 99
            flow.save()
        elif update_post.get('temp_flow') == 'going':
            print(update_post)
            # print(int(update_post.get('flow_id')))
            temp_flow = TempFlows.objects.get(pk=int(update_post.get('flow_id')))
            if update_post.get('return'):
                temp_flow.step -= 1
                temp_flow.save()
            elif update_post.get('delete'):
                temp_flow.delete()
                flow_cost = Costs.objects.filter(account=self.request.user).get(travel_date=update_post['date'])
                flow_cost.status = 0
                flow_cost.save()
            elif update_post.get('init'):
                temp_flow.step = 0
                temp_flow.save()
            else:
                if len(temp_flow.flow.split('-')) == temp_flow.step + 1:
                    temp_flow.delete()
                    CostUpdater(self.request.user, update_post.get('date'), update_post)
                else:
                    temp_flow.step += 1
                    temp_flow.save()
        else:
            username = self.request.user._wrapped.username
            tempname = update_post['date'] + username + Costs.__name__ + '修改流程'
            flows = username + '-' + '何鹏威' + '-' + username
            step = 1
            model = Costs
            data = update_post

            TempFlowsCreater(username, tempname, model, data, flows, step)

            flow_cost = Costs.objects.filter(account=self.request.user).get(travel_date=update_post['date'])
            flow_cost.status = 1
            flow_cost.save()

        return redirect(self.request.get_full_path())
