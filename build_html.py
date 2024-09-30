import plotly.express as px
from jinja2 import Template


def make_dashboard(
        output_html_path:str,
        input_template_path:str,
        figs:list,

    ):
    """
        output_html_path=r"output.html"
        input_template_path = r"templates/template.html"
    """

    plotly_jinja_data = dict()
    for num, fig in enumerate(figs): # Здесь нужно понять как вставлять графики
        plotly_jinja_data[f'fig{num}'] = fig.to_html(full_html=False)

    with open(output_html_path, "w", encoding="utf-8") as output_file:
        with open(input_template_path) as template_file:
            j2_template = Template(template_file.read())
            output_file.write(j2_template.render(plotly_jinja_data))