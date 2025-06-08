class Interface:
    def __init__(self, gerenciador, gerador_relatorio):
        self.gerenciador = gerenciador
        self.gerador_relatorio = gerador_relatorio

    def menu(self):
        while True:
            print("\n--- BookWise ---")
            print("1. Adicionar livro")
            print("2. Atualizar progresso")
            print("3. Gerar relatório")
            print("4. Sair")

            opcao = input("Escolha: ")

            if opcao == "1":
                titulo = input("Título: ")
                autor = input("Autor: ")
                total = int(input("Total de páginas: "))
                self.gerenciador.adicionar_livro(titulo, autor, total)
            elif opcao == "2":
                titulo = input("Título: ")
                paginas = int(input("Páginas lidas: "))
                sucesso = self.gerenciador.atualizar_progresso(titulo, paginas)
                if not sucesso:
                    print("Livro não encontrado.")
            elif opcao == "3":
                print(self.gerador_relatorio.gerar(self.gerenciador.usuario))
            elif opcao == "4":
                break
            else:
                print("Opção inválida.")
