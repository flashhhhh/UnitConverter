import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import pandas as pd
from utils.graph import Graph

conversion_table = pd.read_csv('config/units-conversion-table.csv')

g = Graph()

for index, row in conversion_table.iterrows():
    g.add_edge(row['from'], row['to'], row['multiply_by'], row['addition_by'])

g.build()

def listLengthUnits():
    # List all distinct units (2 columns from and to) in the conversion table for length
    from_units = set(conversion_table[conversion_table['conversion_type'] == 'Length']['from'].unique())
    to_units = set(conversion_table[conversion_table['conversion_type'] == 'Length']['to'].unique())
    units = sorted(set(from_units.union(to_units)))

    return {"units": list(units)}

def listTemperatureUnits():
    # List all distinct units (2 columns from and to) in the conversion table for temperature
    from_units = set(conversion_table[conversion_table['conversion_type'] == 'Temperature']['from'].unique())
    to_units = set(conversion_table[conversion_table['conversion_type'] == 'Temperature']['to'].unique())
    units = sorted(set(from_units.union(to_units)))

    return {"units": list(units)}

def listWeightUnits():
    # List all distinct units (2 columns from and to) in the conversion table for weight
    from_units = set(conversion_table[conversion_table['conversion_type'] == 'Weight']['from'].unique())
    to_units = set(conversion_table[conversion_table['conversion_type'] == 'Weight']['to'].unique())
    units = sorted(set(from_units.union(to_units)))

    return {"units": list(units)}

def convert(value: float, input_unit: str, output_unit: str) -> float:
    pp = g.query(input_unit, output_unit)
    return value * pp[0] + pp[1]

# def main():
#     g = Graph(3)
#     g.add_edge('USD', 'EUR', 0.741)
#     g.add_edge('EUR', 'JPY', 136.24)
#     g.add_edge('JPY', 'USD', 0.0092)
#     g.build()

#     print(g.query('USD', 'EUR')) # 0.741
#     print(g.query('EUR', 'JPY')) # 136.24
#     print(g.query('JPY', 'USD')) # 0.0092