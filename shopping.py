import flet as ft

def main(page: ft.Page):

    compras = []  
    nombre = ft.TextField(label="Item Name")
    view = ft.ListView(expand=True)  # eto es para ir scrolling down mientra tu ve tu lista
    error_message = ft.Text("", size=12) 

    def add_item(e):
        item_name = nombre.value.strip()
        if item_name == "":
            error_message.value = "aha tu no va a quere na pa yo ponete a trabaja."
        else:
            compras.append(item_name)
            view.controls.append(ft.Text(item_name))
            nombre.value = ""
            error_message.value = ""  
        page.update()

    def remove_item(e):
        if compras:
            compras.pop()  # Pop e pa quita el ultimo objeto de una lista, si el ultimo producto e una manzana, se quita
            view.controls.pop()
            error_message.value = ""
        else:
            error_message.value = "La lista ta vacia abusador "
        page.update()

    def clear_list(e):
        compras.clear()  # obviamente su nombre lo dice, clear e pa quita to la vaina de la lista
        view.controls.clear()
        error_message.value = ""
        page.update()

    def save_or_load(e, action):
        if action == "save":
            with open("shopping_list.txt", "w") as file:
                file.write("\n".join(compras))  
            error_message.value = "la lista ta guardada, checkea tu file ahi"
        elif action == "load":
            try:
                with open("shopping_list.txt", "r") as file:
                    items = file.read().splitlines()  # splitlines e pa agrra un texto y ponelo ma chiquito, dividiendolo en lineas
                compras.clear()
                view.controls.clear()
                compras.extend(items)  # extend e pa move variables de una lista para otra lista
                view.controls.extend([ft.Text(item) for item in items])
                error_message.value = "Ahi ta tu lista"
            except FileNotFoundError:
                error_message.value = "bueno mio, no hay lista no."
        page.update()

    def search_items(e):
        search_query = search_input.value.strip().lower()
        filtered_items = [item for item in compras if search_query in item.lower()]
        view.controls[:] = [ft.Text(item) for item in filtered_items]
        page.update()

    
    search_input = ft.TextField(label="busca", on_change=search_items, expand=True)
        
    add_button = ft.ElevatedButton("mete", on_click=add_item)
    remove_button = ft.ElevatedButton("quita", on_click=remove_item)
    clear_button = ft.ElevatedButton("limpia la lista", on_click=clear_list)
    save_button = ft.ElevatedButton("guardar", on_click=lambda e: save_or_load(e, "save"))
    load_button = ft.ElevatedButton("carga la lista", on_click=lambda e: save_or_load(e, "load"))

    
    page.add(
        ft.Row([nombre, add_button], spacing=10),
        error_message,
        search_input,
        ft.Container(view, border=ft.border.all(1), expand=True, padding=10),
        ft.Row([remove_button, clear_button, save_button, load_button], spacing=10)
    )

ft.app(target=main)
