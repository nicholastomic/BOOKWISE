from abc import ABC, abstractmethod

class IGeradorRelatorio(ABC):
    @abstractmethod
    def gerar(self, usuario):
        pass
