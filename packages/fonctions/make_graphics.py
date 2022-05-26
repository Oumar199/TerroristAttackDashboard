
from packages import dbc, html, dcc, dash_table, pd


def make_buttons():
    return html.Div(
                    [
                        dbc.Button(html.I(className= "fa-solid fa-magnifying-glass-minus"), className = "enhance-off btn-primary btn-xs rounded"), 
                        dbc.Button(html.I(className= "fa-solid fa-magnifying-glass"), className = "enhance-on btn-dark btn-xs rounded")
                    ],
                    className = "visual"
                )

def make_figure(figure):
    return dcc.Graph(id="graph", figure=figure)

def phrase(nombre_phrase):
    return html.P(nombre_phrase, className="display-5")

def tab(table):
    return dash_table.DataTable(
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

def make_metrics(title: str, nombre):
    """Conception de métrique

    Args:
        title (str): titre du graphique
        nombre (float): nombre à afficher
    """

    return dbc.Card(
        dbc.CardBody(
            [
                # make_buttons(),
                html.Label(title, id="content-title", style={"margin-bottom": "1rem"}),
                phrase(nombre)
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
    html.Div()
    return dbc.Card(
        dbc.CardBody(
            [
                # make_buttons(),
                html.Label(title, id="content-title", style={"margin-bottom": "1rem"}),
                make_figure(figure) if figure != None else phrase("Pas de graphique")
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
    print(type(table))
    return dbc.Card(
        dbc.CardBody(
            [
                # make_buttons(),
                html.Label(title, id="content-title", style={"margin-bottom": "1rem"}),
                tab(table) if type(table) is pd.DataFrame else phrase("Pas de tableau")
            ],
            className="text-center",
            style = {"paddingLeft": "0!important", "paddingRight": "0!important"}
        ),
        style={"margin": "1rem"},
    )
    


# ===================================================================================

# panorama de graphiques

def make_pan_graphics(figure, number):
    input_radio = dcc.RadioItems(className = "slide-input", id = f"slide-dot-{number}", name="slides")

def panorama():
    """
    <div id="carouselExampleCaptions" class="carousel slide" data-bs-ride="carousel">
  <div class="carousel-indicators">
    <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
    <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="1" aria-label="Slide 2"></button>
    <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="2" aria-label="Slide 3"></button>
  </div>
  <div class="carousel-inner">
    <div class="carousel-item active">
      <img src="..." class="d-block w-100" alt="...">
      <div class="carousel-caption d-none d-md-block">
        <h5>First slide label</h5>
        <p>Some representative placeholder content for the first slide.</p>
      </div>
    </div>
    <div class="carousel-item">
      <img src="..." class="d-block w-100" alt="...">
      <div class="carousel-caption d-none d-md-block">
        <h5>Second slide label</h5>
        <p>Some representative placeholder content for the second slide.</p>
      </div>
    </div>
    <div class="carousel-item">
      <img src="..." class="d-block w-100" alt="...">
      <div class="carousel-caption d-none d-md-block">
        <h5>Third slide label</h5>
        <p>Some representative placeholder content for the third slide.</p>
      </div>
    </div>
  </div>
  <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Previous</span>
  </button>
  <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Next</span>
  </button>
</div>
    """
    