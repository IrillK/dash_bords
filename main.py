from graphs_builders.histograms import build_histogram, build_multiple_histogram
from build_html import make_dashboard
import pandas as pd

# Пример json для построения графиков
# dashbord_dict = {
#     'fig1': {
#         'x_name':'x',
#         'y_name_list': ['x', 'y'],
#         'aggregate_f_list': ['count', 'sum'],
#         'trace_name_list': ['count', 'sum']
#     },
#     'fig2': {
#         'data': 'data',
#         'x_name': 'x',
#         'y_name': 'y',
#         'aggregate_f': 'sum',
#         'trace_name': 'name'
#     }
# }

# блок чтения данных
data = pd.read_excel(r'data\sample1.xlsx')

# блок постраения графикоф
fig1= build_multiple_histogram(
    data=data,
    x_name='x',
    y_name_list=['x', 'y'],
    aggregate_f_list=['count', 'sum'],
    trace_name_list=['count', 'sum']
)

fig2 = build_histogram(
    data=data,
    x_name='x',
    y_name='y',
    aggregate_f='sum',
    trace_name='name'
)

# блок формирования html
make_dashboard(
    output_html_path=r"output1.html",
    input_template_path = r"templates/template.html",
    figs=[
        fig1,
        fig2,
    ]
)