import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Configurar seed para reprodutibilidade (importante para ciência de dados)
np.random.seed(42)
random.seed(42)

# Dados base para simulação
municipios_sc = ['Florianópolis', 'Joinville', 'Blumenau', 'Chapecó', 'Criciúma',
                 'Itajaí', 'São José', 'Lages', 'Jaraguá do Sul', 'Balneário Camboriú']
segmentos = ['Tecnologia', 'Comércio', 'Indústria',
             'Serviços', 'Agronegócio', 'Turismo']
status = ['Ativo', 'Inativo', 'Suspenso']

# Gerar 500 registros
n_registros = 500
dados = {
    'id_empresa': range(1, n_registros + 1),
    'nome_fantasia': [f"Empresa {i} LTDA" for i in range(1, n_registros + 1)],
    'municipio': [random.choice(municipios_sc) for _ in range(n_registros)],
    'segmento': [random.choice(segmentos) for _ in range(n_registros)],
    'data_abertura': [(datetime(2010, 1, 1) + timedelta(days=random.randint(0, 5000))).strftime('%Y-%m-%d') for _ in range(n_registros)],
    'numero_funcionarios': np.random.randint(1, 150, size=n_registros),
    'faturamento_anual': np.round(np.random.uniform(50000, 5000000, size=n_registros), 2),
    'status': [random.choices(status, weights=[0.85, 0.10, 0.05])[0] for _ in range(n_registros)]
}

# Criar DataFrame
df = pd.DataFrame(dados)

# Inserir alguns valores ausentes (NaN) propositalmente para testar o tratamento (ETL)
# Vamos remover alguns municípios e faturamentos aleatoriamente
indices_aleatorios_mun = np.random.choice(df.index, size=20, replace=False)
df.loc[indices_aleatorios_mun, 'municipio'] = np.nan

indices_aleatorios_fat = np.random.choice(df.index, size=15, replace=False)
df.loc[indices_aleatorios_fat, 'faturamento_anual'] = np.nan

# Salvar como CSV bruto
df.to_csv('data/dados_brutos_empreendedorismo_sc.csv',
          index=False, encoding='utf-8-sig')

print(
    f"✅ Dados gerados com sucesso! {len(df)} registros salvos em 'data/dados_brutos_empreendedorismo_sc.csv'")
print(f"📊 Resumo: {df['municipio'].isnull().sum()} municípios nulos, {df['faturamento_anual'].isnull().sum()} faturamentos nulos.")
