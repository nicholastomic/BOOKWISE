class GerenciadorDeLivros:
    def __init__(self, usuario, persistencia):
        self.usuario = usuario
        self.persistencia = persistencia

    def adicionar_livro(self, titulo, autor, total_paginas):
        from domain.livro import Livro
        livro = Livro(titulo, autor, total_paginas)
        self.usuario.adicionar_livro(livro)
        self.persistencia.salvar(self.usuario)

    def atualizar_progresso(self, titulo, paginas_lidas):
        for livro in self.usuario.livros:
            if livro.titulo == titulo:
                livro.atualizar_paginas_lidas(paginas_lidas)
                self.persistencia.salvar(self.usuario)
                return True
        return False
