import os
import streamlit.components.v1 as components

_USE_WEB_DEV_SERVER = False

if _USE_WEB_DEV_SERVER:
    _component_func = components.declare_component(
        "custom_table", url="http://localhost:3001"
    )
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _component_func = components.declare_component("custom_table", path=build_dir)


def custom_table(html, key):
    component_value = _component_func(html=html,                                  
                                    default=None, key=key)
    return component_value
