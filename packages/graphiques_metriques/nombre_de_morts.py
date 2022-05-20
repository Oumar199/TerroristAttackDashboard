from packages import pd, px
from packages.fonctions.supprimer_valeurs import supprimer_valeurs


def graphique_1(df: pd.DataFrame):
    # recuperons les données en regroupant par pays et année
    df_pays_morts = df.groupby(['Pays', 'Année'], as_index = False).sum('Nombre de morts')
    
    # tracons le graphique
    fig = px.line(df_pays_morts, x = "Année", y = "Nombre de morts", color = "Pays")
    
    # Titre
    title = "nombre de morts causés par des attaques terroristes par pays et par année"
    
    # Retournons le résultat
    return title, fig


def graphique_2(df: pd.DataFrame):
    # recuperons les données en regroupant par region et année
    df_region_morts = df.groupby(['Région', 'Année'], as_index = False).sum('Nombre de morts')
    
    # tracons le graphique
    fig = px.line(df_region_morts, x = "Année", y = "Nombre de morts", color = "Région")
    
    # Titre
    title = "nombre de morts causés par des attaques terroristes par région et par année"
    
    # Retournons le résultat
    return title, fig


def graphique_3(df: pd.DataFrame):

    # recuperons les données en regroupant par province ou Etat et par année
    df_provetat_morts = df.groupby(['provstate', 'Année'], as_index = False).sum('Nombre de morts')
    
    # modifions le nom de la colonne provstate
    df_provetat_morts.rename(columns={"provstate": "Province/Etat"}, inplace = True)
    
    # supprimons les valeurs non pertinentes
    df_provetat_morts = supprimer_valeurs(df_provetat_morts, "Province/Etat", ["''", "Unknown", "unknown"])
    
    # tracons le graphique
    fig = px.line(df_provetat_morts, x = "Année", y = "Nombre de morts", color = "Province/Etat")
    
    # Titre
    title = "nombre de morts causés par des attaques terroristes par province/Etat et par année"
    
    # Retournons le résultat
    return title, fig

def graphique_4(df: pd.DataFrame):
    # Sommons les nombres morts de morts par pays
    df_pays_geom = df.groupby("Pays", as_index=False).sum("Nombre de morts") 
    
    # Tracons le choroplèthe en colorant suivant les nombres de morts
    fig = px.choropleth(df_pays_geom, locations="Pays", locationmode="country names", featureidkey="properties.name", color="Nombre de morts", color_continuous_scale="Viridis", scope="world", hover_name="Pays")
    fig.update_layout(margin = {"l":0, "r":0, "t":0, "b":0})
    
    # Titre
    title = "répartition géographique du nombre de morts causés par des attaques terroristes par pays"
    
    # Retournons le résultat
    return title, fig

def graphique_5(df: pd.DataFrame):
    # Sommons les nombres morts de morts par pays
    df_geom_evolution_morts = df.groupby(["Année", "Pays"], as_index=False)["Nombre de morts"].sum() 
    
    # Tracons le choroplèthe en colorant suivant les nombres de morts
    fig = px.choropleth(df_geom_evolution_morts, locations="Pays",
                    color="Nombre de morts",
                    hover_name="Pays",
                    projection='natural earth',
                    locationmode="country names",
                    animation_frame="Année",
                    color_continuous_scale="peach",
                    template="ggplot2")

    fig.update_layout(title=dict(font=dict(size=28),x=0.5,xanchor='center'),
                    margin=dict(l=60, r=60, t=50, b=50))

    # Titre
    title = "évolution annuelle de la répartition géographique du nombre de morts causés par des attaques terroristes"
    
    # Retournons le résultat
    return title, fig

def graphique_6(df: pd.DataFrame):
    # Sommons les nombres morts de blesses par pays
    df_geom_evolution_blesses = df.groupby(["Année", "Pays"], as_index=False)["Nombre de blessés"].sum() 
    
    # Tracons le choroplèthe en colorant suivant les nombres de morts
    fig = px.choropleth(df_geom_evolution_blesses, locations="Pays",
                    color="Nombre de blessés",
                    hover_name="Pays",
                    projection='natural earth',
                    locationmode="country names",
                    animation_frame="Année",
                    color_continuous_scale="peach",
                    template="ggplot2")

    fig.update_layout(title=dict(font=dict(size=28),x=0.5,xanchor='center'),
                    margin=dict(l=60, r=60, t=50, b=50))

    # Titre
    title = "évolution annuelle de la répartition géographique du nombre de personnes blessés par des attaques terroristes"
    
    # Retournons le résultat
    return title, fig







