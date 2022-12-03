# -*- coding: utf-8 -*-
# 先安装库在pip install PySimpleGUI
import PySimpleGUI as sg      # 导入库
# 注意：设置元素的key名称，后续可获取它对应的value,或设置其显示的内容

# 定义窗口的内容
layout = [[sg.Text("Type in your name")],   # 按行、列排版
          [sg.Text("Name:"), sg.Input(do_not_clear=True, key='_NAME_')],
          [sg.Text('', key='_OUTPUT_')],
          [sg.Button('OK'), sg.Button('Exit')]]

# 创建窗口：
window = sg.Window('Name, blah blah blah', layout)

while True:  # 事件循环
    event, values = window.read()  # 获取文本框输入内容
    if event == sg.WIN_CLOSED or event == 'Exit':
        #判断是否点击了关闭窗口或取消按钮
        break

    # 设置文本框信息
    if event == 'OK':
        message = 'Hello, ' + values['_NAME_'] + ' nice to meet you'
        window.Element('_OUTPUT_').Update(message)

window.close()  # 关闭窗口
