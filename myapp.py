import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd


df = px.data.gapminder(return_type='pandas')

countries = df['country'].unique()


app = dash.Dash(__name__)
server = app.server

app.layout = html.Div([
    html.H1("GDP per Capita Growth Dashboard"),
    dcc.Dropdown(
        id='country-dropdown',
        options=[{'label': country, 'value': country} for country in countries],
        value='Canada',
        clearable=False,
        style={'width': '300px'}
    ),
    dcc.Graph(id='gdp-growth')
])

@app.callback(
    Output('gdp-growth', 'figure'),
    Input('country-dropdown', 'value')
)
def update_graph(selected_country):
    filtered_df = df[df['country'] == selected_country]

    fig = px.line(filtered_df,
                  x='year',
                  y='gdpPercap',
                  title=f'GDP Per Capita Growth in {selected_country}',
                  markers=True)
    fig.update_layout(xaxis_title='Year', yaxis_title='GDP Per Capita (USD)')
    return fig

if __name__ == '__main__':
    app.run(debug=True)
