print("Hello, world!")

nomes = str(input("Digite o nome dos filmes que deseja separando por virgula: ")).lower()
filmes_listado = []
for filme in nomes.split(","):
    filmes_listado.append(filme.strip())

print("      Informações Iniciais      ")
print(f"Quantidade de filmes cadastrados: {len(filmes_listado)}")
print(f"Primeiro filme da lista: {filmes_listado[0]}")
print(f"Último filme da lista: {filmes_listado[-1]}")

novo_final = input("Digite um filme para adicionar ao final da lista: ")
filmes_listado.append(novo_final.strip())

novo_inicio = input("Digite um filme para adicionar ao inicio da lista: ")
filmes_listado.insert(0, novo_inicio.strip())

remover = input("Digite o nome de um filme para remover da lista: ")
if remover.strip() in filmes_listado:
    filmes_listado.remove(remover.strip())
    print(f"O filme '{remover}' foi removido da lista")
else:
    print(f"O filme '{remover}' não foi encontrado")

print("      Lista em Ordem Alfabética      ")
print(sorted(filmes_listado))

filmes_listado.reverse()
print("      Lista Invertida      ")
print(filmes_listado)

copia_filmes = filmes_listado.copy()
filmes_listado.clear()

print("      Listas Finais      ")
print(f"Lista original (agora vazia): {filmes_listado}")
print(f"Copia da lista: {copia_filmes}")
