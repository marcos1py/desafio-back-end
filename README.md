# Introdução

E um buscador defilmes, que permite aos usuários buscar informações sobre filmes e adicioná-los aos favoritos.

E tem 2 formas de usar, 1 e pelo script e outro pelo site(django), user qual preferir.

Ele e um codigo simples e facil de ser usado, e lido, nao foi usado banco de dados.

## Como ele funciona?

Primeiro ele impota as biblioteas a ser usada na manipulaçoa da API, e tem um classe "FilmeAPI" que interage com uma API de informações de filmes (OMDb). A classe possui métodos para tratar erros HTTP e da API, além de uma funcionalidade para adicionar filmes aos favoritos, que são armazenados em um arquivo JSON. O programa principal permite aos usuários escolher entre pesquisar filmes, mostrar favoritos ou sair do programa.


## Demonstração dele funcionando

**Terminal:** https://www.youtube.com/watch?v=UgVqwpBplbo&ab_channel=MARCOS

**Site Django:** https://www.youtube.com/watch?v=vz-otp4cywI&ab_channel=MARCOS



## Clone o repositório

```
git clone https://github.com/marcos1py/desafio-back-end
```


## Crie um ambiente virtual Python e ative-o

### Windows



```
python3 -m venv venv
```


### Linux



```
source venv/bin/activate
```


## Instale as dependências



```
pip install -r requirements.txt
```

## Instruções de uso

### Usando o Terminal


Entre na pasta `scriptDoDesafio` no arquivo `main.py`
```
cd scriptDoDesafio
python main.py
```


**Video demonstraçao no terminal:** https://www.youtube.com/watch?v=UgVqwpBplbo&ab_channel=MARCOS

### Usando o site Django


Quando quiser usar/testa basta colocar esse comando no terminal
```
python manage.py runserver
```

Navegue para http://localhost:8000 no seu navegador.

**Demostraçao de como o site:** https://www.youtube.com/watch?v=vz-otp4cywI&ab_channel=MARCOS

## Funcionalidades

* **Busca de filmes por título, ano de lançamento ou gênero.**
* **Adição de filmes aos favoritos.**
* **Visualização da lista de filmes favoritos.**

