import requests
import json
import os

class FilmeAPI:
    def __init__(self):
        self.chave_api = "e6ff776"

    #verifica os http mais padrao
    def tratar_erros_http(self, response):
        if response.status_code == 200:
            return True
        elif response.status_code == 404:
            print("Filme não encontrado.")
        elif response.status_code == 401:
            print("Chave de API não autorizada.")
        return False

    #ver se tem algum erro na api
    def tratar_erros_api_omdb(self, data):
        if "Error" in data:
            print("Erro na API OMDB:", data["Error"])
            return False
        return True

    #busca o filme
    def buscar_filme_por_titulo(self, titulo):
        if not titulo:
            print("Título do filme não fornecido.")
            return None

        url_api = f"https://www.omdbapi.com/?apikey={self.chave_api}&t={titulo}"
        resposta = requests.get(url_api)

        if not self.tratar_erros_http(resposta):
            return None

        dados = resposta.json()

        if not self.tratar_erros_api_omdb(dados):
            return None

        filme = {
            "ID": dados["imdbID"],
            "Nome": dados["Title"],
            "Ano": dados["Year"],
            "Classificação": dados["Rated"],
            "Sinopse": dados["Plot"],
            "Diretor": dados["Director"],
            'img': dados["Poster"]
        }
        return filme

    def adicionar_favorito(self, filme, arquivo_favoritos):
        try:
            if os.path.exists(arquivo_favoritos) and os.path.getsize(arquivo_favoritos) > 0:
                with open(arquivo_favoritos, "r") as arquivo:
                    favoritos = json.load(arquivo)
            else:
                favoritos = []
        except FileNotFoundError:
            favoritos = []

        filme["ID"] = len(favoritos) + 1

        favoritos.append(filme)

        with open(arquivo_favoritos, "w") as arquivo:
            json.dump(favoritos, arquivo, indent=2)

if __name__ == '__main__':
    filme_api = FilmeAPI()
    fim = False

    while not fim:
        print("-----------------------")
        print("DIGITE 1- para pesquisar filme")
        print("DIGITE 2- Para mostrar favoritos")
        print("DIGITE 3 - Sair")
        print("-----------------------")
        resposta = input("Resposta :")

        if resposta == "1":
            titulo_filme = input("Digite o título do filme: ")
            if titulo_filme:
                info_filme = filme_api.buscar_filme_por_titulo(titulo_filme)
                if info_filme:
                    print(f"Informações sobre o filme '{info_filme['Nome']}':")
                    print(f"Ano: {info_filme['Ano']}")
                    print(f"Classificação: {info_filme['Classificação']}")
                    print(f"Sinopse: {info_filme['Sinopse']}")
                    print(f"Diretor: {info_filme['Diretor']}")

                    add_favorito = input("Deseja adicionar aos favoritos? Digite 's' para confirmar: ").strip().lower()
                    if add_favorito == 's':
                        filme_api.adicionar_favorito(info_filme, "favoritos.json")
                        print(f"O filme '{info_filme['Nome']}' foi adicionado aos favoritos com o ID {info_filme['ID']}.")
            else:
                print("Título do filme não fornecido. Não é possível continuar.")
        elif resposta == "2":
            # Mostrar favoritos
            try:
                with open("favoritos.json", "r") as arquivo:
                    favoritos = json.load(arquivo)
                if favoritos:
                    print()
                    print("Lista de filmes favoritos:")
                    for filme in favoritos:
                        print(f"ID: {filme['ID']},  Nome: {filme['Nome']},  Ano: {filme['Ano']}")
                    print()

                else:
                    print("Nenhum filme favorito encontrado.")
            except FileNotFoundError:
                print("Nenhum filme favorito encontrado.")
        elif resposta == "3":
            print("Obrigado e tenha um ótimo dia, FIM")
            fim = True

