import json
import re

import streamlit as st


class AdcashManager:
    """Gerencia o Autotag AdCash com configurações privadas por ambiente."""

    @staticmethod
    def _get_secret(key: str, default: str = "") -> str:
        """Lê um secret sem quebrar o app se ele ainda não estiver configurado."""
        try:
            return str(st.secrets.get(key, default)).strip()
        except Exception:
            return default

    @classmethod
    def is_enabled(cls) -> bool:
        """Retorna True somente quando a monetização estiver habilitada."""
        value = cls._get_secret("ADCASH_ENABLED", "false").lower()
        return value in {"1", "true", "yes", "on"}

    @classmethod
    def _get_zone_id(cls) -> str:
        """Obtém e valida o identificador da zona Autotag."""
        zone_id = cls._get_secret("ADCASH_AUTOTAG_ZONE_ID").lower()

        if re.fullmatch(r"[a-z0-9]{6,64}", zone_id):
            return zone_id

        return ""

    @classmethod
    def inject_autotag(cls) -> bool:
        """
        Carrega a biblioteca AdCash e executa uma zona Autotag uma vez por sessão.

        Retorna True quando o código foi solicitado para carregamento.
        """
        if not cls.is_enabled():
            return False

        zone_id = cls._get_zone_id()

        if not zone_id:
            return False

        session_key = "_adcash_autotag_injected"

        if st.session_state.get(session_key):
            return True

        payload = json.dumps({"zoneId": zone_id})

        script = f"""
        <script>
        (function () {{
            const zoneConfig = {payload};
            const libraryId = "global-multsites-adcash-library";

            function runAutotag() {{
                if (typeof window.aclib !== "undefined") {{
                    window.aclib.runAutoTag(zoneConfig);
                }}
            }}

            const existingLibrary = document.getElementById(libraryId);

            if (existingLibrary) {{
                if (typeof window.aclib !== "undefined") {{
                    runAutotag();
                }} else {{
                    existingLibrary.addEventListener("load", runAutotag, {{ once: true }});
                }}
                return;
            }}

            const library = document.createElement("script");
            library.id = libraryId;
            library.type = "text/javascript";
            library.async = true;
            library.src = "https://acscdn.com/script/aclib.js";
            library.addEventListener("load", runAutotag, {{ once: true }});
            document.head.appendChild(library);
        }})();
        </script>
        """

        st.html(
            script,
            unsafe_allow_javascript=True,
        )