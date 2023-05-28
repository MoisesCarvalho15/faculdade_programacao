"""
- Se a nota for MAIOR OU IGUAL a 7, o estudante foi aprovado.
- Se a nota for MENOR que 7 e MAIOR OU IGUAL a 5, o estudante está em recuperação
- Se a nota for MENOR que 5, o estudante está reprovado.
"""

nota = 5

if nota >= 7:
    print("Aprovado!")
elif nota >= 5:
    print("Recuperação!")
else:
    print("Reprovado!")
