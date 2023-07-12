<h1 align="center"> 🏆 T15 - Projeto Final Backend BiblioteKA 📚 - M5 </h1>

<h3 align="center"> 
	🚀 Projeto Backend BiblioteKA 📚
</h3>

## 💡 Introdução

- O objetivo desse projeto foi construir uma aplicação que faz a gestão de uma biblioteca.

## 📚 Requisitos

<details>

<summary>Saiba mais sobre os Requisitos do Projeto</summary>

###

- Utilizar Django Rest Framework como base do projeto;
- Desenvolver diagrama ER;
- Usar banco de dados postgres;
- Utilizar Autenticação/Autorização;
- Utilizar views desenvolvidas com Generic View;
- Documentação, tanto de como rodar seu projeto, quanto das rotas para validar o uso em produção;
- Deploy da Aplicação;
- Commits padronizados e organizados (Conventional Commits);

</details>

## 💻 Features

- [x] Cadastro de usuários
- [x] Bloqueio de usuários por atraso
- [x] Histórico de Livros por usuário
- [x] Verificação do Status de usuários no momento do empréstimo
- [x] Cadastro de Livros
- [x] Seguir Livros
- [x] Informações de Livros
- [x] Avaliação de Livros
- [x] Livros disponíveis
- [x] Devolução de Livros
- [x] Devolução em Dia útil
- [x] Multa de devolução tardia do Livro
- [x] Send Email para usuários, quando o livro estiver disponível
- [x] Bloqueio e desbloqueio automático de usuário atrasado

## Empréstimo de Livros

- Cada livro só poderá ser emprestado por um período fixo de tempo.

## Devolução de Livros

- Todos os livros emprestados deverão contém data de retorno.
- Quando a devolução cair em um fim de semana (sábado ou domingo), a data de retorno deverá é modificada para ser no próximo dia útil.
- Caso o estudante não devolva o livro até o prazo estipulado, ele é impedido (bloqueado) de solicitar outros empréstimos.

## Bloqueio de Novos Empréstimos

Se um estudante não efetuar a devolução dos livros no prazo estipulado, ele não poderá emprestar mais livros até completar a devolução dos anteriores. Após completar as devoluções pendentes, o bloqueio ainda permanece por alguns dias.

## Usuários

O sistema permite o cadastro de usuários com 2 tipos:

- Estudante
- Colaborador da biblioteca.

É possível também usuários não autenticados acessarem a plataforma para visualizar informações sobre os livros, como disponibilidade, título, etc.

### Funcionalidades permitidas aos estudantes:

De maneira geral, ao acessar a plataforma, um estudante pode:

- Ver seu próprio histórico de livros emprestados.
- Obter informações sobre livros.
- "Seguir" um livro a fim de receber notificações no email conforme a disponibilidade/status do livro.

### Funcionalidades permitidas aos colaboradores:

De maneira geral, ao acessar a plataforma, um colaborador pode:

- Cadastrar novos livros.
- Emprestar livros.
- Verificar o histórico de empréstimo de cada estudante.
- Verificar status do estudante (se está bloqueado não pode emprestar uma nova cópia durante determinado tempo).

### Rota para Login e acesso ao reset_password:

    http://URL_API/login/

- Nesse link tem uma tela de login com um botão reset password.

###

## 🚀 Tecnologias

- **[Django](https://www.djangoproject.com/)**
- **[PostgreSQL](https://www.postgresql.org/)**

</br>

## 💫 Links

- [Github Repo](https://github.com/toledomg/T15-Projeto-Final-Backend-M5)

- [Link Deploy](https://api-biblioteka-hgmd.onrender.com)

</br>

## 🚚 Documentação API / Rotas da Aplicação

- [Link Documentação Swagger](https://api-biblioteka-hgmd.onrender.com/api/docs/swagger/)

- [Link Documentação Redoc](https://api-biblioteka-hgmd.onrender.com/api/docs/redoc/)

</br>

## 🧱 Pré-requisitos

<details>

### 🎲 Rodando o Back End

```bash
git clone https://github.com/toledomg/T15-Projeto-Final-Backend-M5.git
```

### 💾 Instale as dependências

```bash
pip install -r requirements.txt
```

### A partir disso, prossiga com os passos:

1. Crie seu ambiente virtual:

```bash
python -m venv venv
```

2. Ative seu venv:

```bash
# Linux:
source venv/bin/activate

# Windows (Powershell):
.\venv\Scripts\activate

# Windows (Git Bash):
source venv/Scripts/activate
```

3. Execute o Servidor

```bash
python manage.py runserver
```

</details>

</br>

## Import WorkSpace Insomnia

[![Run in Insomnia}](https://insomnia.rest/images/run.svg)](https://insomnia.rest/run/?label=Projeto-Final-T15-m5&uri=https%3A%2F%2Fgithub.com%2Ftoledomg%2FT15-Projeto-Final-Backend-M5%2Fblob%2Fdevelop%2Fwork_insomnia)

</br>

## 🤝 Contribuições

- **Alexsandro Toledo**

  - [Github](https://github.com/toledomg)
  - [Linkedin](https://www.linkedin.com/in/toledomg/)

- **Carol Rocha**

  - [Github](https://github.com/Carol-Rocha)
  - [Linkedin](https://www.linkedin.com/in/carol-rocha-70a819247/)

- **Laisa Andrade**

  - [Github](https://github.com/LaisaCCAndrade)
  - [Linkedin](https://www.linkedin.com/in/laisa-c-c-andrade/)

- **Lucas Ribeiro Marques**
  - [Github](https://github.com/lribeiromarques)
  - [Linkedin]()

##

<!-- [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) -->

[![made-with-django](https://img.shields.io/badge/Made%20with-Django-1f425f.svg)](https://www.djangoproject.com/)
[![made-with-postgres](https://img.shields.io/badge/Made%20with-PostgreSQL-1f425f.svg)](https://www.postgresql.org/)

[![made-with-license](https://badgen.net/github/license/toledomg/T15-Projeto-Final-Backend-M5)](https://opensource.org/license/mit/)
[![contributors](https://badgen.net/github/contributors/toledomg/T15-Projeto-Final-Backend-M5)](https://github.com/toledomg/T15-Projeto-Final-Backend-M5/)
[![commits](https://badgen.net/github/commits/toledomg/T15-Projeto-Final-Backend-M5)](https://github.com/toledomg/T15-Projeto-Final-Backend-M5/)
