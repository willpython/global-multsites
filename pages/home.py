import streamlit as st
from textwrap import dedent

from core.adcash_engine import AdcashManager
from core.styles import inject_editorial_ui
from data.niches_config import NICHES_DATABASE


CATEGORY_UI = {
    "ai_tech": {
        "icon": "🤖",
        "color": "#6366F1",
        "soft_color": "#EEF2FF",
        "label": "IA & Tecnologia",
        "description": "Inovação e automação",
    },
    "business": {
        "icon": "🚀",
        "color": "#F97316",
        "soft_color": "#FFF7ED",
        "label": "Negócios Digitais",
        "description": "Ideias que escalam",
    },
    "personal_finance": {
        "icon": "💸",
        "color": "#16A34A",
        "soft_color": "#F0FDF4",
        "label": "Finanças Pessoais",
        "description": "Controle e escolhas",
    },
    "health_wellness": {
        "icon": "🌿",
        "color": "#0D9488",
        "soft_color": "#F0FDFA",
        "label": "Saúde & Bem-Estar",
        "description": "Rotina com equilíbrio",
    },
    "travel": {
        "icon": "✈️",
        "color": "#0284C7",
        "soft_color": "#F0F9FF",
        "label": "Viagens & Destinos",
        "description": "Planeje novas histórias",
    },
    "home_lifestyle": {
        "icon": "🏠",
        "color": "#D97706",
        "soft_color": "#FFFBEB",
        "label": "Casa & Lifestyle",
        "description": "Conforto no dia a dia",
    },
    "education_careers": {
        "icon": "🎓",
        "color": "#7C3AED",
        "soft_color": "#F5F3FF",
        "label": "Educação & Carreira",
        "description": "Aprenda e evolua",
    },
    "pets": {
        "icon": "🐾",
        "color": "#DB2777",
        "soft_color": "#FDF2F8",
        "label": "Pets & Animais",
        "description": "Cuidado e companhia",
    },
}


def select_category(slug: str) -> None:
    """Salva o nicho escolhido durante a sessão do visitante."""
    st.session_state.selected_niche = slug


def render_category_menu() -> None:
    """Renderiza cards de categorias usando HTML direto e botão transparente."""
    for index, slug in enumerate(NICHES_DATABASE.keys()):
        ui = CATEGORY_UI[slug]
        is_selected = st.session_state.selected_niche == slug

        state_class = "category-selected" if is_selected else ""
        intro_class = "category-intro-animation" if index == 0 else ""

        card_html = dedent(
            f"""
            <div class="category-card {state_class} {intro_class}"
                style="
                    --category-color: {ui['color']};
                    --category-soft-color: {ui['soft_color']};
                    --card-delay: {index * 0.08}s;
                ">
                <div class="category-card-icon">{ui['icon']}</div>

                <div class="category-card-copy">
                    <span class="category-card-title">{ui['label']}</span>
                    <span class="category-card-description">
                        {ui['description']}
                    </span>
                </div>

                <span class="category-card-arrow">→</span>
            </div>
            """
        )

        # st.html renderiza o card como HTML nativo.
        st.html(card_html)

        # Botão invisível que recebe o clique sobre o card.
        st.button(
            f"Abrir categoria: {ui['label']}",
            key=f"category_button_{slug}",
            on_click=select_category,
            args=(slug,),
            use_container_width=True,
        )


if "selected_niche" not in st.session_state:
    st.session_state.selected_niche = "ai_tech"

inject_editorial_ui()

adcash_injected = AdcashManager.inject_autotag()

if st.secrets.get("ADCASH_DEBUG", False):
    st.caption(
        "AdCash diagnóstico: "
        f"enabled={AdcashManager.is_enabled()} | "
        f"injected={adcash_injected}"
    )

with st.sidebar:
    st.markdown(
        '<p class="brand-name">Global Multisites</p>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<p class="brand-caption">'
        'Conteúdo útil para descobrir, aprender e evoluir.'
        '</p>',
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="category-callout">
            <span class="category-callout-dot"></span>
            ESCOLHA ABAIXO UMA CATEGORIA
        </div>
        """,
        unsafe_allow_html=True,
    )

    render_category_menu()

    st.divider()
    st.caption("◈ Novos artigos e guias em cada categoria.")


selected_slug = st.session_state.selected_niche
current_niche = NICHES_DATABASE[selected_slug]
current_ui = CATEGORY_UI[selected_slug]

hero_text, hero_image = st.columns(
    [1.15, 0.85],
    gap="large",
    vertical_alignment="center",
)

with hero_text:
    st.markdown(
        f"""
        <div class="hero-category-pill"
            style="
                --category-color: {current_ui["color"]};
                --category-soft-color: {current_ui["soft_color"]};
            ">
            {current_ui["icon"]} {current_niche["badge"]}
        </div>
        """,
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

    st.button(
        "Explore os artigos abaixo ↓",
        key=f"explore_{selected_slug}",
        type="primary",
    )

with hero_image:
    st.image(
        current_niche["cover_image"],
        use_container_width=True,
        output_format="auto",
    )

st.markdown(
    f"""
    <h2 class="section-title">
        Artigos em destaque
        <span style="color: {current_ui["color"]};">·</span>
    </h2>
    """,
    unsafe_allow_html=True,
)

posts = current_niche["posts"]

for start in range(0, len(posts), 3):
    row_posts = posts[start:start + 3]

    columns = st.columns(
        3,
        gap="medium",
        vertical_alignment="top",
    )

    for column, post in zip(columns, row_posts):
        with column:
            with st.container(border=True):
                st.image(
                    post["image"],
                    use_container_width=True,
                    output_format="auto",
                )

                st.markdown(
                    f"""
                    <p class="article-category"
                       style="color: {current_ui["color"]};">
                        {post["category"]}
                    </p>
                    """,
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
                    f"""
                    <p class="article-meta">
                        ⏱ {post["read_time"]} de leitura
                    </p>
                    """,
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

st.divider()

footer_brand, footer_privacy, footer_terms, footer_contact = st.columns(
    [3.2, 1.45, 1.15, 0.9],
    vertical_alignment="center",
)

with footer_brand:
    st.caption(
        "© 2026 Global Multsites · Conteúdo editorial em múltiplos nichos."
    )

with footer_privacy:
    if st.button(
        "Privacidade",
        key="footer_privacy",
        use_container_width=True,
    ):
        st.switch_page("pages/privacy.py")

with footer_terms:
    if st.button(
        "Termos",
        key="footer_terms",
        use_container_width=True,
    ):
        st.switch_page("pages/terms.py")

with footer_contact:
    if st.button(
        "Contato",
        key="footer_contact",
        use_container_width=True,
    ):
        st.switch_page("pages/contact.py")

