import requests
import tldextract
import whois
from bs4 import BeautifulSoup
from datetime import datetime
import re

def get_domain_info(url):
    domain_info = {
        'Have_IP': 0,
        'Have_At': 0,
        'URL_Length': 0,
        'URL_Depth': 0,
        'Redirection': 0,
        'https_Domain': 0,
        'TinyURL': 0,
        'Prefix/Suffix': 0,
        'DNS_Record': 0,
        'Web_Traffic': 0,
        'Domain_Age': 0,
        'Domain_End_0': 0,
        'Domain_End_1': 0,
        'iFrame': 0,
        'Mouse_Over': 0,
        'Right_Click': 0,
        'Web_Forwards': 0
    }

    # Extrair informações do domínio
    ext = tldextract.extract(url)
    domain = f"{ext.domain}.{ext.suffix}"
    domain_info['Domain'] = domain

    # Verificar se o domínio possui IP
    try:
        ip = requests.get(url).raw._connection.sock.getpeername()[0]
        domain_info['Have_IP'] = 1
    except Exception as e:
        pass

    # Verificar se a URL contém "@"
    domain_info['Have_At'] = 1 if "@" in url else 0

    # Comprimento da URL
    domain_info['URL_Length'] = len(url)

    # Profundidade da URL
    domain_info['URL_Depth'] = url.count('/') - 2

    # Redirecionamentos
    try:
        response = requests.get(url, allow_redirects=True)
        domain_info['Redirection'] = len(response.history)
    except Exception as e:
        pass

    # Verificar se usa HTTPS
    domain_info['https_Domain'] = 1 if url.startswith("https") else 0

    # Verificar se é TinyURL
    tinyurl_services = ["tinyurl.com", "bit.ly", "goo.gl", "t.co"]
    domain_info['TinyURL'] = 1 if ext.domain in tinyurl_services else 0

    # Verificar se possui hífen ou prefixo/sufixo suspeito
    domain_info['Prefix/Suffix'] = 1 if '-' in domain else 0

    # Verificar registros DNS
    try:
        dns_info = whois.whois(domain)
        domain_info['DNS_Record'] = 1 if dns_info else 0
    except Exception as e:
        pass

    # Tráfego web (usando um proxy para simular tráfego; normalmente precisa de uma API paga)
    domain_info['Web_Traffic'] = 0  # Placeholder

    # Idade do domínio
    try:
        creation_date = dns_info.creation_date
        if isinstance(creation_date, list):
            creation_date = creation_date[0]
        domain_age = (datetime.now() - creation_date).days // 365
        domain_info['Domain_Age'] = domain_age
    except Exception as e:
        pass

    # Extensão do domínio
    domain_info['Domain_End_0'] = 1 if ext.suffix == "com" else 0
    domain_info['Domain_End_1'] = 1 if ext.suffix == "org" else 0

    # Verificar iFrames
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        domain_info['iFrame'] = 1 if soup.find('iframe') else 0
    except Exception as e:
        pass

    # Verificar Mouse Over
    try:
        domain_info['Mouse_Over'] = 1 if re.search(r'onmouseover', response.text, re.IGNORECASE) else 0
    except Exception as e:
        pass

    # Verificar Right Click
    try:
        domain_info['Right_Click'] = 1 if re.search(r'contextmenu', response.text, re.IGNORECASE) else 0
    except Exception as e:
        pass

    # Verificar Web Forwards (Placeholder)
    domain_info['Web_Forwards'] = 0  # Placeholder

    return domain_info


