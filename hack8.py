#definir la lista de valores
values = [100,200,300,400,500,600,700]

#definir el alias para reemplazar el valor 300
alias = "alfa"

#buscar y reemplazar el valor 300 con el alias
values[values.index(300)] = alias

#agregar el alias al final de la lista de valores
values += [alias]

#imprimir la lista de valores actualizada
print(values)