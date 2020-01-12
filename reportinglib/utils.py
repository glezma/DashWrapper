import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go

def Header(app):
    # return html.Div([get_header(app), html.Br([]), get_menu()])
    return html.Div([get_header(app), html.Br([])])


def get_header(app):
    header = html.Div(
        [
            html.Div(
                [
                    html.Img(
                        src=app.get_asset_url("bcplogo.png"),
                        className="logo",
                    ),
                    # html.A(
                    #     html.Button("Learn More", id="learn-more-button"),
                    #     href="https://plot.ly/dash/pricing/",
                    # ),
                ],
                className="row",
            ),
            html.Div(
                [
                    html.Div(
                        [html.H5("Reporte Semanal del producto Hipotecario")],
                        className="seven columns main-title",
                    ),
                    # html.Div(
                    #     [
                    #         dcc.Link(
                    #             "Ver todo",
                    #             href="/dash-financial-report/full-view",
                    #             className="full-view-link",
                    #         )
                    #     ],
                    #     className="five columns",
                    # ),
                ],
                className="twelve columns",
                style={"padding-left": "0"},
            ),
        ],
        className="row",
    )
    return header


def get_menu():
    menu = html.Div(
        [
            dcc.Link(
                "Resumen",
                href="/dash-financial-report/overview",
                className="tab first",
            ),
            dcc.Link(
                "Monitoreo de inputs",
                href="/dash-financial-report/price-performance",
                className="tab",
            ),
            dcc.Link(
                "Monitoreo de outputs",
                href="/dash-financial-report/portfolio-management",
                className="tab",
            ),
            dcc.Link(
                "Acapite 0", href="/dash-financial-report/fees", className="tab"
            ),
            dcc.Link(
                "Acapite 1",
                href="/dash-financial-report/distributions",
                className="tab",
            ),
            dcc.Link(
                "Acapite 2",
                href="/dash-financial-report/news-and-reviews",
                className="tab",
            ),
        ],
        className="row all-tabs",
    )
    return menu


def make_dash_table(df):
    """ Return a dash definition of an HTML table for a Pandas dataframe """
    table = []
    html_row = [df.index.name]
    row = df.columns
    for i in range(len(row)):
            html_row.append(html.Td([row[i]]))
    table.append(html.Tr(html_row))

    for index, row in df.iterrows():
        html_row = [index]
        for i in range(len(row)):
            html_row.append(html.Td([row[i]]))
        table.append(html.Tr(html_row))
    return table


def plotgraph1(df, color=0):
    '''
    Grafico de barras
    '''

    data = list()
    if color==0:
        color = ["#294971","#dddddd"]*3
    else:
        color = color*9
    for ii in range(df.shape[1]):
        elem = go.Bar(
                        x=df.index.to_list(),
                        y=df[df.columns[ii]].to_list(),
                        marker={
                            "color": color[ii],
                            "line": {
                                "color": "rgb(255, 255, 255)",
                                "width": 2,
                            },
                        },
                        name=df.columns[ii],
                        text=df[df.columns[ii]].to_list(),
                        textposition='auto',
                        )
        data.append(elem)

    return dcc.Graph(
                # id="graph-1",
                figure={
                    "data": data,
                    "layout": go.Layout(
                        autosize=False,
                        bargap=0.35,
                        font={"family": "Raleway", "size": 10},
                        height=200,
                        hovermode="closest",
                        legend={
                            "x": -0.0228945952895,
                            "y": -0.189563896463,
                            "orientation": "h",
                            "yanchor": "top",
                        },
                        margin={
                            "r": 0,
                            "t": 20,
                            "b": 10,
                            "l": 30,
                        },
                        showlegend=True,
                        title="",
                        width=280,
                        xaxis={
                            "autorange": True,
                            # "range": [-0.5, 4.5],
                            "showline": True,
                            "title": "",
                            "type": "category",
                        },
                        yaxis={
                            "autorange": True,
                            # "range": [0, 22.9789473684],
                            "showgrid": True,
                            "showline": True,
                            "title": "",
                            "type": "linear",
                            "zeroline": False,
                        },
                    ),
                },
                config={"displayModeBar": False},
            )



def plotgraph2(df, color=0):
    '''
    Grafico de lineas
    '''
    data = list()
    if color==0:
        color = ["#294971","#dddddd"]*9
    else: 
        color = color*9
    for ii in range(df.shape[1]):
        # import pdb as pdb
        # pdb.set_trace()
        elem = go.Scatter(
                            x=df.index,
                            y=df[df.columns[ii]],
                            line={"color": color[ii]},
                            mode="lines",
                            name=df.columns[ii],
                        )
        data.append(elem)
    
    return dcc.Graph(
                                        # id="graph-2",
                                        figure={
                                            "data": data,
                                            "layout": go.Layout(
                                                autosize=True,
                                                title="",
                                                font={"family": "Raleway", "size": 10},
                                                height=200,
                                                # width=700,
                                                hovermode="closest",
                                                legend={
                                                    "x": -0.0277108433735,
                                                    "y": -0.142606516291,
                                                    "orientation": "h",
                                                },
                                                margin={
                                                    "r": 20,
                                                    "t": 20,
                                                    "b": 20,
                                                    "l": 50,
                                                },
                                                showlegend=True,
                                                xaxis={
                                                    "autorange": True,
                                                    "linecolor": "rgb(0, 0, 0)",
                                                    "linewidth": 1,
                                                    # "range": [2008, 2018],
                                                    "showgrid": False,
                                                    "showline": True,
                                                    "title": "",
                                                    "type": "linear",
                                                },
                                                yaxis={
                                                    "autorange": True,
                                                    "gridcolor": "rgba(127, 127, 127, 0.2)",
                                                    "mirror": False,
                                                    "nticks": 4,
                                                    # "range": [0, 30000],
                                                    "showgrid": True,
                                                    "showline": True,
                                                    "ticklen": 10,
                                                    "ticks": "outside",
                                                    "title": "",
                                                    "type": "linear",
                                                    "zeroline": False,
                                                    "zerolinewidth": 4,
                                                },
                                            ),
                                        },
                                        config={"displayModeBar": False},
                                    )
 
