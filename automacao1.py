import pandas as pd

# Ler o arquivo CSV
df = pd.read_csv('dados.csv')

# Calcular a média de idade
media_idade = df['Idade'].mean()

# Imprimir o resultado
print("A média de idade das pessoas é:", media_idade)