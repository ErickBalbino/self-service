import requests
import os
import json

URL_API_DROPDOWN = os.getenv('URL_API_DROPDOWN')
URL_API_REPORT = os.getenv('URL_API_REPORT')
URL_FAKE_API = os.getenv('URL_FAKE_API')

from app import logger

def get_ano():
    try:
        response = requests.get(URL_API_DROPDOWN + '/anos')
        logger.info(response.status_code, response.url.split('/')[-1])
        res_json = response.json()
        results = res_json['results']
        logger.info('requisição do ano feita com sucesso')
        return results
    except Exception as e:
        logger.error(f'request ano: {e}')
        return []


def get_mes():
    try:
        response = requests.get(URL_API_DROPDOWN + '/meses')
        logger.info(response.status_code, response.url.split('/')[-1])
        res_json = response.json()
        results = res_json['results']
        logger.info('requisição do mês feita com sucesso')
        return results
    except Exception as e:
        logger.error(f'request mes: {e}')
        return []


def get_iniciativas():
    try:
        response = requests.get(URL_API_DROPDOWN + '/iniciativas')
        logger.info(response.status_code, response.url.split('/')[-1])
        res_json = response.json()
        results = res_json['results']
        logger.info('requisição da iniciativa feita com sucesso')
        return results
    except Exception as e:
        logger.error(f'request iniciativas: {e}')
        return []


def get_categorias():
    try:
        response = requests.get(URL_API_DROPDOWN + '/categorias')
        logger.info(response.status_code, response.url.split('/')[-1])
        res_json = response.json()
        results = res_json['results']
        logger.info('requisição da categoria feita com sucesso')
        return results
    except Exception as e:
        logger.error(f'request categorias: {e}')
        return []


def send_report_data(body):
    try:
        response = requests.post(URL_API_REPORT, 
                                 data=json.dumps(body), 
                                 headers={"Content-type": "application/json"})
        logger.info(response.status_code, response.url.split('/')[-1])
    except Exception as e:
        logger.error(f'requests send_filters: {e}')
        return []
