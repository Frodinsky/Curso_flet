import flet as ft

class TodoApp:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.bgcolor = ft.colors.BLUE_GREY_800
        self.page.title = "To-Do List"
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        # Inicializar elementos de la interfaz
        self.titulo = ft.Text("Mi lista de tareas", size=30, weight=ft.FontWeight.BOLD, color=ft.colors.TEAL_100)
        self.ingrear_tarea = ft.TextField(hint_text="Escribe una nueva Tarea")
        self.ver_lista_tareas = ft.ListView(expand=1, spacing=5)
        self.tareas_seleccionadas = ft.Text("", size=20, weight=ft.FontWeight.BOLD, color=ft.colors.TEAL_100)

        self.lista_tareas = []

        # Botón para agregar la tarea
        self.boton_agregar_tarea = ft.FilledButton(text="Agregar tarea", on_click=self.agregar_tarea)

        # Agregar elementos a la página
        self.page.add(self.titulo, self.ingrear_tarea, self.boton_agregar_tarea, self.ver_lista_tareas, self.tareas_seleccionadas)

    def agregar_tarea(self, e):
        if self.ingrear_tarea.value:
            tarea = ft.ListTile(title=ft.Text(self.ingrear_tarea.value),
                                leading=ft.Checkbox(on_change=self.seleccionar_tareas))
            self.lista_tareas.append(tarea)
            self.ingrear_tarea.value = ""
            self.actualizar_lista()

    def seleccionar_tareas(self, e):
        seleccionadas = [t.title.value for t in self.lista_tareas if t.leading.value]
        self.tareas_seleccionadas.value = "Tareas seleccionadas: " + ", ".join(seleccionadas)
        self.page.update()

    def actualizar_lista(self):
        self.ver_lista_tareas.controls.clear()
        self.ver_lista_tareas.controls.extend(self.lista_tareas)
        self.page.update()

def main(page: ft.Page):
    TodoApp(page)

ft.app(target=main)
