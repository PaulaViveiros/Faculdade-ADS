# Criando um dicionário com suas matérias e notas fictícias
materias_notas = {
    "POO": 9.5,
    "SQL": 8.0,
    "Web": 10.0,
    "Engenharia": 8.5
}

print("--- MEU DESEMPENHO ---")

# Aqui acontece o DESEMPACOTAMENTO no 'for'
# O .items() entrega (Chave, Valor) e o for já guarda em 'materia' e 'nota'
for materia, nota in materias_notas.items():
    if nota >= 9.0:
        status = "Excelente!⭐"
    elif nota >= 7.0:
        status = "Aprovada!✅"
    else:
        status = "Estudar mais📚"
    
    print(f"Matéria: {materia:10} | Nota: {nota:.1f} | Status: {status}")

print("----------------------")