import streamlit as st


st.title("Termos de Uso")
st.caption("Última atualização: 28 de agosto de 2026")

st.markdown("""
Ao acessar ou utilizar o **Global Multsites**, você concorda com estes Termos
de Uso. Caso não concorde, recomendamos que não utilize a plataforma.

## 1. Finalidade do conteúdo

O Global Multsites publica conteúdos informativos e editoriais em diferentes
nichos. Os materiais possuem caráter geral e não constituem aconselhamento
profissional, jurídico, médico, financeiro ou de qualquer outra natureza
especializada.

Antes de tomar decisões com impacto pessoal, profissional ou financeiro,
consulte um profissional habilitado.

## 2. Uso permitido

Você pode acessar, ler e compartilhar links dos conteúdos para fins lícitos e
pessoais. É proibido:

- Usar a plataforma para atividades ilegais, fraudulentas ou abusivas
- Tentar interferir na segurança, disponibilidade ou funcionamento do site
- Copiar, reproduzir ou redistribuir conteúdo protegido sem autorização
- Remover avisos de autoria, direitos ou referências presentes no conteúdo
- Utilizar robôs, scrapers ou automações de forma que prejudique o serviço
- Manipular cliques, impressões, tráfego ou publicidade exibida no site

## 3. Publicidade e links externos

O site pode apresentar publicidade de terceiros, inclusive por meio da rede
AdCash, e links para recursos externos. Não controlamos integralmente o
conteúdo, a disponibilidade, os produtos, os serviços ou as políticas desses
terceiros.

Interações com anúncios e sites externos são de responsabilidade do usuário,
observadas as condições dos respectivos fornecedores.

## 4. Propriedade intelectual

Textos, elementos visuais, marca, identidade e código do Global Multsites
são protegidos pelas normas aplicáveis de propriedade intelectual, salvo
quando houver indicação diferente. Nenhuma disposição destes termos concede
licença sobre esses direitos além do uso pessoal e legítimo do site.

## 5. Disponibilidade e alterações

Podemos modificar, atualizar, suspender ou descontinuar conteúdos,
funcionalidades e páginas a qualquer momento, sem garantia de disponibilidade
contínua ou livre de erros.

## 6. Limitação de responsabilidade

Na máxima extensão permitida pela legislação aplicável, o Global Multsites
não se responsabiliza por decisões tomadas exclusivamente com base em seus
conteúdos, indisponibilidades temporárias, danos decorrentes de serviços de
terceiros ou uso inadequado da plataforma.

## 7. Privacidade

O tratamento de informações relacionadas ao uso da plataforma é descrito na
Política de Privacidade.

## 8. Atualizações e contato

Estes termos podem ser atualizados periodicamente. Dúvidas sobre estes
Termos de Uso podem ser encaminhadas pela página de contato.
""")

col1, col2 = st.columns(2)

with col1:
    if st.button("Política de Privacidade", use_container_width=True):
        st.switch_page("pages/privacy.py")

with col2:
    if st.button("Ir para Contato", use_container_width=True):
        st.switch_page("pages/contact.py")