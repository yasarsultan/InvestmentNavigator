import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

df1 = pd.DataFrame({'X': ['A', 'B', 'C', 'D'], 'Y': [1,2,2,4]})
fig1 = px.line(df1, x='X', y='Y')

df2 = pd.DataFrame({'X': ['A', 'B', 'C', 'D'], 'Y': [1,2,3,5]})
fig2 = px.line(df2, x='X', y='Y')

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Keep Investment Simple"),
    html.Div(
        children=['Gold', html.Hr(), html.H3('Gold Returns', style={'text-align': 'center'}),
                  dcc.Graph(id='graph1', figure=fig1)
                  ],
                  style={'width': '48%', 'flex': '1'}
    ),

    html.Div(
        children=['Real Estate', html.Hr(), html.H3('Real Estate Returns', style={'text-align': 'center'}), 
                  dcc.Graph(id='graph2', figure=fig2)
                  ],
                  style={'width': '48%', 'flex': '1'}
    )
])

# app.layout = html.Div([
#     html.H1('Keep Investment Simple'),
#     html.Div(
#         children=[html.H3('Gold Returns', style={'text-align': 'center'}),
#                   dcc.Graph(id='graph1', figure=fig1)
#         ],
#         style={'flex': '1'}
#     ),
#     # html.Div(
#     #     children=[],
#     #     style={'width': '2px', 'height': '100vh', 'background-color': '#000', 'margin': 'auto'}
#     # ),
#     html.Div(
#         children=[html.H3('Real Estate Returns', style={'text-align': 'center'}), 
#                   dcc.Graph(id='graph2', figure=fig2)
#         ],
#         style={'flex': '1'}
#     )
# ], style={'display': 'flex'})

print("Hell")
if __name__ == '__main__':
    app.run_server(debug=True)