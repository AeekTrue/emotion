import dearpygui.dearpygui as dpg
from .typed_value_field import set_value_field_type, add_typed_value_field
from loguru import logger

def add_property(**kwargs):
    with dpg.group(horizontal=True, **kwargs) as property_id:
        key_field_id = dpg.add_input_text(hint='Key', width=200)
        value_field_id = add_typed_value_field()
        dpg.set_item_user_data(dpg.last_container(),(key_field_id, value_field_id))
    return property_id

def add_property_list(**kwargs):
    with dpg.group(**kwargs):
        with dpg.group(height=-1) as container:
            pass
        dpg.add_button(label='+ Add property', width=-1, user_data=container,
            callback=lambda s, a, u: add_property(parent=u))
    return container

def get_property_value(property_id):
    key_field_id, value_field_id = dpg.get_item_user_data(property_id)
    return dpg.get_values((key_field_id, value_field_id))

def get_property_list_data(property_list_id):
    json_data = dict()
    for property_id in dpg.get_item_children(property_list_id, slot=1):
        key, value = get_property_value(property_id)
        json_data[key] = value
    return json_data

