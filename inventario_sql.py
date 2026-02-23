import sqlite3
from app.producto import Producto

class InventarioSQL:
    def __init__(self, db="inventario.db"):
        self.db = db
        self._crear_tabla()

    def _crear_tabla(self):
        try:
            with sqlite3.connect(self.db) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS productos (
                        codigo TEXT PRIMARY KEY,
                        nombre TEXT NOT NULL,
                        cantidad INTEGER NOT NULL,
                        precio REAL NOT NULL
                    )
                """)
                conn.commit()
        except sqlite3.Error as e:
            print("❌ Error al crear la base de datos:", e)

    def agregar_producto(self, producto: Producto):
        try:
            with sqlite3.connect(self.db) as conn:
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO productos (codigo, nombre, cantidad, precio) VALUES (?, ?, ?, ?)",
                    (producto.codigo, producto.nombre, producto.cantidad, producto.precio)
                )
                conn.commit()
                return True
        except sqlite3.IntegrityError:
            return False
        except sqlite3.Error as e:
            print("❌ Error SQL al agregar:", e)
            return False

    def actualizar_producto(self, codigo, cantidad, precio):
        try:
            with sqlite3.connect(self.db) as conn:
                cursor = conn.cursor()
                cursor.execute(
                    "UPDATE productos SET cantidad = ?, precio = ? WHERE codigo = ?",
                    (int(cantidad), float(precio), codigo)
                )
                conn.commit()
                return cursor.rowcount > 0
        except sqlite3.Error as e:
            print("❌ Error SQL al actualizar:", e)
            return False

    def eliminar_producto(self, codigo):
        try:
            with sqlite3.connect(self.db) as conn:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM productos WHERE codigo = ?", (codigo,))
                conn.commit()
                return cursor.rowcount > 0
        except sqlite3.Error as e:
            print("❌ Error SQL al eliminar:", e)
            return False

    def listar(self):
        try:
            with sqlite3.connect(self.db) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT codigo, nombre, cantidad, precio FROM productos")
                filas = cursor.fetchall()
                return [Producto(*fila) for fila in filas]
        except sqlite3.Error as e:
            print("❌ Error SQL al listar:", e)
            return []