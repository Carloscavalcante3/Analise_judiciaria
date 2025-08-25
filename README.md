# 📊 Análise de Processos Judiciais

Este projeto tem como objetivo analisar dados de processos judiciais obtidos por meio da API Pública do DataJud, disponibilizada pelo Conselho Nacional de Justiça (CNJ).

## Objetivo
- Consumo de API e manipulação de dados com **Python** e **pandas**.
- Cálculo da duração média dos processos.
- Visualizações gráficas usando **matplotlib** e **seaborn**, facilitando a compreensão de padrões nos dados.

## Destaques
- Uso prático de **APIs públicas** para aquisição de dados.
- Transformação e análise de dados estruturados.
- Visualizações claras que podem auxiliar em decisões ou relatórios administrativos.

> Este projeto é uma forma de observar **aplicações de dados na área jurídica**, combinando análise de dados e desenvolvimento Python de forma prática.


## Como Executar
1. Instale as dependências:

```pip install requests pandas matplotlib seaborn```

2. Obtenha uma chave de acesso à API Pública do DataJud em: [https://www.cnj.jus.br/sistemas/datajud/api-publica/](https://www.cnj.jus.br/sistemas/datajud/api-publica/)
3. Substitua `"SUA_CHAVE_AQUI"` no código pelo seu token de acesso.
4. Execute o script:
```python analise_juridica.py```

## Gráficos Gerados
1. **Número de Processos por Tipo**
![Número de Processos por Tipo](processos_por_tipo.png)

2. **Duração Média dos Processos por Tipo**
![Duração Média dos Processos por Tipo](duracao_media_por_tipo.png)

## Tecnologias Utilizadas
- Python
- pandas
- matplotlib
- seaborn
- requests