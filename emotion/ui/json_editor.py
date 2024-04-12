import dearpygui.dearpygui as dpg
from loguru import logger
import json

def set_value_field_type(sender, field_type, field_id):
    dpg.delete_item(field_id) 
    logger.debug((sender, field_type, field_id))
    common_args = {'width': 200, 'before': sender, 'tag': field_id}
    if field_type == 'String':
        dpg.add_input_text(hint='Value', **common_args)
    elif field_type == 'Integer':
        dpg.add_input_int(**common_args)
    elif field_type == 'Float':
        dpg.add_input_float(**common_args)
    elif field_type == 'Bool':
        #dpg.add_selectable(label='Check', **common_args)
        dpg.add_combo(items=(True, False), default_value='True', **common_args)
    
def add_typed_value_field():
    value_field_id = dpg.add_input_text(hint='Value', width=200)
    dpg.add_combo(label='Type', items=('String', 'Integer', 'Float', 'Bool'),
           default_value='String', user_data=value_field_id, width=200,
           callback=set_value_field_type)
    return value_field_id
    
def add_property(sender, app_data, container_id):
    dpg.push_container_stack(container_id)
    with dpg.group(horizontal=True):
        key_field_id = dpg.add_input_text(hint='Key', width=200)
        value_field_id = add_typed_value_field()
        dpg.set_item_user_data(dpg.last_container(),(key_field_id, value_field_id))
    dpg.pop_container_stack()


def get_property_value(property_id):
    key_field_id, value_field_id = dpg.get_item_user_data(property_id)
    return dpg.get_values((key_field_id, value_field_id))


def show_json(sender, app_data, container_id):
    with dpg.window(label='JSON viewer', width=700, height=500, pos=(800, 100)):
        json_data = dict()
        for property_id in dpg.get_item_children(container_id, slot=1):
            key, value = get_property_value(property_id)
            json_data[key] = value
        text_field_id = dpg.add_input_text(default_value=json.dumps(json_data, indent=4),
                multiline=True, readonly=True, width=-1, height=-1)
        dpg.add_button(label='Copy JSON', width=-1,
                callback=lambda: dpg.set_clipboard_text(dpg.get_value(text_field_id)))

def json_editor():
    with dpg.window(label='JSON editor', width=700, height=500):
        with dpg.group(height=-1) as container:
            pass
        dpg.add_button(label='+ Add property', width=-1, user_data=container,
                    callback=add_property)
        dpg.add_button(label='Generate JSON', width=-1, user_data=container, callback=show_json)
