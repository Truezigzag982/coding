from django.contrib import admin

# Register your models here.
from .models import Pet # 导入模型类
#Pet模型的管理器
class PetAdmin(admin.ModelAdmin):
    list_display=('name', 'intro') # 列举Pet类中要在后台管理中显示的属性
#在admin中注册绑定
admin.site.register(Pet, PetAdmin)  