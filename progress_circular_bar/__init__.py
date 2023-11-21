import os
import streamlit.components.v1 as components

_USE_WEB_DEV_SERVER = False

if _USE_WEB_DEV_SERVER:
    _component_func = components.declare_component(
        "progress_circular_bar", url="http://localhost:3001"
    )
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _component_func = components.declare_component("progress_circular_bar", path=build_dir)


def circular_progress_bar(value, width, key, textColor='#6b7280', trailColor="#d6d6d6", pathColor="blueviolet", strokeWidth=11):
    component_value = _component_func(value=value, 
                                      width=width,
                                      textColor=textColor,
                                      trailColor=trailColor,
                                      pathColor=pathColor, 
                                      strokeWidth=strokeWidth,                                   
                                    default=None, key=key)
    return component_value
