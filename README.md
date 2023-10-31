Introdução

E um aplicativo Django/script que permite aos usuários buscar informações sobre filmes e adicioná-los aos favoritos.

Clone o repositório:

git clone https://github.com/marcos1py/desafio-back-end

Crie um ambiente virtual Python e ative-o:

windowns
python3 -m venv venv

linux
source venv/bin/activate

Instale as dependências:
pip install -r requirements.txt

Instruções de uso

* **Usando o Terminal:**

Entre na pasta `scriptDoDesafio` no arquivo `main.py` 
Video demonstraçao no terminal: https://www.youtube.com/watch?v=UgVqwpBplbo&ab_channel=MARCOS

* **Usando o site Django:**

Faz o migrate:
python manage.py migrate

E quando quiser usar/testa basta colocar esse comando no terminal
python manage.py runserver

Navegue para http://localhost:8000 no seu navegador.

Demostraçao de como o site: https://www.youtube.com/watch?v=vz-otp4cywI&feature=youtu.be&ab_channel=MARCOS

Funcionalidades

Busca de filmes por título, ano de lançamento ou gênero.
Adição de filmes aos favoritos.
Visualização da lista de filmes favoritos.

Demonstração

Terminal: https://www.youtube.com/watch?v=UgVqwpBplbo&ab_channel=MARCOS
Site Django: https://www.youtube.com/watch?v=vz-otp4cywI&feature=youtu.be&ab_channel=MARCOS
