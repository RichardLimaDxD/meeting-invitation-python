import flet as ft

def main(page: ft.Page):
    page.title = 'Datezinho?'
    page.window_width = 600
    page.window_height = 600
    page.window_resizable = False
    page.padding = 100
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = 'light'
    page.bgcolor = '#FF90BC'
    page.update()

    img = f"https://raw.githubusercontent.com/liviavianna/pedido_date_py/main/envelope.png"

    text = ft.Text(
            f"Clique no ♥ para uma surpresa!",
            size=20,
            color=ft.colors.BLACK,
            weight=ft.FontWeight.BOLD,
            font_family="Montserrat"
        )  
      
    envolpe_img = ft.Image(
                    src=img,
                    width=200,
                    height=200
    )

    def open_dlg_modal(e):
        page.dialog = dlg_modal
        dlg_modal.open = True
        page.update()
    dlg = ft.AlertDialog(
        title=ft.Text("Diga sim logo")
    )

    def open_love_model(e):
        page.dialog = dlg_true
        dlg_true.open = True
        page.update()
    dlg_true = ft.AlertDialog(
        title=ft.Text("Você é incrível ♥"),
        content=ft.Text("♥ Eu te amo!🌹♥")
    )

    def open_dlg(e):
        page.dialog = dlg
        dlg.open = True
        page.update()
    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("Diga sim"),
        content=ft.Text("Aceitas ir em um date comigo? 🌹"),
        actions=[
            ft.TextButton("Sim", on_click=open_love_model),
            ft.TextButton("Não", on_click=open_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        on_dismiss=lambda e: print("Modal dialog dismissed!"),
    )
    
    b = ft.IconButton(
        icon=ft.icons.FAVORITE, icon_color="red", on_click=open_dlg_modal, data=0, icon_size=40
    )   

    page.add(text, envolpe_img, b)
ft.app(target=main, view=ft.AppView.WEB_BROWSER)
