def cadastrar_item(itens):
  print("\n---CADASTRO DE OBJETO---")
  nome = input("Digite o nome do objeto: ")
  descrição = input("Digite a descrição do objeto: ")
  local = input("Digite o local onde o objeto foi encontrado: ")
  data = input("Digite a data do registro (dd/mm/aaaa: ")
  if nome.strip() =="":
    print("\nO nome do objeto não pode ficar vazio.")
    return
  if descrição.strip() =="":
    print("\nA descrição do objeto não pode ficar vazia.")
    return
  if local.strip() =="":
    print("\nO local do objeto não pode ficar vazio.")
    return
  if data.strip() =="":
    print("\nA data do objeto não pode ficar vazia.")
    return 
  item = {
      "Nome": nome,
      "Descrção": descrição,
      "Local": local,
      "Data": data
  }
  itens.append(item)
  print("\nObjeto cadastrado com sucesso!")
def mostrar_menu():
  print("\n-----------------------")
  print("\nACHADOS E PERDIDOS DA ESCOLA.")
  print("\n-----------------------")
  print("1-Cadastrar objeto")
  print("2-Listar objetos")
  print("3-Excluir objeto")
  print("4-Sair")
def main():
  itens=[]
  while True:
    mostrar_menu()
    opção = input("\nEscolha uma opção: ")
    if opção =="1":
      cadastrar_item(itens)
    elif opção =="2":
      print(itens)
    elif opção =="3":
      print("\nA execução será criada em outra aula.")
    elif opção =="4":
      print("\nPrograma encerrado.")
      break
    else:
      print("\nOpção inválida. Digite 1,2,3, ou 4.")
main()
