import dash
from dash import html
from dash.dependencies import Input, Output, State
from dash import dcc
import dash_uploader as du
import subprocess

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
                filetypes=['pdf', 'png', 'jpeg'],
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
                filetypes=['pdf', 'png', 'jpeg'],
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
        html.Div([
            html.Button('Quickest', id='submit1', n_clicks=0), html.Div('Time Complexity: '), html.Div('Accuracy: '), html.Div('Search Method: ')], style={'height': '200px', 'display': 'flex', 'flex-direction': 'column', 'justify-content': 'space-evenly'}),
        html.Div([
            html.Button('Middle', id='submit2', n_clicks=0), html.Div('Time Complexity: '), html.Div('Accuracy: '), html.Div('Search Method: ')], style={'height': '200px', 'display': 'flex', 'flex-direction': 'column', 'justify-content': 'space-evenly'}),
        html.Div([
            html.Button('Most Accurate', id='submit3', n_clicks=0), html.Div('Time Complexity: '), html.Div('Accuracy: '), html.Div('Search Method: ')], style={'height': '200px', 'display': 'flex', 'flex-direction': 'column', 'justify-content': 'space-evenly'})], style={'margin': '50px auto', 'width': '40vw', 'display': 'flex',   'flex-direction': 'row', 'justify-content': 'space-evenly'}),
], style={'marginTop': '10vh'})


if __name__ == '__main__':
    app.run_server(debug=True)
