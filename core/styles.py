import streamlit as st


def inject_editorial_ui() -> None:
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@600;700&display=swap');

        html, body, [class*="css"] {
            font-family: "DM Sans", sans-serif;
        }

        .stApp {
            background: #F8FAFC;
        }

        .block-container {
            max-width: 1240px;
            padding-top: 1.5rem;
            padding-bottom: 3rem;
        }

        [data-testid="stSidebar"] {
            background: #FFFFFF;
            border-right: 1px solid #E2E8F0;
        }

        .brand-name {
            color: #172033;
            font-family: "Playfair Display", serif;
            font-size: 1.9rem;
            font-weight: 700;
            margin: 0;
        }

        .brand-caption {
            color: #64748B;
            font-size: 0.9rem;
            margin: 0.2rem 0 1rem 0;
        }

        .eyebrow {
            color: #2563EB;
            font-size: 0.76rem;
            font-weight: 700;
            letter-spacing: 0.1em;
            text-transform: uppercase;
        }

        .hero-title {
            color: #172033;
            font-family: "Playfair Display", serif;
            font-size: clamp(2rem, 5vw, 3.4rem);
            font-weight: 700;
            line-height: 1.12;
            margin: 0.5rem 0 0.9rem;
        }

        .hero-description {
            color: #526075;
            font-size: 1.06rem;
            line-height: 1.7;
        }

        .section-title {
            color: #172033;
            font-size: 1.45rem;
            font-weight: 700;
            margin: 1.5rem 0 0.7rem;
        }

        .article-category {
            color: #2563EB;
            font-size: 0.75rem;
            font-weight: 700;
            letter-spacing: 0.07em;
            text-transform: uppercase;
        }

        .article-title {
            color: #172033;
            font-size: 1.15rem;
            font-weight: 700;
            line-height: 1.35;
            margin: 0.4rem 0;
        }

        .article-excerpt {
            color: #64748B;
            font-size: 0.93rem;
            line-height: 1.55;
            min-height: 4.4rem;
        }

        .article-meta {
            color: #94A3B8;
            font-size: 0.8rem;
            margin-top: 0.8rem;
        }
        .article-subtitle {
            color: #526075;
            font-size: 1.15rem;
            line-height: 1.7;
            margin-top: -0.4rem;
            margin-bottom: 1rem;
        }
        div.stButton > button {
            width: 100%;
            border-radius: 8px;
            border: 1px solid #2563EB;
            color: #FFFFFF;
            background: #2563EB;
            font-weight: 600;
        }

        div.stButton > button:hover {
            background: #1D4ED8;
            border-color: #1D4ED8;
        }
    </style>
    """, unsafe_allow_html=True)