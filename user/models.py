from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class MyUser(AbstractUser):

    position = models.CharField(verbose_name='岗位', max_length=50, default='员工')
    avatar = models.ImageField(
        verbose_name='头像', upload_to="avatars", default='avatars/default.jpg',)

    diligent_num = models.IntegerField(verbose_name='勤奋指数', default=80)

    legend = models.IntegerField(verbose_name='传说事迹', default=0)
    epic = models.IntegerField(verbose_name='史诗行为', default=0)
    rare = models.IntegerField(verbose_name='稀有业绩', default=0)

    def __str__(self):
        return self.username


