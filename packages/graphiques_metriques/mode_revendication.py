from packages import pd, px
from packages.fonctions.supprimer_valeurs import supprimer_valeurs


def graphique_1(df: pd.DataFrame):
    mode_reclam = (
        df.groupby("claimmode_txt").size().reset_index(name="Nombre d'attaques")
    )
    mode_reclam = supprimer_valeurs(
        data_frame=mode_reclam, colonne="claimmode_txt", valeurs=['']
    )
    if mode_reclam.empty:
        return '', None
    fig = px.pie(
        mode_reclam,
        names="claimmode_txt",
        values="Nombre d'attaques",
        color="claimmode_txt",
        labels={"claimmode_txt": "Modes de revendication"},
    )
    title = "nombre d’attaques terroristes par mode de revendication"
    return title, fig
