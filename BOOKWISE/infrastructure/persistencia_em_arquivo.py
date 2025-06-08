import pickle
from domain.interface_persistencia import IPersistencia

class PersistenciaEmArquivo(IPersistencia):
    def __init__(self, caminho='usuario.pkl'):
        self.caminho = caminho

    def salvar(self, usuario):
        with open(self.caminho, 'wb') as f:
            pickle.dump(usuario, f)

    def carregar(self):
        try:
            with open(self.caminho, 'rb') as f:
                return pickle.load(f)
        except FileNotFoundError:
            return None
