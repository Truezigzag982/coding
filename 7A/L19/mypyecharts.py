from pyecharts.charts import Bar
from pyecharts.charts import Pie
from pyecharts.charts import Radar
from pyecharts import options as opts
import os



def show_circular(title, data_pair):
    """环状图
    Args:
        title (str): 图示的标题
        data_pair ([iterable, iterable]): = [list(z) for z in zip(list1, list2)]
            格式：[['衬衫', 114], ['毛衣', 55], ['领带', 27], ['裤子', 101]...]

    Returns:
        pyecharts.charts.Pie: 环状图
    """    # 使用链式方法绘制
    circular = (
        # 初始化配置项，内部可设置颜色
        # Pie(init_opts=opts.InitOpts(bg_color="# 2c343c"))
        Pie().add(
            # 系列名称，即该环状图的名称
            series_name="销售量分析",
            # 系列数据项，格式为[(key1,value1),(key2,value2)]
            data_pair=data_pair,
            radius=[80, 150]  # 第一个半径是内半径，第二个半径是外半径。默认的radius为[0,75]
        )
        # 全局设置
        .set_global_opts(
            # 设置标题
            title_opts=opts.TitleOpts(
                # 名字
                title=title,
                # 组件距离容器左侧的位置
                pos_left="center",
                # 组件距离容器上方的像素值
                pos_top="20",
            ),
            # 图例配置项
            # legend_opts=opts.LegendOpts(is_show=False), # 不显示图例
            legend_opts=opts.LegendOpts(
                pos_left="left", orient="vertical")).render(title + ".html"))
    # 打开浏览器查看生成的文件
    os.system(title + ".html")
    return circular


def test_circular():
    title = "商品销售环状图"
    # 设置列名
    columns = ["衬衫", "毛衣", "领带", "裤子", "风衣", "高跟鞋", "袜子"]
    # 设置数据
    data = [114, 55, 27, 101, 125, 27, 105]
    # 添加环状图的数据，格式为[(key1, value1), (key2, value2)]
    data_pair = [list(z) for z in zip(columns, data)]
    print('data_pair:', data_pair)
    # 格式：[['衬衫', 114], ['毛衣', 55], ['领带', 27], ['裤子', 101]...]
    show_circular(title, data_pair)


def show_coxcomb(title, data):
    """玫瑰图，又名:南丁格尔图/鸡冠花图（coxcomb）
    Args:
        title (str): 图示的标题
        data (dict): 数据字典，格式{类型:数量}

    Returns:
        pyecharts.charts.Pie: 玫瑰图
    """
    # 使用链式方法绘制:
    # a链式编程是将多个操作（多行代码）通过点号(.)链接在一起成为一句代码，以增强代码的可读性
    coxcomb = (
        # 初始化配置项，内部可设置颜色
        Pie().add(
            # 系列名称，即该饼图的名称
            series_name=title,
            # 系列数据项，格式为[(key1,value1),(key2,value2)]
            data_pair=[list(z) for z in zip(data.keys(), data.values())],
            # 通过半径区分数据大小 “radius” 和 “area” 两种
            rosetype="radius",  # 玫瑰图，又名:南丁格尔图
            # 饼图的半径，设置成默认百分比，相对于容器高宽中较小的一项的一半
            radius="55%",
            # 饼图的圆心，第一项是相对于容器的宽度，第二项是相对于容器的高度
            center=["50%", "50%"],
        ).set_global_opts(  # 全局设置
            # 设置标题
            title_opts=opts.TitleOpts(
                # 名字
                title=title,
                # 组件距离容器左侧的位置
                pos_left="center",
                # 组件距离容器上方的像素值
                pos_top="20",
            ),
            # 图例配置项
            # legend_opts=opts.LegendOpts(pos_left="left", orient="vertical")  # 垂直显示
            legend_opts=opts.LegendOpts(pos_bottom="left",
                                        orient="horizontal")  # 水平显示
        ).set_series_opts(label_opts=opts.LabelOpts(formatter="{b}:{c}")
                          ).render(title + ".html"))
    os.system(title + ".html")  #  打开浏览器查看生成的文件
    return coxcomb


def test_coxcomb():
    # 设置数据字典
    data = {
        "铅笔": 114,
        "毛笔": 55,
        "圆珠笔": 87,
        "钢笔": 81,
        "文具盒": 25,
        "记号笔": 27,
        "橡皮擦": 105
    }
    title = "文具销量玫瑰图（南丁格尔图）"
    show_coxcomb(title, data)


def show_bar(title1, columns, data1, data2):
    """柱状图
    Args:
        columns (str list): 水平数据
        data1 (float list): 数据1
        data2 (float list): 数据2
    """
    bar = Bar()
    # 添加柱状图的数据及配置项
    bar.add_xaxis(columns)
    bar.add_yaxis("降水量", data1)
    bar.add_yaxis("蒸发量", data2)

    # 系列配置设置
    bar.set_series_opts(
        # 是否显示标签
        label_opts=opts.LabelOpts(is_show=False),
        # 设置显示最大最小值
        markpoint_opts=opts.MarkPointOpts(data=[
            opts.MarkPointItem(type_="max", name="max"),
            opts.MarkPointItem(name="min", type_="min")
        ]),
        # 设置平均分数线
        markline_opts=opts.MarkLineOpts(
            data=[opts.MarkLineItem(name="average", type_="average")]))
    # 全局配置设置,设置柱状图的标题
    bar.set_global_opts(title_opts=opts.TitleOpts(title=title1))

    # 生成本地文件（默认为render.html文件）
    bar.render("降水量柱状图.html")
    # 打开浏览器查看生成的文件
    os.system("降水量柱状图.html")


def test_bar():
    title = "2020年某地降水量与蒸发量情况"
    # 设置行名
    columns_zh = [
        "1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月",
        "12月"
    ]
    # 设置数据
    data1 = [
        2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3
    ]
    data2 = [
        2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3
    ]
    show_bar(title, columns_zh, data1, data2)


"""
def radar_simple(data1, data2) -> Radar:
    radar = (
        Radar().add_schema(
            # 各项的max_值可以不同
            schema=[
                opts.RadarIndicatorItem(name="数学", max_=100),
                opts.RadarIndicatorItem(name="语文", max_=100),
                opts.RadarIndicatorItem(name="英语", max_=100),
                opts.RadarIndicatorItem(name="历史", max_=100),
                opts.RadarIndicatorItem(name="科学", max_=100),
                opts.RadarIndicatorItem(name="体育", max_=100),
            ]).add(
"""


def show_radar(students, subjects, data1, data2):
    """雷达图
    Args:
        students (str list): 学生姓名列表（2位）
        subjects (str list): 学科列表
        data1 (float list): 学生1的成绩
        data2 (float list): 学生2的成绩
    """
    radar = (
        Radar().add_schema(
            # 各项的max_值可以不同
            schema=[
                opts.RadarIndicatorItem(name=subject, max_=100)
                for subject in subjects  # 生成多个,请对比上面注释掉的语句
            ]).add(
                students[0],
                data1,
                color="red",
                areastyle_opts=opts.AreaStyleOpts(  # 设置填充的属性DD
                    opacity=0.5,  # 透明度
                    color="red"),
            ).add(
                students[1],
                data2,
                color="blue",
                areastyle_opts=opts.AreaStyleOpts(opacity=0.5, color="blue"),
            ).set_series_opts(label_opts=opts.LabelOpts(
                is_show=True)).set_global_opts(title_opts=opts.TitleOpts(
                    title="雷达图示例-学科成绩")))
    radar.render("雷达图.html")
    os.system("雷达图.html")


def test_radar():
    students = ["小张", "小明"]
    subjects = ["数学", "语文", "英语", "历史", "科学", "体育"]
    scores1 = [[82, 93, 92, 95, 100, 65]]  # 小明成绩单
    scores2 = [[92, 90, 95, 85, 67, 95]]  # 小张成绩单
    radar_simple(students, subjects, scores1, scores2)


if __name__ == '__main__':
    # test_coxcomb()
    # test_circular()
    # test_bar()
    pass
