from matplotlib.pyplot import title
from packages import pd, px, dash_table, ff, MinMaxScaler

def clustering(df: pd.DataFrame):
    # modification des types d'attaque en codes
    df["attacktype1_txt_codes"] = df["attacktype1_txt"].astype("category").cat.codes
    # df["attacktype1_txt_codes"] = MinMaxScaler().fit_transform(df["attacktype1_txt_codes"])
    attackttype1_txt = df["attacktype1_txt_codes"].to_numpy()
    fig = ff.create_dendrogram(attackttype1_txt, color_threshold=1.5)
    title = "Dendogramme des types d'attaques"
    return title, fig