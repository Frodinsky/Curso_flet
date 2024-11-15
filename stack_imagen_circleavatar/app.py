import flet as ft

def main(page: ft.Page):
    page.bgcolor = ft.colors.BLUE_GREY_800
    page.title = "Demostracions de stacks, imagenes y avatars"
    page.theme_mode = ft.ThemeMode.DARK
    page.scroll = "always"
    text_titulo = ft.Text("Demostracion de stacks, imagenes y CircleAvatars",
                          size=33, weight=ft.FontWeight.BOLD,
                          color= ft.colors.PURPLE
                          )

    def create_example(title, description, content):
        return ft.Container(
            content = ft.Column([
                ft.Text(title, size=24, weight=ft.FontWeight.BOLD, color=ft.colors.BLUE_200),
                ft.Text(description, color=ft.colors.GREY_300),
                ft.Container(content, padding=10, border=ft.border.all(1, ft.colors.BLUE_GREY_400)),
            ]),
            margin=ft.margin.only(bottom=20)
        )
    stack_ejemplo = ft.Stack([
        ft.Container(width=200, height=200, bgcolor=ft.colors.BLUE_900),
        ft.Container(width=150, height=150, bgcolor=ft.colors.BLUE_700, left=25, top=25),
        ft.Container(width=100, height=100, bgcolor=ft.colors.BLUE_900, left=50, top=50),
        ft.Text("Stack Demo", color= ft.colors.WHITE, size=12, left=70, top=80)
    ], width=200, height=200)

    stack_example = create_example("Stack","Stack permite superponer widgets uno encima del otro.", stack_ejemplo)

    imagen_internet = ft.Image(src="https://picsum.photos/200/200", width=200)
    imagen_local = ft.Image(src= "images/morado.jpg",width=200)

    columna_imagen = ft.Column([
        imagen_internet,
        ft.Text("Imagen desde URL", size=14, color=ft.colors.GREY_300),
        imagen_local,
        ft.Text("Imagen local, si esta disponible", size=14, color=ft.colors.GREY_300)
    ])

    image_example = create_example("Imagen","Imagen que permite mostrar diferentes medios de poner imagenes", columna_imagen)

    imagen_internet_avatar = ft.CircleAvatar(
        foreground_image_src="https://avatars.githubusercontent.com/u/5479690",
        radius=50,
    )

    circulo_texto = ft.CircleAvatar(
        content=ft.Text("AB", color=ft.colors.BLUE_GREY_900),
        radius=50,
        bgcolor=ft.colors.BLUE_200
    )
    fila_avatar = ft.Row([imagen_internet_avatar,circulo_texto])

    circle_avatar_examples = create_example("Circle Avatar", "Crea un avatar circular", fila_avatar)

    separador = ft.Divider(color=ft.colors.PINK)



    page.add(text_titulo, separador, stack_example,separador, image_example,separador, circle_avatar_examples)

ft.app(target=main)