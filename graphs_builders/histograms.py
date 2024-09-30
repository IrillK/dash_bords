import plotly
import plotly.graph_objs as go
import plotly.express as px
from plotly.subplots import make_subplots

import pandas as pd

def build_histogram(
        data:pd.DataFrame, 
        x_name:str, 
        y_name:str, 
        aggregate_f:str, 
        trace_name:str
        ) -> go.Figure:
    """
        Возможные агрегатные функции: ['count', 'sum', 'avg', 'min', 'max']
    """
    fig = go.Figure()

    fig.add_trace(
        go.Histogram(
            x=data[x_name],
            y=data[y_name],
            name=trace_name,
            histfunc=aggregate_f,
            texttemplate="%{x}",
            textfont_size=20
            )
        )
    return fig

def build_multiple_histogram(
        data:pd.DataFrame,
        x_name:str,
        y_name_list:list,
        aggregate_f_list:list,
        trace_name_list:list
        ) -> go.Figure:
    """
        Возможные агрегатные функции: ['count', 'sum', 'avg', 'min', 'max']
    """
    fig = go.Figure()
    for y_name, aggregate_f, trace_name in zip(y_name_list, aggregate_f_list, trace_name_list):
        fig.add_trace(
            go.Histogram(
                x=data[x_name],
                y=data[y_name],
                name=trace_name,
                histfunc=aggregate_f,
                texttemplate="%{x}",
                textfont_size=20
                )
            )
    fig.update_layout(
        legend_orientation="h",
        legend=dict(x=.5, xanchor="center"),
        margin=dict(l=0, r=0, t=0, b=0)
        )
    return fig


if __name__ == "__main__":
    # fig = build_histogram(
    #     data=data,
    #     x_name='numbers',
    #     y_name='numbers',
    #     aggregate_f='sum'
    # )
    numbers = ["5", "10", "3", "10", "5", "8", "5", "5"]
    data = pd.DataFrame()
    data['numbers'] = numbers


    fig = build_multiple_histogram(
        data=data,
        x_name='numbers',
        y_name_list=['numbers', 'numbers'],
        aggregate_f_list=['count', 'sum'],
        trace_name_list=['count', 'sum']
    )
    fig.write_html('hist.html')