def exibir_poema(data_extenso, *lista, **dicionario):
    texto = "\n".join(lista)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in dicionario.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

exibir_poema(
    "Sexta-feira, 26 de Agosto de 2022",
    "Zen of Python",
    "Beautiful is better than ugly",
    "Explicit is better than implicit.",
    "Simple is better than complex.",
    "Complex is better than complicated.",
    "Flat is better than nested.",
    "Sparse is better than dense",
    "Redability counts.",
    "Special cases aren't special enought to break the rules.",
    "Although practicality beats purity.",
    "[...] rest of the poem [...]",
    autor="Tim Peters",
    ano = 1999,
)