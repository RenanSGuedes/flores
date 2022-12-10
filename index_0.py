print("Olá Hygor")
import numpy as np
import csv


with open("iris.csv",'r') as Dados: # matriz sem a 1st row
    leitor =  csv.reader(Dados)
    lista =  list(leitor)
    lista.remove(lista[0])
    
        
    

class Teste:
    def __init__(self):
        self.matriz = np.array(lista)
        self.transposta = np.array(self.matriz).T
        self.numeros = np.array(np.delete(self.matriz,4,1), dtype = 'float')
        self.numeros_transpostos = np.array(self.numeros).T
       
        


    def estatisticas(self):
        print("resumo base de dados")
        print("tamanho da amostra: 150 elementos")
        print("tipo:")
        print("Setosas:",np.count_nonzero(self.matriz == 'setosa'))
        print("Versicolores:",np.count_nonzero(self.matriz == 'versicolor'))
        print("Virginicas:",np.count_nonzero(self.matriz == 'virginica'))
        print("  Comprimento_sepala:")
        print("      máximo:", np.max(self.numeros_transpostos[0]))
        print("      minimo:", np.min(self.numeros_transpostos[0]))
        print("      média:", np.mean(self.numeros_transpostos[0]))
        print("      VAR:", np.var(self.numeros_transpostos[0]))
        print("       DP:", np.std(self.numeros_transpostos[0]))
        print("   Largura_sepala:")
        print("      máximo:", np.max(self.numeros_transpostos[1]))
        print("      minimo:", np.min(self.numeros_transpostos[1]))
        print("      média:", np.mean(self.numeros_transpostos[1]))
        print("      VAR:", np.var(self.numeros_transpostos[1]))
        print("       DP:", np.std(self.numeros_transpostos[1]))
        print("   Comprimento_petala:")
        print("      máximo:", np.max(self.numeros_transpostos[2]))
        print("      minimo:", np.min(self.numeros_transpostos[2]))
        print("      média:", np.mean(self.numeros_transpostos[2]))
        print("      VAR:", np.var(self.numeros_transpostos[2]))
        print("       DP:", np.std(self.numeros_transpostos[2]))
        print("   Largura_petala:")
        print("      máximo:", np.max(self.numeros_transpostos[3]))
        print("      minimo:", np.min(self.numeros_transpostos[3]))
        print("      média:", np.mean(self.numeros_transpostos[3]))
        print("      VAR:", np.var(self.numeros_transpostos[3]))
        print("       DP:", np.std(self.numeros_transpostos[3]))
         
        
        
       




if __name__ == '__main__':
    t1 = Teste()

Teste()
