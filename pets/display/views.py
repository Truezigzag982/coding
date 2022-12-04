from django.shortcuts import render

from django.http import HttpResponse

from .models import Pet 

# Create your views here.
def welcome(request):
    return HttpResponse("Hi, welcome to Pets world! ")
def hi(request):
    return HttpResponse("views.hi is called.")

def get_title(request):
    web_title = "宠物网站"
    return render(request,"mytemp.html", {"web_title":web_title})

def get_pets(request):
    pets_list = Pet.objects.all() # 获取数据表中所有记录，转换成对象列表
    return render(request, 'show_pets.html', {'pets_list': pets_list})

def add_pet(request):
    """增加：添加宠物"""
    # 1.根据浏览器请求方式POST/GET进行处理
    if request.method == 'POST':
    # 2. 用户提交了表单，获取表单提交过来的数据
        name = request.POST.get('name')
        intro = request.POST.get('intro')
    # 3. 添加宠物对象到数据库（生成一条相应的数据库记录）
        Pet.objects.create(name=name, intro=intro)
    # 对应SQL语句：f'INSERT INTO pet (name, intro) VALUES({name}, {intro})'
    # 重定向到所有宠物页面（显示所有宠物信息）
        return redirect('/show_pets/')
# 需要增加导入：from django.shortcuts import redirect
    else: # 'GET', 用户访问增加宠物的页面
        return render(request, 'add_pet.html')

def edit_pet(request):
    """修改宠物"""
    if request.method == 'POST':
    # 1.获取提交过来的数据
        name = request.POST.get('name')
        intro = request.POST.get('intro')
        # 2.根据唯一标识去数据库中查询出对象，修改对象
        '''
        # 方法1：缺点：每个字段全部更新
        id = request.POST.get('id')
        pet_obj = Pet.objects.get(id=id)
        # 对象重新赋值
        # 将新的数据赋值给对象
        pet_obj.name = name
        pet_obj.intro = intro
        pet_obj.save()  # 将对象保存到数据库
        '''
        # 方法2：(推荐使用)
        # 优点：能够自动识别被修改的字段，只修改被修改的字段
        # 使用filter() 返回 QuerySet 集合，使用 update() 方法。
        pet_id = request.POST.get('id')
        Pet.objects.filter(id=pet_id).update(name=name, intro=intro)
        # 对应SQL语句：f'UPDATE pet SET name={name}, intro={intro} WHERE id ={pet_id}'
        # 修改成功后重定向到所有宠物页面
        return redirect('/show_pets/')
    else:
        #  GET请求
        # 1.获取 表单提交过来的id
        id = request.GET.get('id')
        # 2. 根据id去数据库中查询记录
        pet_obj = Pet.objects.get(id=id)
        # 3. 传递给模板，通过模板把宠物信息显示到页面上
        return render(request, 'edit_pet.html', {'pet_obj': pet_obj})

def delete_pet(request):
        """删除: 根据id删除宠物"""
    # 1.获取表单传递过来的id
    pet_id = request.GET.get('id')
    # 2.删除数据库中与id对应的记录
    # 方法1：
Pet.objects.filter(id=pet_id).delete() # filter() 根据条件进行过滤。
    # 对应SQL语句：f'DELETE FROM pet  WHERE id={pet_id}'
    # Pet.objects.all().delete()  # 删除全部记录。
'''
# 方法2:
    pet = Pet.objects.get(id=pet_id)
    pet.delete()
    '''
    # 3.删除成功后，重定向到所有宠物页面
    return redirect('/show_pets/')
