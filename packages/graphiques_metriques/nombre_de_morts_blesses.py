from packages import pd, px, np
from packages.fonctions.supprimer_valeurs import supprimer_valeurs
from packages.fonctions.remplacer_valeurs import remplacer_valeurs


def graphique_1(df: pd.DataFrame):
    # recuperons les données en regroupant par pays et année
    df_pays_morts = df.groupby(["Pays", "Année"], as_index=False).sum("Nombre de morts")

    # tracons le graphique
    fig = px.line(df_pays_morts, x="Année", y="Nombre de morts", color="Pays")

    # Titre
    title = "nombre de morts causés par des attaques terroristes par pays et par année"

    # Retournons le résultat
    return title, fig


def graphique_2(df: pd.DataFrame):
    # recuperons les données en regroupant par region et année
    df_region_morts = df.groupby(["Région", "Année"], as_index=False).sum(
        "Nombre de morts"
    )

    # tracons le graphique
    fig = px.line(df_region_morts, x="Année", y="Nombre de morts", color="Région")

    # Titre
    title = (
        "nombre de morts causés par des attaques terroristes par région et par année"
    )

    # Retournons le résultat
    return title, fig


def graphique_3(df: pd.DataFrame):

    # recuperons les données en regroupant par province ou Etat et par année
    df_provetat_morts = df.groupby(["provstate", "Année"], as_index=False).sum(
        "Nombre de morts"
    )

    # modifions le nom de la colonne provstate
    df_provetat_morts.rename(columns={"provstate": "Province/Etat"}, inplace=True)
    
    df_provetat_morts = remplacer_valeurs(df_provetat_morts, "Province/Etat",
                                          [
                                              "(Region) of Republican Subordination (Province)",
                                              "Bosnia and Herzegovina (Federation)",
                                              "Districts of Republican Subordination",
                                              "Federally Administered Tribal Areas",
                                              "Federation of Bosnia and Herzegovina",
                                              "Greater Skopje (Administrative division)",
                                              "Greater Skopje (Special Division)",
                                              "Greater Skopje (Statistical Region)",
                                              "Hong Kong (Special Administrative Region)",
                                              "Hong Kong Special Administrative Region (hksar)",
                                              "Kosovo and Metojia (Autonomous Province)",
                                              "Macau (Special Administrative Region)",
                                              "Mayo (district), Ban Dan (Village)",
                                              "North Caribbean Coast Autonomous Region",
                                              "Pattani, Narathiwat, and Yala Provinces",
                                              "Racha-Lechkhumi and Kvemo Svaneti",
                                              "Sangre Grande Regional Corporation",
                                              "South Caribbean Coast Autonomous Region",
                                              "Su-ngai Kolok  District Su-ngai Kolok",
                                              "Yerevan (Special Administrative Region)",
                                              "Jakarta (Special Capital Region)",
                                              "Jakarta (Special Territory Province)",
                                              "Karachay-Cherkessia (Autonomous Republic)",
                                              "Smolensk Oblast (Administrative Region)",
                                              "South Ossetia (Autonomous Province)"
                                            #   "Greater Spokje ("
                                          ], 
                                          [
                                              "(Region) of Republican Subord.",
                                              "Bosnia and Herzegovina (Fed.)",
                                              "Districts of Republican Subord.",
                                              "Federally Admin. Tribal Areas",
                                              "Fed. of Bosnia and Herzegovina",
                                              "Greater Skopje (Admin. div.)",
                                              "Greater Skopje (Special Div.)",
                                              "Greater Skopje (Stat. Region)",
                                              "Hong Kong (Special Admin. Reg.)",
                                              "H. K. Spe. Admin. Reg. (hksar)",
                                              "Kosovo and Metojia (Auto. Prov.)",
                                              "Macau (Special Admin. Region)",
                                              "Mayo (dist.), Ban Dan (Village)",
                                              "North Caribbean Coast Auto Reg.",
                                              "Pattani, Narathiwat & Yala Prov.",
                                              "Racha-Lechkhumi & Kvemo Svaneti",
                                              "Sangre Grande Regional Corp.",
                                              "South Caribbean Coast Auto. Reg.",
                                              "Su-ngai Kolok Dist. Su-ngai Kolok",
                                              "Yerevan (Special Admin. Region)",
                                              "Jakarta (Spe. Capital Region)",
                                              "Jakarta (Spe. Territory Province)",
                                              "Karachay-Cherkessia (Auto Rep.)",
                                              "Smolensk Oblast (Admin. Region)",
                                              "South Ossetia (Autonomous Prov.)"
                                          ])

    # supprimons les valeurs non pertinentes
    df_provetat_morts = supprimer_valeurs(
        df_provetat_morts, "Province/Etat", ["''", "Unknown", "unknown"]
    )

    # tracons le graphique
    fig = px.line(
        df_provetat_morts, x="Année", y="Nombre de morts", color="Province/Etat"
    )

    # Titre
    title = "nombre de morts causés par des attaques terroristes par province/Etat et par année"

    # Retournons le résultat
    return title, fig


def graphique_4(df: pd.DataFrame):
    # Sommons les nombres morts de morts par pays
    df_pays_geom = df.groupby("Pays", as_index=False).sum("Nombre de morts")

    # Tracons le choroplèthe en colorant suivant les nombres de morts
    fig = px.choropleth(
        df_pays_geom,
        locations="Pays",
        locationmode="country names",
        projection="natural earth",
        color="Nombre de morts",
        color_continuous_scale="Viridis",
        hover_name="Pays",
        template="ggplot2"
    )
    fig.update_layout(margin={"l": 0, "r": 0, "t": 0, "b": 0})

    # Titre
    title = "répartition géographique du nombre de morts causés par des attaques terroristes par pays"

    # Retournons le résultat
    return title, fig


def graphique_5(df: pd.DataFrame):
    # Sommons les nombres morts de morts par pays
    df_geom_evolution_morts = df.groupby(["Année", "Pays"], as_index=False)[
        "Nombre de morts"
    ].sum()

    # Tracons le choroplèthe en colorant suivant les nombres de morts
    fig = px.choropleth(
        df_geom_evolution_morts,
        locations="Pays",
        color="Nombre de morts",
        hover_name="Pays",
        projection="natural earth",
        locationmode="country names",
        animation_frame="Année",
        color_continuous_scale="Viridis",
        template="ggplot2",
    )

    fig.update_layout(
        title=dict(font=dict(size=28), x=0.5, xanchor="center"),
        margin=dict(l=60, r=60, t=50, b=50),
    )

    # Titre
    title = "évolution annuelle de la répartition géographique du nombre de morts causés par des attaques terroristes"

    # Retournons le résultat
    return title, fig


def graphique_6(df: pd.DataFrame):
    # Sommons les nombres morts de blesses par pays
    df_geom_evolution_blesses = df.groupby(["Année", "Pays"], as_index=False)[
        "Nombre de blessés"
    ].sum()

    # Tracons le choroplèthe en colorant suivant les nombres de morts
    fig = px.choropleth(
        df_geom_evolution_blesses,
        locations="Pays",
        color="Nombre de blessés",
        hover_name="Pays",
        projection="natural earth",
        locationmode="country names",
        animation_frame="Année",
        color_continuous_scale="Viridis",
        template="ggplot2",
    )

    fig.update_layout(
        title=dict(font=dict(size=28), x=0.5, xanchor="center"),
        margin=dict(l=60, r=60, t=50, b=50),
    )

    # Titre
    title = "évolution annuelle de la répartition géographique du nombre de personnes blessés par des attaques terroristes"

    # Retournons le résultat
    return title, fig


def graphique_7(df: pd.DataFrame):
    data_nmort = (
        df.groupby(["Pays", "Année"])
        .sum("Nombre de morts")
        .groupby(level=0)
        .cumsum()
        .reset_index()
    )
    fig = px.line(data_nmort, x="Année", y="Nombre de morts", color="Pays")
    title = "cumul annuel du nombre de morts par pays"
    return title, fig


def graphique_8(df: pd.DataFrame):
    data_nmort_region = (
        df.groupby(["Région", "Année"])
        .sum("Nombre de morts")
        .groupby(level=0)
        .cumsum()
        .reset_index()
    )
    fig = px.line(data_nmort_region, x="Année", y="Nombre de morts", color="Région")
    title = "cumul annuel du nombre de morts causés par des attaques terroristes par région"
    return title, fig

def graphique_9(df: pd.DataFrame):
    data_morts_attaques = df.groupby("attacktype1_txt", as_index=False).sum('Nombre de morts')
    fig = px.pie(data_morts_attaques, names = "attacktype1_txt", values="Nombre de morts", labels={"attacktype1_txt", "Types d'attaques"})
    title = "Nombre de morts par types d'attaques"
    return title, fig

def graphique_10(df: pd.DataFrame):
    data_blesses_attaques = df.groupby("attacktype1_txt", as_index=False).sum('Nombre de blessés')
    fig = px.pie(data_blesses_attaques, names = "attacktype1_txt", values="Nombre de blessés", labels={"attacktype1_txt", "Types d'attaques"})
    title = "Nombre de blessés par types d'attaques"
    return title, fig

def graphique_11(df: pd.DataFrame):
    data_morts_blesses_pays_continent = df.groupby(["Région", "Pays"], as_index=False).sum(["Nombre de morts", "Nombre de blessés"])
    fig = px.treemap(data_morts_blesses_pays_continent, path = [px.Constant("World"), "Région", "Pays"],
                     values = "Nombre de morts", color="Nombre de blessés", hover_data=["iso_alpha"],
                     color_continuous_scale="RdBu", color_continuous_midpoint=np.average(df["Nombre de blessés"], weights = df["Nombre de morts"]),
    )
    fig.update_layout(margin = dict(t = 50, l = 25, r = 25, b = 25))
    title = "Nombre de morts et nombre de blessés par région et par pays"
    return title, fig

def graphique_12(df: pd.DataFrame):
    data_morts_pays_continent = df.groupby(["Région", "Pays"], as_index=False).sum("Nombre de morts")
    fig = px.sunburst(data_morts_pays_continent, path = ["Région", "Pays"], values = "Nombre de morts")
    title = "Nombre de morts par pays et par région"
    return title, fig

def graphique_13(df: pd.DataFrame):
    data_blesses_pays_continent = df.groupby(["Région", "Pays"], as_index=False).sum("Nombre de blessés")
    fig = px.sunburst(data_blesses_pays_continent, path = ["Région", "Pays"], values = "Nombre de blessés")
    title = "Nombre de blessés par pays et par région"
    return title, fig
    
    
