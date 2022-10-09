def arithmetic_arranger(problems, solver = False):
    # Variáveis gerais 

    numeroCima = ""
    numeroBaixo = ""
    linha = ""
    resultadoConta = ""
    formatoTotal = ""

    # Checagem de limite 

    if len(problems) > 5:
        return "Error: Too many problems."

    # Armazenando cada item em sua variável

    for problem in problems: 
        primeiroNumero = ""
        segundoNumero  = ""
        operador = ""
        primeiroNumero = problem.split()[0]
        operador = problem.split()[1]
        segundoNumero = problem.split()[2]

    # Validando os itens antes da formatação 

        if primeiroNumero.isdigit() and segundoNumero.isdigit():
            if len(primeiroNumero) > 4 or len(segundoNumero) > 4:
                return "Error: Number cannot be more than four digits."
        else: 
            return "Error: Numbers must only contain digits."

        resultado = ""

        if operador == "+":
            resultado = str(int(primeiroNumero) + int(segundoNumero))
        elif operador == "-":
            resultado = str(int(primeiroNumero) - int(segundoNumero))
        else: 
            return "Error: Operator must be '+' or '-'."

    # Distância
        distancia = max(len(primeiroNumero), len(segundoNumero)) + 2
    
    # Preenchimento 
        if problem != problems[-1]:
            numeroCima = numeroCima + str(primeiroNumero.rjust(distancia)) + "    "
            numeroBaixo = numeroBaixo + operador + str(segundoNumero.rjust(distancia - 1)) + "    "
            linha = linha + "-" * distancia + "    "
            resultadoConta = resultadoConta + resultado.rjust(distancia) + "    "
        else:
            numeroCima = numeroCima + str(primeiroNumero.rjust(distancia))
            numeroBaixo = numeroBaixo + operador + str(segundoNumero.rjust(distancia - 1)) 
            linha = linha + "-" * distancia 
            resultadoConta = resultadoConta + resultado.rjust(distancia)


    # Formatação 
    if solver:
        formatoTotal = numeroCima + "\n" + numeroBaixo + "\n" + linha + "\n" + resultadoConta 
    else:
        formatoTotal = numeroCima + "\n" + numeroBaixo + "\n" + linha
    return formatoTotal

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))

