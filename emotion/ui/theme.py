import dearpygui.dearpygui as dpg
print('lol')
dpg.create_context()
with dpg.theme() as list_view_theme:
    with dpg.theme_component(dpg.mvAll):
        #dpg.add_theme_color(dpg.mvThemeCol_Text, [255, 0, 0],
        #        category=dpg.mvThemeCat_Core) 
        pass
