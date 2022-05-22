from packages import pd
from packages import List


# concevons une fonction qui permet d'éliminer des valeurs dans un jeu de données
def supprimer_valeurs(
    data_frame: pd.DataFrame, colonne: str, valeurs: List
) -> pd.DataFrame:
    """Permet de supprimesr certaines valeurs dans un jeu de données

    Args:
        data_frame (pd.DataFrame): Le jeu de données
        colonne (str): La colonne qui contient les valeurs
        valeurs (List): Une liste de valeurs à supprimer

    Returns:
        pd.DataFrame: Le nouveau jeu de données
    """
    return data_frame[~data_frame[colonne].isin(valeurs)]
