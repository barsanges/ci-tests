import os
print("WORKING DIRECTORY:")
print(os.getcwd())
print("LS:")
print(os.listdir())
print("LS CHEESESHOP:")
print(os.listdir('cheeseshop'))
import sys
print("PYTHON PATH:")
print(sys.path)
import cheeseshop
print(cheeseshop.cheeses.head())
