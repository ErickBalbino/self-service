from os import EX_PROTOCOL
import plotly.express as px
import plotly.graph_objects as go


def usuarios_iniciativa(x=None, y=None):
    try:
        fig_usuarios_iniciativa = px.bar(x=x,
                    y=y,
                    orientation="v",
                    labels=dict(x=" ", y=" "))
    except Exception as e:
        fig_usuarios_iniciativa = {}
    return fig_usuarios_iniciativa
        

def usuarios_periodo(x=None, y=None):  
    try:  
        fig_usuarios_periodo = px.bar(x=x,
                    y=y,
                    orientation="v",
                    labels=dict(x=" ", y=" "))
    except Exception as e:
        fig_usuarios_periodo = {}
    return fig_usuarios_periodo


def usuarios_categoria(x=None, y=None):
    try: 
        fig_usuarios_categoria = px.bar(x=x,
                    y=y,
                    orientation="v",
                    labels=dict(x=" ", y=" "))
    except Exception as e:
        fig_usuarios_categoria = {}
    return fig_usuarios_categoria


def usuarios_regiao(x=None, y=None):
    try:
        fig_usuarios_regiao = px.bar(x=x,
                    y=y,
                    orientation="v",
                    labels=dict(x=" ", y=" "))
        fig_usuarios_regiao.update_layout( xaxis = go.layout.XAxis( tickangle = 45) )
        return fig_usuarios_regiao
    except Exception as e:
        fig_usuarios_regiao = {}
    return fig_usuarios_regiao