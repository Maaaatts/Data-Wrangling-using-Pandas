# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 10:33:27 2019

@author: 2eced-23
"""

import pandas as pd

math = {'Student':['Ice Bear','Panda','Grizzly'],'Math':[80,95,79]}
elex = {'Student':['Ice Bear','Panda','Grizzly'],'Electronics':[85,81,83]}
geas = {'Student':['Ice Bear','Panda','Grizzly'],'GEAS':[90,79,93]}
esat = {'Student':['Ice Bear','Panda','Grizzly'],'ESAT':[93,89,88]}

Math = pd.DataFrame(math, columns = ['Student','Math'])
Elex = pd.DataFrame(elex, columns = ['Student','Electronics'])
Geas = pd.DataFrame(geas, columns = ['Student','GEAS'])
Esat = pd.DataFrame(esat, columns = ['Student','ESAT'])

mlex = pd.merge(Math, Elex, how = 'right', on = 'Student')
gsat = pd.merge(Geas, Esat, how = 'right', on = 'Student')
short = pd.merge(mlex, gsat, how = 'right', on = 'Student')

a = pd.melt(short, id_vars = 'Student', value_vars = ['Math','Electronics','GEAS','ESAT'])
b = a.rename(columns = {'variable':'Subjects','value':'Grades'})
long = b.sort_values('Student').reset_index().drop(columns = ['index'])