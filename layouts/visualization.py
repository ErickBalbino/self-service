from dash import html
from dash import dcc


dashboard_visualization = html.Div([
    html.Div([
        html.Div([
            html.P('Total de aprovados: ', className="dashboard__header__info__text"),
            
            dcc.Loading(id="loading-text", children=[html.P(className="dashboard__header__info__value", id="aprovados_total")], type="circle"),
        ], className="dashboard__header__info"),
        html.A([
            html.Abbr(html.Img(src="/assets/export.png",
                                className="dashboard__header__img-export", id="btn-abrir-modal"),
                                title="Exportar pdf")
        ])
    ], className="dashboard__header"),
    html.Div([
        html.Div([
            html.Div([
                dcc.Loading(
                    id="loading-1",
                    type="default",
                    children=[
                        dcc.Graph(id="chart-iniciativa")
                    ]
                )
                ], className="graphs__graph__img"),
            html.H3('Aprovados por iniciativa', className="graphs__graph__title"),
        ], className="graphs__graph", id="graph1"),

        html.Div([
            html.Div([
                dcc.Loading(
                    id="loading-2",
                    type="default",
                    children=[
                        dcc.Graph(id="chart-periodo")
                    ]
                )
            ], className="graphs__graph__img"),
            html.H3('Aprovados capacitados por mês', className="graphs__graph__title"),
        ], className="graphs__graph", id="graph2"),

        html.Div([
            html.Div([
                dcc.Loading(
                    id="loading-3",
                    type="default",
                    children=[
                        dcc.Graph(id="chart-categoria")
                    ]
                )
            ], className="graphs__graph__img"),
            html.H3('Aprovados por categoria', className="graphs__graph__title"),
        ], className="graphs__graph", id="graph3"),

        html.Div([
            html.Div([
                dcc.Loading(
                    id="loading-4",
                    type="default",
                    children=[
                        dcc.Graph(id="chart-regiao")
                    ]
                )
            ], className="graphs__graph__img"),
            html.H3('Aprovados por região', className="graphs__graph__title"),
        ], className="graphs__graph", id="graph4"),

        html.Div([
            html.Div([
                dcc.Loading(
                    id="loading-5",
                    type="default",
                    children=[
                        dcc.Graph(id="choro-regiao")
                    ]
                )
            ], className="graphs__graph-map__img"),
            html.P('Aprovados por região', className="graphs__graph__title"),
        ], className="graphs__graph", id="graph5"),

        html.Div([
            html.Div([
                dcc.Loading(
                    id="loading-6",
                    type="default",
                    children=[
                        dcc.Graph(id="choro-cidade")
                    ]
                )
            ], className="graphs__graph-map__img"),
            html.P('Aprovados por cidade', className="graphs__graph__title"),
        ], className="graphs__graph", id="graph6"),
    ], className="graphs-area")
], className="dashboard",id="dashboard")