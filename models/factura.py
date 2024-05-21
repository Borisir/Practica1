# se define la clase Factura con sus atributos y un método para convertirla a un diccionario para convertirla a JSON.
class Factura:
    def __init__(self, nombre, apellido, direccion, cedula, tipo_retencion, descripcion, monto, fecha_emision, retencion):
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.cedula = cedula
        self.tipo_retencion = tipo_retencion
        self.descripcion = descripcion
        self.monto = float(monto)
        self.fecha_emision = fecha_emision
        self.retencion = retencion

    def to_dict(self):
        return {
            'nombre': self.nombre,
            'apellido': self.apellido,
            'direccion': self.direccion,
            'cedula': self.cedula,
            'tipo_retencion': self.tipo_retencion,
            'descripcion': self.descripcion,
            'monto': self.monto,
            'fecha_emision': self.fecha_emision,
            'retencion': self.retencion
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            nombre=data['nombre'],
            apellido=data['apellido'],
            direccion=data['direccion'],
            cedula=data['cedula'],
            tipo_retencion=data['tipo_retencion'],
            descripcion=data['descripcion'],
            monto=data['monto'],
            fecha_emision=data['fecha_emision'],
            retencion=data['retencion'],
        )
