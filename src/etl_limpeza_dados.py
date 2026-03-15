import pandas as pd


def realizar_etl():
    print("🔄 Iniciando processo de ETL (Extract, Transform, Load)...")

    # 1. Carregamento (Extract)
    try:
        df = pd.read_csv('data/dados_brutos_empreendedorismo_sc.csv')
        print(f"📥 Dados carregados: {len(df)} linhas.")
    except FileNotFoundError:
        print("❌ Erro: Arquivo de dados brutos não encontrado. Execute primeiro o script de geração.")
        return

    # 2. Tratamento (Transform)

    # Remover linhas onde o município é nulo (dado essencial)
    antes_mun = len(df)
    df = df.dropna(subset=['municipio'])
    print(f"🧹 Removidas {antes_mun - len(df)} linhas com município inválido.")

    # Preencher faturamento nulo com a mediana do segmento (técnica mais inteligente que a média)
    if df['faturamento_anual'].isnull().any():
        df['faturamento_anual'] = df.groupby('segmento')['faturamento_anual'].transform(
            lambda x: x.fillna(x.median())
        )
        print("💰 Faturamentos nulos preenchidos com a mediana do segmento.")

    # Converter datas
    df['data_abertura'] = pd.to_datetime(df['data_abertura'])
    df['anos_atividade'] = (pd.Timestamp.now() -
                            df['data_abertura']).dt.days // 365

    # Filtrar apenas empresas ativas para a análise principal (opcional, mas bom ter o dado completo também)
    # Vamos salvar o dataset completo tratado
    df_tratado = df.copy()

    # 3. Armazenamento (Load)
    df_tratado.to_csv('data/dados_tratados_empreendedorismo_sc.csv',
                      index=False, encoding='utf-8-sig')
    print(
        f"💾 Dados tratados salvos em 'data/dados_tratados_empreendedorismo_sc.csv'. Total: {len(df_tratado)} registros.")

    return df_tratado


if __name__ == "__main__":
    realizar_etl()
