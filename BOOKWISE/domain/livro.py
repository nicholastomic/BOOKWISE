class Livro:
    def __init__(self, titulo: str, autor: str, total_paginas: int):
        self.titulo = titulo
        self.autor = autor
        self.total_paginas = total_paginas
        self.paginas_lidas = 0

    def atualizar_paginas_lidas(self, paginas: int):
        if 0 <= paginas <= self.total_paginas:
            self.paginas_lidas = paginas

    def progresso(self):
        return (self.paginas_lidas / self.total_paginas) * 100 if self.total_paginas else 0
