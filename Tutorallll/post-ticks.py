from http.client import parse_headers

import flet as ft
from anyio.abc import value


def main(page: ft.Page):
    page.title = "Tablero de notas"
    page.padding = 22
    page.theme_mode = "light"
    page.bgcolor = ft.colors.BLUE_GREY_800

    def agregar_nota(evento):
        nueva_nota = create_note("Nueva nota")
        grid.controls.append(nueva_nota)
        page.update()

    def borrar_nota(nota):
        grid.controls.remove(nota)
        page.update()

    def create_note(text):
        nota_contenido = ft.TextField(
            value=text, multiline=True,
            bgcolor=ft.colors.TEAL_100
        )
        nota = ft.Container(
            content=ft.Column([nota_contenido,
                               ft.IconButton(icon=ft.icons.DELETE,
                                             on_click=lambda _: borrar_nota(nota))]),
            width=222,
            height=222,
            bgcolor=ft.colors.TEAL_100,
            border_radius=11,
            padding=11,
        )
        return nota


    grid = ft.GridView(
        expand=True,
        max_extent=222,
        child_aspect_ratio=1,
        spacing=55,
        run_spacing=11
        )

    notas = [
        "Comprar Leche",
        "Cositas",
        "Mas estructurado",
    ]

    for nota in notas:
        grid.controls.append(create_note(nota))

    page.add(
        ft.Row(
            [
                ft.Text("Mis stickers", size=22, weight="bold",
                        color=ft.colors.GREEN_900),
                ft.IconButton(icon=ft.icons.ADD, on_click=agregar_nota, icon_color=ft.colors.GREEN_300)
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        ), grid
    )

ft.app(target=main)