import streamlit as st
import controllers.PagamentoController as PagamentoController
import models.Pagamento as Pagamento
import pandas as pd
import services.database as db
import controllers.ContratanteController as ContratanteController
import controllers.EventoController as EventoController
import controllers.MarcaController as MarcaController
from datetime import datetime	
 

def IncluirPagamento():	
	eventoNome = []
	for item in EventoController.selecionarTodos():
		eventoNome.append(item.nome)

	contratanteNome = []
	for item in ContratanteController.selecionarTodos():
		contratanteNome.append(item.nome)

	marcaNome = []
	for item in MarcaController.selecionarTodos():
		marcaNome.append(item.nome)

	st.title('Nova Pagamento')

	col1, col2,col3 = st.columns(3)
	input_forma = col1.selectbox("Forma",['Débito','Crédito','Pix','Dinheiro'])	

	with st.form(key='include_cliente'):
		input_valor = st.number_input(label='Valor do pagamento')
		if input_forma == "Crédito":
			input_parcela = col2.selectbox("Parcelas",['1x','2x','3x','4x','5x','6x'])
			input_entrada = col3.number_input(label='Entrada',format='%d',step=1)
		input_data = st.date_input(label='Data', format= 'DD/MM/YYYY', min_value=datetime(1990, 1, 1))
		input_status = st.selectbox("Status",['Pago','Pendente','Pago parcialmente'])
		input_event = st.selectbox("Evento",eventoNome)
		input_contratante = st.selectbox("Contratante",contratanteNome)
		input_marca = st.selectbox("Marca",marcaNome)					
		input_button_submit = st.form_submit_button('Salvar')
	
	st.text(input_forma)

	byNameEvento = EventoController.selecionarByName(input_event)
	byNameContratante = ContratanteController.selecionarByName(input_contratante)
	byNameMarca = MarcaController.selecionarByName(input_marca)

	if input_button_submit:
		PagamentoController.incluir(Pagamento.pagamento(0,input_valor, input_forma, input_data,input_status,byNameEvento.id,byNameContratante.id,byNameMarca.id,input_parcela, input_entrada))
		st.success("Pagamento incluido com sucesso!")

	st.markdown("""---""")



		
		
'''pagamento = []
	for item in PagamentoController.selecionarTodos():
		pagamento.append([item.nome,item.idade])'''

'''	db.cursor.execute("SELECT* FROM pagamento")
	rows = db.cursor.fetchall()
	df = pd.DataFrame.from_records(rows, columns=[desc[0] for desc in db.cursor.description])

	st.dataframe(df)
'''