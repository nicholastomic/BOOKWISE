from abc import ABC, abstractmethod

class IPersistencia(ABC):
    @abstractmethod
    def salvar(self, usuario):
        pass

    @abstractmethod
    def carregar(self):
        pass
