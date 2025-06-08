from domain.usuario import Usuario
from infrastructure.persistencia_em_arquivo import PersistenciaEmArquivo
from use_cases.gerenciador_livros import GerenciadorDeLivros
from use_cases.gerador_relatorios import GeradorRelatorio
from infrastructure.proxy_relatorio import ProxyRelatorio
from presentation.interface import Interface

persistencia = PersistenciaEmArquivo()
usuario = persistencia.carregar()

if not usuario:
    nome = input("Digite seu nome: ")
    usuario = Usuario(nome)

gerenciador = GerenciadorDeLivros(usuario, persistencia)
relatorio_real = GeradorRelatorio()
proxy = ProxyRelatorio(relatorio_real)
interface = Interface(gerenciador, proxy)

interface.menu()
