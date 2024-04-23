import dearpygui.dearpygui as dpg
from loguru import logger
import json
from emotion.storage import storage

def set_json_viewer_value(json_viewer_id):
    dpg.set_item_value(json_viewer_id, )


def add_refresh_button(text_field_id, **kwargs):
    def click_callback(sender, app_data, user_data):
        dpg.set_value(text_field_id, json.dumps(storage.data, indent=4, ensure_ascii=False)) 

    dpg.add_button(label='Refresh', user_data=text_field_id, callback=click_callback,
            **kwargs)


def json_viewer():
    with dpg.window(label='JSON viewer', width=700, height=500):
        text_field_id = dpg.add_input_text(multiline=True, readonly=True, width=-1, height=-1,
                default_value=json.dumps(storage.data, indent=4, ensure_ascii=False))
        dpg.add_button(label='Copy JSON', width=-1, before=text_field_id,
                callback=lambda: dpg.set_clipboard_text(dpg.get_value(text_field_id)))
        add_refresh_button(text_field_id, width=-1, before=text_field_id)
    return text_field_id

