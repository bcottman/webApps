from pydataset import data
import pandas as pd
from flask import Flask

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = '\xbfx\x02\xf7\xeao\ro\rp&Q\xa1\xbdV\xd9'

#<more code...>
if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0')