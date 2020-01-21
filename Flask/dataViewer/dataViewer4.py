# !/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Bruce_H_Cottman"
__license__ = "MIT License"


import pandas as pd
from pydataset import data
from flask import Flask, request, render_template, session
from flask_bootstrap import Bootstrap
from bokeh.plotting import Figure
from bokeh.models import ColumnDataSource
from bokeh.embed import components
from bokeh.resources import INLINE
from bokeh.util.string import encode_utf8
from bokeh.palettes import d3

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = '\xbfx\x02\xf7\xeao\ro\rp&Q\xa1\xbdV\xd9'
Bootstrap(app)

@app.route('/show', methods=['GET'])
def dataViewer():
    dataset_name = request.args.get('dataset')
    if dataset_name == None:
        dataset_name = 'Aids2'

    if type(data(dataset_name)) != pd.core.frame.DataFrame:
        return('Bad dataset name:{}'.format(dataset_name))

    df = data(dataset_name)
    session['dataset_name'] = dataset_name

    return render_template("df.html", name=dataset_name, data=df.to_html())

@app.route('/plot')
def dataViewer_4():

    dataset_name = session['dataset_name']

    if dataset_name == None:
        dataset_name = 'Aids2'

    if type(data(dataset_name)) != pd.core.frame.DataFrame:
        return('Bad dataset name:{}'.format(dataset_name))


    if type(data(dataset_name)) != pd.core.frame.DataFrame:
        return('Bad dataset name:{}'.format(dataset_name))

    # get dframe by name
    df = data(dataset_name)
    # Create a ColumnDataSource object

    bp_df = ColumnDataSource(df)
    # Create  plot as a bokeh.figure object
    plot = Figure(height=400,
                       width=400,
                       title=dataset_name,
                       )

    x_ax = [str(i) for i in range(df.shape[0])]
    palette_ = d3['Category10'][10]

    for n, cname in enumerate(df.columns):
       plot.line(x=x_ax, y=list(df[cname].values)
                 , color=palette_[n]
                 , legend='line')

    # grab the static resources
    js_resources = INLINE.render_js()
    css_resources = INLINE.render_css()

    # render template
    script, div = components(plot)
    html = render_template(
        'index_.html',
        plot_script=script,
        plot_div=div,
        js_resources=js_resources,
        css_resources=css_resources,
    )
    return encode_utf8(html)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')