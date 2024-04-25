import dearpygui.dearpygui as dpg
from loguru import logger

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
    
def add_typed_value_field(value_type='String', value=''):
    value_field_id = dpg.add_input_text(hint='Value', width=200)
    switcher = dpg.add_combo(label='Type', items=('String', 'Integer', 'Float', 'Bool'),
           default_value='String', user_data=value_field_id, width=200,
           callback=set_value_field_type)

    set_value_field_type(switcher, value_type, value_field_id)
    dpg.set_value(value_field_id, value)
    return value_field_id

