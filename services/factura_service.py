from dao.factura_dao import FacturaDAO
from models.factura import Factura
# esta clase contiene la lógica de negocio
class FacturaService:
    def __init__(self):
        self.factura_dao = FacturaDAO()

    def validar_ruc(self, ruc):
        import re
        return re.match(r'^[0-9]{1,13}$', ruc) is not None

    def procesar_factura(self, datos_factura):
        factura = Factura.from_dict(datos_factura)
        self.factura_dao.guardar_factura(factura)

    def obtener_facturas(self):
        facturas_data = self.factura_dao.cargar_facturas()
        return [Factura.from_dict(factura_data).to_dict() for factura_data in facturas_data]

    def obtener_factura_por_cedula(self, cedula):
        factura_data = self.factura_dao.obtener_factura_por_cedula(cedula)
        return Factura.from_dict(factura_data) if factura_data else None

    def eliminar_factura(self, cedula):
        self.factura_dao.eliminar_factura(cedula)
