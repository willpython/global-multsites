import streamlit as st


st.set_page_config(
    page_title="Global Multsites",
    page_icon="◈",
    layout="wide",
    initial_sidebar_state="expanded",
)

home_page = st.Page(
    "pages/home.py",
    title="Início",
    icon=":material/home:",
    default=True,
)

article_page = st.Page(
    "pages/article.py",
    title="Artigo",
    icon=":material/article:",
    url_path="artigo",
)

privacy_page = st.Page(
    "pages/privacy.py",
    title="Política de Privacidade",
    icon=":material/privacy_tip:",
    url_path="privacidade",
)

terms_page = st.Page(
    "pages/terms.py",
    title="Termos de Uso",
    icon=":material/gavel:",
    url_path="termos",
)

contact_page = st.Page(
    "pages/contact.py",
    title="Contato",
    icon=":material/contact_mail:",
    url_path="contato",
)

pg = st.navigation(
    [
        home_page,
        article_page,
        privacy_page,
        terms_page,
        contact_page,
    ],
    position="hidden",
)

pg.run()