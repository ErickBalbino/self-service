from dash import html
from dash import dcc


dashboard_modal = html.Div([
    html.I(className="far fa-times-circle", id="btn-fechar-modal"),
    html.H2("Envio de relatório por e-mail", className="modal__header"),
    html.Hr(className="modal__line"),       
    html.Div([
        html.Div([
            html.H3("E-mail:", className="modal__title"),
            dcc.Input(
                type="email",
                id="email-input",
                className="modal__input-email",
                placeholder="Informe seu email..."
            ),
            html.H3("Tipo de Relatório:", className="modal__title"),
            dcc.Dropdown(
                id='typeRelatorio-dropdown', 
                clearable=False, 
                options=[
                    {'label': 'Professores capacitados', 'value': 'PROFISSIONAL-CAPACITADO'},
                    {'label': 'Alunos capacitados', 'value': 'ALUNO-CAPACITADO'}
                ],
                className="modal__dropdown",
                placeholder="Selecione o tipo de relatório",
            ),
        ], className="modal__body__container__fields"),
        
        html.Div([
            html.Img(src="assets/icone_relatorio.png")
        ], className="modal__body__container__image")
    ], className="modal__body__container"),
    html.P(id='status-report'),
    html.Div([
        html.Button('Enviar', className="modal__button", id='btn-send-email', n_clicks=0),
    ], className="modal__footer"),
], className="modal", id="modal")
