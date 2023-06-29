# 🏆 T15 - Projeto Final Backend - M5

<h4 align="center"> 
	🚧  🏆 T15 - Projeto Final Backend - M5 🚀 Em construção...  🚧
</h4>

## 💡 Introdução

- Na empresa em que você trabalha, o líder de tecnologia solicitou que você acesse um projeto antigo, no qual os usuários poderiam se cadastrar, cadastrar álbuns e músicas. Esse projeto foi desenvolvido com Django, utilizando APIView, Serializer e SQLite3. Ele deseja que você faça uma refatoração, aplicando os conceitos de Generic View, Model Serializer e alterando o banco de dados para o PostgreSQL.

</br>

## 📚 Requisitos

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

</br>

## 💻 Features

- [ x ] Estruturação do Projeto

</br>

## 🚀 Tecnologias

- **[Python](https://www.python.org/)**

</br>

## Entregáveis

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

[![Run in Insomnia}](https://insomnia.rest/images/run.svg)](http://seu.link.aqui)

</br>

# 📌 Links Úteis

Link Grupo Slack;

- [Canal Grupo-10](https://app.slack.com/client/TQZR39SET/C05ENM0FARH)

Link do Projeto no Canvas;

- [Projeto no Canvas](https://canvas.kenzie.com.br/courses/76)

</br>

## 🤝 Contribuições

- **Alexsandro Toledo** - [Github](https://github.com/orgs/M3-T15-Projeto-Front-2023/people/toledomg)

##

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
