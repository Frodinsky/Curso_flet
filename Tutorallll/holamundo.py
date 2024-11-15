import flet as ft

def main(page: ft.Page):
    page.bgcolor = ft.colors.BLUE_GREY_800
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    texto = ft.Text("Hola Flet")

    texto2 = ft.Text("Ejemplo 3")


    def cambiar_texto(evento_puede_ser_cualquier_cosa):
        texto2.value = "AHora tengo el poder"
        page.update()

    boton_variable_x = ft.FilledButton(text="Algo", on_click=cambiar_texto)

    page.add(texto,texto2,boton_variable_x)

ft.app(target=main)