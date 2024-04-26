import dearpygui.dearpygui as dpg
from loguru import logger
import json
from emotion.storage import storage, StorageModifiedSignal
from functools import partial


def get_viewer_filter_and_sorter(container_id):
    return dpg.get_item_user_data(container_id)


def set_viewer_filter_and_sorter(container_id, fltr, srtr):
    dpg.configure_item(container_id, user_data=(fltr, srtr)) 


def bind_updater_to_container(updater, container_id):
    def wrapper():
        viewer_filter, viewer_sorter = get_viewer_filter_and_sorter(container_id)
        updater(container_id, storage.data, viewer_filter, viewer_sorter)
    return wrapper


def make_viewer(updater, fltr=None, srtr=None):
    def outer(container_creator):
        def wrapper(*args, **kwargs):
            with dpg.window(label='Dynamic viewer'):
                container_id = container_creator(*args, **kwargs)
                set_viewer_filter_and_sorter(container_id, fltr, srtr)
                storage_modification_handler = bind_updater_to_container(updater, container_id)
                storage_modification_handler()
                StorageModifiedSignal.subscriber(storage_modification_handler)
        return wrapper 
    return outer


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
    with dpg.group(**kwargs):
        for key, value in data.items():
            dpg.add_text(f'{key}: {value}')
        dpg.add_text('----------')


def list_viewer_updater(list_container_id, new_data, filt, srtr):
    dpg.delete_item(list_container_id, children_only=True)
    for item in new_data:
        add_list_viewer_item(item, parent=list_container_id)


@make_viewer(list_viewer_updater)
def list_viewer(*args, **kwargs):
    with dpg.group(*args, **kwargs) as container:
        pass
    return container


