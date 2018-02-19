from .find_nearest_airport import dist_between_two_points
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

df = pd.read_csv('airports.csv')
df = df.sort_values(by=['NAME'])

app = dash.Dash()
app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

app.layout = html.Div(children=[
    # Header
    html.H4(children='Distance to Other Airports'),

    # Dropdown Label
    html.H6(children='Distance From:', style={'fontSize': 12}),
    html.Div([
        dcc.Dropdown(
            id='airport-selection',
            options=[{'label': i.title(), 'value': i} for i in df['NAME']],
            value=df.at[0, 'NAME']
        )
    ], style={'width': '30%'}),

    # Table
    html.Div([
        html.Div(id='output-table'),
    ], style={'width': '30%', 'display': 'inline-block'}),


    # Map
    html.Div([
        dcc.Graph(id='map'),
    ], style={'width': '65%', 'display': 'inline-block', 'verticalAlign': 'top'}),
])


@app.callback(
    dash.dependencies.Output('output-table', 'children'),
    [dash.dependencies.Input('airport-selection', 'value')])
def update_table(airport, max_rows=10):
    """
    Finds the airport in the dataframe, gets coordinates and compares it to all other airports
    Creates a new dataframe without the selected value, appends a distance column with the distance
    from the selected airport, then returns a table with that information.
    :param airport: Value of selection from airport selection dropdown (airport name)
    :return: A table in distance ascending order with nearest 10 airports
    """
    filtered_df = df[df.NAME == airport]
    coords = "%f, %f" % (filtered_df.Latitude, filtered_df.Longitude)
    df_clone = df.copy()
    df_clone['Dist'] = pd.Series()
    df_clone = df_clone[df_clone.NAME != airport]
    for i, row in df_clone.iterrows():
        coords_i = "%f, %f" % (row.Latitude, row.Longitude)
        dist = round(dist_between_two_points(coords, coords_i), 2)
        df_clone.loc[i, 'Dist'] = dist

    df_clone = df_clone.sort_values(by=['Dist'])
    df_clone = df_clone.drop(columns=['Latitude', 'Longitude'])

    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in df_clone.columns])] +

        # Body
        [html.Tr([
            html.Td(df_clone.iloc[i][col]) for col in df_clone.columns
        ], className='airport-row') for i in range(min(len(df_clone), max_rows))]
    )


@app.callback(
    dash.dependencies.Output('map', 'figure'),
    [dash.dependencies.Input('airport-selection', 'value')])
def update_map(airport):
    """
    Uses airport name to find lat/lon coordinates of the currently selected airport, then displays the location
    of this airport with a red marker on a map.
    :param airport: Value of selection from airport selection dropdown (airport name)
    :return: Map with location of airport marked
    """
    filtered_df = df[df.NAME == airport]
    plot = [dict(
        type='scattergeo',
        locationmode='united kingdom',
        lon=filtered_df['Longitude'],
        lat=filtered_df['Latitude'],
        hoverinfo='text',
        text=filtered_df['NAME'],
        mode='markers',
        marker=dict(
            size=5,
            color='rgb(255, 0, 0)',
            line=dict(
                width=3,
                color='rgba(68, 68, 68, 0)'
            )
        ))]
    layout = dict(
        title='Chosen Airport Location:',
        showlegend=False,
        geo=dict(
            scope='europe',
            projection=dict(type='azimuthal equal area', scale=4),
            center=dict(lat=54.37, lon=-1.91),
            resolution="50",
            showland=True,
            landcolor='rgb(243, 243, 243)',
            countrycolor='rgb(204, 204, 204)',
        ),
        margin={'l': 0, 'b': 0, 't': 40, 'r': 0},
        autosize=True,
    )

    return {
        'data': plot,
        'layout': layout,
    }
