
# !/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Bruce_H_Cottman"
__license__ = "MIT License"

import streamlit as st
import pandas as pd
from pydataset import data

df_data = data().sort_values('dataset_id').reset_index(drop=True)
st.dataframe(df_data, width=900, height=150)  #choices

option = st.selectbox(
    'select a dataset to display dataset and chart the dataset numeric columns?', df_data['dataset_id'])

dataset = data(option)

if isinstance(dataset, (pd.core.frame.DataFrame, pd.core.series.Series)):
    st.dataframe(dataset, height=150)
    st.line_chart(dataset)

