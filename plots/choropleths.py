# Constantes auxiliares plotagem Ceará
import plotly.express as px


LAT = -5.30
LON = -39.35
ZOOM = 5.8


def inscritos_cidade(df=None, geojson=None):
    try:
        choropleph_chart = px.choropleth_mapbox(df,
                                                geojson=geojson,
                                                color_continuous_scale="greens",
                                                locations="cidade",
                                                featureidkey="properties.name",
                                                color=df.inscritos,
                                                width=100,
                                                center={"lat": LAT, "lon": LON},
                                                mapbox_style="carto-positron",
                                                zoom=ZOOM)
        choropleph_chart.update_layout(margin=dict(r=0, t=0, l=0, b=0))
    except Exception as e:
        print(f'inscritos_cidade_choropleth: {e}')
        choropleph_chart = {}
    return {}


def inscritos_regiao(df_cidade=None, df_regiao=None, geojson=None):
    try:
        df_cidade['inscritos_regiao'] = df_cidade.apply(lambda x: df_regiao[df_regiao['regiao']==x['regiao']]['inscritos'].values[0], axis=1)
        color_a = 'rgb(213,238,207)'    
        color_b = 'rgb(149,211,145)'
        color_c = 'rgb(74,175,97)'
        color_d = 'rgb(44,141,54)'
        color_discrete_map = {'Grande Fortaleza': color_a, 'Sertão de Crateús': color_a,
                            'Litoral Norte': color_a, 'Centro Sul': color_a, 'Vale do Jaguaribe': color_b,
                            'Sertão de Canindé': color_b, 'Serra da Ibiapaba': color_b, 'Cariri': color_b,
                            'Sertão de Sobral': color_c, 'Litoral Leste': color_c, 'Sertão Central': color_c,
                            'Maciço de Baturité': color_d, 'Sertão dos Inhamuns': color_d,
                            'Litoral Oeste / Vale do Curu': color_d}

        choropleph_chart = px.choropleth_mapbox(df_cidade, 
                                                geojson=geojson,
                                                locations="cidade",
                                                featureidkey="properties.name",
                                                color=df_cidade.regiao,
                                                center={"lat": LAT, "lon": LON},
                                                mapbox_style="carto-positron",
                                                zoom=ZOOM,
                                                hover_data=[ 'inscritos_regiao', 'inscritos'],
                                                color_discrete_map=color_discrete_map,
                                                labels={'regiao': 'Região',
                                                        'inscritos_regiao': 'inscritos (Região)',
                                                        'cidade': 'Cidade', 'inscritos': 'inscritos (Cidade)'})
        choropleph_chart.update_layout(
            hoverlabel=dict(
                bgcolor="white",
                font_size=16,
                font_family="Roboto"))
        choropleph_chart.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    except Exception as e:
        choropleph_chart = {}
    return {}