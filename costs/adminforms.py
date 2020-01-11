from django import forms

from .models import Costs


class CostsAdminForm(forms.ModelForm):
    location = forms.CharField(widget=forms.Textarea, label='出差地点')

    class Meta:
        model = Costs
        fields = ('account', 'travel_date', 'location', 'work', 'employee_status', 'trans_cost',
                  'hotel_cost', 'local_trans_cost', 'meat_cost', 'local_car_cost', 'other_cost_1',
                  'other_cost_2', 'other_cost_1',)

    def dotpolice(self, num):
        if num * 10 - int(num * 10) != 0:
            return False
        else:
            return True

    def clean(self):
        args = ('trans_cost', 'hotel_cost', 'local_trans_cost', 'meat_cost',
                'local_car_cost', 'other_cost_1', 'other_cost_2', 'other_cost_1',)
        for arg in args:
            num = self.cleaned_data.get(arg)
            if num is not None:
                if not self.dotpolice(num):
                    self.add_error(arg, '保留一位小数')
                    return
                self.cleaned_data['trans_cost'] = num
        return super().clean()
