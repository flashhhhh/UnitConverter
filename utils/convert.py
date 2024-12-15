import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from utils.graph import Graph

g = Graph()

g.add_edge('meter', 'kilometer', 0.001)
g.add_edge('meter', 'centimeter', 100)
g.add_edge('meter', 'millimeter', 1000)
g.add_edge('meter', 'micrometer', 1000000)
g.add_edge('meter', 'nanometer', 1000000000)
g.add_edge('meter', 'mile', 0.000621371)
g.add_edge('meter', 'yard', 1.09361)
g.add_edge('meter', 'foot', 3.28084)
g.add_edge('meter', 'inch', 39.3701)
g.add_edge('meter', 'light year', 1.057e-16)

g.build()

def convert(value: float, input_unit: str, output_unit: str) -> float:
    return value * g.query(input_unit, output_unit)

# def main():
#     g = Graph(3)
#     g.add_edge('USD', 'EUR', 0.741)
#     g.add_edge('EUR', 'JPY', 136.24)
#     g.add_edge('JPY', 'USD', 0.0092)
#     g.build()

#     print(g.query('USD', 'EUR')) # 0.741
#     print(g.query('EUR', 'JPY')) # 136.24
#     print(g.query('JPY', 'USD')) # 0.0092