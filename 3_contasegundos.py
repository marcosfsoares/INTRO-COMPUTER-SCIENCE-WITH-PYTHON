# Converte segundos em dias, meses, horas, minutos e segundos
seg_total = input("Por favor, entre com o número de segundos que deseja converter:")

horas = int(seg_total) // 3600
seg_rest = int(seg_total) % 3600
minu = seg_rest // 60
seg = seg_rest % 60
dias = horas // 24
horas = horas % 24

print(dias, "dias,", horas, "horas,", minu, "minutos e", seg, "segundos.")
