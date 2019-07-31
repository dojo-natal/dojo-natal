import unittest


def brainfuck(entrada, instrucoes):
    entrada = list(entrada)
    instrucoes = list(instrucoes)
    vetor = [0] * 30000 # assim como todas as posições do vetor.
    ponteiro = 0  # O ponteiro sempre começa com valor 0
    output_buffer = []

    while instrucoes:
        instrucao = instrucoes.pop(0)
        if instrucao == ">":
            ponteiro += 1
        if instrucao == "<":
            ponteiro -= 1
        if instrucao == "+":
            vetor[ponteiro] += 1
        if instrucao == "-":
            vetor[ponteiro] -= 1
        if instrucao == ",":
            if len(entrada) > 0:
                vetor[ponteiro] = ord(entrada.pop(0))
            else:
                vetor[ponteiro] = 0
        if instrucao == ".":
            output_buffer.append(chr(vetor[ponteiro]))

    return "".join(output_buffer)

