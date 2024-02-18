# Projeto Fomulário Django
Criando uma página de formulário em django para treinar.

## Passos para instalação do projeto no seu computator

- Clonando o repositório
[Link do repositório](https://github.com/jpcadinelli/django-form)

No terminal, vá até a pasta desejada e use o comando:

```
git clone https://github.com/jpcadinelli/django-form
```

- Checando as ferramentas

Abra a pasta criada (django-form) no seu editor de código preferido.

Abra um terminal e confira se você tem instalado o python e o pip na sua máquina com os seguintes comandos:

```
python3 --version
```

```
pip --version
```

Caso não tenha procure um passo a passo na internet para instala-los.

- Preparando o ambiente virtual que irá rodar o 

Dentro da pasta que foi criada com o comando "git clone" abra o terminal e use o comando:

```
pip install virtualenv
```

- Criando o ambiente virtual

Ainda no terminal use o comando:

```
python -m virtualenv .venv
```
Perceberá que vai aparecer uma pasta .venv junto aos aquivos e para ativar este ambiente virtual usaremos o seguinte comando dependendo do sistema operacional:

Para windows:
```
.venv\Scripts\activate
```
Para Linux:
```
source .venv/bin/activate
```

- Instalando o django e outros

Dentro do mesmo terminal e com o .venv ativado (para saber se o .venv está ativado é só olha o início da linha do terminal e ver se tem um "(.venv)" escrito antes dos escritos normais do terminal) use o seguinte comando:

```
pip install -r requirements.txt
```

Você estará instalando as dependências que estão listadas dentro do requirements.txt da pasta do projeto.

Após todos estes passos, basta usar o comando:

```
python3 manage.py runserver
```

Para rodar o projeto.

O link padrão para visualizar no navegador é este [http://127.0.0.1:8000/](http://127.0.0.1:8000/).