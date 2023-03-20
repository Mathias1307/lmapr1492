# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 11:01:25 2023

@author: ptnma
"""

from jupyter_jsmol import JsmolView
from ipywidgets import Layout, widgets, interact

view1 = JsmolView.from_file("data/c2h410.xyz", inline=True) # pythonic way but it might be slower
view1