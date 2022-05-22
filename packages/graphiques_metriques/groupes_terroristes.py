from packages import pd, px
from packages.fonctions.supprimer_valeurs import supprimer_valeurs


def graphique_1(df: pd.DataFrame):
    grp_terr: pd.DataFrame = df.groupby("gname", as_index=False).sum("Nombre de morts")[
        ["gname", "Nombre de morts"]
    ]
    grp_terr.sort_values("Nombre de morts", ascending=False, inplace=True)
    top10 = grp_terr.head(10)
    fig = px.bar(
        top10,
        x="gname",
        y="Nombre de morts",
        template="plotly_dark",
        labels={"gname": "Groupes terroristes"},
    )
    title = "top 10 des perpétrateurs d'attaques terroristes qui ont causés le plus de morts"
    return title, fig


def graphique_2(df: pd.DataFrame):
    nbr_att_terr = (
        df.groupby("gname")
        .size()
        .reset_index(name="Nombre d'attaques par groupe terroriste")
    )
    nbr_att_terr.sort_values(
        "Nombre d'attaques par groupe terroriste", ascending=False, inplace=True
    )
    top10_nbr_att_terr = nbr_att_terr.head(10)
    fig = px.bar(
        top10_nbr_att_terr,
        x="gname",
        y="Nombre d'attaques par groupe terroriste",
        template="plotly_dark",
        labels={"gname": "Groupes terroristes"},
    )
    title = "top 10 des perpétrateurs qui ont effectués le plus grand nombre d’attaques terroristes"
    return title, fig


def graphique_3(df: pd.DataFrame):
    nat_ter = (
        df.groupby("natlty1_txt")
        .size()
        .reset_index(name="Nombre de groupes terroristes")
    )
    nat_ter.sort_values("Nombre de groupes terroristes", ascending=False, inplace=True)
    top20 = nat_ter.head(20)
    fig = px.pie(
        top20,
        names="natlty1_txt",
        values="Nombre de groupes terroristes",
        template="plotly_dark",
        labels={"natlty1_txt": "Nationalités des perpétrateurs"},
    )
    title = "Visualiser le top 20 des nationalités de perpétrateurs avec le plus grand nombre d’attaques terroristes"
    return title, fig
