import datetime
from PIL import Image
import numpy as np
import plotly.express as px
from matplotlib.pyplot import figure

import dash
from dash import html
from dash.dependencies import Input, Output, State
from dash import dcc
import dash_uploader as du
import subprocess

searchMethod = ''
occurences = ''

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
du.configure_upload(app, r'')

app.layout = html.Div([
    html.Div([
        html.Div([
            du.Upload(
                id='upload-document',
                text='Drag and Drop Document Here to upload!',
                text_completed='Uploaded the following document: ',
                filetypes=['pdf'],
                upload_id="documents"
            )],
            style={
                'width': '48vw',
                'margin': '10px',
                'cursor': 'pointer'
        },
        ),
        html.Div(
            [du.Upload(
                id='upload-image',
                text='Drag and Drop Image Here to upload!',
                text_completed='Uploaded the following image: ',
                filetypes=['png'],
                upload_id="images"
            )],
            style={
                'height': '100%',
                'width': '48vw',
                'margin': '10px',
                'cursor': 'pointer'
            },
        ), ], style={'display': 'flex',   'flex-direction': 'row',
                     'justify-content': 'space-between'}),
    html.Div([
        html.Div(
            html.Button('Quickest', id='submit1', n_clicks=0), style={'height': '200px', 'display': 'flex', 'flex-direction': 'column', 'justify-content': 'space-evenly'}),
        html.Div(
            html.Button('Middle', id='submit2', n_clicks=0), style={'height': '200px', 'display': 'flex', 'flex-direction': 'column', 'justify-content': 'space-evenly'}),
        html.Div(
            html.Button('Most Accurate', id='submit3', n_clicks=0), style={'height': '200px', 'display': 'flex', 'flex-direction': 'column', 'justify-content': 'space-evenly'})], style={'margin': 'auto auto', 'width': '40vw', 'display': 'flex',   'flex-direction': 'row',
                                                                                                                                                                                          'justify-content': 'space-evenly'}),
    html.Div(id="occurences-container", children=[
        html.Div([
            html.Button('First Occurence', id='submit4', n_clicks=0),
            html.Button('All Occurences', id='submit5', n_clicks=0)], style={'margin': 'auto auto', 'width': '30vw', 'display': 'flex',   'flex-direction': 'row', 'justify-content': 'space-evenly'})], style={'display': 'none'}),
    html.Div(id='output-image-upload'),
], style={'marginTop': '10vh'})


@app.callback(Output('occurences-container', 'style'), [Input('submit1', 'n_clicks'), Input('submit2', 'n_clicks'), Input('submit3', 'n_clicks')])
def toggleVisbility(btn1, btn2, btn3):
    global searchMethod
    if btn1:
        searchMethod = '0'
    elif btn2:
        searchMethod = '1'
    elif btn3:
        searchMethod = '2'
    if btn1 or btn2 or btn3:
        return {'display': 'block'}
    else:
        return {'display': 'none'}


@app.callback(Output('output-image-upload', 'children'), [Input('submit4', 'n_clicks'), Input('submit5', 'n_clicks')])
def callScript(btn1, btn2):
    global occurences
    if btn1:
        occurences = '0'
    elif btn2:
        occurences = '1'
    if btn1 or btn2:
        subprocess.check_output(
            'python3 convertPDF.py', shell=True)
        result = subprocess.check_output(
            'python3 main.py {} {}'.format(occurences, searchMethod), shell=True)
        try:
            img = np.array(Image.open(f"output/output.png"))
        except OSError:
            raise PreventUpdate

        fig = px.imshow(img)
        fig.update_layout(coloraxis_showscale=False)
        fig.update_xaxes(showticklabels=False)
        fig.update_yaxes(showticklabels=False)

        return dcc.Graph(figure=fig)
    else:
        return False


if __name__ == '__main__':
    app.run_server(debug=True)
