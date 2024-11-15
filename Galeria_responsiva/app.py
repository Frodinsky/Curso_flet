from tkinter.constants import CENTER

import flet as ft
import os
import base64


def crear_producto(nombre, precio, color, imagen_nombre):
    imagen_path = os.path.join(os.path.dirname(__file__),"assets", imagen_nombre)
    try:
        with open(imagen_path, "rb") as imagen_file:
            imagen_bytes = base64.b64encode(imagen_file.read()).decode()
    except FileNotFoundError:
        print(f"Advertencia: La imagen {imagen_nombre} no existe en {imagen_path}")
        imagen_bytes = None
    return ft.Container(
        content=ft.Column(
            [
                ft.Image(
                    src_base64= imagen_bytes,
                    width = 150,
                    height = 150,
                    fit = ft.ImageFit.CONTAIN,
                    error_content = ft.Text("Imagen no encontrada") if imagen_bytes else ft.Text("Imagen no encontrada"),

                ),
                ft.Text(nombre, size= 16, weight=ft.FontWeight.BOLD),
                ft.Text(f"${precio}", size= 14,),
                ft.ElevatedButton("Agregar al carrito", color= ft.colors.WHITE)
            ],
        ),
        bgcolor= color,
        border_radius= 11,
        padding=22,
        alignment=ft.Alignment.center
    )


def main(page: ft.Page):
    page.title = "Galeria de productos resposiva"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = ft.colors.BLUE_GREY_900
    titulo = ft.Text("Galeria de productos", size=33, weight= ft.FontWeight.BOLD)

    productos = [
        crear_producto("Producto 1", "22.22",ft.colors.PURPLE_200, "azul.jpg"),
        crear_producto("Producto 2","11.11", ft.colors.PURPLE_400, "mate.jpg"),
        crear_producto("Producto 3", "33.33", ft.colors.PURPLE_600, "naranja.jpg"),
        crear_producto("Producto 4", "44.44", ft.colors.PURPLE_800, "morado.jpg"),
        crear_producto("Producto 3", "33.33", ft.colors.PURPLE, "negro.jpg"),
        crear_producto("Producto 4", "44.44", ft.colors.PURPLE_ACCENT, "plata.jpg"),
        crear_producto("Producto 3", "33.33", ft.colors.PURPLE_ACCENT_400, "rojo.jpg"),
        crear_producto("Producto 4", "44.44", ft.colors.DEEP_PURPLE_100, "verde.jpg"),
    ]

    galeria = ft.ResponsiveRow(
        [ft.Container(producto, col={"sm":12, "md":6, "lg":3}) for producto in productos],
        run_spacing= 22,
        spacing= 22,
    )

    contenido = ft.Column([

        ft.Text("Galeria de productos", size=33, weight=ft.FontWeight.BOLD),
        ft.Divider(height=22, color=ft.colors.WHITE24),
        galeria
    ], scroll=ft.ScrollMode.AUTO, expand=True
    )
    page.add(contenido)

ft.app(target=main)