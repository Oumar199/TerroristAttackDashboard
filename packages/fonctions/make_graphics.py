from packages import dbc, html, dcc

def make_metrics(title: str, nombre: float):
    """Conception de métrique

    Args:
        title (str): titre du graphique
        nombre (float): nombre à afficher
    """
    
    return dbc.Card(
                dbc.CardBody(
                    [
                        html.Label(title, id = "content-title", style = {"margin-bottom": "1rem"}),
                        html.P(nombre, className="display-5")
                    ],
                    className="text-center"
                ),
                style={
                    "margin": "2rem"
                }
            )


def make_graphics(title: str, figure):
    """Conception de métrique

    Args:
        title (str): titre du graphique
        figure (Any): graphique à afficher
    """
    
    return dbc.Card(
                dbc.CardBody(
                    [
                        html.Label(title, id = "content-title", style = {"margin-bottom": "1rem"}),
                        dcc.Graph(id = "graph", figure=figure)
                    ],
                    className="text-center"
                ),
                style={
                    "margin": "2rem"
                }
            )