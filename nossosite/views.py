# app/views.py
from django.shortcuts import render


def index(request):
    titulos = [
        {"ano": "1958", "torneio": "Copa do Mundo FIFA", "sede": "Suécia"},
        {"ano": "1962", "torneio": "Copa do Mundo FIFA", "sede": "Chile"},
        {"ano": "1970", "torneio": "Copa do Mundo FIFA", "sede": "México"},
        {"ano": "1994", "torneio": "Copa do Mundo FIFA", "sede": "Estados Unidos"},
        {"ano": "2002", "torneio": "Copa do Mundo FIFA", "sede": "Coreia/Japão"},
    ]
    context = {
        "titulos": titulos,
        "total_jogadores": 11,
    }
    return render(request, "nossosite/index.html", context)


def elenco(request):
    jogadores = [
        {"numero": 1,  "nome": "Alisson Becker",  "posicao": "Goleiro",    "idade": 31, "cidade": "Novo Hamburgo-RS",    "clube": "Liverpool",   "foto": "alisson.jpg"},
        {"numero": 2,  "nome": "Wesley",           "posicao": "Lateral D.", "idade": 20, "cidade": "São Luís-Ma",              "clube": "Roma",    "foto": "wesley.jpg"},
        {"numero": 6,  "nome": "Alex Sandro",      "posicao": "Lateral E.", "idade": 32, "cidade": "Catanduva-SP",        "clube": "Flamengo",    "foto": "alexsandro.jpg"},
        {"numero": 14,  "nome": "Bremer",           "posicao": "Zagueiro",   "idade": 27, "cidade": "Itapitanga-BA",       "clube": "Flamengo",    "foto": "bremer.jpg"},
        {"numero": 15,  "nome": "Léo Pereira",      "posicao": "Zagueiro",   "idade": 28, "cidade": "Curitiba-PR",         "clube": "Flamengo",    "foto": "leopereira.jpg"},
        {"numero": 5,  "nome": "Casemiro",         "posicao": "Volante",    "idade": 31, "cidade": "São José dos Campos", "clube": "Man. United", "foto": "casemiro.jpg"},
        {"numero": 8,  "nome": "Bruno Guimarães",  "posicao": "Meia",       "idade": 26, "cidade": "Rio de Janeiro-RJ",   "clube": "Newcastle",   "foto": "bruno.jpg"},
        {"numero": 9, "nome": "Matheus Cunha",    "posicao": "Meia",       "idade": 25, "cidade": "João Pessoa-PB",      "clube": "Man. United",      "foto": "matheuscunha.jpg"},
        {"numero": 21, "nome": "Luiz Henrique",    "posicao": "Atacante",   "idade": 23, "cidade": "Petrópolis-RJ",       "clube": "Zenit",    "foto": "luizhenrique.jpg"},
        {"numero": 11, "nome": "Raphinha",         "posicao": "Ponta D.",   "idade": 26, "cidade": "Porto Alegre-RS",     "clube": "Barcelona",   "foto": "raphinha.jpg"},
        {"numero": 7, "nome": "Vinicius Jr.",     "posicao": "Ponta E.",   "idade": 23, "cidade": "São Gonçalo-RJ",      "clube": "Real Madrid", "foto": "vini.jpg"},
    ]
    context = {"jogadores": jogadores}
    return render(request, "nossosite/elenco.html", context)


def sobre(request):
    autores = [
        {"nome": "Marcos Filho",    "matricula": "20241181110025"},
        {"nome": "Bruno Rafael",  "matricula": "20241181110016"},
    ]
    info_site = {
        "descricao": (
            "Este portal foi criado para divulgar informações sobre a Seleção "
            "Brasileira de Futebol, sua história e o elenco atual. O conteúdo "
            "inclui dados dos atletas, conquistas históricas e curiosidades sobre "
            "a equipe mais vitoriosa do futebol mundial."
        ),
        "disciplina":   "Programação de Aplicação Web",
        "professor":    "Diego Cirilo",
        "instituicao":  "IFRN — Instituo Federal do Rio Grande do Norte",
        "curso":        "Informática para Internet",
        "periodo":      "3º Período",
        "ano":          "2026",
        "tecnologias":  ["Python 3", "Django", "HTML5", "CSS3", "Template Engine Django"],
    }
    context = {
        "autores":   autores,
        "info_site": info_site,
    }
    return render(request, "nossosite/sobre.html", context)

    
