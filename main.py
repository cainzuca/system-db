'''import streamlit as st
import Pages.Artista.Create as CreatePage
import Pages.AlterarArtista.alterar as AlterarPage
import Pages.CriarMarca.Create as CreateMarca
import Pages.AlterarMarca.alterar as AlterarMarca
import Pages.CriarContratante.Create as CreateContratante
import Pages.AlterarContratante.alterar as AlterarContratante
import Pages.CriarEvento.Create as CreateEvento
import Pages.AlterarEvento.alterar as AlterarEvento
import Pages.CriarPagamento.Create as CreatePagamento
import Pages.AlterarPagamento.alterar as AlterarPagamento




#.\streamlit\Scripts\Activate

st.sidebar.title('Menu')

page = st.sidebar.selectbox('Ir para',["Incluir artista","Alterar artista","Incluir marca","Alterar marca","Incluir contratante","Alterar contratante","Incluir evento","Alterar evento","Incluir pagamento","Alterar pagamento"])


if page == 'Incluir artista':
    CreatePage.IncluirArtista()
if page =='Alterar artista':
    AlterarPage.AlterarArtista()


if page =='Incluir marca':
    CreateMarca.IncluirMarca()
if page =='Alterar marca':
    AlterarMarca.AlterarMarca()


if page =='Incluir contratante':
    CreateContratante.IncluirContratante()    
if page =='Alterar contratante':
    AlterarContratante.AlterarContratante()


if page =='Incluir evento':
    CreateEvento.IncluirEvento()    
if page =='Alterar evento':
    AlterarEvento.AlterarEvento()


if page =='Incluir pagamento':
    CreatePagamento.IncluirPagamento()    
if page =='Alterar pagamento':
    AlterarPagamento.AlterarPagamento()
'''

import streamlit as st
import Pages.Artista.Create as CreatePage
import Pages.AlterarArtista.alterar as AlterarPage
import Pages.CriarMarca.Create as CreateMarca
import Pages.AlterarMarca.alterar as AlterarMarca
import Pages.CriarContratante.Create as CreateContratante
import Pages.AlterarContratante.alterar as AlterarContratante
import Pages.CriarEvento.Create as CreateEvento
import Pages.AlterarEvento.alterar as AlterarEvento
import Pages.CriarPagamento.Create as CreatePagamento
import Pages.AlterarPagamento.alterar as AlterarPagamento

#.\streamlit\Scripts\Activate

st.sidebar.title('Menu')

page = st.sidebar.selectbox('Ir para', [
    "Incluir artista", "Alterar artista", "Incluir marca", "Alterar marca",
    "Incluir contratante", "Alterar contratante", "Incluir evento",
    "Alterar evento", "Incluir pagamento", "Alterar pagamento", "Relatório"
])

if page == 'Incluir artista':
    CreatePage.IncluirArtista()
elif page == 'Alterar artista':
    AlterarPage.AlterarArtista()
elif page == 'Incluir marca':
    CreateMarca.IncluirMarca()
elif page == 'Alterar marca':
    AlterarMarca.AlterarMarca()
elif page == 'Incluir contratante':
    CreateContratante.IncluirContratante()
elif page == 'Alterar contratante':
    AlterarContratante.AlterarContratante()
elif page == 'Incluir evento':
    CreateEvento.IncluirEvento()
elif page == 'Alterar evento':
    AlterarEvento.AlterarEvento()
elif page == 'Incluir pagamento':
    CreatePagamento.IncluirPagamento()
elif page == 'Alterar pagamento':
    AlterarPagamento.AlterarPagamento()
elif page == 'Relatório':
    st.markdown(
        """
        <style>
        .iframe-container {
            position: relative;
            overflow: hidden;
            padding-top: 56.25%; /* 16:9 Aspect Ratio */
        }
        .iframe-container iframe {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            border: 0;
        }
        </style>
        <div class="iframe-container">
            <iframe src="https://lookerstudio.google.com/embed/reporting/42dad368-d7c1-4b55-a8b8-47dc0fb9e362/page/p_l09i8rv1hd" allowfullscreen></iframe>
        </div>
        """,
        unsafe_allow_html=True
    )
