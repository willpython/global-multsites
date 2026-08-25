# Global Multsites

> Uma plataforma editorial multi-nicho construída com Streamlit para publicar conteúdo temático, organizar artigos em Markdown e exibir blocos de monetização de forma centralizada.

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-A%20definir-lightgrey)](#licença)

## Visão geral

O **Global Multsites** é a base de uma rede de sites de conteúdo orientada a nichos. O projeto concentra, em uma única aplicação, a configuração de temas editoriais, a renderização de artigos em Markdown, uma experiência de leitura responsiva e pontos preparados para monetização com **AdCash**.

A arquitetura separa claramente apresentação, páginas, conteúdo e configurações de nicho. Isso facilita a expansão para novos verticais, a inclusão de artigos e a evolução do motor de geração/publicação sem acoplar regras de negócio à interface.

## Principais recursos

- **Estrutura multi-nicho**: configurações centralizadas em `data/niches_config.py` para sustentar múltiplos sites/verticais temáticos.
- **Conteúdo em Markdown**: artigos organizados no diretório `content/articles/`, com um template reutilizável para padronização editorial.
- **Leitura de artigos**: página dedicada para renderização de conteúdo e navegação de retorno à listagem.
- **Página inicial editorial**: área de destaque, seleção de nichos, busca e cards de artigos.
- **Monetização desacoplada**: módulo próprio para exibição de anúncios AdCash em áreas como sidebar e conteúdo.
- **Design centralizado**: estilos CSS encapsulados em `core/styles.py` e configuração visual do Streamlit em `.streamlit/config.toml`.
- **Base extensível**: módulos reservados para geração de conteúdo e novos mecanismos de publicação.

## Arquitetura

```text
.
├── .streamlit/
│   └── config.toml              # Tema e configurações da aplicação Streamlit
├── content/
│   ├── articles/                # Artigos publicados em Markdown
│   └── ARTICLE_TEMPLATE.md       # Modelo editorial para novos artigos
├── core/
│   ├── adcash_engine.py          # Integração/renderização de blocos AdCash
│   ├── generator.py              # Espaço para o motor de geração de conteúdo
│   └── styles.py                 # Estilos globais e componentes visuais
├── data/
│   └── niches_config.py          # Catálogo e configurações dos nichos
├── pages/
│   ├── article.py                # Experiência de leitura de artigo
│   └── home.py                   # Home, busca, nichos e cards editoriais
├── app.py                         # Ponto de entrada da aplicação
├── requirements.txt               # Dependências Python
└── README.md
```

## Como funciona

O fluxo principal é simples e preparado para escala editorial:

1. O catálogo de nichos é definido em `data/niches_config.py`.
2. Cada conteúdo é criado a partir de `content/ARTICLE_TEMPLATE.md` e salvo em `content/articles/`.
3. A página `pages/home.py` apresenta os artigos, filtros e mecanismos de descoberta.
4. Ao selecionar um item, `pages/article.py` renderiza o artigo para leitura.
5. `core/adcash_engine.py` injeta os blocos de monetização nos pontos definidos pela interface.

## Pré-requisitos

- Python 3.10 ou superior
- `pip`
- Git

## Instalação

```bash
git clone https://github.com/willpython/global-multsites.git
cd global-multsites
```

Crie e ative um ambiente virtual:

```bash
python -m venv .venv
```

**Windows (PowerShell):**

```powershell
.\.venv\Scripts\Activate.ps1
```

**macOS/Linux:**

```bash
source .venv/bin/activate
```

Instale as dependências do projeto:

```bash
pip install -r requirements.txt
```

## Execução local

Inicie a aplicação pelo Streamlit:

```bash
streamlit run app.py
```

O Streamlit exibirá, no terminal, o endereço local para abrir a aplicação no navegador — normalmente `http://localhost:8501`.

## Publicação de conteúdo

### 1. Crie um artigo

Duplique o template:

```bash
cp content/ARTICLE_TEMPLATE.md content/articles/meu-novo-artigo.md
```

No Windows PowerShell:

```powershell
Copy-Item content\ARTICLE_TEMPLATE.md content\articles\meu-novo-artigo.md
```

### 2. Preencha os metadados

Mantenha o padrão de front matter e de seções definido no template. Isso permite que a aplicação identifique dados como título, nicho, descrição, imagem e demais informações editoriais.

### 3. Relacione ao nicho

Caso necessário, atualize `data/niches_config.py` com a configuração do novo vertical: identidade, tema, categorias ou metadados usados pela interface.

### 4. Valide localmente

Execute `streamlit run app.py`, confira a listagem, a busca e a página de leitura antes de publicar as alterações.

## Monetização com AdCash

A camada de anúncios está isolada em `core/adcash_engine.py`. Essa organização permite centralizar códigos de placement e reaproveitar os blocos de monetização em diferentes páginas sem poluir os componentes de interface.

Antes de colocar o projeto em produção:

- Cadastre e valide seus placements no painel da AdCash.
- Revise os identificadores e scripts utilizados pelo motor de anúncios.
- Teste a renderização em desktop e mobile.
- Garanta conformidade com políticas de privacidade, consentimento de cookies e regras da plataforma de anúncios aplicáveis ao seu público.

## Personalização visual

A identidade visual está distribuída em dois pontos principais:

| Local | Responsabilidade |
|---|---|
| `.streamlit/config.toml` | Configurações globais do Streamlit, incluindo tema e aparência-base. |
| `core/styles.py` | CSS e estilos de componentes, cards, tipografia, espaçamentos e experiência de leitura. |

Para criar uma identidade própria para um nicho, mantenha as regras globais em `styles.py` e concentre os dados específicos do vertical em `niches_config.py`.

## Roadmap sugerido

- [ ] Implementar o motor em `core/generator.py` para geração assistida de artigos.
- [ ] Adicionar validação de front matter e metadados obrigatórios.
- [ ] Criar indexação e paginação para catálogos maiores de conteúdo.
- [ ] Incluir testes automatizados para leitura, filtros e parsing de Markdown.
- [ ] Integrar analytics, SEO técnico e sitemap.
- [ ] Adicionar pipeline de CI para lint, testes e deploy.
- [ ] Configurar gerenciamento seguro de segredos por ambiente.

## Boas práticas de produção

- Não versione chaves, tokens ou scripts privados diretamente no repositório.
- Use `st.secrets` no Streamlit Cloud ou variáveis de ambiente no ambiente de hospedagem.
- Valide o conteúdo Markdown antes da publicação para evitar links quebrados e metadados incompletos.
- Monitore desempenho, Core Web Vitals e métricas de monetização por nicho.
- Mantenha política de privacidade, termos de uso e mecanismos de consentimento atualizados.

## Contribuição

Contribuições são bem-vindas. Para propor uma melhoria:

1. Faça um fork do repositório.
2. Crie uma branch descritiva: `git checkout -b feat/minha-melhoria`.
3. Implemente e teste a alteração localmente.
4. Faça commits claros e objetivos.
5. Abra um Pull Request descrevendo o problema, a solução e como validar a mudança.

## Licença

A licença ainda não está definida no repositório. Antes de disponibilizar o projeto publicamente para uso ou distribuição, adicione um arquivo `LICENSE` com os termos escolhidos — por exemplo, MIT, Apache-2.0 ou uma licença proprietária.

---

Desenvolvido para transformar nichos editoriais em experiências de conteúdo organizadas, escaláveis e preparadas para monetização.