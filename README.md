# 🌿 Nobre Turismo

**O extraordinário é natural.**

A Nobre Turismo é uma aplicação web desenvolvida com Django, voltada à apresentação e divulgação de experiências turísticas na região de Nobres, Mato Grosso.

O projeto busca proporcionar uma experiência digital intuitiva e visualmente agradável, permitindo que visitantes conheçam os atrativos naturais da região, explorem experiências turísticas e obtenham informações sobre os guias que acompanham as atividades.

Além da interface voltada aos visitantes, a aplicação conta com funcionalidades dinâmicas e um painel administrativo para facilitar o gerenciamento dos conteúdos.

---

## ✨ Funcionalidades

- **Página inicial:** apresentação da agência e dos atrativos turísticos.
- **Experiências turísticas:** exibição dinâmica de atividades e destinos disponíveis.
- **Guias turísticos:** apresentação dos profissionais responsáveis pelas experiências.
- **Autenticação de usuários:** funcionalidades de cadastro e login.
- **Área administrativa:** gerenciamento de conteúdos por meio do Django Admin.
- **Conteúdo dinâmico:** integração entre os dados cadastrados e sua apresentação nas páginas.
- **Design responsivo:** interface adaptável a diferentes tamanhos de tela.
- **Elementos visuais interativos:** utilização de imagens, vídeos, animações e componentes de navegação.

## 🛠️ Tecnologias utilizadas

| Tecnologia | Aplicação |
|---|---|
| Python | Linguagem principal do projeto |
| Django 5.2 | Framework para desenvolvimento web |
| HTML5 | Estruturação das páginas |
| CSS3 | Estilização e responsividade |
| JavaScript | Interatividade e funcionalidades do front-end |
| Bootstrap | Componentes e ícones |
| SQLite | Banco de dados, quando utilizada a configuração padrão do Django |

## 📁 Estrutura do projeto

```text
nobreturismo/
│
├── core/
│   ├── migrations/
│   ├── static/
│   │   ├── css/
│   │   ├── images/
│   │   ├── js/
│   │   └── medias/
│   │
│   ├── templates/
│   │
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── nobreturismo/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── manage.py
├── requirements.txt
└── README.md
```

*Observação: a estrutura acima apresenta a organização geral da aplicação.*

## 💻 Acesse o projeto

annajullyp.pythonanywhere.com


## 🚀 Como executar o projeto

### 1. Pré-requisitos

Antes de iniciar, certifique-se de possuir:

- Python 3.13 ou compatível com as dependências.
- Git.
- Pip (gerenciador de pacotes do Python).

### 2. Clone o repositório

```bash
git clone https://github.com/annajullyp/nobreturismo.git
```

Entre na pasta do projeto:

```bash
cd nobreturismo
```

### 3. Crie um ambiente virtual

```bash
python -m venv venv
```

Ative o ambiente virtual:

**Windows:**
```bash
venv\Scripts\activate
```

**Linux / macOS:**
```bash
source venv/bin/activate
```

### 4. Instale as dependências

```bash
pip install -r requirements.txt
```

### 5. Execute as migrações

```bash
python manage.py migrate
```

### 6. Crie um superusuário

Para acessar o painel administrativo do Django:

```bash
python manage.py createsuperuser
```

Informe o nome de usuário, e-mail e senha solicitados.

### 7. Inicie o servidor

```bash
python manage.py runserver
```

A aplicação estará disponível em:

```text
http://127.0.0.1:8000/
```

## 🔐 Painel administrativo

O projeto utiliza o Django Admin para permitir o gerenciamento dos conteúdos cadastrados na aplicação.

Após criar um superusuário, acesse:

```text
http://127.0.0.1:8000/admin/
```

Por meio do painel administrativo, é possível gerenciar os conteúdos disponibilizados nas páginas dinâmicas, como experiências turísticas e guias.

## 🎯 Objetivo do projeto

A Nobre Turismo foi desenvolvida como um projeto acadêmico, com o propósito de aplicar conhecimentos de desenvolvimento web utilizando Python e Django.

Durante seu desenvolvimento, são trabalhados conceitos como:

- Arquitetura de aplicações web com Django.
- Desenvolvimento de funcionalidades CRUD.
- Autenticação e gerenciamento de usuários.
- Utilização de templates e herança de templates.
- Integração entre front-end e back-end.
- Organização de arquivos estáticos e mídias.
- Gerenciamento de conteúdo por meio do Django Admin.

## 🤖 Inteligência Artificial e Ferramentas de Apoio

Durante o desenvolvimento da Nobre Turismo, foram utilizadas ferramentas de inteligência artificial para auxiliar em diferentes etapas do projeto, desde a construção da interface até a implementação e revisão de funcionalidades.

As ferramentas foram utilizadas como apoio ao processo de desenvolvimento, com análise, adaptação e aplicação das sugestões de acordo com as necessidades da aplicação.

| Ferramenta | Utilização |
|---|---|
| **Figma** | Desenvolvimento dos protótipos e definição do design visual das páginas. |
| **Claude** | Auxílio na construção e estilização das páginas, especialmente na elaboração dos códigos HTML e CSS. |
| **Google Gemini** | Suporte no desenvolvimento das estruturas da aplicação e na implementação de funcionalidades relacionadas à autenticação, como verificação de usuários logados, validação do login, controle de sessões e logout. |
| **ChatGPT** | Apoio na resolução de dúvidas, identificação e correção de problemas, explicação de conceitos e aprimoramento de detalhes técnicos durante o desenvolvimento. |

**Observação:** as ferramentas de IA foram utilizadas como recursos complementares, auxiliando no processo de aprendizagem e desenvolvimento da aplicação. As sugestões geradas foram avaliadas e adaptadas conforme os requisitos do projeto.

## 📽️ Vídeo Explicativo

https://drive.google.com/drive/folders/1oa7Vni30vJNnooOrZpeV7X3GHChXFrUj?usp=sharing


## 👩‍💻 Desenvolvedora

**Anna Jullya Gonçalves Pereira**

Estudante de Análise e Desenvolvimento de Sistemas no Instituto Federal de Rondônia (IFRO) — Campus Ariquemes.

- GitHub: [@annajullyp](https://github.com/annajullyp)

---

<p align="center">
  🌿 <strong>Nobre Turismo — O extraordinário é natural.</strong>
</p>
