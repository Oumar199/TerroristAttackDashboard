from packages import dbc, html, dcc, dash_table, pd


def make_metrics(title: str, nombre: float):
    """Conception de métrique

    Args:
        title (str): titre du graphique
        nombre (float): nombre à afficher
    """

    return dbc.Card(
        dbc.CardBody(
            [
                html.Label(title, id="content-title", style={"margin-bottom": "1rem"}),
                html.P(nombre, className="display-5"),
            ],
            className="text-center",
        ),
        style={"margin": "1rem"},
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
                html.Label(title, id="content-title", style={"margin-bottom": "1rem"}),
                dcc.Graph(id="graph", figure=figure),
            ],
            className="text-center",
            style = {"paddingLeft": "0!important", "paddingRight": "0!important"}
        ),
        style={"margin": "1rem"},
    )
    
def make_tables(title: str, table: pd.DataFrame):
    """Conception de métrique

    Args:
        title (str): titre du graphique
        table (Any): tableau à afficher
    """

    return dbc.Card(
        dbc.CardBody(
            [
                html.Label(title, id="content-title", style={"margin-bottom": "1rem"}),
                dash_table.DataTable(
                    id="table",
                    columns=[{"name": i, "id": i} for i in table.columns],
                    data=table.to_dict("records"),
                    style_as_list_view=True,
                    style_header={
                        "backgroundColor": "black",
                        "color": "white",
                        "fontWeight": "bold",
                    },
                    style_cell={
                        "color": "black",
                        "text-align": "center",
                        "overflow": "hidden",
                        "maxWidth": 0,
                    },
                )
            ],
            className="text-center",
            style = {"paddingLeft": "0!important", "paddingRight": "0!important"}
        ),
        style={"margin": "1rem"},
    )
    
    
