# def criar_carro(modelo,ano,placa, / ,marca,motor,combustivel):
#     print(modelo,ano,placa,marca,motor,combustivel)

# criar_carro("Mobi", 2019, "ABC-1718", marca="Fiat", motor="1.0", combustivel="Gasolina")
# # sistema valido

# # criar_carro(modelo="Mobi", ano=2019, placa="ABC-1718", marca="Fiat", motor="1.0", combustivel="Gasolina")
# # # sistema invalido!!!
# # #invalido pois nao seguiu os padroes exigidos para melhor legibilidade do codigo

# def criar_carro(* ,modelo,ano,placa,marca,motor,combustivel):
#     print(modelo,ano,placa,marca,motor,combustivel)

# criar_carro(modelo="Mobi", ano=2019, placa="ABC-1718", marca="Fiat", motor="1.0", combustivel="Gasolina")

def somar(a,b):
    return a + b

def exibir_resultado(a,b,funcao):
    resultado = funcao (a,b)
    print (f"O resultado da operaçao {a} + {b} = {resultado}")

exibir_resultado(10,10,somar)





