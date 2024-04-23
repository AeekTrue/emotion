import dearpygui.dearpygui as dpg
from loguru import logger
import json
from .property import add_property_list, get_property_list_data
from emotion.storage import storage


def add_create_record_button(property_list_id, **kwargs):
    def click_callback(sender, app_data, user_data):
        storage.append(get_property_list_data(user_data))
        logger.debug('Rec created')

    dpg.add_button(label='Create record', user_data=property_list_id,
            callback=click_callback, **kwargs)


def record_editor():
    with dpg.window(label='JSON editor', width=700, height=500):
        property_list_id = add_property_list()
        add_create_record_button(property_list_id, width=-1)
