import requests
import os

URL_API_DROPDOWN = os.getenv('URL_API_DROPDOWN')
URL_API_REPORT = os.getenv('URL_API_REPORT')
URL_FAKE_API = os.getenv('URL_FAKE_API')


def get_ano():
    try:
        response = requests.get(URL_API_DROPDOWN + '/anos')
        print(response.status_code, response.url.split('/')[-1])
        res_json = response.json()
        results = res_json['results']
        return results
    except Exception as e:
        print(f'request ano: {e}')
        return []


def get_mes():
    try:
        response = requests.get(URL_API_DROPDOWN + '/meses')
        print(response.status_code, response.url.split('/')[-1])
        res_json = response.json()
        results = res_json['results']
        return results
    except Exception as e:
        print(f'request mes: {e}')
        return []


def get_iniciativas():
    try:
        response = requests.get(URL_API_DROPDOWN + '/iniciativas')
        print(response.status_code, response.url.split('/')[-1])
        res_json = response.json()
        results = res_json['results']
        return results
    except Exception as e:
        print(f'request iniciativas: {e}')
        return []


def get_categorias():
    try:
        response = requests.get(URL_API_DROPDOWN + '/categorias')
        print(response.status_code, response.url.split('/')[-1])
        res_json = response.json()
        results = res_json['results']
        return results
    except Exception as e:
        print(f'request categorias: {e}')
        return []


def send_report_data(body):
    try:
        response = requests.post(URL_API_REPORT, data=body)
        print(response.status_code, response.url.split('/')[-1])
    except Exception as e:
        print(f'requests send_filters: {e}')
        return []
