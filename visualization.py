from packages import *
from packages.fonctions.supprimer_valeurs import supprimer_valeurs
from packages.fonctions.make_graphics import make_metrics, make_graphics
#=========================================================================

# récupération du temps pour les mises-à-jour
# try:
#     # heure actuel
#     with open("data")
# except Exception as e:
    

#=========================================================================

# Récupération des données prétraitées
try:
    with open("packages/data/new_dataframe.txt", "rb") as f:
        pick = pickle.Unpickler(f)
        df_covid = pick.load()
    
    # ouverture de notre fichier pour effectuer les tests
    df_terror:pd.DataFrame = pd.read_csv("packages/data/cleaned/terror.csv")
    
except Exception as e:
    print("Pickle File Error:",e)
   
#=========================================================================

# configurer lien jquery
external_scripts = ["https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js", "/assets/js/dynamique.js"]

# configurer font-awesome pour les icones
external_style = ["/assets/fontawesome/css/all.css"]

# Initialisation de l'application
app = dash.Dash(__name__, external_scripts = external_scripts, external_stylesheets = external_style)

# ajout server
server = app.server

#=========================================================================


# Mettons la date comme index
df_terror.set_index("date", inplace = True)

# renommons certaines colonnes
df_terror.rename(columns={"nkill":"Nombre de morts", "nwound": "Nombre de blessés", "iday": "Jour", "iyear": "Année", "imonth": "Mois", "country_txt": "Pays", "region_txt": "Région", "city": "Ville"}, inplace=True)

# Récupérons la liste des pays
pays = df_terror["Pays"].unique().tolist()

# Créons une liste contenant les mois de l'année
mois = ["Janvier", "Fevrier", "Mars", "Fevrier", "Mars",
        "Avril", "Mai", "Juin", "Juillet", "Aout", "Septembre", 
        "Octobre", "Novembre", "Novembre", "Décembre"]

# Récupérons la première date ou la date minimale
first_date = df_terror[["Jour", "Mois", "Année"]].head(1)

# Récupérons la dernière date ou la date maximale
last_date = df_terror[["Jour", "Mois", "Année"]].tail(1)

#=========================================================================

# listes de pages
pages = ["Visualisation du nombre de morts", "Visualiser le nombre de morts par pays et par année", "Visualiser le nombre de morts par région et par année", "Visualiser le nombre de morts par province/Etat et par année",
         "Visualiser la répartition géographique du nombre de morts par pays", "Visualiser l'évolution annuelle de la répartition géographique du nombre de morts", "Visualiser l'évolution annuelle de la répartition géographique du nombre de personnes blessés",
         "Morts par jour", "Top des pays - cas", "Top des pays - morts"
]

# liste de boutons de navigation (tests)
navs = []
boutons = [dbc.NavLink(pages[0], href = "/", active = "exact")]
for j in range(2, len(pages)+1):
    boutons.append(dbc.NavLink(pages[j-1], href=f"/page-{j-1}", active="exact"))
    if j%8 == 0:
        navs.append(dbc.Nav(boutons, vertical=True, pills = True))
        boutons = []
 
if len(boutons) != 0:
    navs.append(dbc.Nav(boutons, vertical=True, pills = True))
    
#=========================================================================

# Ajout de la barre de navigation
sidebar = dbc.Card(
    dbc.CardBody(
        html.Div(
            [
                html.Div(
                    [
                        html.H2("Attaques terroristes",
                                className="display-4"),
                        html.Hr(),
                        html.P(
                            "Choisissez une page",
                            className="lead"
                        ),
                        html.Div(
                            navs
                        )
                    ]
                ),
                html.Div(
                    html.Div(
                        [
                            html.I(
                                className="fa-solid fa-circle-arrow-right shadow-lg rounded-circle right-arrow icone-rose fa-3x",
                                style={"position": "absolute", "top": "50%", "left": "30%"}
                            ),
                            html.I(
                                className="fa-solid fa-circle-arrow-left shadow-lg rounded-circle left-arrow icone-rose fa-3x",
                                style={"position": "absolute", "top": "50%", "left": "30%"}
                            )
                        ],
                        className="h-100"
                    ), 
                    className="h-100 indic-slide shadow-md rounded-end",
                    style={"position": "fixed", "top": 0, "left": "100%", "width": "80px"}
                )
            ], 
            className="h-100",
            style = {"position": "relative"}
        )
                    
    ),
            
    
    color="light",
    className="h-100 sidebar shadow-md pd-0",
    style={
            "width": "45rem",
            "position": "fixed",
            # "overflowY": "auto",
            "top": 0,
            "left": "-45rem"
        }
)

#=========================================================================

# Définition de la squelette principale du contenu
content = dbc.Container(
    [
        html.Div(
            dcc.DatePickerRange(
                id = "date-picker",
                calendar_orientation="horizontal",
                day_size=39,
                end_date_placeholder_text="Dernière date",
                start_date_placeholder_text="Première date",
                with_portal=True,
                first_day_of_week=0,
                reopen_calendar_on_clear=True,
                is_RTL=False,
                clearable=True,
                number_of_months_shown=1,
                min_date_allowed=dt(
                    int(first_date["Année"]),
                    int(first_date["Mois"]),
                    int(first_date["Jour"])
                ),
                max_date_allowed=dt(
                    int(last_date["Année"]),
                    int(last_date["Mois"]),
                    int(last_date["Jour"])    
                ),
                # initial_visible_month=dt(
                #     2020, 
                #     1,
                #     1
                # ),
                start_date=dt(
                    int(first_date["Année"]),
                    int(first_date["Mois"]),
                    int(first_date["Jour"])
                ).date(),
                end_date=dt(
                    int(last_date["Année"]),
                    int(last_date["Mois"]),
                    int(last_date["Jour"])
                ).date(),
                display_format="MMM Do, YY",
                month_format="MMMM, YYYY",
                minimum_nights=4,
                persistence=True,
                persisted_props=["start_date", "end_date"],
                persistence_type="session",
                updatemode="singledate",
                className="shadow-lg"
            ),
            style={"textAlign": "right","margin": "1rem"}
        ),
        dbc.Row(
            [
                html.Label(id = "content-title", style = {"margin-bottom": "1rem"}),
                dbc.Col(
                dcc.Dropdown(
                    id = "pays",
                    options=[{"label" : p, "value" : p} for p in pays],
                    # value = "form-control pd-3",
                    # className="form-control",
                    placeholder="Choisissez un pays", 
                    multi=True,
                    style = {"verticalAlign": "middle", "padding": "4px!important"}
                ),
                width = 10
                ),
                dbc.Col(
                    dbc.Button(
                        "Filtrer",
                        id = "filtre",
                        className = "btn btn-lg btn-tertiary rounded-0"
                    ),
                    width = 2
                )
            ],
            className="text-center m-0"
            
        ),
        
        # html.Div(
        #     id = "slider-top",
        #     className="text-center",
        #     children = [
        #         html.Label("Choisissez le nombre de pays dans le top"),
        #         dcc.Slider(
        #             id = "choose-number",
        #             value = 10,
        #             # className="form-control",
        #             min = 5,
        #             max = 100,
        #             marks={i: str(i) for i in range(5, 100+1, 5)}
        #         )
        #     ],
        #     style={"display": "none"}
        # ),
        html.Div(
            id = "principal-content"
        )
    ]
)

#=========================================================================

# Réunissons le location, la barre de navigation et le contenu dans le layout
app.layout = dbc.Container(
    [
        dcc.Location(id = "url"),
        dbc.Row(
            [
                dbc.Col(
                    sidebar,
                    width=2,
                    style={
                        "zIndex": 100
                    }
                ),
                dbc.Col(
                    content,
                    width=9, 
                    # style = {
                        # "margin-left": "20rem" 
                    # }
                )
            ]
        )
    ],
    fluid=True
) 


#=========================================================================
#=========================================================================

######
@contextmanager
def change(path):
    try:
        f = open(path, "w")
        base = sys.stdout
        sys.stdout = f
        yield
    finally:
        sys.stdout = base
######

# # Définition d'un callback pour ajouter ou supprimer un slider
# @app.callback(
#     [
#         # Output(component_id="slider-top", component_property="children"),
#         Output(component_id="slider-top", component_property="style")
#     ],
#     [Input(component_id="url", component_property="pathname")]
# )
# def add_slider(pathname):
#     '''Cette fonction renvoie une marge pour le slider et le rend visible si les utilisateur 
#     accéde à la page 8 ou 9, sinon elle rend invisible le slider
#     Args:
#         pathname(str): contient le chemin d'accés 
#     Returns:
#         style du slider
#     '''
#     if pathname == "/page-8" or pathname == "/page-9":
#         return [
#             {"margin": "1rem"}
#         ]
#     return [
#             {"display": "none"}
#         ]

# Définition des callbacks pour la résolution des questions
@app.callback(
    Output(component_id="principal-content", component_property="children"),
    [
        Input(component_id="url", component_property="pathname"),
        Input(component_id="date-picker", component_property="start_date"),
        Input(component_id="date-picker", component_property="end_date"),
    ],
    [
        Input(component_id="filtre", component_property="n_clicks"),
        State(component_id="pays", component_property="value"),
        # Input(component_id="choose-number", component_property="value")
    ]
)
def add_response(pathname, start_date, end_date, n, pays):
    ''' Fonction qui renvoie une réponse à une question selon le pathname donné en entrée.
    Args:
        pathname(str): Contient le chemin d'accés 
        start_date(str): La date de départ
        end_date(str): La date de fin
        pays(str ou list): Contient le pays ou les pays qui est/sont recherchés dans le dataset
        top(int): Définit le numéro du top des pays à afficher dans les pages 8 et 9
    '''
    if pays:
        
        # Filtrage des données par dates et par pays avant de retourner les résultats
        # en fonction du pathname
        
        if not type(pays) is list:
            pays = [pays] 
        df = df_terror.loc[start_date:end_date]
        
        if n != None:
            df = df[df["Pays"].isin(pays)]
        
        if pathname == "/":
            # Calcul du nombre total de morts enregistré
            total_morts = df["Nombre de morts"].sum()
            
            # Titre
            title1 = "nombre total de morts causés par des attaques terroristes"
            
            # Initialisation des lignes
            rows = []
            
            # pour la métrique
            content1 = dbc.Col(make_metrics(title1, total_morts), width = 4)
            
            
            
        elif pathname == "/page-1":
            
        
        elif pathname == "/page-2": 
            
            
        elif pathname == "/page-3":
           
        
        elif pathname == "/page-4":
            
        elif pathname == "/page-5":
            
            
        elif pathname == "/page-6":
            
           
        elif pathname == "/page-7":
   
        elif pathname == "/page-8":
     
        elif pathname == "/page-9":
            
         
      
    # S'il y a un problème alors faisont en sort que la page ne change pas d'aspect   
    raise dash.exceptions.PreventUpdate

#=========================================================================

# Activons l'application sur le port 4000 
if __name__ == "__main__":
    app.run_server(
        port=4000,
        debug=True
    )