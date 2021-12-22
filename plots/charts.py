import plotly.express as px
import plotly.graph_objects as go
from app import logger

color = '#058D3E'

def usuarios_iniciativa(x=None, y=None):
    try:
        fig_usuarios_iniciativa = px.bar(x=x,
                    y=y,
                    orientation="v",
                    color_discrete_sequence = [color],
                    labels=dict(x=" ", y=" "))
        logger.info('Fig iniciativa carregado com sucesso')
    except Exception as e:
        logger.error(f'fig_inscritos_iniciativa: {e}')
        fig_usuarios_iniciativa = {}
    return fig_usuarios_iniciativa
        

def usuarios_periodo(x=None, y=None):  
    try:  
        fig_usuarios_periodo = px.bar(x=x,
                    y=y,
                    color_discrete_sequence = [color],
                    orientation="v",
                    labels=dict(x=" ", y=" "))
        logger.info('Fig periodo carregado com sucesso')
    except Exception as e:
        logger.error(f'fig_inscritos_periodo: {e}')
        fig_usuarios_periodo = {}
    return fig_usuarios_periodo


def usuarios_categoria(x=None, y=None):
    try: 
        fig_usuarios_categoria = px.bar(x=x,
                    y=y,
                    orientation="v",
                    color_discrete_sequence = [color],
                    labels=dict(x=" ", y=" "))
        logger.info('Fig categoria carregado com sucesso')
    except Exception as e:
        logger.error(f'fig_inscritos_categoria: {e}')
        fig_usuarios_categoria = {}
    return fig_usuarios_categoria


def usuarios_regiao(x=None, y=None):
    try:
        fig_usuarios_regiao = px.bar(x=x,
                    y=y,
                    orientation="v",
                    color_discrete_sequence = [color],
                    labels=dict(x=" ", y=" "))
        fig_usuarios_regiao.update_layout( xaxis = go.layout.XAxis( tickangle = 45) )
        logger.info('Fig regiao carregado com sucesso')
        return fig_usuarios_regiao
    except Exception as e:
        logger.error(f'fig_inscritos_regiao: {e}')
        fig_usuarios_regiao = {}
    return fig_usuarios_regiao