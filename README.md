# Sistema Bancário 2.0

Este é um projeto de **Sistema Bancário** desenvolvido em Python. O foco principal é oferecer uma solução inicial para operações bancárias, como **depósito**, **saque** e **emissão de extrato**.

## Funcionalidades

- **Depositar**: Adicione valores ao saldo da conta.
- **Sacar**: Realize retiradas do saldo, respeitando os limites estabelecidos:
  - Limite de saque diário de R$ 500,00.
  - Limite máximo de 3 saques por dia.
- **Extrato**: Consulte todas as transações realizadas (depósitos e saques) e o saldo disponível.

## Como Executar o Projeto

1. Certifique-se de que o [Python](https://www.python.org/) esteja instalado na sua máquina.
2. Clone o repositório do projeto:
   ```bash
   git clone https://github.com/SantosKelvinBr/Criando_um_Sistema_Bancario_com_Python

## Estrutura do Código

O sistema é baseado em um menu interativo que permite ao usuário escolher entre diferentes opções de operação:

- **Depositar**: Solicita o valor a ser depositado e atualiza o saldo.
- **Sacar**: Verifica se o valor é válido, atende às condições de saldo e limites, e processa o saque.
- **Extrato**: Exibe um relatório das transações e o saldo atual.
- **Sair**: Encerra o programa.

## Limitações da Versão 1.0 --- main_old.py

- Não há autenticação de usuário.
- Apenas uma conta é suportada.
- Operações limitadas a saque, depósito e consulta de extrato.

- ## Limitações da Versão 2.0

- Não há autenticação de usuário.
- Operações limitadas a saque, depósito e consulta de extrato.

## Melhorias Futuras

- Implementação de autenticação para maior segurança.
- Suporte a múltiplas contas. ( Suportado na nova versão)
- Integração com um banco de dados para armazenar transações.
- Adição de uma interface gráfica para facilitar a interação com o sistema.


   
