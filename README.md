# Gerenciador de Tarefas - Krid3rTasks

Este é um projeto simples em Python para gerenciar tarefas diárias. O programa permite adicionar, visualizar, marcar como concluídas e listar tarefas concluídas, com persistência de dados em um arquivo JSON.

**Este é um projeto de estudos iniciais da linguagem Python, desenvolvido como parte da carreira "Desenvolvimento Back-End Python" da Alura.**

## Funcionalidades

- **Adicionar nova tarefa**: Permite criar uma nova tarefa com título único e descrição opcional.
- **Visualizar tarefas ativas**: Exibe uma lista das tarefas ainda não concluídas.
- **Marcar tarefa como concluída**: Move uma tarefa da lista ativa para a lista de concluídas.
- **Listar tarefas concluídas**: Mostra todas as tarefas que foram marcadas como concluídas.
- **Persistência de dados**: As tarefas são salvas automaticamente em um arquivo JSON (`krid3r_tasks.json`) e carregadas ao iniciar o programa.

## Como usar

1. Certifique-se de ter o Python instalado (versão 3.x recomendada).
2. Abra o terminal na pasta do projeto.
3. Execute o arquivo principal com:

```bash
python main.py
```

4. Navegue pelo menu interativo escolhendo as opções de 1 a 5.

## Estrutura do projeto

- `main.py` - Código principal do gerenciador de tarefas.
- `README.md` - Este arquivo de documentação.
- `.gitignore` - Arquivo para ignorar arquivos não versionáveis, como dados pessoais e cache do Python.
- `krid3r_tasks.example.json` - Arquivo de exemplo mostrando a estrutura de dados usada para armazenar as tarefas.

## Estrutura de Dados

As tarefas são armazenadas em um arquivo JSON com a seguinte estrutura:

```json
{
  "ativas": [
    {
      "titulo": "Título da tarefa",
      "descrição": "Descrição opcional da tarefa",
      "concluida": false
    }
  ],
  "concluidas": [
    {
      "titulo": "Tarefa concluída",
      "descrição": "Descrição da tarefa",
      "concluida": true
    }
  ]
}
```

Consulte o arquivo `krid3r_tasks.example.json` para ver um exemplo vazio da estrutura.

## Observações

- Os dados das tarefas são armazenados em um arquivo JSON local (`krid3r_tasks.json`), garantindo persistência entre execuções.
- O arquivo de dados não é versionado no Git para proteger informações pessoais.
- Este projeto é focado em conceitos básicos de Python, como listas, dicionários, manipulação de arquivos JSON e controle de fluxo.
