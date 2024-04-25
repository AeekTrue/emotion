import dearpygui.dearpygui as dpg
from loguru import logger
import json
from emotion.storage import storage, StorageModifiedSignal
from functools import partial


def viewer(add_container, updater, filt=None, **kwargs): 
    with dpg.window(label='Viewer', **kwargs):
        container_id = add_container()        
        updater(container_id, filt)
        storage_modification_handler = partial(updater, container_id, filt)
        StorageModifiedSignal.subscriber(storage_modification_handler)
        

def json_viewer_container():
    text_field_id = dpg.add_input_text(multiline=True, readonly=True, width=-1, height=-1)
    dpg.add_button(label='Copy JSON', width=-1, before=text_field_id,
            callback=lambda: dpg.set_clipboard_text(dpg.get_value(text_field_id)))
    return text_field_id


def json_viewer_updater(text_field_id, filt):
    dpg.set_value(text_field_id,
            json.dumps(list(filter(filt, storage.data)), indent=4, ensure_ascii=False)) 


json_viewer = lambda: viewer(json_viewer_container, json_viewer_updater, width=800, height=600)
