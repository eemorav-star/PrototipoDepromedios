Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import streamlit as st
... 
... st.set_page_config(page_title="App de Promedios", page_icon="👍")
... 
... # ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
... # Prototipo, Calcula pormedios en el sistema de educativo de Panama 
... # Estudiantes : Adrian Luna , Kathia Jaen, Elpidio Mora
... # ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
... 
... 
... #ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
... # ENTRADAS
... #ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
... st.title(" Calculo de promedios en el sistema educativo de PANAMA")
... 
... st.header(" Las notas van de 1.0 a 5.0")
... 
... nombre = st.text_input("Ingrese el nombre del estudiante")
... nota1 = st.number_input("Ingrese la Nota 1", min_value=1.0, max_value=5.0)
... nota2 = st.number_input("Ingrese la Nota 2", min_value=1.0, max_value=5.0)
... nota3 = st.number_input("Ingrese la Nota 3", min_value=1.0, max_value=5.0)
... 
... # ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
... # PROCESO
... # ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
... st.header("Dar clic en el botón")
... 
... if st.button("Calcular promedio"):
... 
...     promedio = (nota1 + nota2 + nota3) / 3
... 
...  # ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
...  #  SALIDA
...  # ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
...     st.header(" El calculo de las notas y  del promedio es:")
... 
...     st.write("Nombre del estudiante:", nombre)
    st.write("Nota 1:", nota1)
    st.write("Nota 2:", nota2)
    st.write("Nota 3:", nota3)

