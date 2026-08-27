import streamlit as st


def inject_editorial_ui() -> None:
    st.markdown(
        """
        <style>
            @import url(
                'https://fonts.googleapis.com/css2?'
                'family=DM+Sans:wght@400;500;600;700;800&'
                'family=Playfair+Display:wght@600;700&display=swap'
            );

            /* =========================
               BASE GLOBAL DO PORTAL
               ========================= */

            html,
            body,
            [class*="css"] {
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

            [data-testid="stSidebar"] .block-container {
                padding-top: 1.55rem;
                padding-bottom: 2rem;
            }

            .brand-name {
                margin: 0;
                color: #172033;
                font-family: "Playfair Display", serif;
                font-size: 1.9rem;
                font-weight: 700;
                letter-spacing: -0.03em;
            }

            .brand-caption {
                margin: 0.25rem 0 0;
                color: #64748B;
                font-size: 0.88rem;
                line-height: 1.5;
            }

            .eyebrow {
                margin-bottom: 0.35rem;
                color: #2563EB;
                font-size: 0.76rem;
                font-weight: 800;
                letter-spacing: 0.1em;
                text-transform: uppercase;
            }

            .hero-title {
                margin: 0.55rem 0 0.9rem;
                color: #172033;
                font-family: "Playfair Display", serif;
                font-size: clamp(2rem, 5vw, 3.4rem);
                font-weight: 700;
                letter-spacing: -0.035em;
                line-height: 1.12;
            }

            .hero-description {
                max-width: 640px;
                color: #526075;
                font-size: 1.06rem;
                line-height: 1.75;
            }

            .section-title {
                margin: 1.85rem 0 0.85rem;
                color: #172033;
                font-size: 1.45rem;
                font-weight: 800;
                letter-spacing: -0.02em;
            }

            .article-category {
                margin: 0.8rem 0 0;
                color: #2563EB;
                font-size: 0.75rem;
                font-weight: 800;
                letter-spacing: 0.07em;
                text-transform: uppercase;
            }

            .article-title {
                margin: 0.4rem 0;
                color: #172033;
                font-size: 1.12rem;
                font-weight: 800;
                line-height: 1.35;
            }

            .article-excerpt {
                min-height: 4.4rem;
                margin: 0.45rem 0;
                color: #64748B;
                font-size: 0.93rem;
                line-height: 1.6;
            }

            .article-meta {
                margin-top: 0.85rem;
                color: #94A3B8;
                font-size: 0.8rem;
                font-weight: 600;
            }

            .article-subtitle {
                margin-top: -0.35rem;
                margin-bottom: 1rem;
                color: #526075;
                font-size: 1.15rem;
                line-height: 1.7;
            }

            /* =========================
               BOTÕES GERAIS
               ========================= */

            div.stButton > button {
                border: 1px solid #2563EB;
                border-radius: 9px;
                color: #FFFFFF;
                background: #2563EB;
                font-weight: 700;
                transition:
                    transform 0.2s ease,
                    box-shadow 0.2s ease,
                    background 0.2s ease;
            }

            div.stButton > button:hover {
                border-color: #1D4ED8;
                background: #1D4ED8;
                box-shadow: 0 8px 16px -10px rgba(37, 99, 235, 0.8);
                transform: translateY(-1px);
            }

            div.stButton > button:focus-visible {
                outline: 3px solid rgba(37, 99, 235, 0.25);
                outline-offset: 2px;
            }

            /* =========================
               HERO: PILULA DE CATEGORIA
               ========================= */

            .hero-category-pill {
                display: inline-flex;
                align-items: center;
                gap: 0.42rem;
                margin-bottom: 0.35rem;
                padding: 0.42rem 0.78rem;
                border: 1px solid color-mix(
                    in srgb,
                    var(--category-color) 30%,
                    #FFFFFF
                );
                border-radius: 999px;
                color: var(--category-color);
                background: var(--category-soft-color);
                font-size: 0.76rem;
                font-weight: 800;
                letter-spacing: 0.06em;
            }

            /* =====================================
               SIDEBAR: CHAMADA PARA AS CATEGORIAS
               ===================================== */

            .category-callout {
                display: flex;
                align-items: center;
                gap: 0.55rem;
                margin: 1rem 0 0.45rem;
                padding: 0.78rem 0.82rem;
                border: 1px solid #DBEAFE;
                border-radius: 13px;
                color: #1E3A5F;
                background: linear-gradient(
                    135deg,
                    #EFF6FF 0%,
                    #F8FAFC 100%
                );
                font-size: 0.82rem;
                font-weight: 800;
                animation: callout-float 3.2s ease-in-out infinite;
            }

            .category-callout-dot {
                width: 9px;
                height: 9px;
                flex: 0 0 9px;
                border-radius: 99px;
                background: #2563EB;
                box-shadow: 0 0 0 0 rgba(37, 99, 235, 0.45);
                animation: callout-pulse 1.9s infinite;
            }

            /* ====================================
               SIDEBAR: CARDS FLUTUANTES DE NICHO
               ==================================== */

            .category-card {
                display: flex;
                align-items: center;
                position: relative;
                gap: 0.7rem;
                min-height: 58px;
                margin-top: 0.52rem;
                padding: 0.62rem 0.7rem;
                overflow: hidden;
                border: 1px solid color-mix(
                    in srgb,
                    var(--category-color) 20%,
                    #FFFFFF
                );
                border-radius: 15px;
                color: #172033;
                background: linear-gradient(
                    135deg,
                    var(--category-soft-color) 0%,
                    #FFFFFF 82%
                );
                pointer-events: none;
                transform: translateY(0);
                transition:
                    transform 0.25s ease,
                    box-shadow 0.25s ease,
                    border-color 0.25s ease;
                animation: card-enter 0.42s ease both;
                animation-delay: var(--card-delay);
            }

            .category-card::before {
                position: absolute;
                top: -35px;
                right: -36px;
                width: 95px;
                height: 95px;
                border-radius: 50%;
                background: var(--category-color);
                content: "";
                opacity: 0.08;
            }

            .category-card::after {
                position: absolute;
                top: 0;
                left: -115%;
                width: 55%;
                height: 100%;
                background: linear-gradient(
                    105deg,
                    transparent 0%,
                    rgba(255, 255, 255, 0.68) 50%,
                    transparent 100%
                );
                content: "";
                transform: skewX(-18deg);
                transition: left 0.65s ease;
            }

            .category-card-icon {
                display: grid;
                width: 40px;
                height: 40px;
                flex: 0 0 40px;
                position: relative;
                z-index: 1;
                place-items: center;
                border: 1px solid rgba(15, 23, 42, 0.05);
                border-radius: 12px;
                background: #FFFFFF;
                box-shadow: 0 5px 14px rgba(15, 23, 42, 0.09);
                font-size: 1.35rem;
                animation: icon-float 3s ease-in-out infinite;
            }

            .category-card-copy {
                display: flex;
                min-width: 0;
                flex: 1;
                flex-direction: column;
                position: relative;
                z-index: 1;
            }

            .category-card-title {
                overflow: hidden;
                color: #172033;
                font-size: 0.82rem;
                font-weight: 800;
                line-height: 1.15;
                text-overflow: ellipsis;
                white-space: nowrap;
            }

            .category-card-description {
                overflow: hidden;
                margin-top: 0.14rem;
                color: #64748B;
                font-size: 0.69rem;
                font-weight: 600;
                text-overflow: ellipsis;
                white-space: nowrap;
            }

            .category-card-arrow {
                position: relative;
                z-index: 1;
                color: var(--category-color);
                font-size: 1.16rem;
                font-weight: 900;
                transform: translateX(0);
                transition: transform 0.25s ease;
            }

            .category-selected {
                border: 2px solid var(--category-color);
                box-shadow: 0 12px 24px -14px var(--category-color);
                animation: selected-card-pulse 2.4s ease-in-out infinite;
            }

            .category-selected .category-card-icon {
                background: var(--category-color);
                box-shadow: 0 7px 18px color-mix(
                    in srgb,
                    var(--category-color) 35%,
                    transparent
                );
            }

            .category-selected .category-card-title,
            .category-selected .category-card-arrow {
                color: var(--category-color);
            }

            .category-intro-animation {
                animation:
                    card-enter 0.42s ease both,
                    category-invite 2.8s ease-in-out 1.3s infinite;
                animation-delay:
                    var(--card-delay),
                    1.3s;
            }

            /*
            O botão Streamlit é transparente e fica sobre o card,
            mantendo clique, teclado e acessibilidade nativos.
            */

            [data-testid="stSidebar"] div.stButton {
                position: relative;
                z-index: 4;
                margin-top: -58px;
                margin-bottom: 0.52rem;
                min-height: 58px;
            }

            [data-testid="stSidebar"] div.stButton > button {
                width: 100%;
                min-height: 58px;
                padding: 0;
                border: 0 !important;
                border-radius: 15px;
                color: transparent !important;
                background: transparent !important;
                box-shadow: none !important;
                font-size: 0;
                cursor: pointer;
            }

            [data-testid="stSidebar"] div.stButton > button:hover,
            [data-testid="stSidebar"] div.stButton > button:focus-visible {
                border: 2px solid var(--category-color, #2563EB);
                outline: none;
                background: transparent;
                box-shadow: 0 0 0 4px rgba(37, 99, 235, 0.14);
            }

            [data-testid="stSidebar"] div.stButton:hover {
                transform: translateY(-3px);
            }

            /* =========================
               ANIMAÇÕES
               ========================= */

            @keyframes card-enter {
                from {
                    opacity: 0;
                    transform: translateX(-12px);
                }

                to {
                    opacity: 1;
                    transform: translateX(0);
                }
            }

            @keyframes icon-float {
                0%,
                100% {
                    transform: translateY(0) rotate(0deg);
                }

                50% {
                    transform: translateY(-2px) rotate(-3deg);
                }
            }

            @keyframes selected-card-pulse {
                0%,
                100% {
                    transform: translateX(0);
                    box-shadow: 0 12px 24px -14px var(--category-color);
                }

                50% {
                    transform: translateX(3px);
                    box-shadow: 0 14px 28px -12px var(--category-color);
                }
            }

            @keyframes category-invite {
                0%,
                100% {
                    transform: translateX(0);
                }

                50% {
                    transform: translateX(4px);
                }
            }

            @keyframes callout-pulse {
                0% {
                    box-shadow: 0 0 0 0 rgba(37, 99, 235, 0.45);
                }

                70% {
                    box-shadow: 0 0 0 8px rgba(37, 99, 235, 0);
                }

                100% {
                    box-shadow: 0 0 0 0 rgba(37, 99, 235, 0);
                }
            }

            @keyframes callout-float {
                0%,
                100% {
                    transform: translateY(0);
                }

                50% {
                    transform: translateY(-2px);
                }
            }

            /* =========================
               RESPONSIVIDADE E ACESSO
               ========================= */

            @media (max-width: 768px) {
                .block-container {
                    padding-top: 1rem;
                    padding-right: 1rem;
                    padding-left: 1rem;
                }

                .hero-title {
                    font-size: 2.2rem;
                }

                .article-excerpt {
                    min-height: auto;
                }
            }

            @media (prefers-reduced-motion: reduce) {
                *,
                *::before,
                *::after {
                    scroll-behavior: auto !important;
                }

                .category-callout,
                .category-callout-dot,
                .category-card,
                .category-card-icon,
                .category-selected,
                .category-intro-animation {
                    animation: none !important;
                    transition: none !important;
                }
            }
        </style>
        """,
        unsafe_allow_html=True,
    )