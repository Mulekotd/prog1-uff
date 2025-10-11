turmas = int(input("Digite o número de turmas: "))

soma_total_notas = 0
total_alunos = 0

for i in range(1, turmas + 1):
    alunos = int(input(f"\nTurma {i} - quantidade de alunos: "))
    soma_notas = 0

    for j in range(1, alunos + 1):
        nota = float(input(f"Nota {j}: "))
        soma_notas += nota

    media_turma = soma_notas / alunos
    print(f"Média da turma {i}: {media_turma:.1f}")

    # Acumula para o cálculo geral
    soma_total_notas += soma_notas
    total_alunos += alunos

# Média geral considerando todos os alunos
media_geral = soma_total_notas / total_alunos
print(f"\nMédia geral de todas as turmas: {media_geral:.1f}")
