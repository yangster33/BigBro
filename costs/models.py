from django.db import models

# Create your models here.
class Costs(models.Model):

    STATUS_GO = 1
    STATUS_COME = 0
    STATUS_STAY = 2
    STATUS_ITEM = (
        (STATUS_GO, '去分公司'),
        (STATUS_COME, '回办公室'),
        (STATUS_STAY, '在办事处'),
    )

    account = models.ForeignKey(
        User, verbose_name='账户', on_delete=models.DO_NOTHING)
    travel_date = models.DateField(verbose_name='出差日期')
    location = models.CharField(
        verbose_name='出差地点', default='重庆', max_length=30)
    work = models.CharField(verbose_name='工作内容', max_length=100)
    employee_status = models.PositiveIntegerField(
        verbose_name='人员状态', choices=STATUS_ITEM, default=2)
    trans_cost = models.FloatField(verbose_name='交通费', default=0)
    hotel_cost = models.FloatField(verbose_name='住宿费', default=0)
    local_trans_cost = models.FloatField(verbose_name='本地交通费', default=0)
    meat_cost = models.FloatField(verbose_name='餐费', default=0)
    local_car_cost = models.FloatField(verbose_name='本地租车费', default=0)
    other_cost_1 = models.FloatField(verbose_name='其他费用1', default=0)
    other_cost_2 = models.FloatField(verbose_name='其他费用2', default=0)
    other_cost_3 = models.FloatField(verbose_name='其他费用3', default=0)

    class Meta:
        verbose_name = '差旅成本'
        verbose_name_plural = '差旅成本'
        ordering = ['-travel_date']
        unique_together = ('account', 'travel_date',)

    def __str__(self):
        return self.account.username

    @classmethod
    def sum_cost(cls, obj):
        meta = cls._meta
        field_names = [field.name for field in meta.fields][6:]
        costs_dict = cls.objects.values(*field_names).get(pk=obj.pk)

        return round(sum(costs_dict.values()), 2)

    @classmethod
    def days_num(cls, startday, endday, r_user):
        user_objs = User.objects.all()
        days_total_costs_dict = dict()
        qs = cls.objects.all()
        for user in user_objs:
            sum_costs = cls.days_costs(startday, endday, user, qs)
            days_total_costs_dict[user.username] = sum_costs
        days_total_costs_dict = sorted(
            days_total_costs_dict.items(), key=lambda x: x[1])
        return yangster_no1(days_total_costs_dict)[r_user._wrapped.username]

    @classmethod
    def days_costs(cls, starday, endday, user, qs):
        sum_dict = qs.filter(account=user).filter(travel_date__range=(starday, endday)).aggregate(
            Sum('hotel_cost'), Sum('trans_cost'), Sum(
                'local_trans_cost'), Sum('meat_cost'),
            Sum('local_car_cost'), Sum('other_cost_1'), Sum('other_cost_2'), Sum('other_cost_3'))
        for i in sum_dict:
            if sum_dict[i] is None:
                sum_dict[i] = 0

        return sum(sum_dict.values())

    @classmethod
    def favoriteloction(cls, startday, endday, user, qs):
        qs = qs.filter(account=user).filter(
            travel_date__range=(startday, endday))
        locations = [i['location'] for i in qs.values(
            'location').distinct().order_by('location')]
        locations_dict = {v: 0 for v in locations}
        for i in locations_dict:
            times = qs.filter(location=i).aggregate(Count('location'))
            locations_dict[i] = times['location__count']
        locations_list = sorted(
            locations_dict.items(), key=lambda x: x[1])
        return locations_list

    @classmethod
    def global_compare(cls, startday, enday, user_obj, qs):

        if qs.exists():
            username_qs = qs.values(
                'account__username').distinct().order_by('account__username')
            user_list = []
            for i in username_qs:
                user_list.append(User.objects.get(
                    username=i['account__username']))

            costs_dict = {user: 0 for user in user_list}
            for user in costs_dict:
                costs_dict[user] = cls.days_costs(
                    startday, enday, user, qs)

            if sum(costs_dict.values()) == 0:
                per = '∞'
            else:
                sum_costs = sum(costs_dict.values())
                per = costs_dict[user_obj] / sum_costs
                per = round(per * 100, 1)
        else:
            costs_dict = {user: 0 for user in user_list}
            return (0, 0, costs_dict)

        return (per, costs_dict[user_obj], costs_dict)