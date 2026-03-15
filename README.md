# 📊 Análise de Dados: Empreendedorismo em Santa Catarina

## 1. Descrição do Problema e Solução
Este projeto tem como objetivo analisar o cenário do empreendedorismo em Santa Catarina, identificando padrões de distribuição geográfica, desempenho por setor e evolução temporal. A solução desenvolvida abrange todo o fluxo de dados: desde a geração (ou coleta), passando pelo tratamento (ETL) até a Análise Exploratória de Dados (AED) com visualizações gráficas.

A análise busca responder perguntas como: Quais municípios lideram em número de empresas? Qual segmento possui o maior faturamento médio? Como foi a evolução de abertura de negócios na última década?

## 2. Origem dos Dados
Os dados utilizados neste projeto são **simulados**, porém construídos com base em parâmetros realistas do ecossistema empresarial de Santa Catarina (municípios reais, segmentos econômicos válidos e distribuições estatísticas plausíveis).
- **Justificativa:** A simulação permite garantir a qualidade didática do tratamento de dados (inserção proposital de ruídos e valores nulos) e focar na metodologia de análise, atendendo ao permitido no edital quando bases públicas específicas não estão disponíveis ou são excessivamente complexas para o escopo do desafio.
- **Volume:** Base inicial com 500 registros de empresas.

## 3. Tecnologias Empregadas
- **Linguagem:** Python 3.x
- **Manipulação de Dados:** Pandas
- **Visualização:** Matplotlib e Seaborn
- **Ambiente:** Jupyter Notebook
- **Versionamento:** Git e GitHub

## 4. Estrutura do Projeto
```text
desafio-dados-sc/
├── data/                       # Conjunto de dados (Brutos e Tratados)
│   ├── dados_brutos_empreendedorismo_sc.csv
│   └── dados_tratados_empreendedorismo_sc.csv
├── src/                        # Scripts Python de lógica
│   ├── gerar_dados_sc.py       # Script de geração da base simulada
│   └── etl_limpeza_dados.py    # Script de tratamento e limpeza
├── notebooks/                  # Notebooks de análise
│   └── analise_exploratoria_sc.ipynb
├── requirements.txt            # Dependências do projeto
└── README.md                   # Esta documentação