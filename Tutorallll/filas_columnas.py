import flet as ft

def main(page: ft.Page):
    page.bgcolor = ft.colors.BLUE_GREY_800
    page.title = "Filas y columnas"
    texto1 = ft.Text("Texto1", size=24, color=ft.colors.TEAL)
    texto2 = ft.Text("Texto2", size=24, color=ft.colors.TEAL)
    texto3 = ft.Text("Texto3", size=24, color=ft.colors.TEAL)

    fila_textos = ft.Row(
        controls=[texto1,texto2,texto3],
        alignment= ft.MainAxisAlignment.CENTER,
        spacing = 50
    )
    page.add(fila_textos)

    boton1 = ft.FilledButton(text="Boton 1")
    boton2 = ft.FilledButton(text="Boton 2")
    boton3 = ft.FilledButton(text="Boton 3")
    fila_botones = ft.Row(
        controls=[boton1,boton2,boton3],
        alignment= ft.MainAxisAlignment.CENTER,
        spacing = 50
    )
    page.add(fila_botones)

    textos_columba1 = [
        ft.Text("Columna 1 - Fila 1",size=18, color=ft.colors.TEAL_100),
        ft.Text("Columna 1 - Fila 2", size=18, color=ft.colors.TEAL_100),
        ft.Text("Columna 1 - Fila 3", size=18, color=ft.colors.TEAL_100)
    ]
    columna_textos1 = ft.Column(controls=textos_columba1)
    #page.add(columna_textos1)

    textos_columba2 = [
        ft.Text("Columna 2 - Fila 1", size=18, color=ft.colors.TEAL_100),
        ft.Text("Columna 2 - Fila 2", size=18, color=ft.colors.TEAL_100),
        ft.Text("Columna 2 - Fila 3", size=18, color=ft.colors.TEAL_100)
    ]
    columna_textos2 = ft.Column(controls=textos_columba2)
    #page.add(columna_textos2)

    fila_columnas = ft.Row(
        controls=[columna_textos1,columna_textos2],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing= 50
    )
    page.add(fila_columnas)




ft.app(target=main)
