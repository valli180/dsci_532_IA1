import dash
from dash import Dash, html, dcc, Input, Output
import altair as alt
import pandas as pd
import numpy as np


data = pd.read_csv("data/customer_churn.csv")
numerical_features_to_analyze = ['Account_Length', 'Vmail_Message', 'Day_Mins', 'Eve_Mins',
       'Night_Mins', 'Intl_Mins', 'CustServ_Calls', 'Day_Calls', 'Day_Charge',
       'Eve_Calls', 'Eve_Charge', 'Night_Calls', 'Night_Charge', 'Intl_Calls',
       'Intl_Charge', 'Churn']
data = data[numerical_features_to_analyze]


def plot_altair_num(xcol):
    chart_num = alt.Chart(data).mark_bar().encode(
        x=xcol,
        y=alt.Y('count(Churn)'),
        color='Churn').interactive()
    return chart_num.to_html()


app = Dash(__name__, external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])
app.layout = html.Div([
        dcc.Dropdown(
            id='xcol', value="Account_Length",
            options=[{'label': i, 'value': i} for i in data.columns]),
        html.Iframe(
            id='barplot',
            style={'border-width': '0', 'width': '100%', 'height': '400px'},
            srcDoc=plot_altair_num(xcol="Account_Length"))])

@app.callback(
    Output('barplot', 'srcDoc'),
    Input('xcol', 'value'))
def update_output(xcol):
    return plot_altair_num(xcol)    

if __name__=='__main__':
    app.run_server(debug=True, port=9096)

server = app.server
