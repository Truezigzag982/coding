# pet manager GUI
# 新知识点： sg.Col列，显示图片sg.Image
import io
import os
import sys
import shutil  # 用于复制文件
import PySimpleGUI as sg
from PIL import Image  # 图像库PIL(Python Image Library),显示图像
# pip install pillow  # 需要先打开终端，安装

import object_save_and_read as pets_io
from pet4 import Pet

# 设置重要的变量

# determine if application is a script file or exe
# 获取当前文件所在目录
if getattr(sys, 'frozen', False):
    current_work_dir = os.path.dirname(sys.executable)  # exe文件
elif __file__:
    current_work_dir = os.path.dirname(__file__)  # python文件

pets_io_file = current_work_dir + "\\pets_info.data"  # 用于存储序列化的对象
image_folder_path = current_work_dir + "\\images\\"  # 保存pets图片文件的目录
pets_list = []  # 全局变量,保存全部pets的对象
petsname_list = []  # 全局变量,保存全部pets的对象的名称
selected_petname = None  # 选中的宠物对象名称
selected_pet = None  # 选中的宠物对象



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
        #[sg.Text('', size=(6, 1))],  # 空白区域,
        [sg.Button('Save', size=(8, 2))],
        [sg.Text('', size=(6, 1))],  # 空白区域,
        [sg.Button('Delete', size=(8, 2))],
        [sg.Text('', size=(6, 1))],  # 空白区域,
        [sg.Button('Image', size=(8, 2))],
        [sg.Text('', size=(6, 1))],  # 空白区域,
        [sg.Button('Add', size=(8, 2), key='-ADD-')],
        #[sg.Text('', size=(6, 1))]  # 空白区域,        
    ]

    # 分成三列显示，有利于布局显示
    layout = [[sg.Col(col1, key='-COL1-'), 
               sg.Col(col2, key='-COL2-'), 
               sg.Col(col3, key='-COL3-')]
    ]

    window = sg.Window('宠物信息管理助手', layout, 
                       size=(450, 320), finalize=True)
    return window

def main():
    global petsname_list, pets_list, selected_pet, selected_petname

    window = create_window()

    while True:  # 事件循环
        event, values = window.read()

        if event in (sg.WIN_CLOSED, 'Exit'):
            # 判断是否点击了关闭窗口或取消按钮
            break
    window.close()


if __name__ == '__main__':
    main()
