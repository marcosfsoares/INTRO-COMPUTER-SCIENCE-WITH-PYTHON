# escreva o seu programa
def main():
    alunos = int(input("Digite o numero de alunos: "))
    cont = alunos
    total = 0.0
    
    recup = 0
    repro = 0
    apro = 0
    muitobom = 0
    while cont > 0:
        nota = float(input("Digite a nota do aluno: "))
        if 0 <= nota <= 10:
            total = total+nota
            if nota < 3:
                repro = repro + 1
            elif 3 <= nota < 5:
                recup += 1
            elif nota > 8:
                muitobom = muitobom + 1
                apro += 1
            else:
                apro += 1
            
            cont -= 1
        else:
            print("Nota invalida")
            cont = -1
    if cont != -1:
        media = total / alunos
        print("Total de alunos=", alunos)
        print("A media do grupo=", media)
        print("Numero de alunos reprovados =", repro)
        print("Numero de alunos de recuperacao =", recup)
        print("Numero de alunos aprovados =", apro)
        print("Numero de alunos com desempenho muito bom =", muitobom)
    else:
        print("Por favor, reinicie o programa")


main()
