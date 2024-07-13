import streamlit as st
import controllers.MarcaController as MarcaController
import models.Marca as Marca


def AlterarMarca():	
	st.button('Atualizar')

	marcaNome = []
	marcaId = []
	col0, col1 = st.columns((1,1))
	
	for item in MarcaController.selecionarTodos():
		marcaNome.append(item.nome)

	box = st.selectbox('Selecione a marca',marcaNome)
	byName = MarcaController.selecionarByName(box)
	st.query_params = byName.id
			
	#box = st.selectbox('Artista',artistaId)
	
	'''if box != None:
		st.query_params = byNome.id'''

	
	MarcaRecuperado = None
	MarcaRecuperado = MarcaController.selecionarById(st.query_params)	
	st.title('Alterar marca')
	with st.form(key='include_cliente'):
		
		input_name = st.text_input(label='Nome da marca',value=MarcaRecuperado.nome)
		input_phone = st.text_input(label='Telefone',value=MarcaRecuperado.telefone)
		input_email = st.text_input(label='Email',value=MarcaRecuperado.email)
		input_cnpj = st.text_input(label='CNPJ',value=MarcaRecuperado.cnpj)
		col1,col2,col3,col4,col5,col6,col7= st.columns(7)
		input_button_submit = col1.form_submit_button('Salvar')
		input_button_submit2 = col2.form_submit_button('Excluir')
	
	if input_button_submit:
		MarcaController.Alterar(Marca.marca(MarcaRecuperado.id, input_name, input_phone, input_email,input_cnpj))
		st.success("Marca alterada com sucesso!")
	if input_button_submit2:
		MarcaController.Excluir(byName.id)
		st.success("Marca excluída com sucesso!")