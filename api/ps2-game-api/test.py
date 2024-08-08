from flask import Flask
from flask_restful import Api, Resource
import pandas as pd

def get():
    data = pd.read_csv('ps2_data.csv')
    ps2_data = data.to_dict()
    print(ps2_data)

get()