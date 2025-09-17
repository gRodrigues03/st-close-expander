import streamlit.components.v1 as components
import os.path
_component_func = components.declare_component("st_close_expander",path=os.path.join(os.path.dirname(__file__), "frontend"))
def close_expander():
    return _component_func(id='st_close_expander')