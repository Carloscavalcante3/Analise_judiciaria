# 📊 Análise Exploratória de Dados de Processos Judiciais do TJPE

Este projeto é um case de Data Science que tem como objetivo analisar dados de processos judiciais obtidos por meio da API Pública do DataJud, disponibilizada pelo Conselho Nacional de Justiça (CNJ) para extrair insights sobre a volumetria e a duração de diferentes classes de processos no Tribunal de Justiça de Pernambuco (TJPE).

## Objetivo
- Realizar a ingestão de dados judiciais via **API REST** utilizando **Python** e a biblioteca **requests**.
- Aplicar técnicas de pré-processamento e engenharia de atributos com pandas para calcular métricas de duração.
- Desenvolver um dashboard para análise exploratória com **matplotlib** e **seaborn** para comunicar os insights gerados.

## Destaques
- Construção de um pipeline de dados end-to-end, da extração via API até a visualização.
- Aplicação de técnicas de limpeza de dados, como tratamento de datas e valores ausentes.
- Geração de um **dashboard** que traduz dados brutos em insights sobre a volumetria e a eficiência do sistema judiciário.

> Este projeto é uma forma de observar **aplicações de dados na área jurídica**, combinando análise de dados e desenvolvimento Python de forma prática.

## Estrutura do Repositório
```
├── api_tjpe.py             # Script de ingestão de dados via API
├── analise_judiciario.py   # Script para EDA e visualização
├── bd.csv                  # Dados brutos (gerado por api_tjpe.py)
├── analise_judiciaria.png  # Dashboard com os resultados (gerado por analise_judiciario.py)
└── README.md               # Documentação do projeto
```
## Como Executar
1. Instale as dependências:

```pip install requests pandas matplotlib seaborn```

2. Obtenha uma chave de acesso à API Pública do DataJud em: [https://www.cnj.jus.br/sistemas/datajud/api-publica/](https://www.cnj.jus.br/sistemas/datajud/api-publica/)
3. Substitua a chave antiga no código pelo seu token de acesso caso necessário.
4. Execute o script:
```python api_tjpe.py```
Este script irá se conectar à API e criar o arquivo bd.csv com os dados dos processos.
5. Execute o script:
```python analise_judiciario.py```
Este script irá ler o bd.csv, processar os dados e gerar a imagem analise_judiciaria.png com o dashboard final.

## Tecnologias Utilizadas
- Python
- pandas
- matplotlib
- seaborn
- requests
- json
