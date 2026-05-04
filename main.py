'''
    Ana precisa de um programa simples para gerenciar suas tarefas diárias. Ela quer poder adicionar, visualizar e remover tarefas de uma lista.

    Crie um programa com um menu interativo que permita ao usuário adicionar, visualizar e remover tarefas. Use uma lista para armazenar as tarefas.
'''
import os
import json

'''
    Listas globais
'''
tarefas = []
tarefas_concluidas = []
ARQUIVO_JSON = 'krid3r_tasks.json'

def salvar_dados():
    '''Salva o estado atual das listas no arquivo JSON'''

    dados = {
        'ativas': tarefas,
        'concluidas': tarefas_concluidas
    }

    with open(ARQUIVO_JSON, 'w', encoding='utf-8') as f: json.dump(dados, f, indent=4, ensure_ascii=False)


def carregar_dados():
    '''
        Carrega os dados do arquivo JSON para as listas globais
    '''

    global tarefas, tarefas_concluidas

    if os.path.exists(ARQUIVO_JSON):
        with open(ARQUIVO_JSON, 'r', encoding='utf-8') as f:
            try:
                dados = json.load(f)
                tarefas = dados.get('ativas', [])
                tarefas_concluidas = dados.get('concluidas', [])
            except json.JSONDcodeError:
                tarefas, tarefas_concluidas = [], []
            

def exibir_nome_do_gerenciador():

    '''Exibe o nome do programa'''

    print('''
        K̠̠͙r̢͙i̺̪͙d͕͔͍3̙͚̪r̢͙͎T̙͕̘a̝͔͉s͇͎͜k̙͎͜s̢͙͎ -͓͙͜ G̡̢̝e͖͕͉r͚̞̼e͎̝͔n͓͉c̙͇͕i̙͙͔a̪̙͜d̪̺̫o̡̙͇r̼͉ d͕͚e͙̞ t͇̙̪a̢͕̫r̢̪͔e͙̺͜f͎͉̝a̢̘s̟͓̺
''')
    

def exibir_opcoes():

    '''Exibe as opções disponíveis no menu principal'''

    print('1. Adicionar tarefa')
    print('2. Visualizar tarefas ativas')
    print('3. Marcar tarefa como concluída')
    print('4. Listar tarefas concluídas')
    print('5. Sair\n')


def finalizar_gerenciador():

    '''Exibe mensagem de finalização do gerenciador'''

    exibir_subtitulo('Saindo do gerenciador de tarefas. Até mais!')


def voltar_ao_menu_principal():
    '''
    Solicita uma tecla para retornar ao menu principal
    '''

    input('\nDigite "Enter" para voltar ao menu.')
    main()


def opcao_invalida():

    '''
    Exibe mensagem de opção inválida e retorna ao menu principal.

    Outputs:
    - Tetorna ao menu principal
    '''

    print('Opção inválida! Escolha uma opção entre 1 e 5.\n')
    voltar_ao_menu_principal()


def exibir_subtitulo(texto):

    '''Exibe um subtítulo estilizado na tela 
    
    Inputs:
    - texto: str - O texto do subtítulo'''

    os.system('cls')
    linha = '*' * (len(texto) + 4)
    print(linha)
    print(texto)
    print(linha)
    print()

def input_obrigatorio(mensagem):
    '''
    Evita que o título das tarefas fiquem vazios ou com espaços adicionais
    '''
    while not (valor := input(mensagem).strip()):
        print('Este campo é obrigatório!')
    return valor

def adicionar_nova_tarefa():

    exibir_subtitulo('Adicionar nova tarefa')
    '''
        Verificando se o título já existe
    '''
    while True:
        titulo_da_tarefa = input_obrigatorio('Digite o título: ')
        # Validando o que ACABOU de ser digitado
        if any(t['titulo'].lower() == titulo_da_tarefa.lower() for t in tarefas + tarefas_concluidas):
            print(f'Erro: O título "{titulo_da_tarefa}" já existe!')
        else:
            # Se não existe, saímos do loop com a variável 'titulo_da_tarefa' pronta para usar
            break

    descricao = input('Digite a descrição da tarefa: ')
    dados_da_tarefa = {'titulo':titulo_da_tarefa, 'descrição':descricao, 'concluida':False}
    tarefas.append(dados_da_tarefa)
    salvar_dados() # Salva no JSON após adicionar
    print(f'Tarefa {titulo_da_tarefa} adicionada com sucesso!')
    voltar_ao_menu_principal()


def visualizar_tarefas_ativas():

    exibir_subtitulo('Visualizar tarefas ativas')
    
    if not tarefas:
        print('Nenhuma tarefa cadastrada.')
    else:
        print(f'{'Título da tarefa'.ljust(20).upper()} | {'Descrição'.ljust(20).upper()} | {'Status'.upper()}')
        for tarefa in tarefas:
            titulo_tarefa = tarefa['titulo']
            descricao = tarefa['descrição']
            concluida = 'Concluída' if tarefa['concluida'] else 'Ativa'
            print(f'- {titulo_tarefa.ljust(20)} | {descricao.ljust(20)} | {concluida}')
    
    voltar_ao_menu_principal()


def marcar_tarefa_como_concluida():

    exibir_subtitulo('Marcar tarefa como concluída')
    titulo_tarefa = input_obrigatorio('Digite o nome da tarefa que deseja marcar como concluída: ')
    tarefa_encontrada = None

    for tarefa in tarefas:
        if titulo_tarefa.lower() == tarefa['titulo'].lower():
            tarefa_encontrada = tarefa
            break
    
    if tarefa_encontrada:
        tarefa_encontrada['concluida'] = True
        tarefas_concluidas.append(tarefa_encontrada)
        tarefas.remove(tarefa_encontrada)
        salvar_dados() # Salva no JSON após mover
        print(f'A tarefa "{tarefa_encontrada["titulo"]}" foi concluída com sucesso!')
    else:
        print('Tarefa não encontrada.')

    voltar_ao_menu_principal()


def listar_tarefas_concluidas():

    exibir_subtitulo('Listar tarefas concluídas')
    
    if not tarefas_concluidas:
        print('Nenhuma tarefa concluída.')
    else:
        print(f'{'Título da tarefa'.ljust(20).upper()} | {'Descrição'.ljust(20).upper()} | {'Status'.upper()}')
        for tarefa in tarefas_concluidas:
            titulo_tarefa = tarefa['titulo']
            descricao = tarefa['descrição']
            concluida = 'Concluída' if tarefa['concluida'] else 'Ativa'
            print(f'- {titulo_tarefa.ljust(20)} | {descricao.ljust(20)} | {concluida}')
    
    voltar_ao_menu_principal()



def escolher_opcao():

    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        match opcao_escolhida:
            case 1:
                adicionar_nova_tarefa()

            case 2:
                visualizar_tarefas_ativas()

            case 3:
                marcar_tarefa_como_concluida()

            case 4:
                listar_tarefas_concluidas()

            case 5:
                finalizar_gerenciador()

            case _:
                opcao_invalida()

    except ValueError:
        opcao_invalida()


def main():

    '''Função principal que inicia o programa'''

    #inicializa os dados na primeira execução
    if not tarefas and not tarefas_concluidas:
        carregar_dados()

    os.system('cls')
    exibir_nome_do_gerenciador()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()