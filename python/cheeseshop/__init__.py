"""
Mock functions and objects used to test CI tools on GitHub, based on
Monthy Python's "Cheese shop".
"""

import pandas as pd
from cheeseshop.sketch import *

cheesesdata = pd.read_csv("cheeseshop/cheesesdata.csv", header=0)
