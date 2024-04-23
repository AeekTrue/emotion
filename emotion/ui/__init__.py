import dearpygui.dearpygui as dpg
import json
from emotion.storage import storage
from .json_editor import record_editor, get_property_list_data
from .json_viewer import json_viewer
from loguru import logger

def init_ui():
    dpg.create_context()
    dpg.create_viewport(title="kanban by Aeek")
    with dpg.font_registry():
        with dpg.font('data/fonts/OpenSans-Regular.ttf', 24) as default_font:
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Cyrillic)
        dpg.bind_font(default_font)

    logger.debug(storage)
    json_viewer()
    record_editor()
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.maximize_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()
    storage.save()

