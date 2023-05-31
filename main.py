from gerador_pdf import gera_pdf

cliente = input("Informe o cliente: ")
projeto = input("Digite uma descrição do projeto: ")
hora_estimada = input("Digite a quantidade de horas estimadas do projeto: ")
valor_hora = input("Digite o valor da hora trabalhada: ")
prazo = input("Informe o prazo para entrega do projeto: ")

total_orcamento = int(hora_estimada) * int(valor_hora)
print(total_orcamento)

gera_pdf(cliente, projeto, hora_estimada, valor_hora, prazo, total_orcamento)