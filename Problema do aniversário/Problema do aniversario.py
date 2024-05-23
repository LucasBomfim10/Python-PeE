import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


Dias = 365

# Função que calcula a probabilidade de duas pessoas terem a mesma data de aniversário


def Probabilidade_Aniversario(Num_Pessoas):

    Probabilidade = 1
    for i in range(Num_Pessoas):
        Probabilidade = np.prod((Dias - np.arange(Num_Pessoas)) / Dias)
    return ((1 - Probabilidade)*100)


while True:
    Num_Pessoas = input("Digite o número de pessoas: ")
    if Num_Pessoas.isdigit() and int(Num_Pessoas) > 0:
        Num_Pessoas = int(Num_Pessoas)
        break
    else:
        print("Digite um número inteiro e maior que 0")


print(
    f"A probabilidade de duas pessoas terem a mesma data de aniversário é de: {Probabilidade_Aniversario(Num_Pessoas):.4f}%")


Probabilidades = []


for i in range(1, 366):
    Probabilidades.append(Probabilidade_Aniversario(i))

plt.figure()

plt.plot(range(1, 366), Probabilidades)

plt.title("Probabilidade por número de pessoas")

plt.xlabel("Número de pessoas")
plt.ylabel("Probabilidade (%)")

plt.show()

df = pd.DataFrame({"Número de pessoas": range(1, 366),
                  "Probabilidade (%)": Probabilidades})

df.to_csv("Probabilidade_Aniversario.csv", index=False)
