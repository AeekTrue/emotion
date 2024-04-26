import dearpygui.dearpygui as dpg
from loguru import logger
import json
from .property import add_property_list, get_property_list_data, set_property_list_data
from emotion.storage import storage, StorageModifiedSignal


@StorageModifiedSignal.subject
def create_record_from_property_list(property_list_id):
    data = get_property_list_data(property_list_id)
    if data:
        storage.append()
        logger.debug('Rec created')
    else:
        logger.debug('Rec not created. Empty')


def add_create_record_button(property_list_id, **kwargs):
    def click_callback(sender, app_data, user_data):
        create_record_from_property_list(user_data)

    dpg.add_button(label='Create record',
            user_data=property_list_id,
            callback=lambda s, a, u: create_record_from_property_list(u),
            **kwargs)


def record_editor():
    with dpg.window(label='JSON editor', width=700, height=500):
        property_list_id = add_property_list()
        add_create_record_button(property_list_id, width=-1)
