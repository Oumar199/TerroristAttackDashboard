from packages import pd, px
from packages.fonctions.supprimer_valeurs import supprimer_valeurs


def graphique_1(df: pd.DataFrame):
    countsTop = df["kidhijcountry"].value_counts()
    countsTop = (
        df.groupby(["kidhijcountry"]).size().reset_index(name="Nombre d'attaques")
    )
    countsTop = supprimer_valeurs(countsTop, "kidhijcountry", ["''"])
    tri = countsTop.sort_values(["Nombre d'attaques"], ascending=False)
    tri = tri.head(20)
    fig = px.bar(
        tri,
        x="kidhijcountry",
        y="Nombre d'attaques",
        color="Nombre d'attaques",
        color_continuous_scale=px.colors.sequential.Rainbow,
        orientation="v",
        labels={"kidhijcountry": "Pays d'évasion"},
    )
    title = "top 20 des pays qui ont été utilisés pour des opérations d’évasion pour enlèvement ou détournement"
    return title, fig
