# def exibir_mensagem():
#     print("Ola mundo")

# def exibir_mensagem_2(nome):
#     print(f"Seja bem vindo {nome}!")

# def exibir_mensagem_3(nome="Aiko"):
#     print(f"Seja bem vindo {nome}!")

# exibir_mensagem()
# exibir_mensagem_2(nome="pamonha")
# exibir_mensagem_3()
# exibir_mensagem_3(nome="aikozinha")


# def calcular_total(numeros):
#     return sum(numeros)

# def retorna_antecessor_e_sucessor(numero):
#     antecessor = numero - 1
#     sucessor = numero + 1

#     return antecessor, sucessor

# print (calcular_total([10,30,50]))
# print (retorna_antecessor_e_sucessor(10))

# def salvar_carro_do_cliente (marca, modelo, ano, placa):
#     print(f"Carro salvo com sucesso:{marca}/{modelo}/{ano}/{placa}")

# salvar_carro_do_cliente ("Fiat", "MOBI", 2019, "CAI-1213")
# salvar_carro_do_cliente (marca="Fiat", modelo="MOBI", ano=2019, placa="CAI-1213")

def exibir_poema(data_extenso, *tupulas, **dicionarios):
    texto = "\n".join(tupulas)
    dados = "\n".join([f"{chave.title()}: {valor}"for chave, valor in dicionarios.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{dados}"
    print (mensagem)

exibir_poema(
    "Sexta feira, 16 de junho de 2024", #primeiro parametro é puxado primeiro
    "poema teste",# tupulas ou args
    "poema teste",# tupulas ou args
    "poema teste",# tupulas ou args
    "poema teste",# tupulas ou args
    "poema teste",# tupulas ou args
    autor = "Aiko M",# dicionarios ou kwargs
    Ano = 2024,# dicionarios ou kwargs
)






