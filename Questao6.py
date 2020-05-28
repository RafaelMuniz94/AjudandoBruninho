# 6-Foram anotadas as idades e alturas de 30 alunos.
#  Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.

IdadeAlunos = [12, 16, 11, 13, 14, 12, 11, 15, 14, 11, 15, 10, 14,
               11, 14, 13, 13, 11, 14, 11, 16, 11, 11, 15, 13, 14, 15, 13, 16, 10]
AlturaAlunos = [1.3, 1.8, 1.3, 1.5, 1.6, 1.5, 1.6, 1.8, 1.3, 1.5, 1.2, 1.2, 1.4, 1.3,
                1.5, 1.2, 1.6, 1.5, 1.6, 1.8, 1.3, 1.5, 1.2, 1.2, 1.5, 1.6, 1.8, 1.3, 1.25, 1.33]


def ObterMediaAlturas(vetorAltura):
    media = 0
    for altura in vetorAltura:
        media += altura
    media = media/30
    return media


def ObterQuantidadeAlunos(media, vetorAltura, vetorIdade):
    quantidade = 0
    for aluno in range(29):
        if(vetorIdade[aluno] > 13 and vetorAltura[aluno] < media):
            quantidade += 1
    return quantidade


print(f"A quantidade de alunos cuja idade é maior que 13 e altura menor que a media: {ObterMediaAlturas(AlturaAlunos)} é {ObterQuantidadeAlunos(ObterMediaAlturas(AlturaAlunos),AlturaAlunos,IdadeAlunos)} alunos")
