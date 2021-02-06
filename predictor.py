# @Author: Shounak Ray <Ray>
# @Date:   05-Feb-2021 19:02:50:501  GMT-0700
# @Email:  rijshouray@gmail.com
# @Filename: predictor.py
# @Last modified by:   Ray
# @Last modified time: 06-Feb-2021 01:02:89:894  GMT-0700
# @License: [Private IP]

import math
import os
import re

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

pbp_files = list(os.walk(r'Data'))[0][2]
df_ALL = []
for f_name in pbp_files:
    name = 'df_' + re.findall(r"\d{4}", f_name)[0]
    try:
        print('Importing ' + '`' + name + '`...')
        exec(name + " = pd.read_csv('Data/" + f_name + "')")
    except Exception as e:
        print('`' + name + '`' + ' didn\'t import' + '\n\t'
              + str(e) + '\tTrying again...')
        try:
            exec(name + " = pd.read_csv('Data/"
                 + f_name + "', error_bad_lines=False)")
        except Exception as e:
            print('Failed, please see data!\n\t' + str(e) + '\n\n')

    exec('df_ALL.append(' + name + ')')

df_MERGED = pd.concat(df_ALL, axis=0, ignore_index=True)
infer_objects = df_MERGED.infer_objects()

trivial = ['GameId', 'Description']

for col in df_MERGED.columns:
    try:
        if(len(df_MERGED[col].unique()) == 1):
            print('Dropping `' + col + '`...')
            print(list(df_MERGED[col].unique()))
            df_MERGED.drop(col, axis=1, inplace=True)
    except Exception as e:
        print('Unable to accurately process `' + col + '`' + '\n' + str(e))

math.isnan(list(df_MERGED['IsMeasurement'].unique())[1])

# EOF
