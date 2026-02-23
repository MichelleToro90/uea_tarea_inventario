import tkinter as tk
from tkinter import messagebox
from app.inventario_sql import InventarioSQL
from app.producto import Producto

class InventarioGUI:
    def __init__(self):
        self.inventario = InventarioSQL()

        self.root = tk.Tk()
        self.root.title("Sistema de Inventarios - UEA (SQL)")
        self.root.geometry("520x450")

        tk.Label(self.root, text="Código").pack()
        self.entry_codigo = tk.Entry(self.root)
        self.entry_codigo.pack()

        tk.Label(self.root, text="Nombre").pack()
        self.entry_nombre = tk.Entry(self.root)
        self.entry_nombre.pack()

        tk.Label(self.root, text="Cantidad").pack()
        self.entry_cantidad = tk.Entry(self.root)
        self.entry_cantidad.pack()

        tk.Label(self.root, text="Precio").pack()
        self.entry_precio = tk.Entry(self.root)
        self.entry_precio.pack()

        tk.Button(self.root, text="Agregar", command=self.agregar).pack(pady=5)
        tk.Button(self.root, text="Actualizar", command=self.actualizar).pack(pady=5)
        tk.Button(self.root, text="Eliminar", command=self.eliminar).pack(pady=5)
        tk.Button(self.root, text="Mostrar Inventario", command=self.mostrar).pack(pady=5)

        self.texto = tk.Text(self.root, height=10)
        self.texto.pack(pady=10)

        self.root.mainloop()

    def limpiar_campos(self):
        for e in (self.entry_codigo, self.entry_nombre, self.entry_cantidad, self.entry_precio):
            e.delete(0, tk.END)

    def agregar(self):
        try:
            p = Producto(
                self.entry_codigo.get(),
                self.entry_nombre.get(),
                self.entry_cantidad.get(),
                self.entry_precio.get()
            )
            ok = self.inventario.agregar_producto(p)
            if ok:
                messagebox.showinfo("Éxito", "Producto agregado")
                self.limpiar_campos()
            else:
                messagebox.showwarning("Duplicado", "Ya existe un producto con ese código")
        except ValueError:
            messagebox.showerror("Error", "Cantidad y precio deben ser números")

    def actualizar(self):
        try:
            ok = self.inventario.actualizar_producto(
                self.entry_codigo.get(),
                self.entry_cantidad.get(),
                self.entry_precio.get()
            )
            if ok:
                messagebox.showinfo("Actualizado", "Producto actualizado")
                self.limpiar_campos()
            else:
                messagebox.showwarning("No encontrado", "Producto no existe")
        except ValueError:
            messagebox.showerror("Error", "Cantidad y precio deben ser números")

    def eliminar(self):
        ok = self.inventario.eliminar_producto(self.entry_codigo.get())
        if ok:
            messagebox.showinfo("Eliminado", "Producto eliminado")
            self.limpiar_campos()
        else:
            messagebox.showwarning("No encontrado", "Producto no existe")

    def mostrar(self):
        self.texto.delete("1.0", tk.END)
        for p in self.inventario.listar():
            self.texto.insert(tk.END, f"{p.codigo} | {p.nombre} | {p.cantidad} | ${p.precio}\n")