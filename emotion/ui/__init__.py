import dearpygui.dearpygui as dpg
from .json_editor import json_editor
from loguru import logger

def init_ui():
    dpg.create_context()
    dpg.create_viewport(title="kanban by Aeek")
    with dpg.font_registry():
        default_font = dpg.add_font('data/fonts/OpenSans-Regular.ttf', 24)
    dpg.bind_font(default_font)
    
    json_editor()
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.maximize_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()

