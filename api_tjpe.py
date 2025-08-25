import requests
import json
import csv
from datetime import datetime

url = "https://api-publica.datajud.cnj.jus.br/api_publica_tjpe/_search"
headers = {
    'Authorization': 'ApiKey SUA_CHAVE_AQUI',
    'Content-Type': 'application/json'
}

payload = json.dumps({
    "size": 100, 
    "query": {"match_all": {}},
    "_source": [
        "numeroProcesso",
        "classe.nome",
        "orgaoJulgador.nome",
        "assuntos.nome",
        "dataAjuizamento",
        "dataBaixa"
    ]
})

response = requests.post(url, headers=headers, data=payload)
dados = response.json()

with open("bd.csv", "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f)
    writer.writerow(["id_processo", "classe", "orgao_julgador", "assunto", "data_inicio", "data_fim"])

    for item in dados.get("hits", {}).get("hits", []):
        fonte = item.get("_source", {})
        writer.writerow([
            fonte.get("numeroProcesso", ""),
            fonte.get("classe", {}).get("nome", ""),
            fonte.get("orgaoJulgador", {}).get("nome", ""),
            (fonte.get("assuntos", [{}])[0].get("nome", "")) if fonte.get("assuntos") else "",
            fonte.get("dataAjuizamento", ""),
            fonte.get("dataBaixa", "")
        ])
