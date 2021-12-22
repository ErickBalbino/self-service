from dash import html
from dash import dcc
from datetime import date
from dateutil.relativedelta import relativedelta

dashboard_filters = html.Div([
    html.Div([
        html.P('Data', className="panel__item-filter__dropdown-label"),
        dcc.DatePickerRange(
            id='my-date-picker-range',
            className="panel__item-filter__dropdown",
            min_date_allowed=date(2016, 1, 1),
            max_date_allowed=date.today(),
            initial_visible_month=date.today(),
            start_date=date.today() - relativedelta(years=1),
            end_date=date.today(),
            display_format='DD/MM/YYYY',
        ),
        html.Div(id='output-container-date-picker-range')   
    ], className="panel__item-filter"),
    html.Div([
        html.P('Iniciativa', className="panel__item-filter__dropdown-label"),
        html.Div(dcc.Dropdown(
            id='iniciativa-dropdown', 
            clearable=False, 
            value=[],
            className="panel__item-filter__dropdown",
            placeholder="Selecione a iniciativa",
            multi=True
        )),
    ], className="panel__item-filter"),
    html.Div([
        html.P('Categoria', className="panel__item-filter__dropdown-label"),
        html.Div(dcc.Dropdown(
            id='categoria-dropdown',  
            clearable=False,
            className="panel__item-filter__dropdown",
            value = [],
            placeholder="Selecione a categoria",
            multi=True
        )),
    ], className="panel__item-filter")
], className="panel__bar",)
