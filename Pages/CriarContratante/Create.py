import streamlit as st
import controllers.ContratanteController as ContratanteController
import models.Contratante as Contratante
import pandas as pd
import services.database as db


def IncluirContratante():	
	st.title('Novo Contratante')
	with st.form(key='include_cliente'):
		input_name = st.text_input(label='Nome do contratante')
		input_phone = st.number_input(label='Telefone',format='%d',step=1)
		input_email = st.text_input(label='Email')
		input_cnpj = st.number_input(label='CNPJ',format='%d',step=1)
		input_button_submit = st.form_submit_button('Salvar')



	if input_button_submit:
		ContratanteController.incluir(Contratante.contratante(0,input_name, input_phone, input_email, input_cnpj))
		st.success("Contratante incluido com sucesso!")

	st.markdown("""---""")
		
		
	'''contratante = []
	for item in ContratanteController.selecionarTodos():
		contratante.append([item.nome,item.idade])'''

'''	db.cursor.execute("SELECT* FROM contratante")
	rows = db.cursor.fetchall()
	df = pd.DataFrame.from_records(rows, columns=[desc[0] for desc in db.cursor.description])

	st.dataframe(df)'''
