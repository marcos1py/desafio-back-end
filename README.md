## README - Uso do FilmeView

Este é um aplicativo Django que permite aos usuários buscar informações sobre filmes e adicioná-los aos favoritos.

### Configuração Inicial

1. Clone o repositório, navegue até o diretório do projeto, crie um ambiente virtual Python (recomendado) e ative-o, e instale as dependências necessárias a partir do arquivo `requirements.txt`:

   ```bash
   git clone https://github.com/marcos1py/desafio-back-end
   cd desafio-back-end
   python -m venv venv
   .\venv\Scripts\activate
   pip install -r requirements.txt

Tem 2 formas de testar
Uma e pelo terminal na pasta `scriptDoDesafio` no arquivo `main.py` 

e outro e usando o django, para isso voce vai precisar escrever esse comando apos instalar o requirements
comando para ligar o servidor django:
   ```bash
   python manage.py runserver      