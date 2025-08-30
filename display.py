from business import GraphBuilder
from dash import Input, Output, State, dcc, html, Dash, dash_table
from database import load_data


app = Dash(__name__)
data = load_data()
gb = GraphBuilder()


# Tasks 7.4.1, 7.4.2, 7.4.3, 7.4.11, 7.4.14, 7.4.16
app.layout = html.Div(
    [
        html.H1("Customer Segmentation App"),
        html.Div([
            dash_table.DataTable(
                data=data.sample_data(),
                page_size=10,
            )
        ]),
        dcc.Dropdown(
            options=data.country(),
            value=data.country()[0],
            multi=False,
            id="chosen-country-dropdown"
        ),
        html.H1("Experiment"),
        dcc.Dropdown(
            options=["Histogram", "Scatter Plot", "Box Plot"],
            value="Histogram",
            multi=False,
            id="graph-type-dropdown"
        ),
        html.Div(id="ft-visual-output-display"),
        html.H2("Choose your expected cluster groups"),
        dcc.RangeSlider(
            id='cluster-range-slider',
            min=2,
            max=20,
            step=1,
            value=[2, 11],  # Default range
            marks={i: str(i) for i in range(2, 21, 2)}
        ),
        html.Div(id="scoring-clusters-display"),
        html.H2("Choose cluster number for experiment"),
        dcc.Slider(
            min=2, 
            max=20, 
            step=1, 
            value=3,
            marks={i: str(i) for i in range(2, 21, 2)},
            id="cluster-number-slider"
        ),
        dcc.Dropdown(
            options=["2D Scatter Plot", "3D Scatter Plot"],
            value="2D Scatter Plot",
            multi=False,
            id="plot-type-dropdown"
        ),
        html.H1("Results"),
        html.Button("Begin experiment", id="start-experiment-button", n_clicks=0),
        html.Div(id="results-display")
    ]
)


@app.callback(
    Output("ft-visual-output-display", "children"),
    Input("chosen-country-dropdown", "value"),
    Input("graph-type-dropdown", "value")
)
def display_feature(selected_country, graph_type):

    img = gb.build_graph(selected_country, graph_type)

    return html.Div(
        [
            html.H2("Feature Distribution"),
            html.Img(src=f"data:image/png;base64,{img}", style={"width": "100%", "max-width": "900px"})
        ]
    )


@app.callback(
    Output("scoring-clusters-display", "children"),
    Input("cluster-range-slider", "value")
)
def display_scoring_cluster(given_range):
   
    img = gb.line_plot(range(given_range[0], given_range[1]))

    return html.Div(
        [
            html.H2("Scenario of Different Cluster Groups"),
            html.Img(src=f"data:image/png;base64,{img}", style={"width": "100%", "max-width": "900px"}),
            html.H4("You should choose the number of clusters at the elbow point for Inertia Errors."
            " The Silhouette Score should be as close to 1 as possible.")
        ]
    )


@app.callback(
    Output("results-display", "children"),
    Input("start-experiment-button", "n_clicks"),
    Input("cluster-number-slider", "value"),
    Input("plot-type-dropdown", "value")
)
def display_results(n_clicks, cluster_number, plot_type):
    if n_clicks == 0:
        return html.Div()
    else:
        fig = gb.result(cluster_number, plot_type)

    return html.Div(
        [
            html.H2("Observations"),
            dcc.Graph(figure=fig),
        ]
    )

if __name__ == "__main__":
    app.run(debug=True)