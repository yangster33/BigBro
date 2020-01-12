from django.shortcuts import render
from django.views.generic import ListView, TemplateView

import datetime

from .models import Costs
from .timetraveler import which_week, which_season, yangster_no1
from user.models import MyUser
from .middleware import ArchivesMixin

# Create your views here.


class IndexView(ArchivesMixin, ListView):
    template_name = 'index_main.html'
    model = Costs

    def get_queryset(self):
        qs = Costs.objects.all()
        return qs.filter(account=self.request.user)

    def get_context_data(self, **kargs):
        # 很关键，必须把原方法的结果拿到
        context = super().get_context_data(**kargs)
        now = datetime.datetime.now().date()
        onday = datetime.timedelta(days=1)
        qs = context['object_list']

        last_week_costs = Costs.days_costs(
            *which_week(now, -1), self.request.user, qs)
        last_2week_costs = Costs.days_costs(
            *which_week(now, -2), self.request.user, qs)
        this_season_costs = Costs.days_costs(
            *which_season(now, 0), self.request.user, qs)
        last_season_costs = Costs.days_costs(
            *which_season(now, -1), self.request.user, qs)
        this_year_costs = Costs.days_costs(
            now.replace(month=1, day=1), now, self.request.user, qs)
        last_year_costs = Costs.days_costs(
            now.replace(year=now.year-1, month=1, day=1), now.replace(year=now.year-1, month=12, day=31), self.request.user, qs)
        location_list = Costs.favoriteloction(
            now.replace(month=1, day=1), now, self.request.user, qs)
        last_week_location_list = Costs.favoriteloction(
            now.replace(month=1, day=1), now - onday * 7, self.request.user, qs)
        location_list.reverse()
        last_week_location_list.reverse()

        if last_2week_costs == 0:
            last_week_per = '∞'
        else:
            last_week_per = round(
                (last_week_costs - last_2week_costs) / last_2week_costs * 100, 2)

        if last_season_costs == 0:
            last_season_per = '∞'
        else:
            last_season_per = round((this_season_costs -
                                     last_season_costs) / last_season_costs * 100, 2)

        if last_year_costs == 0:
            last_year_per = '∞'
        else:
            last_year_per = round(
                (this_year_costs - last_year_costs) / last_year_costs * 100, 2)

        update_dict = dict(
            last_week_costs=last_week_costs,
            last_2week_costs=last_2week_costs,
            this_season_costs=this_season_costs,
            last_season_costs=last_season_costs,
            this_year_costs=this_year_costs,
            last_year_costs=last_year_costs,
            location_list=location_list,
            last_week_location_list=last_week_location_list,
            last_week_per=last_week_per,
            last_season_per=last_season_per,
            last_year_per=last_year_per,
        )

        context.update(update_dict)

        # print(context)
        return context


class ChartsView(ArchivesMixin, ListView):
    template_name = 'index_charts.html'
    model = Costs

    def get_context_data(self, **kargs):

        context = super().get_context_data(**kargs)

        now = datetime.datetime.now().date()
        qs = context['object_list']
        print(context['object_list'])

        last_week_data = Costs.global_compare(
            *which_week(now, -1), self.request.user, qs)
        this_season_data = Costs.global_compare(
            *which_season(now, 0), self.request.user, qs)
        this_year_data = Costs.global_compare(now.replace(
            month=1, day=1), now, self.request.user, qs)

        last_week_list = sorted(last_week_data[2].items(), key=lambda x: x[1])
        this_year_list = sorted(this_year_data[2].items(), key=lambda x: x[1])
        try:
            last_week_num = yangster_no1(last_week_list)[self.request.user]
            this_year_num = yangster_no1(this_year_list)[self.request.user]
        except KeyError:
            last_week_num = 0
            this_year_num = 0
        
        update_dict = dict(
            last_week_data=last_week_data,
            this_season_data=this_season_data,
            this_year_data=this_year_data,
            last_week_list=last_week_list,
            this_year_list=this_year_list,
            last_week_num=last_week_num,
            this_year_num=this_year_num,
        )
        
        context.update(update_dict)

        test = 10000
        context.update({'test':test})
        # print(last_week_num)
        return context


class FlowsView(ArchivesMixin, TemplateView):
    template_name = 'index_flows.html'
    model = Costs

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        context = self.get_context_data()
        print(request.GET)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        text = request.POST.get('text', None)
