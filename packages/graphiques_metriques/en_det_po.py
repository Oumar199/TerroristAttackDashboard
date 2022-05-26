from packages import pd, px
from packages.fonctions.remplacer_valeurs import remplacer_valeurs
from packages.fonctions.supprimer_valeurs import supprimer_valeurs


def graphique_1(df: pd.DataFrame):
    countsTop = df["kidhijcountry"].value_counts()
    countsTop = (
        df.groupby(["kidhijcountry"]).size().reset_index(name="Nombre d'attaques")
    )
    countsTop = supprimer_valeurs(countsTop, "kidhijcountry", [''])
    if countsTop.empty:
        return '', None
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

def graphique_2(df: pd.DataFrame):
    attaque_ev_pays=df.groupby(['kidhijcountry']).size().reset_index(name="Nombre d'attaques")
    attaque_ev_pays = supprimer_valeurs(attaque_ev_pays, "kidhijcountry", [''])
    attaque_ev_pays.rename(columns={"kidhijcountry": "Pays d'évasion"}, inplace = True)
    if attaque_ev_pays.empty:
        return '', None
    fig = px.choropleth(
        attaque_ev_pays,
        locations="Pays d'évasion",
        projection="natural earth",
        locationmode="country names",
        color="Nombre d'attaques",
        color_continuous_scale="Viridis",
        hover_name="Pays d'évasion",
        template="ggplot2")
    title = "répartition géographique du nombre d'attaques terroristes par pays d'évasion des enlèvements ou des détournements"
    return title, fig
    
def graphique_3(df: pd.DataFrame):
    nb_att_enlev = df.groupby(['Pays', 'hostkidoutcome_txt']).size().reset_index(name="Nombre d'attaques")
    nb_att_enlev = supprimer_valeurs(nb_att_enlev, "hostkidoutcome_txt", [''])
    if nb_att_enlev.empty:
        return '', None
    nb_att_enlev = remplacer_valeurs(nb_att_enlev, "hostkidoutcome_txt",
                                          [
                                              "Hostage(s) escaped (not during rescue attempt)",
                                              "Hostage(s) killed (not during rescue attempt)",
                                              "Hostage(s) released by perpetrators",
                                          ], 
                                          [
                                              "Hostage(s) escaped",
                                              "Hostage(s) killed",
                                              "Hostage(s) released"
                                          ])
    fig = px.treemap(nb_att_enlev, path=["Pays", "hostkidoutcome_txt"], values="Nombre d'attaques",
                 labels={"hostkidoutcome_txt": "Dénouement des enlèvements/prises d'otages"})
    title = "nombre d'attaques terroristes par dénouements d'enlèvements/de prises d'otages et par pays"
    return title, fig
