from django.db import models

# Create your models here.
# 定义模型Pet（对应数据表）, 添加类的属性（对应数据表的字段）
class Pet(models.Model):
    name = models.CharField(max_length=20, blank=False, null=False) # 宠物名
    intro = models.CharField(max_length=200, blank=True, null=True) # 宠物介绍

    def __str__(self):
        return self.name

    class Meta:
        db_table = "pet" # 定义表名
        verbose_name='宠物' # 后台管理显示的名称
        verbose_name_plural='宠物们' # 