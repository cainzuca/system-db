import streamlit as st
import controllers.EventoController as EventoController
import models.Evento as Evento
import pandas as pd
import services.database as db
import controllers.ContratanteController as ContratanteController
import controllers.ArtistaController as ArtistaController
import controllers.MarcaController as MarcaController
from datetime import datetime


'''artistaNome = []
for item in ArtistaController.selecionarTodos():
	artistaNome.append(item.nome)

contratanteNome = []
for item in ContratanteController.selecionarTodos():
	contratanteNome.append(item.nome)

marcaNome = []
for item in MarcaController.selecionarTodos():
	marcaNome.append(item.nome)	'''	



def IncluirEvento():
	artistaNome = []
	for item in ArtistaController.selecionarTodos():
		artistaNome.append(item.nome)

	contratanteNome = []
	for item in ContratanteController.selecionarTodos():
		contratanteNome.append(item.nome)

	marcaNome = []
	for item in MarcaController.selecionarTodos():
		marcaNome.append(item.nome)	
		
	st.button('Atualizar')	
	st.title('Novo Evento')
	with st.form(key='include_cliente'):
		input_name = st.text_input(label='Nome do evento')
		input_local = st.text_input(label='Local')
		input_value = st.number_input(label='Valor')
		input_porcentagem = st.number_input(label='Porcentagem')
		input_custos = st.number_input(label='Custos')
		input_date = st.date_input(label='Data do Evento', format= 'DD/MM/YYYY', min_value=datetime(1990, 1, 1))
		input_artist = st.selectbox("Artista",artistaNome)
		input_contratante = st.selectbox("Contratante",contratanteNome)
		input_marca = st.selectbox("Marca",marcaNome)
		input_button_submit = st.form_submit_button('Salvar')

	byNameArtista = ArtistaController.selecionarByName(input_artist)
	byNameContratante = ContratanteController.selecionarByName(input_contratante)
	byNameMarca = MarcaController.selecionarByName(input_marca)

	if input_button_submit:
		EventoController.incluir(Evento.evento(0,input_name, input_local, input_value,input_date,byNameArtista.id,byNameContratante.id,byNameMarca.id,input_porcentagem,input_custos))
		st.success("Evento incluida com sucesso!")

	st.markdown("""---""")		

'''	db.cursor.execute("SELECT* FROM evento")
	rows = db.cursor.fetchall()
	df = pd.DataFrame.from_records(rows, columns=[desc[0] for desc in db.cursor.description])

	st.dataframe(df)'''