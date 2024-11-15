import flet as ft
from openpyxl import Workbook
from datetime import datetime

wb = Workbook()

def main(page: ft.Page):
    page.bgcolor = ft.colors.BLUE_GREY_800
    page.title = "Datatable en flet  con excel"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    titulo = ft.Text("Datatable en flet", size=24, color=ft.colors.PURPLE)

    data_table = ft.DataTable(
        bgcolor = ft.colors.BLUE_GREY_600,
        border = ft.border.all(2, ft.colors.BLUE_GREY_200),
        border_radius= 11,
        vertical_lines = ft.border.BorderSide(3,ft.colors.BLUE_GREY_200),
        horizontal_lines=ft.border.BorderSide(1, ft.colors.BLUE_GREY_600),
        columns = [
            ft.DataColumn(ft.Text("ID", color = ft.colors.BLUE_200)),
            ft.DataColumn(ft.Text("Nombre", color=ft.colors.BLUE_200)),
            ft.DataColumn(ft.Text("Edad", color=ft.colors.BLUE_200)),
        ],
        rows=[]
    )

    def agregar_fila(e):
        nueva_fila = ft.DataRow(
            cells=[
                ft.DataCell(ft.Text(str(len(data_table.rows)+1),color=ft.colors.PINK_400)),
                ft.DataCell(ft.Text(nombre_input.value,color=ft.colors.PINK_400)),
                ft.DataCell(ft.Text(edad_input.value, color=ft.colors.PINK_400))
            ]
        )
        data_table.rows.append(nueva_fila)
        nombre_input.value = ""
        edad_input.value = ""
        page.update()

    def guardar_excel(e):
        ws = wb.active
        ws.title = "Datos de la tabla"
        ws.append(["ID", "Nombre", "Edad"])
        for row in data_table.rows:
            ws.append([cell.content.value for cell in row.cells])

            fecha_hora = datetime.now().strftime("%Y%m%d")
            nombre_archivo = f"datos_tabla_{fecha_hora}.xslx"
            wb.save(nombre_archivo)

            snack_bar = ft.SnackBar(
                content=ft.Text(f"Datos guardados con exito en {nombre_archivo}")
            )
            page.overlay.append(snack_bar)
            snack_bar.open = True
            page.update()

    nombre_input = ft.TextField(
        label= "Nombre",
        bgcolor = ft.colors.BLUE_GREY_700,
        color = ft.colors.PINK_400,
    )
    edad_input = ft.TextField(
        label= "Edad",
        bgcolor = ft.colors.BLUE_GREY_700,
        color = ft.colors.PINK_400,
    )
    agregar_boton = ft.ElevatedButton(
        "Agregar",
        on_click=agregar_fila,
        color=ft.colors.PINK_400,
        bgcolor=ft.colors.BLUE
    )
    guardar_boton = ft.ElevatedButton(
        "Guardar en excel",
        on_click=guardar_excel,
        color=ft.colors.PINK_400,
        bgcolor=ft.colors.ORANGE
    )

    input_conteiner = ft.Row(
        controls=[nombre_input, edad_input, agregar_boton, guardar_boton],
        alignment=ft.MainAxisAlignment.CENTER,
    )



    page.add(titulo, data_table, input_conteiner)

ft.app(target=main)