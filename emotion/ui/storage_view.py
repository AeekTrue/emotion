from emotion.storage import storage

def add_storage_content_view():
    for r in storage.get_all():
        with dpg.tree_node(label=str(r.get('id')), default_open=True):
            for k in r:
                with dpg.group(horizontal=True):
                    dpg.add_text(str(k))
                    dpg.add_text(str(r[k]))

def make_updater(container_id, content_generator):
    def updater():
        dpg.delete_item(container_id, children_only=True)
        dpg.push_container_stack(container_id)
        content_generator()
        dpg.pop_container_stack()
    return updater

def show_storage(storage):
    container_id = dpg.generate_uuid()
    with dpg.window(label=storage.get_path(), width=800, height=640):
        with dpg.group(horizontal=True):
            dpg.add_button(label='Refresh', callback=make_updater(container_id, add_storage_content_view))
            dpg.add_button(label='New', callback=lambda: storage.append({'id': dpg.generate_uuid(), 'a':3}))
            dpg.add_button(label='Save', callback=lambda: storage.save_data())
        with dpg.group(tag=container_id): 
            add_storage_content_view()
