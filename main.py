import threading
import time
import random

# trecho crítico
trecho_critico = threading.Lock()

# lista para armazenar a ordem de chegada
ordem_chegada = []
chegada_lock = threading.Lock()

class Carro(threading.Thread):
    def __init__(self, nome):
        super().__init__()
        self.nome = nome

    def run(self):
        print(f"{self.nome} começou a corrida!")

        # início da corrida (livre)
        self.andar("reta inicial")

        # trecho crítico
        self.entrar_trecho_critico("ponte")

        # parte final da corrida
        self.andar("reta final")

        # registro da chegada (com lock)
        with chegada_lock:
            ordem_chegada.append(self.nome)
            print(f"{self.nome} cruzou a linha de chegada!")

    def andar(self, trecho):
        tempo = random.uniform(0.5, 2.0)
        print(f"{self.nome} está passando pela {trecho} (tempo: {tempo:.2f}s)")
        time.sleep(tempo)

    def entrar_trecho_critico(self, nome_trecho):
        print(f"{self.nome} está esperando para entrar no trecho crítico: {nome_trecho}")
        with trecho_critico:
            print(f"{self.nome} entrou no trecho crítico: {nome_trecho}")
            time.sleep(random.uniform(0.5, 1.5))
            print(f"{self.nome} saiu do trecho crítico: {nome_trecho}")

# criando os carros (threads)
carros = [Carro(f"Carro {i+1}") for i in range(5)]

# iniciando a corrida
for carro in carros:
    carro.start()

# esperando todos terminarem
for carro in carros:
    carro.join()

# exibindo a ordem de chegada
print("\nOrdem de chegada:")
for i, nome in enumerate(ordem_chegada, start=1):
    print(f"{i}º - {nome}")