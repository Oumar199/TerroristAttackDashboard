from packages import pd, px, dash_table
from packages.fonctions.supprimer_valeurs import supprimer_valeurs


def graphique_1(df: pd.DataFrame):
    df = supprimer_valeurs(
        data_frame=df, colonne="propextent_txt", valeurs=['']
    )
    property_damages = (
        df.groupby(["propextent_txt"])
        .size()
        .reset_index(name="Nombre d'attaques")
    )
    if property_damages.empty:
        return '', None
    table = property_damages.rename(columns = {"propextent_txt": "Catégories des propriétés"})

    title = "nombre d’attaques terroristes par catégorie de dommages de propriété(s)"
    return title, table


def graphique_2(df: pd.DataFrame):
    df = supprimer_valeurs(
        data_frame=df, colonne="propextent_txt", valeurs=['']
    )
    property_damages = df[
        df["propextent_txt"] == "Catastrophic (likely >= $1 billion)"
    ][
        [
            "Ville",
            "Pays",
            "Année",
            "Nombre de morts",
            "propvalue"
        ]
    ]
    if property_damages.empty:
        return '', None
    property_damages["Valeur propriété"] = property_damages["propvalue"].apply(lambda x: str(x) if x != 0 else "non connue")
    property_damages.drop("propvalue", axis = 1, inplace = True)
    table = property_damages.rename( columns= {"Nombre de morts": "Morts", "Nombre de blessés": "Blessés"})
    title = "liste des attaques accompagnées de dommages de propriétés très grave (> 1 milliard de dollars)"
    return title, table
