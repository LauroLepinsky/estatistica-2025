# %%
import pandas as pd

# %%
df = pd.read_csv("data/points_tmw.csv")
df.head()
# %%

print("Estatísticas de Posição para Transações")

minimo = df["qtdPontos"].min()
print(f"Mínimo: {minimo}")

media = df["qtdPontos"].mean()
print(f"Média: {media}")

quartil_1 = df["qtdPontos"].quantile(0.25)
print(f"1o Quartil: {quartil_1}")

median = df["qtdPontos"].median()
print(f"1o Quartil: {median}")

quartil_3 = df["qtdPontos"].quantile(0.75)
print(f"1o Quartil: {quartil_3}")

maximo = df["qtdPontos"].max()
print(f"Máximo: {maximo}")

variancia = df["qtdPontos"].var()
print(f"Variância: {variancia:.2f}")

desvio_padrao = df["qtdPontos"].std()
print(f"Desvio Padrão: {desvio_padrao:.2f}")

amplitude = df["qtdPontos"].max() - df["qtdPontos"].min()
print(f"Amplitude: {amplitude:.2f}")

df["qtdPontos"].describe()

# %%
print("\n#####################\n")
print("Estatísticas de Posição para Usuarios")

usuarios = (
    df.groupby(["idUsuario"])
    .agg(
        {
            "idTransacao": "count",
            "qtdPontos": "sum",
        }
    )
    .reset_index()
)
usuarios

# %%

sumario = usuarios[["idTransacao", "qtdPontos"]].describe()
print(sumario.to_string())
