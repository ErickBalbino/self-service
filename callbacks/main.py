import re
import json
from dash import html
from server import app
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from plots import charts, choropleths
from store.components.main import get_iniciativas, get_categorias, \
                                  send_report_data
from store.visualization.main import get_usuarios_total, get_usuarios_iniciativa, \
                                    get_usuarios_periodo, get_usuarios_categoria, \
                                    get_usuarios_regiao, get_usuarios_cidade, \
                                    get_geojson_ceara

@app.callback(
    Output(component_id='iniciativa-dropdown', component_property='options'),
    Output(component_id="categoria-dropdown", component_property='options'),
    Input(component_id='iniciativa-dropdown', component_property='value'),
)
def load_options_components(initial):
    iniciativas = get_iniciativas()
    categorias = get_categorias()
    return iniciativas, categorias

@app.callback(
    Output(component_id='aprovados_total', component_property='children'),
    Output(component_id='chart-iniciativa', component_property='figure'),
    Output(component_id='chart-periodo', component_property='figure'),
    Output(component_id='chart-categoria', component_property='figure'),
    Output(component_id='chart-regiao', component_property='figure'),
    Output(component_id='choro-regiao', component_property='figure'),
    Output(component_id='choro-cidade', component_property='figure'),
    Input(component_id='iniciativa-dropdown', component_property='value'), 
    Input(component_id='categoria-dropdown', component_property='value'),
    Input(component_id='my-date-picker-range', component_property='start_date'),
    Input(component_id='my-date-picker-range', component_property='end_date')
)
def update_dashboard(iniciativa, categoria, start_date, end_date,):
    payload = {
        "iniciativas": iniciativa,
        "categories": categoria,
        "start_date": start_date,
        "end_date": end_date
    }

    payload = json.dumps(payload)

    usuarios_total = get_usuarios_total(payload)
    usuarios_iniciativa = get_usuarios_iniciativa(payload)
    usuarios_periodo = get_usuarios_periodo(payload)
    usuarios_categoria = get_usuarios_categoria(payload)
    usuarios_regiao = get_usuarios_regiao(payload)
    usuarios_cidade = get_usuarios_cidade()
    geojson_ceara = get_geojson_ceara()

    chart_usuarios_iniciativa = charts.usuarios_iniciativa(x=usuarios_iniciativa["iniciativa"],
                                                           y=usuarios_iniciativa["aprovados"])                       
    chart_usuarios_periodo = charts.usuarios_periodo(x=usuarios_periodo["periodo"],
                                                       y=usuarios_periodo["aprovados"])
    chart_usuarios_categoria = charts.usuarios_categoria(x=usuarios_categoria["categoria"],
                                                           y=usuarios_categoria["aprovados"])
    chart_usuarios_regiao = charts.usuarios_regiao(x=usuarios_regiao["regiao"],
                                                     y=usuarios_regiao["aprovados"])
    choro_usuarios_regiao = choropleths.inscritos_regiao(df_cidade=usuarios_cidade,
                                                        df_regiao=usuarios_regiao,
                                                        geojson=geojson_ceara)
    choro_usuarios_cidade = choropleths.inscritos_cidade(df=usuarios_cidade,
                                                          geojson=geojson_ceara)

    return usuarios_total, \
        chart_usuarios_iniciativa, \
        chart_usuarios_periodo, \
        chart_usuarios_categoria, \
        chart_usuarios_regiao, \
        choro_usuarios_regiao, \
        choro_usuarios_cidade

@app.callback(
    Output(component_id='status-report', component_property='children'),
    [Input(component_id='btn-send-email', component_property='n_clicks')],
    State(component_id='my-date-picker-range', component_property='start_date'),
    State(component_id='my-date-picker-range', component_property='end_date'),
    State(component_id='iniciativa-dropdown', component_property='value'), 
    State(component_id='categoria-dropdown', component_property='value'),
    State(component_id='email-input', component_property='value'),
    State(component_id='typeRelatorio-dropdown', component_property='value'),
)
def get_filters(n_clicks, data_inicio, data_fim, iniciativa, categoria, email, tipo_relatorio):
    if n_clicks == 0:
        return

    if email == None or tipo_relatorio == None or email == '':
        return html.P("Faltam dados! Por favor, verifique \
                       o campo de e-mail ou tipo de relatório",className="modal__feedback-email")

    if not re.fullmatch(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', email):
        return html.P("Email inválido! Por favor, insira novamente", className="modal__feedback-email")

    body = {
        "iniciativa": iniciativa,
        "categoria": categoria,
        "periodo_inicio": data_inicio,
        "periodo_fim": data_fim,
        "email": email,
        "template": tipo_relatorio
    }

    print(body)

    status_report = send_report_data(body)

    return status_report