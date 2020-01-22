from django.db import models

# Create your models here.

class WeekendCostsFlows(models.Model):

    name = models.CharField(verbose_name='流程名称', max_length=50)
    desc = models.CharField(verbose_name='流程描述', max_length=200)
    flow = models.CharField(verbose_name='流程内容', max_length=200)
    step = models.IntegerField(verbose_name='当前流程状态', default=0)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    done_time = models.DateTimeField(verbose_name='完成时间')

    class Meta:
        verbose_name = '流程'
        verbose_name_plural = '流程'
    
    def __str__(self):
        return self.name
