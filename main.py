import os

# Listas
clientes = []
agenda = []
horarios = []

# limpar tela
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Pausa
def pressione_enter():
    input("\nPressione ENTER para continuar...")

# Título
def show_title():
    print("=" * 40)
    print(" SISTEMA DE AGENDAMENTO BARBEARIA ")
    print("=" * 40)

# Mostrar menu
def show_menu(menu):
    clear_screen()
    show_title()

    if menu == "principal":
        print("1 - Cliente")
        print("2 - Horários")
        print("3 - Agenda")
        print("0 - Sair")

    elif menu == "cliente":
        print("1 - Novo Cliente")
        print("2 - Listar Clientes")
        print("3 - Excluir Cliente")
        print("0 - Voltar")

    elif menu == "agenda":
        print("1 - Novo Agendamento")
        print("2 - Listar Agenda")
        print("3 - Excluir Agendamento")
        print("0 - Voltar")

    elif menu == "horarios":
        print("1 - Cadastrar Horário")
        print("2 - Listar Horários")
        print("3 - Excluir Horário")
        print("0 - Voltar")

# Validar Horário
def horario_valido(horario):
    try:
        hora, minuto = horario.split(":")
        hora = int(hora)
        minuto = int(minuto)

        # Horário de funcionamento
        if hora < 8 or hora > 18:
            return False

        # Valida minutos (Intervalos de 30 min)
        if minuto not in [0, 30]:
            return False

        return True

    except:
        return False
        
# Verificar horário ocupado
def horario_ocupado(horario):
    for agendamento in agenda:
        if agendamento[2] == horario:
            return True
    return False

# Cadastrar horário
def cadastrar_horario():
    horario = input("Horário (HH:MM): ")

    if not horario_valido(horario):
        print("Horário inválido! Funcionamento: 08:00 às 18:00.")
        return

    if horario in horarios:
        print("Horário já cadastrado!")
        return

    horarios.append(horario)
    print("Horário cadastrado com sucesso!")

# Listar horários
def listar_horarios():
    if len(horarios) == 0:
        print("Nenhum horário cadastrado.")
        return

    for horario in sorted(horarios):
        print(horario)

# Excluir horário
def excluir_horario():
    horario = input("Digite o horário: ")

    if horario in horarios:

        for agendamento in agenda:
            if agendamento[2] == horario:
                print ("Existe um agendamento neste horário!")
                return

        horarios.remove(horario)
        print("Horário removido!")

    else:
        print("Horário não encontrado!")

# Cadastrar cliente
def novo_cliente():
    username = input("Username: ")
    email = input("Email: ")

    for cliente in clientes:
        if cliente[0] == username:
            print("Username já existe!")
            return

    clientes.append([username, email])
    print("Cliente cadastrado com sucesso!")

# Listar clientes
def listar_clientes():
    if len(clientes) == 0:
        print("Nenhum cliente cadastrado.")
        return

    for cliente in clientes:
        print(f"Username: {cliente[0]}")
        print(f"Email: {cliente[1]}")
        print("-" * 30)

# Excluir cliente
def excluir_cliente():
    username = input("Digite o username: ")

    for cliente in clientes:
        if cliente[0] == username:
            clientes.remove(cliente)
            print("Cliente removido!")
            return

    print("Cliente não encontrado!")

# Novo agendamento
def novo_agendamento():
    numero = len(agenda) + 1

    username = input("Username do cliente: ")

    cliente_existe = False

    for cliente in clientes:
        if cliente[0] == username:
            cliente_existe = True

    if not cliente_existe:
        print("Cliente não cadastrado!")
        return

    horario = input("Horário desejado: ")

    if horario not in horarios:
        print("Horário não cadastrado!")
        return

    if horario_ocupado(horario):
        print("Horário já ocupado!")
        return

    agenda.append([numero, username, horario])
    print("Agendamento realizado!")

# Listar agenda
def listar_agenda():
    if len(agenda) == 0:
        print("Nenhum agendamento.")
        return

    for agendamento in agenda:
        print(
            f"Agendamento {agendamento[0]} | "
            f"Cliente: {agendamento[1]} | "
            f"Horário: {agendamento[2]}"
        )

# Excluir agendamento
def excluir_agendamento():
    numero = int(input("Número do agendamento: "))

    for agendamento in agenda:
        if agendamento[0] == numero:
            agenda.remove(agendamento)
            print("Agendamento removido!")
            return

    print("Agendamento não encontrado!")

# Programada principal
while True:

    show_menu("principal")
    opcao = input("\nEscolha: ")

    if opcao == "1":

        while True:

            show_menu("cliente")
            opcao_cliente = input("\nEscolha: ")

            if opcao_cliente == "1":
                novo_cliente()
                pressione_enter()

            elif opcao_cliente == "2":
                listar_clientes()
                pressione_enter()

            elif opcao_cliente == "3":
                excluir_cliente()
                pressione_enter()

            elif opcao_cliente == "0":
                break

            else:
                print("Opcção inválida!")
                pressione_enter()

    elif opcao == "2":

        while True:
            
            show_menu("horarios")
            opcao_horario = input("\nEscolha: ")

            if opcao_horario == "1":
                cadastrar_horario()
                pressione_enter()

            elif opcao_horario == "2":
                listar_horarios()
                pressione_enter()

            elif opcao_horario == "3":
                excluir_horario()
                pressione_enter()

            elif opcao_horario == "0":
                break

            else:
                print("Opção inválida!")
                pressione_enter()

    elif opcao == "3":

        while True:

            show_menu("agenda")
            opcao_agenda = input("\nEscolha: ")

            if opcao_agenda == "1":
                novo_agendamento()
                pressione_enter()

            elif opcao_agenda == "2":
                listar_agenda()
                pressione_enter()

            elif opcao_agenda == "3":
                excluir_agendamento()
                pressione_enter()

            elif opcao_agenda == "0":
                break

            else:
                print("Opção inválida!")
                pressione_enter()

    elif opcao == "0":
        break

    else:
        print("Opção inválida!")
        pressione_enter()

clear_screen()
print("Programa encerrado.")