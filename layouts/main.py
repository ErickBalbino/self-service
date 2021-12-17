from dash import html
from layouts.inputs import dashboard_filters
from layouts.visualization import dashboard_visualization
from layouts.modal import dashboard_modal


layout = html.Div([
    html.Div([
        html.P('Painel de Acompanhamento de Aprovados', className='panel__title'),
        dashboard_filters,
        html.Img(src="/assets/logo-ced.png", className="panel__logo")
    ], className="panel", id="panel"),
    dashboard_visualization,
    dashboard_modal
], className="page")