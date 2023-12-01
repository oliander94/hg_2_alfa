def agregar_alias(items, alias_map):
    output = []
    for item in items:
        output.append(item)
        if item in alias_map:
            output.extend(alias_map[item])
    return output

items = [100,200,300,400,500,600,700]
alias_map = {500: ['qux', 'thud']}

result = agregar_alias(items, alias_map)
print(result) # > [100,200,300,400,500,qux,thud,600,700]