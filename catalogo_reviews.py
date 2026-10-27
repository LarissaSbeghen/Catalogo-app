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
    

def main():
    avaliacaao = avaliacao("Lari", 9, "Amei o filme")
    print(avaliacaao)

if __name__ == "__main__":
    main()