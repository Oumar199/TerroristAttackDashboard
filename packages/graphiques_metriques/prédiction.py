from typing import List

import numpy as np
from packages import pickle, pd, date, warnings

warnings.filterwarnings('ignore')

liste_variables = ['country', 'country_txt', 'attacktype1', 'attacktype1_txt', 'targtype1', 'targtype1_txt', 'natlty1', 'natlty1_txt',
                    'weaptype1', 'weaptype1_txt', 'country', 'country_txt']


variables_dict_lists = {}

for variable in liste_variables:
    with open(f'packages/data/sauvegardes/{variable}.txt', "rb") as f:
        pick = pickle.Unpickler(f)
        get_list= pick.load()
        variables_dict_lists[variable] = get_list


def encode_my_variables(variables: dict):
    """Changement des variables qualitatives en variables quantitative

    Args:
        variables (dict): dictionnaires de données 
    """
    for key, value1 in variables.items():
        for i, value2 in enumerate(variables_dict_lists[f'{key}_txt']):
            if value1 == value2:
                variables[key] = variables_dict_lists[key][i]
    return variables

def prediction(date:str):
    """Effectuer un prédiction à l'aide du modèle ARMA

    Args:
        date (str): La date pour laquelle on souhaite effectuer la prédiction       

    Returns:
        _type_: _description_
    """
    date = pd.to_datetime(date)  # type: ignore
    with open('packages/modeles/ARMA/arma.txt', "rb") as f:
        depick = pickle.Unpickler(f)
        model = depick.load()
        
    # model = SARIMAXResults.load('packages/modeles/ARMA/arma.pkl')
    y_pred = model.get_forecast(11000)
    y_pred_df = y_pred.conf_int(alpha = 0.05)
    prediction = model.predict(start = date)
    prediction = int(prediction)
    title = "Nombre de morts"
    return title, prediction 


def true_prediction(month, day, suicide, attacktype, targtype, natlty, weaptype, country, nkill):
    """Effectuer une prédiction du succès d'une attaque suivant les données fournies

    Args:
        month (_type_): Mois
        day (_type_): Jour
        multiple (_type_): Multiple ou pas
        suicide (_type_): Suicide
        attacktype (_type_): Type d'attaque
        targtype (_type_): Type de cible
        natlty (_type_): Nationalités des groupes terroristes
        individual (_type_): Attaque
        weaptype (_type_): _description_
    """
    variables = encode_my_variables({"attacktype1": attacktype, "targtype1": targtype, "natlty1": natlty,
                                     "weaptype1": weaptype, "country": country})
    
    variables = np.array([[month, day, suicide, variables['attacktype1'],
                 variables['targtype1'], variables['natlty1'], variables['weaptype1'], variables['country'],
                 nkill]])
    
    # recuperation du modele
    with open('packages/modeles/RandomForest/random.txt', "rb") as f:
        depick = pickle.Unpickler(f)
        model = depick.load()
    
    # print('model', model)
    prediction = model.predict(variables)
    # print('variables', variables, variables.shape)
    print('predictions', prediction)

    title = "Prédiction du succès d'une attaque terroriste"
    return title, 'Succès' if int(prediction) == 1 else "Echec"
    