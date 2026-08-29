import streamlit as st


st.title("Contato")
st.caption("Fale com a equipe do Global Multsites")

st.markdown("""
Use este canal para dúvidas gerais, sugestões, correções editoriais,
solicitações relacionadas à privacidade, denúncias de abuso ou assuntos
comerciais.

Não envie senhas, tokens, documentos de identificação, dados bancários ou
qualquer outra informação sensível por este formulário.
""")

with st.form("contact_form", clear_on_submit=True):
    name = st.text_input("Nome", max_chars=100)
    email = st.text_input("E-mail", max_chars=150)
    subject = st.selectbox(
        "Assunto",
        [
            "Dúvida geral",
            "Sugestão ou correção editorial",
            "Privacidade e dados pessoais",
            "Denúncia de abuso",
            "Parceria ou assunto comercial",
            "Outro",
        ],
    )
    message = st.text_area("Mensagem", max_chars=2000, height=180)
    submitted = st.form_submit_button("Enviar mensagem", use_container_width=True)

if submitted:
    if not name.strip() or not email.strip() or not message.strip():
        st.error("Preencha nome, e-mail e mensagem antes de enviar.")
    elif "@" not in email or "." not in email.rsplit("@", 1)[-1]:
        st.error("Informe um endereço de e-mail válido.")
    else:
        st.success(
            "Mensagem registrada localmente na interface. "
            "A integração de envio será adicionada em uma próxima etapa."
        )
        st.info(
            "Importante: este formulário ainda não envia e-mails nem armazena "
            "mensagens em um banco de dados."
        )

st.divider()

if st.button("Ler Política de Privacidade", use_container_width=True):
    st.switch_page("pages/privacy.py")