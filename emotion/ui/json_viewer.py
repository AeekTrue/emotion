import dearpygui.dearpygui as dpg
from loguru import logger
import json
from .viewer import make_viewer
from .theme import list_view_theme

def json_viewer_updater(text_field_id, new_data, filt, srtr):
    dpg.set_value(text_field_id,
            json.dumps(new_data, indent=4, ensure_ascii=False))


@make_viewer(json_viewer_updater)
def json_viewer(*args, **kwargs):
    text_field_id = dpg.add_input_text(multiline=True, readonly=True, width=-1, height=-1)
    dpg.add_button(label='Copy JSON', width=-1, before=text_field_id,
            callback=lambda: dpg.set_clipboard_text(dpg.get_value(text_field_id)))
    return text_field_id


def add_list_viewer_item(data: dict, **kwargs):
    with dpg.child_window(height=100, **kwargs):
        for key, value in data.items():
            dpg.add_text(f'{key}: {value}')


def list_viewer_updater(list_container_id, new_data, filt, srtr):
    dpg.delete_item(list_container_id, children_only=True)
    for item in filter(filt, new_data):
        add_list_viewer_item(item, parent=list_container_id)


@make_viewer(list_viewer_updater)
def list_viewer(*args, **kwargs):
    with dpg.child_window(*args, **kwargs) as container:
        pass
    dpg.bind_item_theme(container, list_view_theme)
    return container


