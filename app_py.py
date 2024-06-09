import streamlit as st
import streamlit.components.v1 as components

def run():
    iframe_src = "basic.html"
    components.iframe(iframe_src)
   # You can add height and width to the component of course.

if __name__ == "__main__":
    run()