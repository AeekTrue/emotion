import dearpygui.dearpygui as dpg
from loguru import logger

def set_property_value_field_type(sender, field_type, field_id):
    dpg.delete_item(field_id) 
    logger.debug((sender, field_type, field_id))
    new_field_id = dpg.generate_uuid()
    common_args = {'width': 200, 'before': sender, 'tag': new_field_id}
    if field_type == 'String':
        dpg.add_input_text(hint='Value', **common_args)
    elif field_type == 'Integer':
        dpg.add_input_int(**common_args)
    elif field_type == 'Float':
        dpg.add_input_float(**common_args)
    elif field_type == 'Bool':
        dpg.add_combo(items=('True', 'False'), default_value='True', **common_args)
    dpg.configure_item(sender, user_data=new_field_id)
    
    

def add_property(sender, app_data, container_id):
    dpg.push_container_stack(container_id)
    with dpg.group(horizontal=True):
        dpg.add_input_text(hint='Key', width=200)
        value_field_id = dpg.add_input_text(hint='Value', width=200)
        dpg.add_combo(label='Type', items=('String', 'Integer', 'Float', 'Bool'),
               default_value='String', user_data=value_field_id, width=200,
               callback=set_property_value_field_type)
    dpg.pop_container_stack()


def show_json(sender, app_data, container_id):
    with dpg.window(label='JSON viewer', width=700, height=500, pos=(800, 100)):
        dpg.add_text('lol')
def json_editor():
    with dpg.window(label='JSON editor', width=700, height=500):
        with dpg.group() as container:
            pass
        dpg.add_button(label='+ Add property', width=-1,
                    user_data=container,
                    callback=add_property)
        dpg.add_button(label='Generate JSON', width=-1, user_data=container, callback=show_json)
