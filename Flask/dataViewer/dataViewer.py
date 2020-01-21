# !/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Bruce_H_Cottman"
__license__ = "MIT License"


import pandas as pd
from pydataset import data
from flask import Flask, request

app = Flask(__name__)
app.debug = True
#app.config['SECRET_KEY'] = '\xbfx\x02\xf7\xeao\ro\rp&Q\xa1\xbdV\xd9'


@app.route('/show', methods=['GET'])
def dataViewer_1():
    dataset_name = request.args.get('dataset')
    if dataset_name == None:
        dataset_name = 'Aids2'

    if type(data(dataset_name)) != pd.core.frame.DataFrame:
        return('Bad dataset name:{}'.format(dataset_name))

    return data(dataset_name).to_html(header="true", table_id="table")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
