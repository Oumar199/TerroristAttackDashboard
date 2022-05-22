from packages import pd, List


def remplacer_valeurs(df: pd.DataFrame, colonne:str, valeurs_a_remplacer: List, valeurs_de_remplacement: List)->pd.DataFrame:
    """Remplacer certaines valeurs d'une colonne

    Args:
        df (pd.DataFrame): le jeu de données
        colonne (str): la colonne
        valeurs_a_remplacer (List): les valeurs à remplacer
        valeurs_de_remplacement (List): les valeurs de remplacement

    Returns:
        pd.DataFrame: Le jeu de données de sortie
    """
    
    def replace(colonne):
        for i, value in enumerate(valeurs_a_remplacer):
            if colonne == value:
                colonne = valeurs_de_remplacement[i]
        return colonne
    
    df[colonne] = df[colonne].apply(replace)
    return df
    

    