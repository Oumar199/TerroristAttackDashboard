from packages import pd, px, dash_table
from packages.fonctions.supprimer_valeurs import supprimer_valeurs


def traitement(df: pd.DataFrame):
    df_africa_sub_sahara = df[df["Région"] == "Sub-Saharan Africa"]
    df_africa_sub_sahara = df[df["Région"] == "Sub-Saharan Africa"]
    df_africa_north = df[df["Région"] == "Middle East & North Africa"]
    df_africa = df_africa_sub_sahara.append(df_africa_north)

    hors_africa = [
        "Jordan",
        "Turkey",
        "Iran",
        "South Yemen",
        "Israel",
        "Kuwait",
        "West Bank and Gaza Strip",
        "North Yemen",
        "Syria",
        "United Arab Emirates",
        "Iraq",
        "Saudi Arabia",
        "Bahrain",
        "Qatar",
        "Yemen",
        "International",
    ]

    index_hors_africa = []
    for pays in hors_africa:
        idx = df_africa.index[df_africa["Pays"] == pays].tolist()
        index_hors_africa = index_hors_africa + idx

    df_africa.drop(index=index_hors_africa, inplace=True)
    return df_africa


def graphique_1(df: pd.DataFrame):
    df_africa = traitement(df)
    df_africa = (
        df_africa.groupby(["Pays", "Année"]).sum("Nombre de morts").reset_index()
    )
    fig = px.treemap(
        df_africa,
        path = ["Année", "Pays"],
        values="Nombre de morts"
    )

    title = "nombre d’africains morts du terrorisme par région et par année"
    return title, fig


def graphique_2(df: pd.DataFrame):
    df_africa = traitement(df)
    df_blesse = (
        df_africa.groupby(["Pays", "Année"]).sum("Nombre de blessés").reset_index()
    )
    
    fig = px.treemap(
        df_blesse,
        path = ["Année", "Pays"],
        values="Nombre de blessés"
    )

    title = "nombre d’attaques terroristes par année et par type d’attaque"
    return title, fig
