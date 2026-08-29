import streamlit as st


st.title("Política de Privacidade")
st.caption("Última atualização: 28 de agosto de 2026")

st.markdown("""
Esta Política de Privacidade descreve como o **Global Multsites** coleta,
utiliza e protege informações quando você navega em nossos sites e conteúdos.

## 1. Informações coletadas

Podemos coletar informações técnicas de navegação, como endereço IP, tipo de
dispositivo, navegador, páginas acessadas, data, horário e interações com o
conteúdo. Esses dados podem ser coletados diretamente por tecnologias da
plataforma de hospedagem ou por parceiros de publicidade e medição.

Não solicitamos dados pessoais sensíveis para acesso ao conteúdo editorial.

## 2. Cookies e publicidade

Utilizamos cookies e tecnologias semelhantes para melhorar a navegação,
medir audiência, prevenir fraudes e viabilizar publicidade.

Este site pode exibir anúncios fornecidos por parceiros de publicidade,
incluindo a AdCash. Esses parceiros podem utilizar cookies, identificadores
ou tecnologias equivalentes para entregar anúncios, limitar frequência,
medir desempenho e combater tráfego inválido, conforme suas próprias
políticas de privacidade.

Você pode gerenciar cookies nas configurações do seu navegador. A desativação
de cookies pode afetar algumas funcionalidades e a personalização de anúncios.

## 3. Finalidades de uso

As informações podem ser utilizadas para:

- Operar, manter e melhorar o Global Multsites
- Entender a audiência e o desempenho dos conteúdos
- Detectar fraudes, abusos e incidentes de segurança
- Exibir, medir e otimizar publicidade
- Cumprir obrigações legais aplicáveis

## 4. Compartilhamento

Podemos compartilhar dados técnicos limitados com fornecedores que ajudam a
operar a plataforma, medir audiência, hospedar o serviço e veicular anúncios.
Esses fornecedores tratam dados conforme suas políticas e termos aplicáveis.

Não comercializamos dados pessoais diretamente a terceiros.

## 5. Retenção e segurança

Mantemos informações pelo período necessário às finalidades descritas nesta
política, obrigações legais e prevenção de fraudes. Adotamos medidas
razoáveis de segurança, mas nenhuma transmissão ou armazenamento digital é
totalmente isento de riscos.

## 6. Seus direitos

Conforme a legislação aplicável, incluindo a Lei Geral de Proteção de Dados
(LGPD), você pode solicitar informações sobre o tratamento de seus dados,
correção, anonimização, bloqueio, eliminação ou revisão de consentimentos,
quando aplicável.

## 7. Alterações nesta política

Esta política pode ser atualizada para refletir mudanças na plataforma,
parceiros, funcionalidades ou exigências legais. A data de atualização será
ajustada nesta página.

## 8. Contato

Para dúvidas, solicitações relacionadas à privacidade ou exercício de
direitos, use nossa página de contato.
""")

if st.button("Ir para Contato", use_container_width=True):
    st.switch_page("pages/contact.py")