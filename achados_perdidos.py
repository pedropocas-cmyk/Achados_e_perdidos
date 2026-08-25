def mostrar_menu():
 print("\n================================")
 print("Achados e perdidos da escola!") 
 print("================================")
 print("1 - Cadastrar objeto")
 print("2 - Listar objetos")
 print("3 - Excluir objeto")
 print("4 - Sair")
def mostrar_menu():
  print("\n================================")
  print("Achados e perdidos da escola!") 
  print("================================")
  print("1 - Cadastrar objeto")
  print("2 - Listar objetos")
  print("3 - Excluir objeto")
  print("4 - Sair")
def main():
  while True:
    escolha = input("Escolha uma das opções acima: ")
    if escolha =="1":
      print("\nAbrindo cadastro de objeto...")
    elif escolha =="2":
      print("\nMostrando os objetos cadastrados...")
    elif escolha=="3":
      print("\nAbrindo exclusão de objeto...")
    elif escolha =="4":
      print("\nPrograma encerrado!")
    break
  else:
   print("Opção inválida. Digite 1,2,3 ou 4.")
mostrar_menu()
main()






