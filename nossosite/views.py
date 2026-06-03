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
        {"numero": 1,  "nome": "Alisson Becker",    "posicao": "Goleiro",    "idade": 31, "cidade": "Novo Hamburgo-RS",   "clube": "Liverpool"},
        {"numero": 2,  "nome": "Danilo",             "posicao": "Lateral D.", "idade": 32, "cidade": "Bicas-MG",           "clube": "Juventus"},
        {"numero": 3,  "nome": "Marquinhos",         "posicao": "Zagueiro",   "idade": 29, "cidade": "São Paulo-SP",       "clube": "PSG"},
        {"numero": 4,  "nome": "Éder Militão",       "posicao": "Zagueiro",   "idade": 25, "cidade": "São Paulo-SP",       "clube": "Real Madrid"},
        {"numero": 6,  "nome": "Alex Sandro",        "posicao": "Lateral E.", "idade": 32, "cidade": "Catanduva-SP",       "clube": "Juventus"},
        {"numero": 5,  "nome": "Casemiro",           "posicao": "Volante",    "idade": 31, "cidade": "São José dos Campos","clube": "Man. United"},
        {"numero": 8,  "nome": "Fred",               "posicao": "Meia",       "idade": 30, "cidade": "Belo Horizonte-MG",  "clube": "Man. United"},
        {"numero": 11, "nome": "Raphinha",           "posicao": "Ponta D.",   "idade": 26, "cidade": "Porto Alegre-RS",    "clube": "Barcelona"},
        {"numero": 10, "nome": "Neymar Jr.",         "posicao": "Meia-ata.",  "idade": 31, "cidade": "Mogi das Cruzes-SP", "clube": "Al-Hilal"},
        {"numero": 20, "nome": "Vinicius Jr.",       "posicao": "Ponta E.",   "idade": 23, "cidade": "São Gonçalo-RJ",     "clube": "Real Madrid"},
        {"numero": 9,  "nome": "Richarlison",        "posicao": "Centroavante","idade": 26, "cidade": "Nova Venécia-ES",   "clube": "Tottenham"},
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

    
