import streamlit as st
import streamlit.components.v1 as components

class AdcashManager:
    """Gerenciador central de injeção de scripts e zonas Adcash."""

    @staticmethod
    def inject_verification_or_autotag(zone_script_url: str):
        """
        Injeta o script global (Autotag / Pop-under / Interstitial) 
        executando no escopo da página pai (window.top).
        """
        raw_code = f"""
        <script type="text/javascript">
            (function() {{
                var d = window.top.document;
                var s = d.createElement('script');
                s.type = 'text/javascript';
                s.async = true;
                s.src = '{zone_script_url}';
                d.getElementsByTagName('head')[0].appendChild(s);
            }})();
        </script>
        """
        components.html(raw_code, height=0, width=0)

    @staticmethod
    def render_display_banner(zone_id: str, width: int = 728, height: int = 90):
        """
        Renderiza banners de display Adcash (ex: 728x90 Leaderboard, 300x250 Medium Rectangle).
        """
        banner_html = f"""
        <div style="display:flex; justify-content:center; align-items:center; width:100%;">
            <script type="text/javascript">
                aclib.runBanner({{
                    zoneId: '{zone_id}',
                    maxHeight: {height},
                    maxWidth: {width}
                }});
            </script>
        </div>
        """
        components.html(banner_html, width=width, height=height)