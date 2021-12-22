from server import app
from layouts.main import layout
from callbacks.main import *
import logging 

logging.basicConfig(
    filename='web.log',
    filemode='a',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(name)s %(message)s'
)
logger = logging.getLogger(__name__)


app.layout = layout

if __name__ == '__main__':
    app.run_server(debug=True)
