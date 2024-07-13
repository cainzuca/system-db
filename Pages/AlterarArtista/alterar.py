import streamlit as st
import controllers.ArtistaController as ArtistaController
import models.Artista as Artista
from datetime import datetime


def AlterarArtista():	
	st.button('Atualizar')

	artistaNome = []
	artistaId = []
	col0, col1 = st.columns((1,1))
	
	for item in ArtistaController.selecionarTodos():
		artistaNome.append(item.nome)

	box = st.selectbox('Selecione o artista',artistaNome)
	byName = ArtistaController.selecionarByName(box)
	st.query_params = byName.id
			
	#box = st.selectbox('Artista',artistaId)
	
	'''if box != None:
		st.query_params = byNome.id'''

	
	ArtistaRecuperado = None
	ArtistaRecuperado = ArtistaController.selecionarById(st.query_params)	
	st.title('Alterar artista')
	with st.form(key='include_cliente'):
		
		input_name = st.text_input(label='Nome do artista',value=ArtistaRecuperado.nome)

		col1,col2,col3= st.columns(3)

		input_age = col1.number_input(label='Idade',format='%d',step=1,value=ArtistaRecuperado.idade)
		input_cpf = col2.number_input(label='CPF',format='%d',step=1)
		input_data_nascimento = col3.date_input(label='Data de nascimento',value=ArtistaRecuperado.data_nascimento, format= 'DD/MM/YYYY', min_value=datetime(1990, 1, 1))
		input_pix = st.text_input(label='Pix',value=ArtistaRecuperado.pix)
		input_rg = col1.number_input(label='rg',format='%d',step=1,value=ArtistaRecuperado.rg)
		input_titulo = col2.number_input(label='Titulo de eleitor',format='%d',step=1,value=ArtistaRecuperado.titulo_eleitor)
		input_cnpj = col3.number_input(label='CNPJ',format='%d',step=1,value=ArtistaRecuperado.cnpj)

		col1,col2= st.columns(2)

		input_login_sesc = col1.text_input(label='Login SESC',value=ArtistaRecuperado.login_sesc)
		input_senha_sesc = col2.text_input(label='Senha SESC',value=ArtistaRecuperado.senha_sesc,type='password')
		input_login_nota = col1.text_input(label='Login Nota Carioca',value=ArtistaRecuperado.login_nota)
		input_senha_nota = col2.text_input(label='Senha Nota',value=ArtistaRecuperado.senha_nota,type='password')
		input_login_gov = col1.text_input(label='Login Gov',value=ArtistaRecuperado.login_gov)
		input_senha_gov = col2.text_input(label='Senha Gov',value=ArtistaRecuperado.senha_gov,type='password')
		input_presskit = col1.text_input(label='Presskit',value=ArtistaRecuperado.presskit)
		input_senha_presskit = col2.text_input(label='Senha Presskit',value=ArtistaRecuperado.senha_presskit,type='password')
		input_nota = st.text_input(label='Nota',value=ArtistaRecuperado.nota)

		col1,col2,col3= st.columns(3)

		input_banco = col1.text_input(label='Banco',value=ArtistaRecuperado.banco)
		input_conta = col2.number_input(label='Conta',format='%d',step=1,value=ArtistaRecuperado.conta)
		input_agencia = col3.number_input(label='Agência',format='%d',step=1,value=ArtistaRecuperado.agencia)

		col1,col2,col3,col4,col5,col6,col7= st.columns(7)
		input_button_submit = col1.form_submit_button('Salvar')
		input_button_submit2 = col2.form_submit_button('Excluir')
	
	if input_button_submit:
		#st.write('miau')
		ArtistaController.Alterar(Artista.artista(ArtistaRecuperado.id, input_name, input_age, input_cpf,input_conta,input_pix,input_rg,input_titulo,input_cnpj,input_data_nascimento,input_login_sesc,input_login_nota,input_login_gov,input_presskit,input_nota, input_senha_sesc, input_senha_nota, input_senha_gov, input_senha_presskit,input_banco,input_agencia))
		st.success("Artista alterado com sucesso!")
	if input_button_submit2:
		ArtistaController.Excluir(byName.id)
		st.success("Artista excluído com sucesso!")