import dearpygui.dearpygui as dpg
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
            with dpg.window(*args, **kwargs):
                container_id = container_creator()
                set_viewer_filter_and_sorter(container_id, fltr, srtr)
                storage_modification_handler = bind_updater_to_container(updater, container_id)
                storage_modification_handler()
                StorageModifiedSignal.subscriber(storage_modification_handler)
        return wrapper 
    return outer
