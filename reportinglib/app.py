# -*- coding: utf-8 -*-

import pandas as pd
import pathlib
import dash_core_components as dcc
import dash_html_components as html
from utils import Header, make_dash_table, plotgraph1, plotgraph2

# import pdb as pdb
# pdb.set_trace()
import dash
from dash.dependencies import Input, Output
from pages import (
    overview,
    pricePerformance,
    portfolioManagement,
    feesMins,
    distributions,
    newsReviews,
)

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("data").resolve()
ASSETS_PATH = PATH.joinpath("assets").resolve()

# Pagina 1
# Datos
df_1 = pd.read_csv(DATA_PATH.joinpath("hip_df1.csv"))
df_1.loc[:,['Fecha']] = pd.to_datetime(df_1['Fecha'],format='%Y-%m-%d')
df_1_table = df_1.set_index(['Fecha'])
df_2 = pd.read_csv(DATA_PATH.joinpath("df_price_perf.csv"))     
# df_plot1 = pd.read_csv(DATA_PATH.joinpath("df_graph1.csv"))
# df_plot1 = df_plot1.set_index(['year'])
df_plot2 = pd.read_csv(DATA_PATH.joinpath("df_graph2.csv"))
df_plot2 = df_plot2.set_index(['year'])
# Objetos
table1 = html.Table(make_dash_table(df_1_table.tail(8)),className="medium-header")
ult = df_1.tail(1)['Compra de deuda'].values[0]
TituloDinamico='El ultimo dato de venta nueva fue {} y {} para compra de deuda'.format(ult,ult)
table2 = html.Table(make_dash_table(df_2))
graph1 = plotgraph2(df_1)
graph2 = plotgraph1(df_plot2)
graph3 = plotgraph2(df_plot2)
image1 = html.Img(
                        src=ASSETS_PATH.joinpath("risk_reward.png"),
                        className="risk-reward", )
paragraph1 = html.P(
                            "\
                        As the industry’s first index fund for individual investors, \
                        the Calibre Index Fund is a low-cost way to gain diversified exposure",
                            style={"color": "#ffffff"},
                            className="row",
                        )
report_list1 =   [   [('Product Highlights',paragraph1,"product")],
                    [('Titulo de tabla', table1,"six columns"),('Nombre Grafico 1', graph1,"six columns" )],
                    [('Monto',graph2,"six columns"),('Monto',graph2,"six columns")],
                    [('Tabla 2',table2,"six columns"),('Imagen 1',table2,"six columns")],
                    # [('Monto 2',graph2,"six columns"),('Monto 2',graph1,"six columns")],
                ]

# Pagina 2
# Datos
df_current_prices = pd.read_csv(DATA_PATH.joinpath("df_current_prices.csv"))
df_hist_prices = pd.read_csv(DATA_PATH.joinpath("df_hist_prices.csv"))
df_avg_returns = pd.read_csv(DATA_PATH.joinpath("df_avg_returns.csv"))
df_after_tax = pd.read_csv(DATA_PATH.joinpath("df_after_tax.csv"))
df_recent_returns = pd.read_csv(DATA_PATH.joinpath("df_recent_returns.csv"))
df_graph = pd.read_csv(DATA_PATH.joinpath("df_graph.csv"))

# Objetos
table_cp = html.Table(make_dash_table(df_current_prices))
table2 = html.Table(make_dash_table(df_2))
graph5 = plotgraph2(df_graph)
report_list2 =   [   [('Current Prices',table_cp,"six columns"),('Current Prices',table_cp,"six columns")],
                    [('Nombre Tabla 1', table1,"six columns"),('Nombre Grafico 1', graph1,"six columns" )],
                    [('Monto',graph5,"twelve columns")],
                    [('Tabla 2',table2,"six columns"),('Imagen 1',table2,"six columns")],
                    [('Monto 2',graph2,"six columns"),('Monto 2',graph1,"six columns")],
                ]

# Application
app = dash.Dash(
    __name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}]
                )

# Describe the layout/ UI of the app
app.layout = html.Div(
    [dcc.Location(id="url", refresh=False), html.Div(id="page-content")]
)

# Update page
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    return (
        overview.create_layout(app, report_list1),
        overview.create_layout(app, report_list2),
        # pricePerformance.create_layout(app),
        # portfolioManagement.create_layout(app),
        # feesMins.create_layout(app),
        # distributions.create_layout(app),
        # newsReviews.create_layout(app),
    )


if __name__ == "__main__":
    app.run_server(debug=True)
