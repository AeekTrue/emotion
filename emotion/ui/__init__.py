import dearpygui.dearpygui as dpg
from emotion.storage import storage

def init_ui():
    dpg.create_context()
    dpg.create_viewport(title="kanban by Aeek")
    with dpg.font_registry():
        default_font = dpg.add_font('data/fonts/OpenSans-Regular.ttf', 24)
    dpg.bind_font(default_font)
    
    show_storage(storage)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.maximize_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()

def show_storage(storage):
    def show_records():
        for r in storage.get_all():
            dpg.add_text(r)
    with dpg.window(label=storage.get_path(), width=800, height=640):
        with dpg.group(horizontal=True):
            dpg.add_button(label='Refresh')
            dpg.add_button(label='New', callback=lambda: True)
        with dpg.group(): 
            show_records()
            
