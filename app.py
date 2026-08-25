import streamlit as st

st.set_page_config(
    page_title="Global Multisites",
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

pg = st.navigation(
    [home_page, article_page],
    position="hidden",
)

pg.run()