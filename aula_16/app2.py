class Aluno:
    def __init__(self):
        self.aluno = "Alberto"
        self.nota1 = 7
        self.nota2 = 8
    
    def calc_media(self):
        return f"A nota final é: {self.nota1 + self.nota2}"
    
    def veri_faltas():
        pass
    
    

alberto = Aluno()

print(alberto.calc_media())