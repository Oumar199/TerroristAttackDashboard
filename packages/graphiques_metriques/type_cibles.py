from packages import pd, px
from packages.fonctions.supprimer_valeurs import supprimer_valeurs


def graphique_1(df: pd.DataFrame):
    df_targtype = df.groupby("targtype1_txt").size().reset_index()
    df_targtype.columns = ["targtype1_txt", "Nombre d'attaques"]
    df_targtype = df_targtype.sort_values(ascending=False, by=["Nombre d'attaques"])
    if df_targtype.empty:
        return '', None
    fig = px.bar(
        df_targtype,
        x="targtype1_txt",
        y="Nombre d'attaques",
        labels={"targtype1_txt": "Types de cible"},
    )
    title = "nombre d’attaques terroristes par catégories de cible de première classe"
    return title, fig


def graphique_2(df: pd.DataFrame):
    df_targtype = df.groupby("targtype2_txt").size().reset_index()
    df_targtype = supprimer_valeurs(df_targtype, "targtype2_txt", [''])
    df_targtype.columns = ["targtype2_txt", "Nombre d'attaques"]
    df_targtype = df_targtype.sort_values(ascending=False, by=["Nombre d'attaques"])
    if df_targtype.empty:
        return '', None
    fig = px.bar(
        df_targtype,
        x="targtype2_txt",
        y="Nombre d'attaques",
        labels={"targtype2_txt": "Types de cible"},
    )
    title = "nombre d’attaques terroristes par catégorie de cible de deuxième classe"
    return title, fig


def graphique_3(df: pd.DataFrame):
    df_targtype = df.groupby("targtype3_txt").size().reset_index()
    df_targtype = supprimer_valeurs(df_targtype, "targtype3_txt", [''])
    df_targtype.columns = ["targtype3_txt", "Nombre d'attaques"]
    # print(df_targtype)
    if df_targtype.empty:
        return '', None
    
    df_targtype = df_targtype.sort_values(ascending=False, by=["Nombre d'attaques"])
    fig = px.bar(
        df_targtype,
        x="targtype3_txt",
        y="Nombre d'attaques",
        labels={"targtype3_txt": "Types de cible"},
    )
    title = "nombre d’attaques terroristes par catégorie de cible de troisième classe"
    return title, fig


def graphique_4(df: pd.DataFrame):
    df_targtype = df.groupby("targsubtype1_txt").size().reset_index()
    df_targtype = supprimer_valeurs(df_targtype, "targsubtype1_txt", [''])
    df_targtype.columns = ["targsubtype1_txt", "Nombre d'attaques"]
    df_targtype = df_targtype.sort_values(ascending=False, by=["Nombre d'attaques"])
    if df_targtype.empty:
        return '', None
    fig = px.bar(
        df_targtype,
        x="targsubtype1_txt",
        y="Nombre d'attaques",
        labels={"targsubtype1_txt": "Types de cible"},
    )
    title = (
        "nombre d’attaques terroristes par sous-catégorie de cible de première classe"
    )
    return title, fig


def graphique_5(df: pd.DataFrame):
    df_targtype = df.groupby("targsubtype2_txt").size().reset_index()
    df_targtype = supprimer_valeurs(df_targtype, "targsubtype2_txt", [''])
    df_targtype.columns = ["targsubtype2_txt", "Nombre d'attaques"]
    df_targtype = df_targtype.sort_values(ascending=False, by=["Nombre d'attaques"])
    if df_targtype.empty:
        return '', None
    fig = px.bar(
        df_targtype,
        x="targsubtype2_txt",
        y="Nombre d'attaques",
        labels={"targsubtype2_txt": "Types de cible"},
    )
    title = (
        "nombre d’attaques terroristes par sous-catégorie de cible de deuxième classe"
    )
    return title, fig


def graphique_6(df: pd.DataFrame):
    df_targtype = df.groupby("targsubtype3_txt").size().reset_index()
    df_targtype = supprimer_valeurs(df_targtype, "targsubtype3_txt", [''])
    df_targtype.columns = ["targsubtype3_txt", "Nombre d'attaques"]
    df_targtype = df_targtype.sort_values(ascending=False, by=["Nombre d'attaques"])
    if df_targtype.empty:
        return '', None
    fig = px.bar(
        df_targtype,
        x="targsubtype3_txt",
        y="Nombre d'attaques",
        labels={"targsubtype4_txt": "Types de cible"},
    )
    title = (
        "nombre d’attaques terroristes par sous-catégorie de cible de troisième classe"
    )
    return title, fig
