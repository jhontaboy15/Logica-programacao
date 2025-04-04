# -*- coding: utf-8 -*-
"""Meu primeiro Algoritimo.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1csGX3O7ypRVJ7lgf-uTO5OVgD4R06e-U

#Operador Aritmético
"""

# Adição
10 + 2

# Subtração
10 - 2

# Multiplicação
10 * 2

# Divisão
10 / 2

# Divisão inteira
10 // 2

# Resto da divisão
10 % 2

# Potenciação
10 ** 2

"""# Operadores de relacionais"""

# Menor
10 < 2

# Menor ou Igual
10 <- 2

# Maior
10 > 2

# Maior ou Igual
10 >- 2

# Igual
7 == 7

# Diferente
7 != 7

"""#Operadores Lógicos

*   And
*   Or
*   Not

#Tabela Verdade

And
"""

print(5 > 7 and 6 < 2)     # V and V - V
print(10 > 20 and 5 > 6)     # V and F - F
print(11 < 15 and 25 < 60)     # V and F - F
print(15 < 10 and 20 > 6)     # F and F - F

"""Or"""

print(10 > 2 or 4 < 6)      # V or V - V
print(10 > 2 or 4 > 6)      # V or F - V
print(10 < 2 or 4 < 6)      # V or F - V
print(10 < 2 or 4 > 6)      # F or F - F

"""Not"""

not 10 > 2    # V - F

not 10 < 2    # F - V

"""#Variáveis

Variáveis estão alocadas em espaços na memória
"""

# Nome da variável é "x" que armazena o valor em um espaço na memória
x = 10

   print(x) #Utilizar a referencia no nome atribuido

"""Regras

**Case Sensitive**

A != a

**Boas Práticas com Variáveis**
   
> Exemplo: Multiplicação de 2 números


Não usar

  *   Multiplicação
  *   MultiplicaçãoDeDoisNumeros
  *   M

Usar

*   Multiplicacao
*   Mult
*   Mult_total (snake_case)

Tipos de Variáveis

  Python é uma linguagem de alto nível
  
  Não é Necessário especificar o tipo de dados quando declarar a variável
  
  Python defini o tipo de dados na declaração
"""