"""
    1. Pq usar?
        Função é um bloco de código, você escrevendo função
        não vai precisar repetiro o código se for preciso.
        - Chamar a função.
        
    2. Funções trabalham com dados dinamicos
        Dados dinâmicos são dados que dependem do usuário para informar.    
     
"""

aluno = {
    'faltas': 26,
    'prova1': 7,
    'prova2': 8,
    'nome': 'Alberto' 
}

aluno2 = {
    'faltas': 21,
    'prova1': 8,
    'prova2': 8,
    'nome': 'Andre' 
}

def calc_media(student):
    soma = student['prova1'] + student['prova2']
    return soma / 2

def veri_falta(student):
    if student['faltas'] >= 25:
        return False
    
def resultado_final(media, falta):
    if media >= 6 and falta == True:
        return "Aprovado"
    else:
        return "Reprovado"

alberto = calc_media(aluno)
andre = calc_media(aluno2)
bam = calc_media({
    'faltas': 21,
    'prova1': 8,
    'prova2': 8,
    'nome': 'Bam' 
})

alberto_falta = veri_falta(aluno)

resultado_alberto = resultado_final(alberto, alberto_falta)
print(resultado_alberto)