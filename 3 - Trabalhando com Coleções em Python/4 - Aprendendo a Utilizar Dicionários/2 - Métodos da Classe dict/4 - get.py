contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
}

#print(contatos["chave"])

contato = contatos.get("chave")
print(contato)

contato = contatos.get("chave", {})
print(contato)

contato = contatos.get("guilherme@gmail.com", {})
print(contato)