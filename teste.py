def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = usuarios
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            usuario.append(usuarios_filtrados)

    return usuarios_filtrados[0] if usuarios_filtrados else "none"