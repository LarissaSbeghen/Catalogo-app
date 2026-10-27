#avaliaçao: o que o usuario escreve sobre uma obra
class Avaliacao:
    def __init__(self, autor, nota, comentario = ""):
        if not 0 <= nota <= 10:
            raise ValueError("A nota deve estar entre 0 a 10.")
        self.autor = autor
        self.nota = nota 
        self.comentario = comentario

    def __str__(self):
        texto = f"{self.autor}: {self.nota}/10"
        if self.comentario:
            texto += f' - "{self.comentario}"'
        return texto

#obra: classe base, todas as outras classes vao herdar dela
class Obra:
    tipo = "Obra"
    def __init__(self, titulo, ano, genero):
        self.titulo = titulo
        self.ano = ano
        self.genero = genero
        self.avaliacoes = []

    def adicionar_ava(self, avaliacao):
        self.avaliacoes.append(avaliacao)

    def media(self):
        if not self.avaliacoes:
            return 0.0
        total = sum(a.nota for a in self.avaliacoes)
        return total / len(self.avaliacoes)

    def detalhes(self):
        # Infos especificas de cada tipo, as subclasses sobreescrevem
        return ""

    def __str__(self):
        base = f"[{self.tipo}] {self.titulo} ({self.ano}) - {self.genero}"
        extra = self.detalhes()
        if extra:
            base += f" | {extra}"
        return f"{base} | média: {self.media():.1f} ({len(self.avaliacoes)} avaliações)"

class Filme(Obra):
    tipo = "Filme"

    def __init__(self, titulo, ano, genero, duracao_min):
        super().__init__(titulo, ano, genero)
        self.duracao_min = duracao_min

    def detalhes(self):
        return f"{self.duracao_min} min"


def main():
    avaliacao = Avaliacao("Lari", 10, "EU AMOOOO, MTO BOM RECOMENDO MUITO")
    print(avaliacao)
    obrayay = Obra("The Owl House", 2020, "Aventura")
    print(obrayay)

    obrayay.adicionar_ava(Avaliacao("Mi", 7))
    obrayay.adicionar_ava(Avaliacao("Mily", 9))
    obrayay.adicionar_ava(Avaliacao("Lari", 10))
    print(obrayay)
    print("Media: ", obrayay.media())

    filme = Filme("SuperMarioGalaxy", 2026, "Aventura", 99)
    filme.adicionar_ava(Avaliacao("Carla", 10))
    print(filme)

if __name__ == "__main__":
    main()