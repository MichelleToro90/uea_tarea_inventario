class Producto:
    def __init__(self, codigo, nombre, cantidad, precio):
        self.codigo = codigo.strip()
        self.nombre = nombre.strip()
        self.cantidad = int(cantidad)
        self.precio = float(precio)