import streamlit as st
from helpers import *




st.title("¡Hola Neurona!")



st.image("https://educacionadistancia.juntadeandalucia.es/centros/malaga/pluginfile.php/751448/mod_label/intro/neurona_fp_1000.jpg")

tab1, tab2, tab3 = st.tabs(["Una entrada", "Dos entradas", "Tres entradas y sesgo"])

with tab1:
    st.markdown("Peso $w_0$")

    weight = st.slider(
        'Slider 1',
        0.0, 5.0,
        label_visibility="collapsed",
        key="neurona1"

    )
    st.markdown("Entrada $x_0$")
    input_value = st.number_input("Introduzca el valor de la entrada", key="Neurona1_input")
    button = st.button(label="Calcular la salida", key="Neurona1_button")
    if button:
      st.write(f'{neurona(input_value, weight)}')



with tab2:
  col1, col2 = st.columns(2)
  with col1: 
    st.markdown("Peso $w_0$")

    weight_1 = st.slider(
        'Slider 1',
        0.0, 5.0,
        label_visibility="collapsed",
        key="Neurona2_1"


    )
    st.markdown("Entrada $x_0$")
    input_value_1 = st.number_input("Introduzca el valor de la entrada", key="Neurona2_input1_1")
  
  with col2:
    st.markdown("Peso $w_1$")

    weight_2 = st.slider(
    'Slider 1',
    0.0, 5.0,
    label_visibility="collapsed",
    key="Neurona2_2"
    )
  
    st.markdown("Entrada $x_1$")
    input_value_2 = st.number_input("Introduzca el valor de la entrada", key="Neurona2_input1_2")

    
  button2 = st.button(label="Calcular la salida", key="Neurona2_button") 
  if button2: 
    st.write(f'La salida es: {neurona2(input_value_1, input_value_2, weight_1, weight_2)}')  
      

      


with tab3:
    st.header("Neurona Con Sesgo")

    col_s_1, col_s_2, col_s_3 = st.columns(3)

    with col_s_1:
      st.markdown("Peso $w_0$")
      weight_bias_0 = st.slider("Slider_bias_1", 0.0, 5.0, label_visibility="collapsed", key="neurona_bias_peso0")
      st.markdown("Entrada $x_0$")
      input_bias_0 = st.number_input("Introduzca el valor de la entrada", key="neurona_bias_input0")


    with col_s_2:
      st.markdown("Peso $w_1$")
      weight_bias_1 = st.slider("Slider_bias_1", 0.0, 5.0, label_visibility="collapsed", key="neurona_bias_peso1")
      st.markdown("Entrada $x_1$")
      input_bias_1 = st.number_input("Introduzca el valor de la entrada", key="neurona_bias_input1")

    with col_s_3:
      st.markdown("Peso $w_2$")
      weight_bias_2 = st.slider("Slider_bias_1", 0.0, 5.0, label_visibility="collapsed", key="neurona_bias_peso2")
      st.markdown("Entrada $x_2$")
      input_bias_2 = st.number_input("Introduzca el valor de la entrada", key="neurona_bias_input2")

    input_bias_value = st.number_input("Introduzca el sesgo: ", key="bias_value")

    button3 = st.button(label="Calcular la salida", key="neurona_bias_button")

    if button3:
      st.write(f'El resultado de la salida es: {biased(input_bias_0, input_bias_1,input_bias_2, weight_bias_0, weight_bias_1, weight_bias_2, input_bias_value)}')



