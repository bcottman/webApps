# !/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Bruce_H_Cottman"
__license__ = "MIT License"


import pandas as pd
from pydataset import data
from flask import Flask, request, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.debug = True
Bootstrap(app)

@app.route('/show', methods=['GET'])
def dataViewer():
    dataset_name = request.args.get('dataset')
    if dataset_name == None:
        dataset_name = 'Aids2'

    if type(data(dataset_name)) != pd.core.frame.DataFrame:
        return('Bad dataset name:{}'.format(dataset_name))

    df = data(dataset_name)

    return render_template("df.html", name=dataset_name, data=df.to_html())

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')