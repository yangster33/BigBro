from costs.models import Costs
from .models import WeekendCostsFlows

import datetime

from costs.timetraveler import which_week


class WeekendCostsFlowsPilot:
    def __init__(self, user):
        self.user = user
        self.now = datetime.datetime.now()
        self.thisweek = which_week(self.now, 0)

    def creater(self):
        oneday = datetime.timedelta(days=1)
        temp_now = self.thisweek[0]
        while temp_now == self.thisweek[1]:
            i = Costs(account=self.user)
            i.travel_date = temp_now
            i.save()
            temp_now += oneday
