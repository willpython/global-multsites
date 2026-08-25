import streamlit as st

from core.styles import inject_editorial_ui
from data.niches_config import NICHES_DATABASE


st.set_page_config(
    page_title="Global Multisites",
    page_icon="◈",
    layout="wide",
    initial_sidebar_state="expanded",
)

inject_editorial_ui()

with st.sidebar:
    st.markdown('<p class="brand-name">Global Multisites</p>', unsafe_allow_html=True)
    st.markdown(
        '<p class="brand-caption">Conteúdo útil para descobrir, aprender e evoluir.</p>',
        unsafe_allow_html=True,
    )

    st.divider()

    selected_slug = st.selectbox(
        "Explore uma categoria",
        options=list(NICHES_DATABASE.keys()),
        format_func=lambda slug: NICHES_DATABASE[slug]["title"],
        index=0,
    )

    st.divider()
    st.caption("Novos conteúdos selecionados regularmente.")

current_niche = NICHES_DATABASE[selected_slug]

# Hero editorial: 55% texto / 45% imagem
hero_text, hero_image = st.columns([1.15, 0.85], gap="large", vertical_alignment="center")

with hero_text:
    st.markdown(
        f'<div class="eyebrow">{current_niche["badge"]}</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        f'<h1 class="hero-title">{current_niche["title"]}</h1>',
        unsafe_allow_html=True,
    )
    st.markdown(
        f'<p class="hero-description">{current_niche["description"]}</p>',
        unsafe_allow_html=True,
    )
    st.button("Explorar conteúdos", type="primary", use_container_width=False)

with hero_image:
    st.image(
        current_niche["cover_image"],
        use_container_width=True,
        output_format="auto",
    )

st.markdown('<h2 class="section-title">Artigos em destaque</h2>', unsafe_allow_html=True)

posts = current_niche["posts"]

# Três colunas, que viram blocos verticais automaticamente no mobile.
for start in range(0, len(posts), 3):
    row_posts = posts[start:start + 3]
    columns = st.columns(3, gap="medium", vertical_alignment="top")

    for column, post in zip(columns, row_posts):
        with column:
            with st.container(border=True):
                st.image(
                    post["image"],
                    use_container_width=True,
                    output_format="auto",
                )
                st.markdown(
                    f'<p class="article-category">{post["category"]}</p>',
                    unsafe_allow_html=True,
                )
                st.markdown(
                    f'<p class="article-title">{post["title"]}</p>',
                    unsafe_allow_html=True,
                )
                st.markdown(
                    f'<p class="article-excerpt">{post["excerpt"]}</p>',
                    unsafe_allow_html=True,
                )
                st.markdown(
                    f'<p class="article-meta">⏱ {post["read_time"]} de leitura</p>',
                    unsafe_allow_html=True,
                )
                if st.button(
                    "Ler artigo",
                    key=f"article_{selected_slug}_{post['slug']}",
                    use_container_width=True,
                ):
                    st.switch_page(
                        "pages/article.py",
                        query_params={
                            "nicho": selected_slug,
                            "slug": post["slug"],
                        },
                    )