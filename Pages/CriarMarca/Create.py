import streamlit as st
import controllers.MarcaController as MarcaController
import models.Marca as Marca
import pandas as pd
import services.database as db


def IncluirMarca():	
	st.title('Nova Marca')
	with st.form(key='include_cliente'):
		input_name = st.text_input(label='Nome da marca')
		input_phone = st.number_input(label='Telefone',format='%d',step=1)
		input_email = st.text_input(label='Email')
		input_cnpj = st.number_input(label='CNPJ',format='%d',step=1)
		input_button_submit = st.form_submit_button('Salvar')



	if input_button_submit:
		MarcaController.incluir(Marca.marca(0,input_name, input_phone, input_email,input_cnpj))
		st.success("Marca incluida com sucesso!")

	st.markdown("""---""")
		
		
'''	marca = []
	for item in MarcaController.selecionarTodos():
		marca.append([item.nome])'''

'''	db.cursor.execute("SELECT* FROM marca")
	rows = db.cursor.fetchall()
	df = pd.DataFrame.from_records(rows, columns=[desc[0] for desc in db.cursor.description])

	st.dataframe(df)'''
