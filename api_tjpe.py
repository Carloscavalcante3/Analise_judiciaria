import requests
import json
import csv

# Caso necessário, alterar chave pós "ApiKey" pela chave atualizada do site do CNJ
url = "https://api-publica.datajud.cnj.jus.br/api_publica_tjpe/_search"
headers = {
    'Authorization': 'ApiKey cDZHYzlZa0JadVREZDJCendQbXY6SkJlTzNjLV9TRENyQk1RdnFKZGRQdw==',
    'Content-Type': 'application/json'
}

total = 25

queries = [
    {"match": {"classe.nome": "Execução Fiscal"}},
    {"match": {"classe.nome": "Divórcio Litigioso"}},
    {"match": {"classe.nome": "Busca e Apreensão em Alienação Fiduciária"}},
    {"match": {"assuntos.nome": "Tráfico de Drogas e Condutas Afins"}}
]

todos_os_processos = []
tamanho_busca = total // len(queries)

for query in queries:
    payload = json.dumps({
        "size": tamanho_busca,
        "query": query,
        "_source": [
            "numeroProcesso", "classe.nome", "orgaoJulgador.nome",
            "assuntos.nome", "dataAjuizamento", "dataBaixa"
        ]
    })
    
    response = requests.post(url, headers=headers, data=payload)
    dados = response.json()
    todos_os_processos.extend(dados.get("hits", {}).get("hits", []))

with open("bd.csv", "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f)
    writer.writerow(["id_processo", "classe", "orgao_julgador", "assunto", "data_inicio", "data_fim"])

    for item in todos_os_processos:
        fonte = item.get("_source", {})
        writer.writerow([
            fonte.get("numeroProcesso", ""),
            fonte.get("classe", {}).get("nome", ""),
            fonte.get("orgaoJulgador", {}).get("nome", ""),
            (fonte.get("assuntos", [{}])[0].get("nome", "")) if fonte.get("assuntos") else "",
            fonte.get("dataAjuizamento", ""),
            fonte.get("dataBaixa", "")
        ])