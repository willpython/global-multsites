import streamlit as st

from core.styles import inject_editorial_ui
from data.niches_config import NICHES_DATABASE
from pathlib import Path

inject_editorial_ui()


def get_post(niche_slug: str, post_slug: str) -> tuple[dict | None, dict | None]:
    """Encontra um post pelo nicho e slug."""
    niche = NICHES_DATABASE.get(niche_slug)

    if not niche:
        return None, None

    post = next(
        (
            item
            for item in niche["posts"]
            if item.get("slug") == post_slug
        ),
        None,
    )

    return niche, post

def load_article_markdown(
    niche_slug: str,
    article_slug: str,
) -> str | None:
    article_path = (
        Path("content")
        / "articles"
        / niche_slug
        / f"{article_slug}.md"
    )

    if not article_path.exists():
        return None

    return article_path.read_text(encoding="utf-8")


niche_slug = st.query_params.get("nicho", "")
post_slug = st.query_params.get("slug", "")

niche, post = get_post(niche_slug, post_slug)

if not niche or not post:
    st.error("Artigo não encontrado ou link inválido.")

    if st.button("Voltar para a página inicial"):
        st.switch_page("pages/home.py")

    st.stop()


left, center, right = st.columns([1, 4, 1])

with center:
    st.divider()
    if st.button("← Voltar para os artigos"):
        st.switch_page("pages/home.py")

    st.markdown(
    f'<p class="article-category">{niche["badge"]} · {post["category"]}</p>',
    unsafe_allow_html=True,
    )

    st.title(post["title"])

    st.markdown(
        f'<p class="article-subtitle">{post["subtitle"]}</p>',
        unsafe_allow_html=True,
    )

    author = post.get("author", "Equipe Global Multisites")
    published_at = post.get("published_at", "Em breve")
    updated_at = post.get("updated_at", published_at)

    st.caption(
        f"Por {author} · Publicado em {published_at} · "
        f"Atualizado em {updated_at} · ⏱ {post['read_time']} de leitura"
    )

    st.image(
        post["image"],
        caption=post["alt"],
        use_container_width=True,
    )

    st.divider()

    article_content = load_article_markdown(niche_slug, post["slug"])

    if article_content:
        st.markdown(article_content)
    else:
        st.info(
            "Este artigo está em preparação. "
            "Em breve teremos o conteúdo completo."
        )