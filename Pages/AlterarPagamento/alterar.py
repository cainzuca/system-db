import streamlit as st
import controllers.PagamentoController as PagamentoController
import models.Pagamento as Pagamento
import controllers.ContratanteController as ContratanteController
import controllers.EventoController as EventoController
import controllers.MarcaController as MarcaController
from datetime import datetime


'''contratanteNome = []
for item in ContratanteController.selecionarTodos():
	contratanteNome.append(item.nome)'''


def AlterarPagamento():	
	st.button('Atualizar')

	pagamentoNome = []
	pagamentoId = []
	col0, col1 = st.columns((1,1))
	
	for item in PagamentoController.selecionarTodos():
		pagamentoNome.append(item.id)

	box = st.selectbox('Selecione a pagamento',pagamentoNome)
	byName = PagamentoController.selecionarById(box)
	st.query_params = byName.id			
	
	PagamentoRecuperado = None
	PagamentoRecuperado = PagamentoController.selecionarById(st.query_params)	

	eventoNome = []
	for item in EventoController.selecionarById2(PagamentoRecuperado.fk_evento):
		eventoNome.append(item.nome)
		
	contratanteNome = []
	for item in ContratanteController.selecionarById2(PagamentoRecuperado.fk_contratante):
		contratanteNome.append(item.nome)

	marcaNome = []
	for item in MarcaController.selecionarById2(PagamentoRecuperado.fk_marca):
		marcaNome.append(item.nome)				

	st.title('Alterar pagamento')

	col1, col2,col3 = st.columns(3)
	input_forma = col1.selectbox('Forma',[PagamentoRecuperado.forma,'Débito','Crédito','Pix','Dinheiro'])

	with st.form(key='include_cliente'):		
		input_value = st.number_input(label='Valor',value=PagamentoRecuperado.valor)
		if input_forma == "Crédito":
			input_parcela = col2.selectbox("Parcelas",[PagamentoRecuperado.parcela,'1x','2x','3x','4x','5x','6x'])
			input_entrada = col3.number_input(label='Entrada',format='%d',step=1,value=PagamentoRecuperado.entrada)
		input_date = st.date_input(label='Data do Pagamento',value=PagamentoRecuperado.data, format= 'DD/MM/YYYY', min_value=datetime(1990, 1, 1))
		input_status = st.selectbox('Status',[PagamentoRecuperado.status,'Pago','Pendente','Pago parcialmente'])
		input_evento = st.selectbox('Evento',eventoNome)
		input_contratante = st.selectbox("Contratante",contratanteNome)
		input_marca = st.selectbox("Marca",marcaNome)
		col1,col2,col3,col4,col5,col6,col7= st.columns(7)
		input_button_submit = col1.form_submit_button('Salvar')
		input_button_submit2 = col2.form_submit_button('Excluir')
	
	byNameEvento = EventoController.selecionarByName(input_evento)
	byNameContratante = ContratanteController.selecionarByName(input_contratante)
	byNameMarca = MarcaController.selecionarByName(input_marca)	

	if input_button_submit:
		PagamentoController.Alterar(Pagamento.pagamento(PagamentoRecuperado.id, input_value,input_forma,input_date,input_status,byNameEvento.id,byNameContratante.id,byNameMarca.id,input_parcela,input_entrada))
		st.success("Pagamento alterado com sucesso!")
	if input_button_submit2:
		PagamentoController.Excluir(byName.id)
		st.success("Pagamento excluído com sucesso!")