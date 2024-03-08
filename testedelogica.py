"""int INDICE = 13, SOMA = 0, K = 0;

enquanto K < INDICE faça

{

K = K + 1;

SOMA = SOMA + K;

}

imprimir(SOMA);

O valor da variavel soma será de 91

"""

def fibonacci(n):
    seq_fibonacci = [0, 1]
    while seq_fibonacci[-1] < n:
        seq_fibonacci.append(seq_fibonacci[-1] + seq_fibonacci[-2])
    return seq_fibonacci

def pertence_fibonacci(numero):
    seq_fibonacci = fibonacci(numero)
    return numero in seq_fibonacci

def main():
    num = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))
    if pertence_fibonacci(num):
        print(f"O número {num} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {num} não pertence à sequência de Fibonacci.")

if __name__ == "__main__":
    main()
   



    
"""
3) a) 1,3,5,7,9 (a lógica aqui é adicionar 2 ao numero anterior)
   b) 2,4,8,16,32,64,128 (Cada número é o dobro do anterior)
   c)0,1,4,9,16,25,36,49 (Esses são os quadrados dos números naturais começando de 0.)
   d)4,16,36,64,100: (Esses são os quadrados dos números pares em ordem crescente.)
   e)1,1,2,3,5,8,13: (Esta é a sequência de Fibonacci.)
   f)2,10,12,16,17,18,19,20:(sequência segue a lógica de adicionar números em sequência ou com base em uma progressão.)
"""

"""
4) Preparação:
Ligue o primeiro interruptor por um curto período e depois disso desligue o mesmo que ligou.
Ligue o segundo interruptor.
Observação:
Se uma lâmpada estiver acesa, o primeiro interruptor controla essa lâmpada.
Se uma lâmpada estiver desligada e quente, o segundo interruptor controla essa lâmpada.
Se uma lâmpada estiver desligada e fria, o terceiro interruptor controla essa lâmpada.
"""

def inverter_string(string_original):
    string_invertida = ""
    for indice in range(len(string_original) - 1, -1, -1):
        string_invertida += string_original[indice]
    return string_invertida

# Exemplo de uso
string_original = input("Digite uma string para inverter: ")
string_invertida = inverter_string(string_original)
print("String original:", string_original)
print("String invertida:", string_invertida)
