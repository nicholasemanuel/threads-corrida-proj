# 🏁 Simulador de Corrida com Threading

Este projeto simula uma corrida virtual em que cada carro é representado por uma **thread**. O foco principal é demonstrar o uso de **concorrência** e **sincronização de threads** em Python, especialmente quando múltiplas threads competem por **recursos compartilhados**, como trechos críticos da pista (ex: ponte ou curva estreita).

## 📌 Objetivos

- Simular uma corrida onde cada carro é uma thread independente.
- Criar um trecho crítico onde apenas um carro pode passar por vez.
- Utilizar **mecanismos de sincronização** (`Lock`) para controlar o acesso ao recurso compartilhado.
- Registrar a ordem de chegada dos carros com segurança.

## ⚙️ Tecnologias Utilizadas

- **Python 3.12.2+**
- Biblioteca padrão `threading`
- `random` e `time` para simulação
