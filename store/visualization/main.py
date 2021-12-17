import requests
import pandas as pd
import os
import json

from store.components.main import URL_FAKE_API

URL_API = os.getenv('URL_API')


def get_usuarios_total(payload):
    try:
        response = requests.get(URL_API, 
                                data=payload,
                                headers={'Content-Type':'application/json'})
        print(response.status_code, response.url.split('/')[-1])
        res_json = response.json()
        results = res_json['results'][0]['aprovados_total']
        return results
    except Exception as e:
        print(f'request usuarios total: {e}')
        return []


def get_usuarios_iniciativa(payload):
    try:
        response = requests.get(URL_API + '/iniciativas', 
                                data=payload, 
                                headers={'Content-Type':'application/json'})
        print(response.status_code, response.url.split('/')[-1])
        res_json = response.json()
        results = res_json['results']
        df = pd.DataFrame(results)
        df['aprovados'] = pd.to_numeric(df['aprovados'])
        df = df.sort_values(by=['aprovados'], ascending=True)
        return df
    except Exception as e:
        print(f'request usuarios iniciativa: {e}')
        return []


def get_usuarios_periodo(payload):
    try:
        response = requests.get(URL_API + '/periodo', 
                                data=payload, 
                                headers={'Content-Type':'application/json'})
        print(response.status_code, response.url.split('/')[-1])
        res_json = response.json()
        results = res_json['results']
        df = pd.DataFrame(results)
        return df
    except Exception as e:
        print(f'request usuarios periodo: {e}')
        return []


def get_usuarios_categoria(payload):
    try:
        response = requests.get(URL_API + '/categoria',
                                data=payload,
                                headers={'Content-Type':'application/json'})
        print(response.status_code, response.url.split('/')[-1])
        res_json = response.json()
        results = res_json['results']
        df = pd.DataFrame(results)
        return df
    except Exception as e:
        print(f'request usuarios categoria: {e}')
        return []


def get_usuarios_regiao(payload):
    try:
        response = requests.get(URL_API + '/regiao',
                                data=payload,
                                headers={'Content-Type':'application/json'})
        print(response.status_code, response.url.split('/')[-1])
        res_json = response.json()
        results = res_json['results']
        df = pd.DataFrame(results)
        return df
    except Exception as e:
        print(f'request usuarios regiao: {e}')
        return []


def get_geojson_ceara():
    try:
        with open("store/json/geojson_ceara.json") as file:
            geojson_ceara = json.load(file)
        return geojson_ceara
    except Exception as e:
        print(f'request geojson: {e}')
        return []


def get_usuarios_cidade():
    try:
        with open("store/json/inscritos_cidade.json") as file:
            inscritos_cidade = json.load(file)
       
        df = pd.DataFrame(inscritos_cidade)

        with open("store/json/translate_cities.json") as file:
            translator = pd.DataFrame(json.load(file))

        for i, item in df.iterrows():
            city = translator[translator['city_api']==item['cidade']]
            if city.shape[0]:
                correct_name = city['city'].values[0]
                df.loc[i, 'cidade'] = correct_name
        return df
    except Exception as e:
        print(f'request usuarios cidade: {e}')
        return []
    
