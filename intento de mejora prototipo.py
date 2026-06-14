import streamlit as st

st.set_page_config(page_title="App de Promedios", page_icon="😄")

# ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
# PROYECTO CALCULADORA DE PROMEDIOS ESTUDIANTILES
# Creadores del proyecto: Adrian Luna , Kathia Jaen, Elpidio Mora
# ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
notaprimertrimestre = 0.0 # Variable para almacenar la nota del primer trimestre ingresada por el usuario
notasegundotrimestre = 0.0 # Variable para almacenar la nota del segundo
numeroDeParciales = 0 # Variable para almacenar el número de parciales a acumular
NotaParcial = 0.0 # Variable para almacenar la nota parcial ingresada por el usuario
promedioParciales = 0.0 # Variable para almacenar el promedio de las notas parciales
sumaNotas = 0.0 # Variable para almacenar la suma de las notas parciales
NotasApreciacion = 0.0 # Variable para almacenar la nota de apreciación ingresada por el usuario
promedioApeciacion = 0.0 # Variable para almacenar el promedio de la nota de apreciación
notaEXATrimestral = 0.0 # Variable para almacenar la nota del examen trimestral ingresada por el usuario

#ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
# ENTRADAS
#ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
st.title(" Programa para el calculo de promedios MEDUCA PANAMA")

st.header(" Las notas van de 1.0 a 5.0")


# ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
# ENTRADAS
# ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
numeroDeParciales = st.number_input("Cuantas notas parciales va a calcular?", min_value=1, max_value=10, step=1)

nombre = st.text_input("Ingrese el nombre del estudiante")
for i in range(numeroDeParciales):
    globals()[f"nota{i+1}"] = st.number_input(f"Ingrese la Nota {i+1}", min_value=1.0, max_value=5.0)

# ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
# PROCESO
# ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
st.header("Dar clic en el botón")

if st.button("Calcular promedio"):

    PromedioParciales = 
    
    #ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
    #  SALIDA
    # ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
    st.header(" Resultados de estos calculo del promedio")

    st.write("Nombre del estudiante:", nombre)
    st.write("Nota 1:", nota1)
    st.write("Nota 2:", nota2)
    st.write("Nota 3:", nota3)

    st.success(f"El promedio final es: {promedio:.2f}")