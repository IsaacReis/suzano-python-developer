contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
}

print(contatos.pop("guilherme@gmail.com"))
print(contatos)

print(contatos.pop("guilherme@gmail.com", {}))
print(contatos)