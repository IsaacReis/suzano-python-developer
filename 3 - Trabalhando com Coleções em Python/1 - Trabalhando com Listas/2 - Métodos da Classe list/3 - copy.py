lista = [1, 'Python', [40, 30, 20]]

l2 = lista.copy()

print(f"lista original: {lista}\nlista copiada: {l2}")
print(id(l2), id(lista))

l2[0] = 2

print(f"lista original: {lista}\nlista copiada: {l2}")