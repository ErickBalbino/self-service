from server import app
from layouts.main import layout
from callbacks.main import *

app.layout = layout

if __name__ == '__main__':
    app.run_server(debug=True)
