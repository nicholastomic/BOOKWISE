from domain.interface_relatorio import IGeradorRelatorio

class GeradorRelatorio(IGeradorRelatorio):
    def gerar(self, usuario):
        relatorio = f"Relatório de {usuario.nome}:\n"
        for livro in usuario.livros:
            relatorio += f"- {livro.titulo} ({livro.progresso():.2f}% lido)\n"
        return relatorio
