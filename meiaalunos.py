import pandas as pd
df = pd.read_csv ("C:/Users/luan/OneDrive/cursosoftexrecife/notas_alunos.csv")
media = (df["nota1"] + df["nota2"])/2

df["média"] = media

df.loc[df["Média"] >=7, "situação"] = "Aprovado"
df.loc[df["Média"] <7, "Situação"] = "Reprovado"
df.loc[df["Faltas"] >5, "Sitação"] = "Reprovado"

df.to_csv("C:/Users/luan/OneDrive/cursosoftexrecife/notas_alunos.csv")

maiorNumFaltas = df["faltas"].max()
print("O maior números de faltas é:",(maiorNumFaltas))

mediaGeral = df["média"].median()
print("A média geral das notas é:",(mediaGeral))

maiorMedia = df["média"].max()
print("A maior média é:",(maiorMedia))
