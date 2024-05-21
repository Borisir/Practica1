from flask import Blueprint, render_template, request, redirect, url_for
from services.factura_service import FacturaService
# en clase se definen las rutas y las funciones que gestionan las solicitudes HTTP.

factura_blueprint = Blueprint('factura_blueprint', __name__)
factura_service = FacturaService()

@factura_blueprint.route('/')
def index():
    return render_template('index.html')

@factura_blueprint.route('/procesar_factura', methods=['POST'])
def procesar_factura():
    datos_factura = {
        'nombre': request.form['nombre'],
        'apellido': request.form['apellido'],
        'direccion': request.form['direccion'],
        'cedula': request.form['cedula'],
        'tipo_retencion': request.form['tipo_retencion'],
        'descripcion': request.form['descripcion'],
        'monto': request.form['monto'],
        'fecha_emision': request.form['fecha_emision'],
        'retencion': request.form['retencion']
    }

    if not factura_service.validar_ruc(datos_factura['cedula']):
        return "El RUC debe contener solo números y tener hasta 13 dígitos.", 400

    factura_service.procesar_factura(datos_factura)
    return redirect(url_for('factura_blueprint.index'))

@factura_blueprint.route('/tabla_facturas', methods=['GET'])
def tabla_facturas():
    facturas_para_mostrar = factura_service.obtener_facturas()
    return render_template('tabla.html', facturas=facturas_para_mostrar)

@factura_blueprint.route('/detalle_factura/<cedula>', methods=['GET'])
def detalle_factura(cedula):
    factura_detalle = factura_service.obtener_factura_por_cedula(cedula)
    return render_template('detalle.html', factura=factura_detalle.to_dict() if factura_detalle else None)

@factura_blueprint.route('/eliminar/<cedula>', methods=['GET'])
def eliminar_factura(cedula):
    factura_service.eliminar_factura(cedula)
    return redirect(url_for('factura_blueprint.tabla_facturas'))
