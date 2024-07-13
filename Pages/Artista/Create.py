import streamlit as st
import controllers.ArtistaController as ArtistaController
import models.Artista as Artista
import pandas as pd
import services.database as db
from datetime import datetime


def IncluirArtista():	
	st.title('Novo artista')
	with st.form(key='include_cliente'):
		input_name = st.text_input(label='Nome do artista')

		col1,col2,col3= st.columns(3)

		input_age = col1.number_input(label='Idade',format='%d',step=1)
		input_cpf = col2.number_input(label='CPF',format='%d',step=1)
		input_data_nascimento = col3.date_input(label='Data de nascimento', format= 'DD/MM/YYYY', min_value=datetime(1990, 1, 1))
		input_pix = st.text_input(label='Pix')
		input_rg = col1.number_input(label='rg',format='%d',step=1)
		input_titulo = col2.number_input(label='Titulo de eleitor',format='%d',step=1)
		input_cnpj = col3.number_input(label='CNPJ',format='%d',step=1)

		col1,col2= st.columns(2)

		input_login_sesc = col1.text_input(label='Login SESC')
		input_senha_sesc = col2.text_input(label='Senha SESC',type='password')
		input_login_nota = col1.text_input(label='Login Nota Carioca')
		input_senha_nota = col2.text_input(label='Senha Nota Carioca',type='password')
		input_login_gov = col1.text_input(label='Login Gov')
		input_senha_gov = col2.text_input(label='Senha Gov',type='password')
		input_presskit = col1.text_input(label='Presskit')
		input_senha_presskit = col2.text_input(label='Senha Presskit',type='password')
		#input_porcentagem = st.number_input(label='Porcentagem')
		input_nota = st.text_input(label='Nota')

		col1,col2,col3= st.columns(3)

		input_banco = col1.text_input(label='Banco')
		input_conta = col2.number_input(label='Conta',format='%d',step=1)
		input_agencia = col3.number_input(label='Agência',format='%d',step=1)

		input_button_submit = st.form_submit_button('Salvar')



	if input_button_submit:
		ArtistaController.incluir(Artista.artista(0,input_name, input_age, input_cpf,input_conta,input_pix,input_rg,input_titulo,input_cnpj,input_data_nascimento,input_login_sesc,input_login_nota,input_login_gov,input_presskit,input_nota,input_senha_sesc,input_senha_nota,input_senha_gov,input_senha_presskit,input_banco,input_agencia))
		st.success("Artista incluido com sucesso!")

	st.markdown("""---""")
		
		
	'''artista = []
	for item in ArtistaController.selecionarTodos():
		artista.append([item.nome,item.idade])'''

'''	db.cursor.execute("SELECT* FROM artista")
	rows = db.cursor.fetchall()
	df = pd.DataFrame.from_records(rows, columns=[desc[0] for desc in db.cursor.description])

	st.dataframe(df)'''
