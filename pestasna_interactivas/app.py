import flet as ft
from random import sample
def main(page: ft.Page):
    page.bgcolor=ft.colors.GREEN_500
    page.title = "Pestañas en flet"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    titulo = ft.Text("Ejemplo de tabs o pestañas en flet", size=24, color=ft.colors.DEEP_PURPLE_ACCENT_400)
    def generar_tareas():
        tareas = ["Hacer la compra","Lavar el baño","Lavar trastes","Hacer de comer","Trapear","Barrer","Jugar"]
        return sample(tareas, 4)

    lista_tareas = ft.ListView(spacing=11, padding=22)

    def actualizar_tareas():
        lista_tareas.controls.clear()
        for tarea in generar_tareas():
            lista_tareas.controls.append(ft.Text(tarea, color=ft.colors.DEEP_ORANGE_ACCENT_700))
        page.update()
    actualizar_tareas()

    boton_actualizar_tareas = ft.ElevatedButton("Actualizar tareas", on_click=lambda _: actualizar_tareas())
    contenido_tareas = ft.Column([lista_tareas,boton_actualizar_tareas])

    #Contendio para la pestaña de perfil
    campo_nombre =ft.TextField(label="Nombre", bgcolor=ft.colors.BLUE_GREY_600)
    campo_email = ft.TextField(label="Email", bgcolor=ft.colors.BLUE_GREY_600)
    boton_guardar = ft.ElevatedButton("Guardar Perfil")
    contenido_perfil = ft.Column([campo_nombre,campo_email,boton_guardar])

    #contendio para la pestaña de configuracion
    switch_notificaciones = ft.Switch(label="Notificaciones",value=True)
    slider_volumen = ft.Slider(min=0, max=100, divisions=10, label="Volumen")
    contenido_configuraciones = ft.Column([switch_notificaciones,slider_volumen])


    pestañas = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[
            ft.Tab(text="Tareas", icon=ft.icons.LIST_ALT, content=contenido_tareas),
            ft.Tab(text="Perfil", icon=ft.icons.PERSON, content=contenido_perfil),
            ft.Tab(text="Configuracion", icon=ft.icons.SETTINGS, content=contenido_configuraciones),
        ],
        expand=1,
    )

    page.add(titulo, pestañas)

ft.app(target=main)
