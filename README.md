# 🏦 Banco Py

Simulador de banco em Python, feito via terminal, com cadastro de clientes, criação de contas e operações bancárias básicas (depósito, saque e consulta de saldo).

Projeto desenvolvido como estudo de **Programação Orientada a Objetos**, **tratamento de erros** e **validação de dados** em Python.

## ✨ Funcionalidades

- Cadastro de clientes (nome, CPF e telefone)
- Validação de CPF (aceita formatos com ou sem pontuação, exige 11 dígitos)
- Validação de telefone (aceita fixo ou celular, com DDD)
- Criação de contas vinculadas a um cliente
- Depósito e saque, com validação de valores (não aceita números negativos, zero ou texto)
- Consulta de saldo
- Listagem de clientes e contas cadastradas
- Tratamento de erros de digitação em todas as entradas numéricas (evita que o programa quebre)

## 🛠️ Tecnologias

- Python 3 (sem bibliotecas externas)
- Programação Orientada a Objetos (classes `Cliente` e `ContaBancaria`)

## ▶️ Como executar

1. Clone o repositório:
   ```bash
   git clone <url-do-repositorio>
   ```
2. Entre na pasta do projeto e rode:
   ```bash
   python banco.py
   ```
3. Use o menu interativo no terminal para navegar entre as opções.

## 📋 Menu

```
1. Cadastrar cliente
2. Listar clientes
3. Criar conta
4. Listar contas
5. Depositar
6. Sacar
7. Mostrar saldo
8. Sair
```

## 🧠 O que aprendi com este projeto

- Estruturar um programa com classes e objetos
- Validar entradas do usuário de forma robusta (`try/except`, loops de repetição até obter um dado válido)
- Escrever funções reutilizáveis para leitura segura de dados (`ler_int`, `ler_float`, `verifica_num`, `validar_cpf`, `validar_tel`)
- Fluxo de trabalho com Git/GitHub, incluindo resolução de conflitos de merge entre dois computadores

## 🚀 Próximos passos

- [ ] Separar o código em múltiplos arquivos/módulos (classes, funções de validação e menu principal), já que o projeto está com mais de 200 linhas
- [ ] Persistir dados em arquivo (JSON ou banco de dados) para não perder os cadastros ao fechar o programa
- [ ] Adicionar histórico de transações por conta
- [ ] Permitir múltiplas contas por cliente

---

Projeto pessoal desenvolvido como parte dos estudos em Python.
