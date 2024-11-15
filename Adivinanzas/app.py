import flet as ft
from random import randint

def main(page: ft.Page):
    page.bgcolor = ft.colors.BLUE_GREY_800
    page.title = "Cards, dividers, verticaldividers en flet"
    page.theme_mode =ft.ThemeMode.DARK
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    titulo = ft.Text("Cards, divider y verticaldividers en flet", size=30,  weight=ft.FontWeight.BOLD,)

    numero_secreto = randint(1,5)
    intentos = 0

    def verificar_intento(e):
        nonlocal intentos
        intento = int(input_numero.value)
        intentos +=1
        if intento == numero_secreto:
            resultado.value = f"Correcto lo adivinaste en {intentos} intentos"
            resultado.color = ft.colors.GREEN
            verificar_btn.disabled = True
        elif intento < numero_secreto:
            resultado.value = "Demasiado Bajo. Intenta de nuevo"
            resultado.color = ft.colors.ORANGE
        else:
            resultado.value = "Demasiado alto, intenta de nuevo"
            resultado.color = ft.colors.ORANGE

        intentos_text.value = f"Intentos {intentos}"
        page.update()

    def reinicar_juego(e):
        nonlocal numero_secreto, intentos
        numero_secreto = randint(1,100)
        intentos = 0
        resultado.value = "Adivina el numero entre 1 y 10"
        resultado.color = ft.colors.WHITE
        intentos_text.value = "Intentos 0"
        verificar_btn.disabled = False
        page.update()


    #Variables
    titulo_juego = ft.Text("Juego de adivinanzas", size=20, weight=ft.FontWeight.BOLD, color=ft.colors.PURPLE_200)
    input_numero = ft.TextField(label="Tu intento", width=100)
    verificar_btn = ft.ElevatedButton("Verificar", on_click=verificar_intento)
    resultado = ft.Text("Adivina el numero entre el 1 y el 100")
    intentos_text = ft.Text("Intentos: 0")
    reinicar_btn = ft.ElevatedButton("Reiniciar el juego", on_click=reinicar_juego)


    divider_simple = ft.Divider(height=10, color=ft.colors.PURPLE_200)
    divider_vertical = ft.VerticalDivider(width=10, color=ft.colors.PURPLE_200)
    card1 = ft.Card(
        content=ft.Container(
            content=ft.Column(
                [titulo_juego, input_numero,verificar_btn,resultado, intentos_text, reinicar_btn,],
            alignment=ft.MainAxisAlignment.CENTER, spacing= 20),

            padding=10,
        ),
        width=300,
        height=400,
    )

    def cambiar_tema(e):
        if page.theme_mode == ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.LIGHT
            page.bgcolor = ft.colors.BLUE_GREY_100
            tema_btn.text = "Modo oscuro"
        else:
            page.theme_mode = ft.ThemeMode.DARK
            page.bgcolor = ft.colors.BLUE_GREY_800
            tema_btn.text = "Modo Claro"
        page.update()

    titulo_tema = ft.Text("Cambiar el tema", size =20, weight=ft.FontWeight.BOLD)
    tema_btn = ft.ElevatedButton("Modo Claro", on_click=cambiar_tema)
    columna_tema = ft.Column([titulo_tema, tema_btn],
                             alignment= ft.MainAxisAlignment.CENTER,
                             spacing=22
                             )


    card2 = ft.Card(
        content=ft.Container(
            content=columna_tema,
            padding=10,
        ),
        width=300,
        height=400,
    )
    card3 = ft.Card(
        content=ft.Container(
            content=ft.Text("Card 3"),
            padding=10,
        ),
        width=150,
        height=100,
    )
    layout = ft.Row([
        card1,
        divider_vertical,
        card2,
        divider_vertical,
        card3
    ],alignment=ft.MainAxisAlignment.CENTER )



    page.add(titulo, divider_simple ,layout)

ft.app(target=main)