from django.shortcuts import render, redirect


from costs.models import Costs
from flows.models import TempFlows
import datetime

# class WeekendUpdateMixin:

#     def post(self, requset, *arg, **kargs):
#         qs = Costs.objects.filter(account=self.requset.user)
#         update_post = self.requset.POST
#         for i in range(1, 7):
#             now_qs = qs.get(travel_date=update_post['date '+str(i)])
#             for m in self.model_fields:
#                 set_data = update_post[m+' '+str(i)]
#                 if m[-4:] == 'cost' or m[-6:-2] == 'cost':
#                     if set_data == '':
#                         set_data = 0
#                     else:
#                         set_data = float(set_data)
#                 setattr(now_qs, m, set_data)
#             now_qs.save()

#         return redirect('flows')


def TempFlowsCreater(username, name, model, data, flows, step=0):

    done_time = datetime.datetime(year=1900, month=1, day=1)
    data=data.dict()
    if data.get('csrfmiddlewaretoken'):
        data.pop('csrfmiddlewaretoken')
    if data.get('temp_flow'):
        data.pop('temp_flow')

    if model.__name__ == 'Costs':
        modelname = '差旅'
    else:
        modelname = model.__name__
    TempFlows.objects.create(
        name=name,
        desc='tempflow',
        model=modelname,
        data=data,
        flow=flows,
        step=step,
        done_time=done_time,
    )
