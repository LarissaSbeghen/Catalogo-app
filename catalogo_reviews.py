#avaliaçao: o que o usuario escreve sobre uma obra
class avaliacao:
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
class obra:
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

def main():
    avaliacaao = avaliacao("Lari", 10, "EU AMOOOO, MTO BOM RECOMENDO MUITO")
    print(avaliacaao)
    obrayay = obra("The Owl House", 2020, "Aventura")
    print(obrayay)

    obrayay.adicionar_ava(avaliacao("Mi", 7))
    obrayay.adicionar_ava(avaliacao("Mily", 9))
    obrayay.adicionar_ava(avaliacao("Lari", 10))
    print(obrayay)
    print("Media: ", obrayay.media())

if __name__ == "__main__":
    main()