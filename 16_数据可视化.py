import json
import datetime

from pyecharts.charts import Map
from pyecharts import options as opts  # pyecharts接口手册：https://pyecharts.org/#/zh-cn/chart_api

today = datetime.date.today().strftime('%Y%m%d')
# 读取原始文件
with open('data/coll_new_day_data_of_province.json', encoding='utf8') as f:
    json_array = json.load(f)

# 分析全国实时确诊数据: 'confirmedIncr'字段
china_data = []
for province in json_array:
    china_data.append((province['provinceShortName'], province['confirmedIncr']))
china_data = sorted(china_data, key=lambda x: x[1], reverse=True)  # reverse=True，表示降序

print(china_data)
# 全国疫情地图
# 定义每个字段的范围，以及每个字段的样式
pieces = [
    {'min': 10000, 'color': '#540d0d'},
    {'max': 9999, 'min': 1000, 'color': '#9c1414'},
    {'max': 999, 'min': 500, 'color': '#d92727'},
    {'max': 499, 'min': 100, 'color': '#ed3232'},
    {'max': 99, 'min': 10, 'color': '#f27777'},
    {'max': 9, 'min': 1, 'color': '#f7adad'},
    {'max': 0, 'color': '#f7e4e4'},
]
labels = [data[0] for data in china_data]
counts = [data[1] for data in china_data]

m = Map()
m.add('昨日确诊人数', [list(z) for z in zip(labels, counts)], 'china')

# 系列配置项，可配置图元样式、文字样式、标签样式、电线样式等
m.set_series_opts(label_opts=opts.LabelOpts(font_size=12), is_show=False)
# 全局配置项，可配置标题、动画、坐标轴、图例等
m.set_global_opts(title_opts=opts.TitleOpts(title='全国实时确诊数据', subtitle='数据来源：丁香园网站'),
                  legend_opts=opts.LegendOpts(is_show=False),
                  visualmap_opts=opts.VisualMapOpts(pieces=pieces, is_piecewise=True,
                                                    is_show=True))  # is_piecewise参数表示是否分段，is_show参数表示是否显示视觉映射配置
# render()会生成本地html文件
filepath = './' + '新冠肺炎全国实时昨日确诊数据' + today + '.html'
m.render(path=filepath)
