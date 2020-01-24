from costs.models import Costs

class WeekendUpdateMixin:

    def post(self, requset, *arg, **kargs):
        qs = Costs.objects.filter(account=self.requset.user)
        update_post = self.requset.POST
        for i in range(1,7):
            now_qs = qs.get(travel_date=update_post['date '+str(i)])
            for m in self.model_fields:
                set_data = update_post[m+' '+str(i)]
                if m[-4:] == 'cost' or m[-6:-2] == 'cost':
                    if set_data == '':
                        set_data = 0
                    else:
                        set_data = float(set_data)
                setattr(now_qs, m, set_data)
            now_qs.save()