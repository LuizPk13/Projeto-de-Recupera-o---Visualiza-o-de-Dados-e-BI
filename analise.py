"""
Análise Exploratória de Dados (EDA) - Projeto RH
Lê query_01.csv e query_02.csv, calcula estatísticas descritivas
e gera gráficos (histograma e boxplot) sobre salários e distribuição
geográfica dos funcionários.
"""
import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------------------------------------
# 1. Carregar os dados
# ---------------------------------------------------------
df_salarios = pd.read_csv("dados/query_01.csv")
df_localidade = pd.read_csv("dados/query_02.csv")

print("=== Query 1 - Salários por Departamento e Cargo ===")
print(df_salarios.head(), "\n")

print("=== Query 2 - Distribuição por Localidade ===")
print(df_localidade.head(), "\n")

# ---------------------------------------------------------
# 2. Estatísticas descritivas dos salários
# ---------------------------------------------------------
media = df_salarios["SALARY"].mean()
mediana = df_salarios["SALARY"].median()
minimo = df_salarios["SALARY"].min()
maximo = df_salarios["SALARY"].max()
desvio_padrao = df_salarios["SALARY"].std()

print("=== Estatísticas Descritivas - Salários ===")
print(f"Média:         {media:,.2f}")
print(f"Mediana:       {mediana:,.2f}")
print(f"Mínimo:        {minimo:,.2f}")
print(f"Máximo:        {maximo:,.2f}")
print(f"Desvio padrão: {desvio_padrao:,.2f}\n")

# Salário médio por departamento
media_por_departamento = (
    df_salarios.groupby("DEPARTMENT_NAME")["SALARY"]
    .mean()
    .sort_values(ascending=False)
)
print("=== Salário Médio por Departamento ===")
print(media_por_departamento, "\n")

# Salário médio por cargo
media_por_cargo = (
    df_salarios.groupby("JOB_TITLE")["SALARY"]
    .mean()
    .sort_values(ascending=False)
)
print("=== Salário Médio por Cargo ===")
print(media_por_cargo, "\n")

# ---------------------------------------------------------
# 3. Distribuição geográfica dos funcionários
# ---------------------------------------------------------
funcionarios_por_regiao = df_localidade["REGION_NAME"].value_counts()
funcionarios_por_pais = df_localidade["COUNTRY_NAME"].value_counts()
funcionarios_por_cidade = df_localidade["CITY"].value_counts()

print("=== Funcionários por Região ===")
print(funcionarios_por_regiao, "\n")

print("=== Funcionários por País ===")
print(funcionarios_por_pais, "\n")

print("=== Funcionários por Cidade ===")
print(funcionarios_por_cidade, "\n")

# ---------------------------------------------------------
# 4. Gráficos
# ---------------------------------------------------------

# 4.1 Histograma da distribuição de salários
plt.figure(figsize=(8, 5))
plt.hist(df_salarios["SALARY"], bins=10, color="#2E8B57", edgecolor="black")
plt.title("Distribuição de Salários dos Funcionários")
plt.xlabel("Salário")
plt.ylabel("Quantidade de Funcionários")
plt.tight_layout()
plt.savefig("graficos/histograma_salarios.png", dpi=150)
plt.close()

# 4.2 Boxplot de salários por departamento
plt.figure(figsize=(10, 6))
df_salarios.boxplot(column="SALARY", by="DEPARTMENT_NAME", rot=45)
plt.title("Boxplot de Salários por Departamento")
plt.suptitle("")
plt.xlabel("Departamento")
plt.ylabel("Salário")
plt.tight_layout()
plt.savefig("graficos/boxplot_salarios_departamento.png", dpi=150)
plt.close()

# 4.3 Funcionários por região (gráfico de barras, complementar)
plt.figure(figsize=(7, 5))
funcionarios_por_regiao.plot(kind="bar", color="#4682B4", edgecolor="black")
plt.title("Funcionários por Região")
plt.xlabel("Região")
plt.ylabel("Quantidade de Funcionários")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("graficos/funcionarios_por_regiao.png", dpi=150)
plt.close()

print("Gráficos salvos na pasta 'graficos/'.")
