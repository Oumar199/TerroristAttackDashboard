from packages import pd
from packages import pickle
from typing import *


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
    

def ajout_date(df: pd.DataFrame, colonne_jour: str, colonne_mois: str, colonne_annee: str) -> pd.DataFrame:
    """Ajouter une nouvelle colonne date

    Args:
        df (pd.DataFrame): Le jeu de données initial
        colonne_jour (str): Le nom de la colonne jour
        colonne_mois (str): Le nom de la colonne mois
        colonne_annee (str): Le nom de la colonne annee

    Returns:
        pd.DataFrame: Le jeu de données avec une date
    """
    # enlever les lignes avec des numéros de jour égals à 0
    df.drop(index = df[(df["iday"] == 0)].index, axis = 0, inplace = True)
    
    # création d'une nouvelle colonne date
    df['date'] = df["iyear"].astype("str") + "-" + df["imonth"].astype("str") + "-" + df["iday"].astype("str")
    
    # transformation de la colonne en format date_time
    df["date"] = pd.to_datetime(df['date'])
    
    # trier les lignes suivant les dates
    df.sort_values('date', inplace=True)
    
    return df

def convertir_type(df: pd.DataFrame, colonnes: List, type: str):
    """Permet de convertir des colonnes en une autre type

    Args:
        df (pd.DataFrame): Le jeu de données
        colonnes (List): Les colonnes à convertir
        type (str): Le type des données
    """
    for colonne in colonnes:
        df = remplacer_valeurs(df, colonne, [''], ["0"])
        df[colonne] = df[colonne].astype(type)
    return df

def remplacer_valeurs_manquantes_quant(df: pd.DataFrame, valeur_de_remplacement: float)->pd.DataFrame:
    """remplacer les valeurs manquantes quantitatives

    Args:
        df (pd.DataFrame): Le jeu de données avec valeurs manquantes
        valeur_de_remplacement (float): La valeur de remplacement

    Returns:
        pd.DataFrame: Le jeu de données sans valeurs manquantes quantitatives
    """
    # recuperations des noms des colonnes quantitatives
    quant: pd.Index = df.columns[~df.columns.isin(df.select_dtypes('object').columns.to_list())]
    
    # remplacements des valeurs manquantes
    df[quant] = df[quant].fillna(valeur_de_remplacement)
    
    return df
    
def remplacer_valeurs_manquantes_qual(df: pd.DataFrame, valeur_de_remplacement: float)->pd.DataFrame:
    """remplacer les valeurs manquantes qualitatives

    Args:
        df (pd.DataFrame): Le jeu de données avec valeurs manquantes
        valeur_de_remplacement (float): La valeur de remplacement

    Returns:
        pd.DataFrame: Le jeu de données sans valeurs manquantes qualitatives
    """
    # recuperations des noms des colonnes qualitatives
    qual = df.select_dtypes('object').columns
    
    # remplacements des valeurs manquantes
    df[qual] = df[qual].fillna(valeur_de_remplacement)      
    
    return df

def pretraitement(df_terror: pd.DataFrame) -> pd.DataFrame:
    """Effectuer le prétraitement des données

    Args:
        df_terror (pd.DataFrame): Le jeu de données original

    Returns:
        pd.DataFrame: Le jeu de données nettoyé
    """
    ## Les traitements qui seront effectués ont été étudié avant 
    ## d'être entrepris
    
    # modification des types des variables quantitatives
    df_terror = convertir_type(df_terror, ['iyear', 'iday', 'imonth', 'nkill',
                                           'nwound', 'nkillus', 'nwoundus', 'ndays',
                                           'nhostkidus', 'propextent', 'suicide', 'nhostkid', 'nhours'],'int')
    df_terror = convertir_type(df_terror, ['latitude', 'longitude', 'ransompaid', 'ransompaidus', 'propvalue'],"float")
    # Ajout d'une nouvelle colonne date
    df_terror = ajout_date(df_terror, "iday", "imonth", "iyear")
    
    
    
    # remplacement des valeurs manquantes quantitatives
    df_terror = remplacer_valeurs_manquantes_quant(df_terror, 0)
    
    # remplacements des valeurs manquantes restantes qui doivent etre qualitatives
    df_terror.fillna("''", inplace = True)  
    
    return df_terror      
    
    
    
    
    