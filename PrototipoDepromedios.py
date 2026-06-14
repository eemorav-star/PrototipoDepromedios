import streamlit as st

st.set_page_config(page_title="App de Promedios", page_icon="👍")

# ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
# PROYECTO : Calcula pormedios en el sistema de educativo de Panama 
# Creadores del proyecto: Adrian Luna , Kathia Jaen, Elpidio Mora
# ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

i = 0
j = 0
promedio = 0.0
notasParciales = []
notasAP = []
promedioParciales = 0.0
promedioAp = 0.0
promediofinal = 0.0

#ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
# ENTRADAS
#ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
st.title(" Cálculo de notas promedios en el sistema educativo de Panama")

st.header(" Las notas van de 1.0 a 5.0")

nombre = st.text_input("Nombre del estudiante")
numeroDeNotas = st.number_input("¿Cuantas notas parciales son?", min_value=1, max_value=15, step=1)

notas = []
for i in range(i, numeroDeNotas):
    notaParcial = st.number_input(f"Ingrese la nota {i + 1}", min_value=1.0, max_value=5.0, step=0.1)
    notas.append(notaParcial)

# ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
# PROCESO
# ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo


    promedioParciales = sum(notas) / len(notas)
   

numeroDeNotasAP = st.number_input("¿Cuantas notas de apreciación son?", min_value=1, max_value=15, step=1)
notasAP = []
for j in range(j, numeroDeNotasAP):
    notaApreciacion = st.number_input(f"Ingrese la nota de apreciación {j + 1}", min_value=1.0, max_value=5.0, step=0.1)
    notasAP.append(notaApreciacion)
    
    promedioAp = sum(notasAP) / len(notasAP)
promediofinal = (promedioParciales + promedioAp) / 2

 # ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
 #  SALIDA
 # ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
st.header(" Las notas y  el promedio final es:")

st.write("Nombre del estudiante:", nombre)
for i, nota in enumerate(notas, start=1):
        st.write(f"Nota Parcial {i}:", nota)
for j, nota in enumerate(notasAP, start=1):
        st.write(f"Nota de apreciación {j}:", nota)
st.success(f"El promedio final es: {promediofinal:.2f}")