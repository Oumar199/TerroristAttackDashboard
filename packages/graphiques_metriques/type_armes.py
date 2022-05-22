from packages import pd, px
from packages.fonctions.supprimer_valeurs import supprimer_valeurs
from packages.fonctions.remplacer_valeurs import remplacer_valeurs


def graphique_1(df: pd.DataFrame):
    counts1 = df.groupby(["weaptype1_txt"]).size().reset_index(name="Nombre d'attaques")
    counts1 = supprimer_valeurs(counts1, "weaptype1_txt", ["''"])
    counts1 = remplacer_valeurs(counts1, "weaptype1_txt", ["Vehicle (not to include vehicle-borne explosives, i.e., car or truck bombs)"],
                                ["Vehicle"])
    counts1.sort_values(["Nombre d'attaques"], ascending=False, inplace=True)
    fig = px.bar(
        counts1,
        x="weaptype1_txt",
        y="Nombre d'attaques",
        color="Nombre d'attaques",
        orientation="v",
        labels={"weaptype1_txt": "Types d'arme"},
    )
    title = "nombre d’attaques terroristes par types d’armes de première classe"
    return title, fig


def graphique_2(df: pd.DataFrame):
    counts2 = df.groupby(["weaptype2_txt"]).size().reset_index(name="Nombre d'attaques")
    counts2 = supprimer_valeurs(counts2, "weaptype2_txt", ["''"])
    counts2 = remplacer_valeurs(counts2, "weaptype2_txt", ["Vehicle (not to include vehicle-borne explosives, i.e., car or truck bombs)"],
                                ["Vehicle"])
    counts2.sort_values(["Nombre d'attaques"], ascending=False, inplace=True)
    fig = px.bar(
        counts2,
        x="weaptype2_txt",
        y="Nombre d'attaques",
        color="Nombre d'attaques",
        orientation="v",
        labels={"weaptype2_txt": "Types d'arme"},
    )
    title = "nombre d’attaques terroristes par types d’armes de deuxième classe"
    return title, fig


def graphique_3(df: pd.DataFrame):
    counts3 = df.groupby(["weaptype3_txt"]).size().reset_index(name="Nombre d'attaques")
    counts3 = supprimer_valeurs(counts3, "weaptype3_txt", ["''"])
    counts3 = remplacer_valeurs(counts3, "weaptype3_txt", ["Vehicle (not to include vehicle-borne explosives, i.e., car or truck bombs)"],
                                ["Vehicle"])
    counts3.sort_values(["Nombre d'attaques"], ascending=False, inplace=True)
    fig = px.bar(
        counts3,
        x="weaptype3_txt",
        y="Nombre d'attaques",
        color="Nombre d'attaques",
        orientation="v",
        labels={"weaptype3_txt": "Types d'arme"},
    )
    title = "nombre d’attaques terroristes par types d’armes de troisième classe"
    return title, fig


def graphique_4(df: pd.DataFrame):
    counts4 = df.groupby(["weaptype4_txt"]).size().reset_index(name="Nombre d'attaques")
    counts4 = supprimer_valeurs(counts4, "weaptype4_txt", ["''"])
    counts4 = remplacer_valeurs(counts4, "weaptype4_txt", ["Vehicle (not to include vehicle-borne explosives, i.e., car or truck bombs)"],
                                ["Vehicle"])
    tri = counts4.sort_values(["Nombre d'attaques"], ascending=False)
    fig = px.bar(
        tri,
        x="weaptype4_txt",
        y="Nombre d'attaques",
        color="Nombre d'attaques",
        orientation="v",
        labels={"weaptype4_txt": "Types d'arme"},
    )
    title = "nombre d’attaques terroristes par types d’armes de quatrième classe"
    return title, fig
