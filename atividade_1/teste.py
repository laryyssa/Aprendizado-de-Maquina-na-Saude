import seaborn as sns

# Carregar um conjunto de dados fictício
dados = sns.load_dataset("iris")

# Criar uma matriz de gráficos de dispersão
sns.pairplot(dados)

# Mostrar o gráfico
plt.show()
