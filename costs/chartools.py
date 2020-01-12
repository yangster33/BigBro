from django.db.models import Sum

# Create your tests here.*
import json

from .timetraveler import which_month


def chartsdumps(Costs, MyUser):

    user_list = MyUser.objects.all()
    json_list = []

    for user in user_list:
        now_costs = []
        for month in range(1, 13):

            sum_dict = Costs.objects.filter(account=user).filter(travel_date__range=(which_month(2019, month))).aggregate(
                Sum('hotel_cost'), Sum('trans_cost'), Sum(
                    'local_trans_cost'), Sum('meat_cost'),
                Sum('local_car_cost'), Sum('other_cost_1'), Sum('other_cost_2'), Sum('other_cost_3'))
            if sum_dict['hotel_cost__sum'] is None:
                now_costs.append(0)
            else:
                now_costs.append(sum(sum_dict.values()))

        json_list.append(dict(label=user.username,
                              backgroundColor='#007bff',
                              borderColor='#007bff',
                              data=now_costs))

    print(json.dumps(json_list, ensure_ascii=False)[1:-1])
