import flet as ft

def main(page: ft.Page):
    page.bgcolor = ft.colors.BLUE_GREY_800
    page.title = "To-Do List"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    titulo = ft.Text("Mi lista de tareas", size=30, weight=ft.FontWeight.BOLD, color=ft.colors.TEAL_100)

    # Lista para almacenar las tareas
    lista_tareas = []

    # Campo de texto para ingresar nuevas tareas
    ingrear_tarea = ft.TextField(hint_text="Escribe una nueva Tarea")

    # Vista para mostrar las tareas
    ver_lista_tareas = ft.ListView(expand=1, spacing=5)

    # Texto para mostrar las tareas seleccionadas
    tareas_seleccionadas = ft.Text("", size=20, weight=ft.FontWeight.BOLD, color=ft.colors.TEAL_100)

    def agregar_tarea(e):
        if ingrear_tarea.value:
            tarea = ft.ListTile(title=ft.Text(ingrear_tarea.value),
                                leading=ft.Checkbox(on_change=seleccionar_tareas))
            lista_tareas.append(tarea)  # Agregar la tarea a la lista
            ingrear_tarea.value = ""
            actualizar_lista()

    def seleccionar_tareas(e):
        seleccionadas = [t.title.value for t in lista_tareas if t.leading.value]
        tareas_seleccionadas.value = "Tareas seleccionadas: " + ", ".join(seleccionadas)
        page.update()  # Actualizar la página para mostrar el texto actualizado

    def actualizar_lista():
        ver_lista_tareas.controls.clear()
        ver_lista_tareas.controls.extend(lista_tareas)  # Agregar las tareas a la vista
        page.update()  # Actualizar la página

    # Botón para agregar la tarea
    boton_agregar_tarea = ft.FilledButton(text="Agregar tarea", on_click=agregar_tarea)

    # Agregar los elementos a la página
    page.add(titulo, ingrear_tarea, boton_agregar_tarea, ver_lista_tareas, tareas_seleccionadas)

ft.app(target=main)
