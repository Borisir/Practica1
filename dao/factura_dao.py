import json
import os

# Esta clase maneja el acceso a datos

class FacturaDAO:
    def __init__(self):
        self.filename = os.path.join('static', 'factura.json')

    def cargar_facturas(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as json_file:
                return json.load(json_file)
        return []

    def guardar_factura(self, factura):
        facturas = self.cargar_facturas()
        facturas.append(factura.to_dict())
        with open(self.filename, 'w') as json_file:
            json.dump(facturas, json_file, indent=4)

    def obtener_factura_por_cedula(self, cedula):
        facturas = self.cargar_facturas()
        factura_data = next((factura for factura in facturas if factura['cedula'] == cedula), None)
        return factura_data

    def eliminar_factura(self, cedula):
        facturas = self.cargar_facturas()
        facturas = [factura for factura in facturas if factura['cedula'] != cedula]
        with open(self.filename, 'w') as json_file:
            json.dump(facturas, json_file, indent=4)
