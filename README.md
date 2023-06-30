<h1 align="center"> 🏆 T15 - Projeto Final Backend BiblioteKA 📚 - M5 </h1>

<h3 align="center"> 
	🚧  Projeto Backend BiblioteKA 📚 - 🚀 Em construção...  🚧
</h3>

## 💡 Introdução

- O objetivo desse desafio é construir uma aplicação que faz a gestão de uma biblioteca.

## 📚 Requisitos

<details>

<summary>Saiba mais sobre os Requisitos do Projeto</summary>

###

- Desenvolvimento do Projeto
- Utilizar Django Rest Framework como base do projeto;
- Obrigatório desenvolver diagrama ER;
- Obrigatório usar banco de dados postgres;
- Obrigatório utilizar Autenticação/Autorização;
- Obrigatório utilizar views desenvolvidas com Generic View;
- Obrigatório ter documentação, tanto de como rodar seu projeto, quanto das rotas, para a equipe de ensino conseguir corrigir e validar o uso em produção;
- Deploy é obrigatório;
- Tem que ser validável em produção;
- Commits padronizados e organizados (Conventional Commits);
- Frontend é opcional, priorizem o backend;
- Testes são opcionais, mas será um ótimo diferencial;
- Pode usar o nome da Kenzie Academy Brasil nos projetos se precisar.

</details>

## 💻 Features

## Empréstimo de Livros

- Cada livro só poderá ser emprestado por um período fixo de tempo.
- Se desejarem desenvolver algo mais complexo, deem uma olhada na seção Modo Hard.

## Devolução de Livros

- Todos os livros emprestados deverão ter uma data de retorno.
- Deverá ser criada uma lógica onde, se a devolução cair em um fim de semana (sábado ou domingo), a data de retorno deverá ser modificada para ser no próximo dia útil.
- Caso o estudante não devolva o livro até o prazo estipulado, deverá ser impedido (bloqueado) de solicitar outros empréstimos.

## Bloqueio de Novos Empréstimos

Se um estudante não efetuar a devolução dos livros no prazo estipulado, ele não poderá emprestar mais livros até completar a devolução dos anteriores. Após completar as devoluções pendentes, o bloqueio deve permanecer por alguns dias.

## Usuários

O sistema deve permitir o cadastro de usuários. Deve haver, no mínimo, 2 tipos de usuários:

- Estudante
- Colaborador da biblioteca.

Deve ser possível também usuários não autenticados acessarem a plataforma para visualizar informações sobre os livros, como disponibilidade, título, etc.

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

###

## 🚀 Tecnologias

- **[Python](https://www.python.org/)**

</br>

## 🚛 Entregáveis

Link deste repositório no GitHub;

- [Github Repo]()

- [Link Deploy]()

</br>

## 🧱 Pré-requisitos

<details>

### 🎲 Rodando o Back End

```bash
git clone https://github.com/toledomg/T15-Projeto-Final-Backend-M5.git
```

### Instale as dependências

```bash
pip install -r requirements.txt
```

## Instalação dos pacotes de teste

- Verifique se os pacotes `pytest` e/ou `pytest-testdox` estão instalados globalmente em seu sistema:

```shell
pip list
```

- Caso seja listado o `pytest` e/ou `pytest-testdox` e/ou `pytest-django` em seu ambiente global, utilize os seguintes comando para desinstalá-los globalmente:

```shell
pip uninstall pytest
```

```shell
pip uninstall pytest-testdox
```

```shell
pip uninstall pytest-django
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

4. Instale o pacote `pytest-testdox`:

```shell
pip install pytest-testdox pytest-django
```

5. Agora é só rodar os testes no diretório principal do projeto:

```shell
pytest --testdox -vvs
```

6. Caso queira um log mais resumido, basta executar com os testes sem as flags **verbose**:

```shell
pytest --testdox
```

</details>

</br>

## 🧪 Testes

<details>
  
## <summary>Rodando os testes por partes</summary>
  
Caso você tenha interesse em rodar apenas um diretório de testes específico, pode utilizar o comando:

- Rodando testes de users:

```python
pytest --testdox -vvs tests/test1/
```

- Rodando testes de test2:

```python
pytest --testdox -vvs tests/test2/
```

- Rodando testes de test3:

```python
pytest --testdox -vvs tests/test3/
```

</details>

</br>

## Import WorkSpace Insomnia

[![Run in Insomnia}](https://insomnia.rest/images/run.svg)](https://insomnia.rest/run/?label=Projeto-Final-T15-m5&uri=https%3A%2F%2Fgithub.com%2Ftoledomg%2FT15-Projeto-Final-Backend-M5%2Fblob%2Fdevelop%2Fwork_insomnia)

</br>

# 📌 Links Úteis

Link Grupo Slack;

- [Canal Grupo-10](https://app.slack.com/client/TQZR39SET/C05ENM0FARH)

Link do Projeto no Canvas;

- [Projeto no Canvas](https://canvas.kenzie.com.br/courses/76)

</br>

## 🤝 Contribuições

- **Alexsandro Toledo** - [Github](https://github.com/toledomg)
- **Carol Rocha** - [Github](https://github.com/Carol-Rocha)
- **Laisa Andrade** - [Github](https://github.com/LaisaCCAndrade)
- **Lucas Ribeiro Marques** - [Github](https://github.com/lribeiromarques)

##

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
