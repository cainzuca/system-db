import streamlit as st
import controllers.ContratanteController as ContratanteController
import models.Contratante as Contratante


def AlterarContratante():	
	st.button('Atualizar')

	contratanteNome = []
	contratanteId = []
	col0, col1 = st.columns((1,1))
	
	for item in ContratanteController.selecionarTodos():
		contratanteNome.append(item.nome)

	box = st.selectbox('Selecione o contratante',contratanteNome)
	byName = ContratanteController.selecionarByName(box)
	st.query_params = byName.id
			
	#box = st.selectbox('Artista',artistaId)
	
	'''if box != None:
		st.query_params = byNome.id'''

	
	ContratanteRecuperado = None
	ContratanteRecuperado = ContratanteController.selecionarById(st.query_params)	
	st.title('Alterar contratante')
	with st.form(key='include_cliente'):
		
		input_name = st.text_input(label='Nome do contratante',value=ContratanteRecuperado.nome)
		input_phone = st.text_input(label='Telefone',value=ContratanteRecuperado.telefone)
		input_email = st.text_input(label='Email',value=ContratanteRecuperado.email)
		input_cnpj = st.text_input(label='CNPJ',value=ContratanteRecuperado.cnpj)
		col1,col2,col3,col4,col5,col6,col7= st.columns(7)
		input_button_submit = col1.form_submit_button('Salvar')
		input_button_submit2 = col2.form_submit_button('Excluir')
	
	if input_button_submit:
		ContratanteController.Alterar(Contratante.contratante(ContratanteRecuperado.id, input_name, input_phone, input_email, input_cnpj))
		st.success("Contratante alterada com sucesso!")
	if input_button_submit2:
		ContratanteController.Excluir(byName.id)
		st.success("Contratante excluída com sucesso!")