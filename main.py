import requests as req
import socket
import logging
import time

logging.basicConfig(
    filename='status_site.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def get_site(url_para_ip):
    try:
        return socket.gethostbyname(url_para_ip)
    except socket.gaierror as e:
        logging.error(f'Erro ao obter o IP do site {e}')

def checarStatus(url, url_para_ip):
    try:
        response = req.get(url)
        if response.status_code == 200:
            logging.info(f"Site funcionando OK! Status: {response.status_code}, IP: {get_site(url_para_ip)}")
            print(f"Site funcionando OK! Status: {response.status_code}, IP: {get_site(url_para_ip)}")
        else:
            logging.warning(f"Site caiu (NOK)! Status code: {response.status_code}, IP: {get_site(url_para_ip)}")
            print(f"Site caiu (NOK)! Status code: {response.status_code}, IP: {get_site(url_para_ip)}")
    except req.exceptions.RequestException as e:
        logging.error(f"Exception ao enviar requisição. {e}")

def monitoramento(url, url_para_ip):
    while True:
        checarStatus(url, url_para_ip)
        time.sleep(3)

if __name__ == '__main__':
    link = input('digite o link do site http://')
    monitoramento(f'https://{link}', link)