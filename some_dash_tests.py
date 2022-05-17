import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


app = dash.Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.LITERA])


def recup_and_process_data():
    try:
        df = pd.read_csv("data/cleaned/terror.csv")
        
        print(df.dtypes)
        # regroupons les données par pays, année et mois
        df_pays_morts_anim: pd.DataFrame = df.groupby(['country_txt', 'date', "imonth"], as_index = False).sum('nkill')
        
        # changeons les noms des colonnes
        df_pays_morts_anim.rename(columns={"country_txt": "Pays", "nkill": "Nombre de morts", "imonth": "Mois"}, inplace=True)
        
        # trier par année
        # df_pays_morts_anim.sort_values("Année")
        
        # definition de limites pour l'axe des ordonnées
        range_y = [df_pays_morts_anim["Nombre de morts"].min()-30, df_pays_morts_anim["Nombre de morts"].max()+30]
        
        fig = px.line(df_pays_morts_anim ,x = "Mois", y = "Nombre de morts", color = "Pays", animation_frame="date", range_y=range_y)
        
        fig.update_layout(dict(title = dict(text = "Animation par année du nombre de morts par pays et par mois")))
        
        return fig
    
    except Exception as e:
        print(f"Error occured {e}")

app.layout = html.Div(
    [
        html.H4("Tache de visualisation", className="display-5 bg-light text-center", style={"padding": "2rem", "margin-bottom": "2rem"}),
        dbc.Container(
            dbc.Card(
                dbc.CardBody(
                    dcc.Graph(figure = recup_and_process_data(), id="graphic")
                ),
                className="bg-light"
            )
        )
    ]
)

if __name__ == "__main__":
    print("port 8050")
    app.run_server(debug=True)