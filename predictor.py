# @Author: Shounak Ray <Ray>
# @Date:   05-Feb-2021 19:02:50:501  GMT-0700
# @Email:  rijshouray@gmail.com
# @Filename: predictor.py
# @Last modified by:   Ray
# @Last modified time: 05-Feb-2021 20:02:11:118  GMT-0700
# @License: [Private IP]

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

    df_ALL.append(name)


# EOF
