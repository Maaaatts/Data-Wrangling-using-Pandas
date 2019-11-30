# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 13:19:19 2019

@author: Matthew Rabanes
"""

import pandas as pd

bx = {'Box':['Box1','Box1','Box1','Box2','Box2','Box2'],
      'Dimension':['Length','Width','Height','Length','Width','Height'], 
      'Value':[6,4,2,5,3,4]}

messy = pd.DataFrame(bx, columns = ['Box','Dimension','Value'])
tidy = messy.pivot(index = 'Box', columns = 'Dimension', values = 'Value')
Volume = (tidy.Height)*(tidy.Width)*(tidy.Length)
final_bx = pd.concat([tidy, Volume], axis = 1).rename(columns = {0:'Volume'})