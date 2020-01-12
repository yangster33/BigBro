from django.db.models import Sum

# Create your tests here.*
import json

from .timetraveler import which_month
from .colors import myrgb


def chartsdumps(Costs, MyUser, username):

    user_list = MyUser.objects.all()
    json_list = []
    mycolor = '#FF0601'

    for i, user in enumerate(user_list):
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
                              backgroundColor=0,
                              borderColor=0,
                              data=now_costs))

    pop_list = []
    for i, j in enumerate(json_list):
        if sum(j["data"]) == 0:
            pop_list.append(i)
        if j["label"] == username:
            j["backgroundColor"] = mycolor
            j["borderColor"] = mycolor

    pop_list.reverse()
    for i in pop_list:
        json_list.pop(i)

    rgb_list = myrgb(110, 144, 255, len(json_list))

    for i, j in enumerate(json_list):
        j["backgroundColor"] = rgb_list[i]
        j["borderColor"] = rgb_list[i]

    return json.dumps(json_list, ensure_ascii=False)[1:-1]