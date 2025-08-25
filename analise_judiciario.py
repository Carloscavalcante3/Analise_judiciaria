import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("bd.csv")
print("Prévia dos dados:\n", df.head(), "\n")

# Converter datas para datetime UTC e remover timezone
df['data_inicio'] = pd.to_datetime(df['data_inicio'], errors='coerce', utc=True).dt.tz_convert(None)
df['data_fim'] = pd.to_datetime(df['data_fim'], errors='coerce', utc=True).dt.tz_convert(None)

hoje = pd.Timestamp.now().normalize()
df['data_fim'] = df['data_fim'].fillna(hoje)

# Calcular duração em dias
df['duracao'] = (df['data_fim'] - df['data_inicio']).dt.days

processos_por_classe = df['classe'].value_counts()
processos_por_assunto = df['assunto'].value_counts().head(10)
duracao_media = df.groupby('classe')['duracao'].mean().sort_values(ascending=False)

total_processos = len(df)

sns.set_theme(style="whitegrid")
fig, axes = plt.subplots(1, 3, figsize=(22, 6), constrained_layout=True)

# Gráfico 1: Processos x Classe
sns.barplot(x=processos_por_classe.index, y=processos_por_classe.values, palette="viridis", ax=axes[0], hue=processos_por_classe.index, legend=False)
axes[0].set_title(f"Número de Processos por Classe\n(Analisados: {total_processos})", fontsize=14)
axes[0].set_xlabel("Classe", fontsize=12)
axes[0].set_ylabel("Quantidade", fontsize=12)
axes[0].tick_params(axis="x", rotation=45)
plt.setp(axes[0].get_xticklabels(), ha="right")


#Gráfico 2: Duração X Classe
sns.barplot(x=duracao_media.index, y=duracao_media.values, palette="mako", ax=axes[1], hue=duracao_media.index, legend=False)
axes[1].set_title("Duração Média por Classe (dias)", fontsize=14)
axes[1].set_xlabel("Classe", fontsize=12)
axes[1].set_ylabel("Duração Média (dias)", fontsize=12)
axes[1].tick_params(axis="x", rotation=45)
plt.setp(axes[1].get_xticklabels(), ha="right")


# Gráfico 3: Asssuntos tratados
sns.barplot(x=processos_por_assunto.values, y=processos_por_assunto.index, palette="crest", ax=axes[2], hue=processos_por_assunto.index, legend=False)
axes[2].set_title("Temas Recorrentes", fontsize=14)
axes[2].set_xlabel("Quantidade", fontsize=12)
axes[2].set_ylabel("Assunto", fontsize=12)

plt.savefig("analise_judiciaria.png", dpi=300)
plt.show()