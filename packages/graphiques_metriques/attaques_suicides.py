from packages import pd, px, dash_table
from packages.fonctions.supprimer_valeurs import supprimer_valeurs


def graphique_1(df: pd.DataFrame):
    num_attack = (
        df.groupby(["Année", "suicide"]).size().reset_index(name="Nombre d'attaques")
    )
    num_attack = num_attack[num_attack["suicide"].isin([1])]
    if num_attack.empty:
        return '', None
    fig = px.bar(
        num_attack,
        x="Année",
        y="Nombre d'attaques",
        color="Nombre d'attaques"
    )
    title = "nombre d’attaques terroristes accompagnées de suicides par année"
    return title, fig


def graphique_2(df: pd.DataFrame):
    attaque_suicide_pays = (
        df[df["suicide"] == 1]
        .groupby(["Pays", "suicide"])
        .size()
        .reset_index(name="Nombre d'attaques suicides")
    )
    if attaque_suicide_pays.empty:
        return '', None
    fig = px.choropleth(
        attaque_suicide_pays,
        locations="Pays",
        projection="natural earth",
        locationmode="country names",
        color="Nombre d'attaques suicides",
        color_continuous_scale="Viridis",
        hover_name="Pays",
        template="ggplot2"
    )
    fig.update_layout(margin={"l": 0, "r": 0, "t": 0, "b": 0})
    title = "répartition géographique du nombre d’attaques terroristes accompagnés de suicide"
    return title, fig
