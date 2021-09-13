segundos = int(input("Por favor entre com o número de segundos que deseja converter: "))

dias = segundos // (60*60*24)
segundos_restantes = segundos % (60*60*24)
horas = segundos_restantes // (60*60)
segundos_restantes = segundos_restantes % (60*60)
minutos = segundos_restantes // 60
segundos_final = segundos_restantes % 60

print(dias,"dias,",horas,"horas,",minutos,"minutos e",segundos_final,"segundos.")