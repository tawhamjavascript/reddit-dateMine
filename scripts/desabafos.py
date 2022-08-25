import os
import requests # importando a biblioteca requests
import json # importando a biblioteca json


palavras_chaves = ["deprê", "ansiedade", "chorar", "morrer", "matar", "medo", "crises", "chorando", "Só", "sozinho", "solidão", "desolado", "morto", "vazio", "suicídio", "surto",  "surtei", "surtar", "depressivo","ansioso", "ansiosa", "desespero", "desesperado", "desesperada", "solitário", "melancólico", "desânimo", "tristeza", "depresso", "infeliz", "neura", "neurótico", "psiquiatra", "psicólogo", "psicóloga", "noia", "noiada", "noiado", "ajuda", "problema", "problemas"]
quantidade_de_posts = 500  # O máximo permitido é 500 comentários
tipo_de_busca = "comment" # pode procurar por post ou por comentário
ordenacao_dos_comentarios = "desc" # do comentário mais antigo para novo


os.mkdir(f"../desabafos/titulo")
for palavra in palavras_chaves:
    os.mkdir(f"../desabafos/titulo/{palavra}")
    base_url = f"https://api.pushshift.io/reddit/search/{tipo_de_busca}/?q={palavra}&subreddit=desabafos&sort={ordenacao_dos_comentarios}&size={quantidade_de_posts}"
    requisicao = requests.get(base_url)
    if requisicao is not None or requisicao != "":
        with open(f"../desabafos/titulo/{palavra}/{palavra}.json", "a", encoding="utf-8") as arquivo:
            json.dump(requisicao.json(), arquivo, indent=4, ensure_ascii=False)