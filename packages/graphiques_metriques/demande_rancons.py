from packages import pd, px, dash_table
from packages.fonctions.supprimer_valeurs import supprimer_valeurs


def graphique_1(df: pd.DataFrame):
    attaque_ranc_pays: pd.DataFrame = df[df["ransompaid"] > 0].groupby(["Pays"]).ransompaid.agg(["sum", "size"]).reset_index()
    # print(attaque_ranc_pays)
    attaque_ranc_pays.rename(columns={"sum": "Somme rancons payées", "size": "Nombre d'attaques"}, inplace = True)  # type: ignore
    if attaque_ranc_pays.empty:
        return '', None
    fig = px.choropleth(
        attaque_ranc_pays,
        locations="Pays",
        locationmode="country names",
        projection="natural earth",
        color="Nombre d'attaques",
        color_continuous_scale="Viridis",
        hover_name="Pays",
        hover_data=["Pays", "Somme rancons payées", "Nombre d'attaques"],
        template="ggplot2"
    )
    fig.update_layout(margin={"l": 0, "r": 0, "t": 0, "b": 0})
    title = (
        "répartition géographique du nombre d’attaques avec demande de rançons par pays"
    )
    return title, fig


def graphique_2(df: pd.DataFrame):
    attaque_ranc_reg_ann = (
        df[df["ransompaid"] > 0]
        .groupby(["Année", "Région"])
        .size()
        .reset_index(name="Nombre d'attaques")
    )
    if attaque_ranc_reg_ann.empty:
        return '', None
    fig = px.bar(
        attaque_ranc_reg_ann,
        x="Région",
        y="Nombre d'attaques",
        color="Nombre d'attaques",
        animation_frame="Année",
        range_y = [0, attaque_ranc_reg_ann["Nombre d'attaques"].max()]
    )
    title = (
        "nombre d’attaques terroristes avec demande de rançons par région et par année"
    )
    return title, fig
