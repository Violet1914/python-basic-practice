import pyecharts.options
from pyecharts.charts import Line

line = Line()

line.add_xaxis(["中国", "美国", "英国"])

line.add_yaxis("GDP", [30, 20 , 10])

line.set_global_opts(
    toolbox_opts= pyecharts.options.ToolboxOpts(is_show=True),
)

line.render()
