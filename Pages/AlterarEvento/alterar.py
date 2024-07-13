import streamlit as st
import controllers.EventoController as EventoController
import models.Evento as Evento
import controllers.ContratanteController as ContratanteController
import controllers.ArtistaController as ArtistaController
import controllers.MarcaController as MarcaController
from datetime import datetime


'''contratanteNome = []
for item in ContratanteController.selecionarTodos():
	contratanteNome.append(item.nome)'''


def AlterarEvento():	
	st.button('Atualizar')

	eventoNome = []
	eventoId = []
	col0, col1 = st.columns((1,1))
	
	for item in EventoController.selecionarTodos():
		eventoNome.append(item.nome)

	box = st.selectbox('Selecione a evento',eventoNome)
	byName = EventoController.selecionarByName(box)
	st.query_params = byName.id			
	
	EventoRecuperado = None
	EventoRecuperado = EventoController.selecionarById(st.query_params)	

	artistaNome = []
	for item in ArtistaController.selecionarById2(EventoRecuperado.fk_artista):
		artistaNome.append(item.nome)
		
	contratanteNome = []
	for item in ContratanteController.selecionarById2(EventoRecuperado.fk_contratante):
		contratanteNome.append(item.nome)

	marcaNome = []
	for item in MarcaController.selecionarById2(EventoRecuperado.fk_marca):
		marcaNome.append(item.nome)				

	st.title('Alterar evento')
	with st.form(key='include_cliente'):		
		input_name = st.text_input(label='Nome da evento',value=EventoRecuperado.nome)
		input_local = st.text_input(label='local',value=EventoRecuperado.local)
		input_value = st.number_input(label='Valor',value=EventoRecuperado.valor)
		input_porcentagem = st.number_input(label='Porcentagem',value=EventoRecuperado.porcentagem)
		input_custos = st.number_input(label='Custos',value=EventoRecuperado.custos)
		input_date = st.date_input(label='Data do Evento',value=EventoRecuperado.data, format= 'DD/MM/YYYY', min_value=datetime(1990, 1, 1))
		#input_fk_artist = st.number_input(label='fk_artista',format='%d',step=1,value=EventoRecuperado.fk_artista)
		#input_fk_contratante = st.number_input(label='fk_contratante',format='%d',step=1,value=EventoRecuperado.fk_contratante)
		#input_fk_marca = st.number_input(label='fk_marca',format='%d',step=1,value=EventoRecuperado.fk_marca)
		input_artist = st.selectbox("Artista",artistaNome)
		input_contratante = st.selectbox("Contratante",contratanteNome)
		input_marca = st.selectbox("Marca",marcaNome)
		col1,col2,col3,col4,col5,col6,col7= st.columns(7)
		input_button_submit = col1.form_submit_button('Salvar')
		input_button_submit2 = col2.form_submit_button('Excluir')
	
	byNameArtista = ArtistaController.selecionarByName(input_artist)
	byNameContratante = ContratanteController.selecionarByName(input_contratante)
	byNameMarca = MarcaController.selecionarByName(input_marca)	

	if input_button_submit:
		EventoController.Alterar(Evento.evento(EventoRecuperado.id, input_name, input_local, input_value,input_date,byNameArtista.id,byNameContratante.id,byNameMarca.id,input_porcentagem,input_custos))
		st.success("Evento alterado com sucesso!")
	if input_button_submit2:
		EventoController.Excluir(byName.id)
		st.success("Evento excluído com sucesso!")