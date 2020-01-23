from costs.models import Costs

class WeekendUpdateMixin:

    def post(self, requset, *arg, **kargs):
        qs = Costs.objects.filter(account=self.requset.user)
        for i in self.request.POST.keys():
            if i[:4] == 'date':
                pass