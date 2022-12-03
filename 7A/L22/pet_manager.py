# pet manager GUI
# 新知识点： sg.Col列，显示图片sg.Image
import io
import os
import sys
import shutil# 用于复制文件
import PySimpleGUI as sg
from PIL import Image  # 图像库PIL(Python Image Library),显示图像
# pip install pillow  # 需要先打开终端，安装

import object_save_and_read as pets_io  # Model：对象的数据存取
from pet4 import Pet

# 设置重要的变量：
# 获取当前文件所在目录（根据是python文件还是exe程序）
if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    current_work_dir = os.path.dirname(sys.executable)  # exe文件
elif __file__:
    current_work_dir = os.path.dirname(__file__)  # python文件

pets_data_file = current_work_dir + "\\data\\pets_info.data"  # 用于存储序列化的对象
image_folder_path = current_work_dir + "\\images\\"  # 保存pets图片文件的目录
pets_list = []  # 全局变量,保存全部pets的对象
petsname_list = []  # 全局变量,保存全部pets的对象的名称
selected_petname = None  # 选中的宠物对象名称
selected_pet = None  # 选中的宠物对象
# 可将以上内容放到__init__.py文件中

# View：创建图形用户界面窗口
def create_window():
    sg.theme('BrightColors')

    # 分成三列显示，有利于布局显示
    # 列1:宠物名称
    col1 = [
        [sg.Listbox(petsname_list, size=(12, 4), 
                    enable_events=True, key='-LIST-')],
        [sg.Text('', size=(12, 6))],        
    ]

    # 列2: 选定宠物的详细信息
    # 用于显示宠物的默认图像
    image_file = current_work_dir + "\\images\\pet.png"  
    col2 = [
        [sg.Text('宠物名:', size=(6, 1)),
         sg.Input(key='-NAME-', size=(18, 1))],
        [sg.Text('颜色:', size=(6, 1)),
         sg.Input(key='-COLOR-', size=(18, 1))],
        [sg.Text('品种:', size=(6, 1)),
         sg.Input(key='-BREED-', size=(18, 1))],
        [sg.Text('年龄:', size=(6, 1)),
         sg.Input(key='-AGE-', size=(18, 1))],
        [sg.Text('性别:', size=(6, 1)),
         sg.Input(key='-SEX-', size=(18, 1))],
        [sg.Text('前主人:', size=(6, 1)),
         sg.Input(key='-PREOWNER-', size=(18, 1))],
        [sg.Image(size=(200, 200), 
         filename=image_file, key="-IMAGE-")],
        # 图片文件仅支持GIF和PNG，不支持JPG！        
    ]
    
    # 列3:操作按钮和宠物图片
    col3 = [
        [sg.Button('Save', size=(8, 2))],
        [sg.Text('', size=(6, 1))],  # 空白区域,
        [sg.Button('Delete', size=(8, 2))],
        [sg.Text('', size=(6, 1))],  # 空白区域,
        [sg.Button('Image', size=(8, 2))],
        [sg.Text('', size=(6, 1))],  # 空白区域,
        [sg.Button('Add', size=(8, 2), key='-ADD-')],        
    ]

    # 分成三列显示，有利于布局显示
    layout = [[sg.Col(col1, key='-COL1-'), 
               sg.Col(col2, key='-COL2-'), 
               sg.Col(col3, key='-COL3-')]
    ]

    window = sg.Window('宠物信息管理助手', layout, 
                       size=(450, 360), finalize=True)
    return window

# View：刷新显示图片
def update_image(window, image_file):
    # display selected image
    image = Image.open(image_file)
    image.thumbnail((200, 200)) # 缩略图
    bio = io.BytesIO()
    image.save(bio, format="PNG")
    window['-IMAGE-'].update(data=bio.getvalue())

# View：刷新显示：选定宠物的详细信息
def update_petinfo(window, selected_pet):
    # global selected_pet # 有此行函数就不必有参数
    if selected_pet is not None:
        window['-NAME-'].update(selected_pet.name)
        window['-COLOR-'].update(selected_pet.color)
        window['-BREED-'].update(selected_pet.breed)
        window['-AGE-'].update(selected_pet.age)
        window['-SEX-'].update(selected_pet.sex)
        window['-PREOWNER-'].update(selected_pet.get_preowner())
        image_file = current_work_dir + \
                    "\\images\\" + selected_pet.image  
        update_image(window, image_file)  # 显示宠物的图像
    
# View：刷新显示宠物名称列表ListBox
def update_petslist(window):
    global petsname_list, pets_list, selected_petname
    # 声明是全局变量很重要, 退出本函数后，修改的数据才有效
    petsname_list = []
    for pet in pets_list:
        petsname_list.append(pet.name)
    # 刷新：选定宠物名称列表
    window['-LIST-'].update(petsname_list)
    window['-LIST-'].SetValue(selected_petname)

# View：显示选定宠物的详细信息
def display_petinfo(window, values):
    global pets_list, selected_pet, selected_petname
    # 在列表中选中的宠物名
    if selected_petname is None:  # 之前删除了宠物的情况
        if len(pets_list)>0:  # 列表不为空时
            # 删除一个宠物之后还没选中宠物，默认选择第一个宠物
            window['-LIST-'].update(set_to_index=0)
            selected_petname=pets_list[0].name            
        else:  # 列表中没有宠物，也就无选中的宠物
            selected_pet = None 
    else: 
        selected_petname = values['-LIST-'][0] 
    
    if len(pets_list)>0:
        for pet in pets_list:  # 从列表中获取当前选中宠物的详细信息
            if pet.name == selected_petname:
                selected_pet = pet  # 修改选中的宠物
                update_petinfo(window, selected_pet)
                break
    else: # 一个宠物也没有，需要输入
        window['-NAME-'].update('请输入宠物名')
        window['-COLOR-'].update('')
        window['-BREED-'].update('')
        window['-AGE-'].update('')
        window['-SEX-'].update('')
        window['-PREOWNER-'].update('')
        image_file = current_work_dir + "\\images\\" + 'pet.png'
        update_image(window, image_file)  # 显示默认宠物的图像

# Model：添加一只新的宠物信息：
def add_pet(window, values):
    #TODO:小组讨论，再各人编程实现
    # (1) View: 添加函数clear_petinfo(),清空各个属性对应的Input内容
    # (2) Input:用户输入各个属性的信息
    # (3) Controller->Model: 用户点击Save按钮，追加新的宠物信息到列表，再保存到数据文件
    #     Tip： 可能需要添加变量is_adding_pet来判断
    #                           False：修改当前选定宠物
    #                           True:  添加新的宠物
    # (4) View: update_petslist
    sg.popup_ok('add pet')
    print('add pet')
    pass

# Model：加载宠物数据
def load_data(window):
    global petsname_list, pets_list  
    # 声明是全局变量很重要，否则后面不会显示内容
    petsname_list = [] # 先清空
    pets_list = pets_io.read_object(pets_data_file)
    for pet in pets_list:
        petsname_list.append(pet.name)
    # 把宠物名称填入列表框中：
    window['-LIST-'].update(petsname_list)
    
# Model: 保存选定宠物的详细信息
def save_data(window, values):
    global selected_pet, pets_list, selected_petname
    # 判断输入信息的有效性：
    if len(values['-NAME-']) == 0:
        sg.popup_error('请输入宠物名!')
    if len(values['-COLOR-']) == 0:
        sg.popup_error('请输入宠物颜色!')
    if len(values['-BREED-']) == 0:
        sg.popup_error('请输入宠物品种!')
    if len(values['-AGE-']) == 0:
        sg.popup_error('请输入宠物年龄!')
    if len(values['-SEX-']) == 0:
        sg.popup_error('请输入宠物性别!')
    if len(values['-PREOWNER-']) == 0:
        sg.popup_error('请输入宠物前主人!'),
        
    # 以下属性如果修改了，就用Input的内容来修改选中宠物的属性
    # 无法确定是Cat或Dog,就用Pet生成实例对象
    selected_pet = Pet(
        values['-NAME-'],
        values['-COLOR-'],
        values['-BREED-'],
        values['-AGE-'],
        values['-SEX-']
    )  
    # 通过实例方法修改私有属性
    selected_pet.set_preowner(values['-PREOWNER-'])
    
    if not pets_list:  # 包括[]或None
        pets_list.append(selected_pet)  # 没有一个宠物的情况

    # 修改选定的宠物信息到列表中
    for i in range(len(pets_list)):
        if pets_list[i].name == selected_petname:  # 原来选定的宠物名
            pets_list[i] = selected_pet
            # 以便后续把pets_list写入数据文件，保存信息的更新
            break            

    if values['-NAME-'] != selected_petname:  # 修改了宠物名
        selected_petname = selected_pet.name # 选定的宠物名为修改后的名称
        # petsname_list需要刷新显示ListBox
        update_petslist(window)

    # Model：把宠物列表最新内容刷新到数据文件里
    pets_io.write_object(pets_data_file, pets_list)

# Model: 删除选定宠物的详细信息
def delete_data(window, values):
    global petsname_list, pets_list, selected_petname, selected_pet
    # 提示是否删除：
    if sg.popup_yes_no(f'确定要删除{selected_petname}的记录吗？') == 'Yes':
        if len(pets_list)>0:
            # 删除当前pet对象，重新保存pets到对象文件中
            for pet0 in pets_list:
                if pet0.name == selected_petname:
                    pets_list.remove(pet0)  # 删除对象列表中对应的对象
                    #删除宠物名列表中对应的宠物名
                    petsname_list.remove(selected_petname)  
                    # 更新数据文件保存的对象内容
                    if pets_io.write_object(pets_data_file, pets_list):
                        sg.popup_ok(f'已经删除{selected_petname}的记录。')
                        selected_petname = None
                        selected_pet = None
                        update_petslist(window)  # 刷新显示宠物名称列表框
                        display_petinfo(window, values)  # 刷新显示宠物详细信息
                    else:
                        sg.popup_error(f'删除{selected_petname}的操作失败！')

# Model: 保存宠物的图片
def save_image():
    global selected_pet
    # 支持显示的图片文件格式仅为png和gif,不支持jpg!
    file_types = [("PNG (*.png)", "*.png"), ("GIF (*.gif)", "*.gif")]
    # 弹出窗口，选择图片文件
    image_file = sg.popup_get_file('Image file to display',
                                    file_types=file_types,
                                    no_window=True)
    if len(image_file) > 0:  # 避免没选文件的情况
        # 复制，保存文件到images目录下
        try:
            shutil.copy(image_file, image_folder_path)
        except shutil.SameFileError:  # 文件已经存在则不用复制
            print(f'图片文件{image_file}已经存在。')

        #去掉路径名，只保存文件名，修改pet的属性
        filepath, filename = os.path.split(image_file)
        # 刷新pet的图片属性，只保存文件名（不包括路径）
        selected_pet.image = filename  
        # 修改选定的宠物信息到列表中
        for i in range(len(pets_list)):
            if pets_list[i].name == selected_petname:  # 原来选定的宠物名
                pets_list[i] = selected_pet
                # 以便后续把pets_list写入数据文件，保存信息的更新
                break
        # Model：把最新内容刷新到数据文件里
        pets_io.write_object(pets_data_file, pets_list)

    return image_file

# 主函数作控制器Controller:
def main():
    global selected_petname
    window = create_window()
    load_data(window)
    while True:  # 事件循环
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            # 判断是否点击了关闭窗口或取消按钮
            break
        # 如果在列表框中选中一只宠物，就显示详细信息
        if event == '-LIST-' and len(values['-LIST-']) > 0:
            selected_petname = values['-LIST-'][0]  #后面的[0]很重要！
            display_petinfo(window, values)
        if event == 'Save':
            save_data(window, values)
        if event == 'Delete':
            delete_data(window, values)
        if event == 'Image':  # 修改pet的图片
            image_file = save_image()  # Model: 更新显示宠物图片
            if len(image_file) > 0:
                update_image(window, image_file)  # View: 刷新显示选择的图片
        if event == '-ADD-': # View中有key, 就不能写按钮上的文字'Add'!
            add_pet(window, values) # TODO
    window.close()


if __name__ == '__main__':
    main()
