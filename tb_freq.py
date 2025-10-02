# %%
import pandas as pd
import sqlalchemy

# %%
df = pd.read_csv("data/points_tmw.csv")
df.head()

engine = sqlalchemy.create_engine("sqlite:///data/tmw.db")
df.to_sql("points", engine, if_exists="replace")

# %%
# pd.value_counts(df['descProduto']) deprecated
freq_prod = (
    df.groupby(["descProduto"])[["idTransacao"]]
    .count()
    .rename(columns={"idTransacao": "Freq. Abs."})
)

freq_prod["Freq. Abs. Acum."] = freq_prod["Freq. Abs."].cumsum()

freq_prod["Freq. Rel."] = freq_prod["Freq. Abs."] / freq_prod["Freq. Abs."].sum()

freq_prod["Freq. Rel. Acum."] = freq_prod["Freq. Rel."].cumsum()

freq_prod

# %%

freq_cat = (
    df.groupby(["descCategoriaProduto"])[["idTransacao"]]
    .count()
    .rename(columns={"idTransacao": "Freq. Abs."})
)

freq_cat["Freq. Abs. Acum."] = freq_cat["Freq. Abs."].cumsum()

freq_cat["Freq. Rel."] = freq_cat["Freq. Abs."] / freq_cat["Freq. Abs."].sum()

freq_cat["Freq. Rel. Acum."] = freq_cat["Freq. Rel."].cumsum()

freq_cat
