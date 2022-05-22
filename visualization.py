from packages import *
# from packages.fonctions.supprimer_valeurs import supprimer_valeurs
# from packages.fonctions.remplacer_valeurs import remplacer_valeurs
from packages.fonctions.make_graphics import make_metrics, make_graphics, make_tables
from packages.graphiques_metriques import nombre_de_morts_blesses as nmb
from packages.graphiques_metriques import type_cibles as tc
from packages.graphiques_metriques import type_armes as ta
from packages.graphiques_metriques import en_det_po as edp
from packages.graphiques_metriques import groupes_terroristes as gt
from packages.graphiques_metriques import attaques_afrique as aa
from packages.graphiques_metriques import mode_reclamation as mr
from packages.graphiques_metriques import dommages_proprietes as dp
from packages.graphiques_metriques import attaques_suicides as asu
from packages.graphiques_metriques import demande_rancons as dr
from packages.graphiques_metriques import clustering as cl
from packages.graphiques_metriques import prédiction as pred

# =========================================================================

# récupération du temps pour les mises-à-jour
# try:
#     # heure actuel
#     with open("data")
# except Exception as e:


# =========================================================================

# initialisation vide de df_terror
df_terror = None

# Récupération des données prétraitées
try:
    with open("packages/data/cleaned/terror.txt", "rb") as f:
        pick = pickle.Unpickler(f)
        df_terror = pick.load()

except Exception as e:
    print("Pickle File Error:", e)

# =========================================================================

# configurer lien jquery
external_scripts = [
    "https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js",
    "/assets/js/dynamique.js",
]

# configurer font-awesome pour les icones
external_style = ["/assets/fontawesome/css/all.css"]

# Initialisation de l'application
app = dash.Dash(
    __name__, external_scripts=external_scripts, external_stylesheets=external_style,
    suppress_callback_exceptions = True
)

# ajout server
# server = app.server

# =========================================================================


# Mettons la date comme index
df_terror.set_index("date", inplace=True)

# renommons certaines colonnes
df_terror.rename(
    columns={
        "nkill": "Nombre de morts",
        "nwound": "Nombre de blessés",
        "iday": "Jour",
        "iyear": "Année",
        "imonth": "Mois",
        "country_txt": "Pays",
        "region_txt": "Région",
        "city": "Ville",
    },
    inplace=True,
)

# Récupérons la liste des pays
pays = df_terror["Pays"].unique().tolist()

# Créons une liste contenant les mois de l'année
mois = [
    "Janvier",
    "Fevrier",
    "Mars",
    "Fevrier",
    "Mars",
    "Avril",
    "Mai",
    "Juin",
    "Juillet",
    "Aout",
    "Septembre",
    "Octobre",
    "Novembre",
    "Novembre",
    "Décembre",
]

# Récupérons la première date ou la date minimale
first_date = df_terror[["Jour", "Mois", "Année"]].head(1)

# Récupérons la dernière date ou la date maximale
last_date = df_terror[["Jour", "Mois", "Année"]].tail(1)

# =========================================================================

# listes de pages
pages = [
    "Visualisation des nombres de morts et de blessés",
    "Visualisation des types de cibles",
    "Visualisation des types d'armes",
    "Visualisation des nombres d'enlèvements, de détournements ou de prises d'otages",
    "Visualisation des groupes terroristes",
    "Visualisation du terrorisme en Afrique",
    "Visualisation des modes de réclamation",
    "Visualisation des dommages de propriétés",
    "Visualisation des nombres d'attaques suicides",
    "Visualisation des demandes de rançon",
    "Classement",
    "Prédiction du nombre de morts"
]

# liste de boutons de navigation (tests)
navs = []
boutons = [dbc.NavLink(pages[0], href="/", active="exact")]
for j in range(2, len(pages) + 1):
    boutons.append(dbc.NavLink(pages[j - 1], href=f"/page-{j-1}", active="exact"))

# =========================================================================

# Ajout de la barre de navigation
sidebar = dbc.Card(
    dbc.CardBody(
        html.Div(
            [
                html.Div(
                    [
                        html.H2("Attaques terroristes", className="display-4"),
                        html.Hr(),
                        html.P("Choisissez une page", className="lead"),
                        dbc.Nav(boutons, vertical=True, pills=True)
                    ],
                    className="h-100 nav-container p-2"
                ),
                html.Div(
                    html.Div(
                        [
                            html.I(
                                className="fa-solid fa-circle-arrow-right shadow-lg rounded-circle right-arrow icone-rose fa-3x",
                                style={
                                    "position": "absolute",
                                    "top": "50%",
                                    "left": "30%",
                                },
                            ),
                            html.I(
                                className="fa-solid fa-circle-arrow-left shadow-lg rounded-circle left-arrow icone-rose fa-3x",
                                style={
                                    "position": "absolute",
                                    "top": "50%",
                                    "left": "30%",
                                },
                            ),
                        ],
                        className="h-100",
                    ),
                    className="h-100 indic-slide shadow-md rounded-end",
                    style={
                        "position": "fixed",
                        "top": 0,
                        "left": "100%",
                        "width": "80px",
                    },
                ),
            ],
            className="h-100",
            style={"position": "relative"},
        ),
        className="h-100"
    ),
    color="light",
    className="h-100 sidebar shadow-md pd-0",
    style={
        "width": "49rem",
        "position": "fixed",
        # "overflowY": "auto",
        "top": 0,
        "left": "-49rem",
    },
)

# =========================================================================

# Définition de la squelette principale du contenu
content = dbc.Container(
    [
        html.Div(
            dcc.DatePickerRange(
                id="date-picker",
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
                    int(first_date["Jour"]),
                ),
                max_date_allowed=dt(
                    int(last_date["Année"]),
                    int(last_date["Mois"]),
                    int(last_date["Jour"]),
                ),
                # initial_visible_month=dt(
                #     2020,
                #     1,
                #     1
                # ),
                start_date=dt(
                    int(first_date["Année"]),
                    int(first_date["Mois"]),
                    int(first_date["Jour"]),
                ).date(),
                end_date=dt(
                    int(last_date["Année"]),
                    int(last_date["Mois"]),
                    int(last_date["Jour"]),
                ).date(),
                display_format="YY, MMM DD",
                month_format="MMMM, YYYY",
                minimum_nights=4,
                persistence=True,
                persisted_props=["start_date", "end_date"],
                persistence_type="session",
                updatemode="singledate",
                className="shadow-lg"
            ),
            style={"textAlign": "right", "margin": "1rem"},
        ),
        dbc.Row(
            [
                html.Label(id="content-title", style={"margin-bottom": "1rem"}),
                dbc.Col(
                    dcc.Dropdown(
                        id="pays",
                        options=[{"label": p, "value": p} for p in pays],
                        # value = "form-control pd-3",
                        # className="form-control",
                        placeholder="Choisissez un pays",
                        multi=True,
                        style={"verticalAlign": "middle", "padding": "4px!important"},
                    ),
                    width=9,
                ),
                dbc.Col(
                    dbc.Button(
                        "Filtrer par pays",
                        id="filtre",
                        className="btn btn-lg btn-tertiary rounded-0",
                    ),
                    width=3,
                ),
            ],
            id = "header-1",
            className="text-center m-0",
        ),
        html.Div(
            [
                html.H2("Prédiction du nombre de morts"),
                dcc.DatePickerSingle(
                    date=date(2023, 6, 21),
                    display_format='Y, MMMM DD'
                ),  
                dbc.Button(
                    dbc.Button(
                        "Effectuer une prédiction",
                        id="prediction",
                        className="btn btn-lg btn-tertiary rounded-0"
                    )
                ) 
            ],
            id = "header-2",
            className = "text-center",
            style = {"display": "none"}
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
        html.Div(id="principal-content-1"),
        # html.Div(id="principal-content-2", style = {"display": "none"})
    ]
)

# =========================================================================

# Réunissons le location, la barre de navigation et le contenu dans le layout
app.layout = dbc.Container(
    [
        dcc.Location(id="url"),
        dbc.Row(
            [
                dbc.Col(sidebar, width=2, style={"zIndex": 100}),
                dbc.Col(
                    content,
                    width=9,
                    # style = {
                    # "margin-left": "20rem"
                    # }
                ),
            ]
        ),
        html.Div(id = "shad", style = {"display": "none"})
    ],
    fluid=True,
)


# =========================================================================
# =========================================================================

######
# @contextmanager
# def change(path):
#     try:
#         f = open(path, "w")
#         base = sys.stdout
#         sys.stdout = f
#         yield
#     finally:
#         sys.stdout = base


######

# # Définition d'un callback pour ajouter ou supprimer un header
@app.callback(
    [
        # Output(component_id="slider-top", component_property="children"),
        Output(component_id="header-1", component_property="style"),
        Output(component_id="header-2", component_property="style")
        # Output(component_id="principal-content-1", component_property="style"),
        # Output(component_id="principal-content-2", component_property="style")
    ],
    [Input(component_id="url", component_property="pathname")]
)
def add_header(pathname: str):
    '''Cette fonction rend un header visible ou pas 
    Args:
        pathname(str): contient le chemin d'accés
    Returns:
        style du slider
    '''
    if pathname == "/page-10":
        return (
            {"display": "none"}
        ,
            {"display": "flex"}
        # ,
        #     {"display": "none"}
        # ,
        #     {"display": "flex"}
        )
    return (
        {"display": "flex"}
    ,
        {"display": "none"}
    # ,
    #     {"display": "flex"}
    # ,
    #     {"display": "none"}
    )

# Définition des callbacks pour la résolution des questions
@app.callback(
    Output(component_id="principal-content-1", component_property="children"),
    [
        Input(component_id="url", component_property="pathname"),
        Input(component_id="date-picker", component_property="start_date"),
        Input(component_id="date-picker", component_property="end_date"),
    ],
    [
        Input(component_id="filtre", component_property="n_clicks"),
        State(component_id="pays", component_property="value"),
        # Input(component_id="choose-number", component_property="value")
    ],
)
def add_response(pathname, start_date, end_date, n, pays):
    """Fonction qui renvoie une réponse à une question selon le pathname donné en entrée.
    Args:
        pathname(str): Contient le chemin d'accés
        start_date(str): La date de départ
        end_date(str): La date de fin
        pays(str ou list): Contient le pays ou les pays qui est/sont recherchés dans le dataset
        top(int): Définit le numéro du top des pays à afficher dans les pages 8 et 9
    """
    global df_terror
    
    # Filtrage des données par dates et par pays avant de retourner les résultats
    # en fonction du pathname
    df = df_terror.loc[start_date:end_date]
    
    # filtrage par pays si nécessaire
    if n != None:
        if pays != None and pays != "" and pays != []:
            if not type(pays) is list:
                pays = [pays]
            df = df[df["Pays"].isin(pays)]

    
    

    if pathname == "/":
        # Calcul du nombre total de morts enregistrés
        total_morts = df["Nombre de morts"].sum()

        # Titre1
        title1 = "nombre total de personnes mortes à cause du terrorisme"

        # Calcul du nombre total de blessés enregistrés
        total_blesses = df["Nombre de blessés"].sum()

        # Titre2
        title2 = "nombre total de personnes blessées à cause du terrorisme"

        # Initialisation des lignes
        rows = []

        # pour la métrique1
        content1 = dbc.Col(make_metrics(title1, total_morts), width=5)

        # pour la métrique2
        content2 = dbc.Col(make_metrics(title2, total_blesses), width=5)

        # ligne 1
        rows.append([content1, content2])

        # ligne 2
        rows.append(
            [
                dbc.Col(make_graphics(*nmb.graphique_1(df)), width=11)
            ]
        )
        # ligne 3
        rows.append(
            [
                dbc.Col(make_graphics(*nmb.graphique_2(df)), width=11)
            ]
        )
        # ligne 4
        rows.append(
            [
                dbc.Col(make_graphics(*nmb.graphique_12(df)), width=11)
            ]
        )
        # ligne 5
        rows.append(
            [
                dbc.Col(make_graphics(*nmb.graphique_13(df)), width=11)
            ]
        )
        # ligne 6
        rows.append(
            [
                dbc.Col(make_graphics(*nmb.graphique_3(df)), width=11)
            ]
        )
        # ligne 7
        rows.append(
            [
                dbc.Col(make_graphics(*nmb.graphique_4(df)), width=11)
            ]
        )
        # ligne 8
        rows.append(
            [
                dbc.Col(make_graphics(*nmb.graphique_5(df)), width=11)
            ]
        )
        # ligne 9
        rows.append(
            [
                dbc.Col(make_graphics(*nmb.graphique_6(df)), width=11)
            ]
        )
        # ligne 10
        rows.append(
            [
                dbc.Col(make_graphics(*nmb.graphique_7(df)), width=11)
            ]
        )
        # ligne 11
        rows.append(
            [
                dbc.Col(make_graphics(*nmb.graphique_8(df)), width=11)
            ]
        )

        return html.Div([dbc.Row(line, className = "justify-content-around") for line in rows], className = "text-center")

    elif pathname == "/page-1":
        # initialisation lignes
        rows = []
        
        # ligne 1
        rows.append(
            [
                dbc.Col(make_graphics(*tc.graphique_1(df)), width = 11)
            ]
        )
        
        # ligne 2
        rows.append(
            [
                dbc.Col(make_graphics(*tc.graphique_2(df)), width = 11)
            ]
        )
        
        # ligne 3
        rows.append(
            [
                dbc.Col(make_graphics(*tc.graphique_3(df)), width = 11)
            ]
        )
        
        
        return html.Div([dbc.Row(line, className = "justify-content-around") for line in rows], className = "text-center")
        

    elif pathname == "/page-2":
        
        # initialisation lignes
        rows = []
        
        # ligne 1
        rows.append(
            [
                dbc.Col(make_graphics(*ta.graphique_1(df)), width = 11)
            ]
        )
        
        # ligne 2
        rows.append(
            [
                dbc.Col(make_graphics(*ta.graphique_2(df)), width = 11)
            ]
        )
        
        # ligne 3
        rows.append(
            [
                dbc.Col(make_graphics(*ta.graphique_3(df)), width = 11)
            ]
        )
        
        # ligne 4
        rows.append(
            [
                dbc.Col(make_graphics(*ta.graphique_4(df)), width = 11)
            ]
        )
        
        return html.Div([dbc.Row(line, className = "justify-content-around") for line in rows], className = "text-center")

    elif pathname == "/page-3":
        
        # initialisation lignes
        rows = []
        
        # ligne 1
        rows.append(
            [
                dbc.Col(make_graphics(*edp.graphique_1(df)), width = 11)
                # dbc.Col(make_graphics(*ta.graphique_2(df)), width = 5)
            ]
        )
        
        return html.Div([dbc.Row(line, className = "justify-content-around") for line in rows], className = "text-center")
        
    elif pathname == "/page-4":
        # initialisation lignes
        rows = []
        
        # ligne 1
        rows.append(
            [
                dbc.Col(make_graphics(*gt.graphique_1(df)), width = 11)
                # dbc.Col(make_graphics(*ta.graphique_2(df)), width = 5)
            ]
        )
        
        # ligne 2
        rows.append(
            [
                dbc.Col(make_graphics(*gt.graphique_2(df)), width = 11)
                # dbc.Col(make_graphics(*ta.graphique_2(df)), width = 5)
            ]
        )
        
        # ligne 3
        rows.append(
            [
                dbc.Col(make_graphics(*gt.graphique_3(df)), width = 11)
            ]
        )
        
        return html.Div([dbc.Row(line, className = "justify-content-around") for line in rows], className = "text-center")
        

    elif pathname == "/page-5":
        
        # initialisation lignes
        rows = []
        
        # ligne 1
        rows.append(
            [
                dbc.Col(make_graphics(*aa.graphique_1(df)), width = 11),
                # dbc.Col(make_graphics(*ta.graphique_2(df)), width = 5)
            ]
        )
        
        # ligne 2
        rows.append(
            [
                dbc.Col(make_graphics(*aa.graphique_2(df)), width = 11),
                # dbc.Col(make_graphics(*ta.graphique_2(df)), width = 5)
            ]
        )
        
        return html.Div([dbc.Row(line, className = "justify-content-around") for line in rows], className = "text-center")
        
        
    elif pathname == "/page-6":
        # initialisation lignes
        rows = []
        
        # ligne 1
        rows.append(
            [
                dbc.Col(make_graphics(*mr.graphique_1(df)), width = 11),
                # dbc.Col(make_graphics(*ta.graphique_2(df)), width = 5)
            ]
        )
        
        return html.Div([dbc.Row(line, className = "justify-content-around") for line in rows], className = "text-center")
        

    elif pathname == "/page-7":
        # initialisation lignes
        rows = []
        
        # ligne 1
        rows.append(
            [
                dbc.Col(make_tables(*dp.graphique_1(df)), width = 11)
            ]
        )
        # ligne 2
        rows.append(
            [
                dbc.Col(make_tables(*dp.graphique_2(df)), width = 11)
            ]
        )
        
        return html.Div([dbc.Row(line, className = "justify-content-around") for line in rows], className = "text-center")
        
        

    elif pathname == "/page-8":
        
        # initialisation lignes
        rows = []
        
        # ligne 1
        rows.append(
            [
                dbc.Col(make_graphics(*asu.graphique_1(df)), width = 11)
            ]
        )
        # ligne 2
        rows.append(
            [
                dbc.Col(make_graphics(*asu.graphique_2(df)), width = 11)
            ]
        )
        
        return html.Div([dbc.Row(line, className = "justify-content-around") for line in rows], className = "text-center")
        
        

    elif pathname == "/page-9":
        
        # initialisation lignes
        rows = []
        
        # ligne 1
        rows.append(
            [
                dbc.Col(make_graphics(*dr.graphique_1(df)), width = 11)
            ]
        )
        # ligne 2
        rows.append(
            [
                dbc.Col(make_graphics(*dr.graphique_2(df)), width = 11)
            ]
        )
        
        return html.Div([dbc.Row(line, className = "justify-content-around") for line in rows], className = "text-center")
        
        

    # S'il y a un problème alors faisont en sort que la page ne change pas d'aspect
    # raise dash.exceptions.PreventUpdate


# =========================================================================

# Activons l'application sur le port 4000
if __name__ == "__main__":
    app.run_server(port=4000, debug=True)
