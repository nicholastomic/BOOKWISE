from domain.interface_relatorio import IGeradorRelatorio

class ProxyRelatorio(IGeradorRelatorio):
    def __init__(self, relatorio_real):
        self.relatorio_real = relatorio_real

    def gerar(self, usuario):
        if not usuario.livros:
            return "Nenhum livro registrado."
        return self.relatorio_real.gerar(usuario)
