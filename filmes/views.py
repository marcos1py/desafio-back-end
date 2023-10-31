from django.shortcuts import render
from scriptDoDesafio.main import FilmeAPI
from django.http import HttpResponse
import json
import os

class FilmeView:
    def __init__(self):
        # Inicializa a classe FilmeView com uma instância de FilmeAPI para usar suas funções
        self.filme_api = FilmeAPI()

    def carregar_favoritos(self):
        favoritos = []

        if os.path.exists("favoritos.json") and os.path.getsize("favoritos.json") > 0:
            with open("favoritos.json", "r") as arquivo:
                favoritos = json.load(arquivo)

        return favoritos



    def index(self, request):
        mensagens = ""
        favoritos = []

        if request.method == 'POST':
            # Verifica se a requisição HTTP é um POST (envio de formulário)
            titulo_filme = request.POST.get('titulo_filme')
            info_filme = None

            # Verifica se o usuário forneceu um título de filme no formulário
            if titulo_filme:
                # Armazena as informações do filme na sessão para uso posterior
                info_filme = self.filme_api.buscar_filme_por_titulo(titulo_filme)
                request.session['info_filme'] = info_filme
            else:
                mensagens = "Filme não encontrado"

            # Verifica se o usuário solicitou adicionar o filme aos favoritos
            
            if 'add_favorito' in request.POST:
                info_filme = request.session.get('info_filme')
                print(info_filme)
                if info_filme:
                    favoritos = self.carregar_favoritos()

                    filme_já_adicionado = any(f['Nome'] == info_filme['Nome'] for f in favoritos)

                    if not filme_já_adicionado:
                        self.filme_api.adicionar_favorito(info_filme, "favoritos.json")
                        mensagens = "Adicionado com sucesso"
                    else:
                        mensagens = "ESSE FILME JÁ FOI ADICIONADO AOS FAVORITOS"

            favoritos = self.carregar_favoritos()
            context = {
                'info_filme': info_filme, 
                'favoritos': favoritos, 
                'mensagens': mensagens,
                }
            
            return render(request, 'filmes/index.html', context)

        else:
            favoritos = self.carregar_favoritos()
            context = {
                'favoritos': favoritos, 
                "info_filme": None,
                }
            return render(request, 'filmes/index.html', context)

