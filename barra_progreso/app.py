import flet as ft
import time

def main(page: ft.Page):
    page.bgcolor = ft.colors.BLUE_GREY_800
    page.title = "Barras de progreso"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    titulo = ft.Text("barras de procesos de dos tippos", size=24, color=ft.colors.WHITE)
    archvios = ft.Text("Selecciona archivos para descargar", size=16, color=ft.colors.WHITE70)

    def simulador_descarga(e):
        archivos_seleccionados = [checkbox for checkbox in file_list.controls if checkbox.value]
        if not archivos_seleccionados:
            status_text.value = "Seleciona al menos un archivo"
            page.update()
            return
        progress_bar.value = 0
        progress_ring.value = 0
        page.update()
        total_size = sum([float(archivo.label.split("(")[1].replace("MB)", "").strip()) for archivo in archivos_seleccionados])
        dowload = 0

        for archivo in archivos_seleccionados:
            file_size = float(archivo.label.split("(")[1].replace("MB)", "").strip())
            status_text.value = f"Descargando {archivo.label}..."

            for _ in range(10):
                time.sleep(0.3)
                dowload += file_size /10
                progrees = min(dowload/total_size,1)
                progress_bar.value = progrees
                progress_ring.value = progrees
                page.update()

        progress_bar.value = 1
        progress_ring.value = 1
        status_text.value = "Descarga completada"
        page.update()

        time.sleep(1)
        progress_bar.value = 0
        progress_ring.value = 0
        status_text.value = ""
        for checkbox in file_list.controls:
            checkbox.value = False
        page.update()

    file_list = ft.Column([
        ft.Checkbox(label="Documento .pdf (2.5MB)", value=False),
        ft.Checkbox(label="Imagen.jpg (5MB)", value=False),
        ft.Checkbox(label="Video.mp4 (50MB)", value=False),
        ft.Checkbox(label="Archivo.zip (100 MB)", value=False),
    ])

    contenedor_file_list = ft.Container(content=file_list, padding=20)
    
    #Barra de progres
    progress_bar = ft.ProgressBar(width=400, color="amber", bgcolor="#263238", value=0)
    progress_ring = ft.ProgressRing(stroke_width=5, color="amber", value=1,)
    fila = ft.Row([progress_bar,progress_ring], alignment=ft.MainAxisAlignment.CENTER)
    status_text = ft.Text("", color=ft.colors.WHITE)
    boton_download = ft.ElevatedButton("Incia la descargas", on_click=simulador_descarga,
                                       bgcolor=ft.colors.AMBER, color=ft.colors.BLACK)



    page.add(titulo, archvios, contenedor_file_list, fila, status_text, boton_download)
ft.app(target=main)
