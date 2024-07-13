# Formato de Cadenas en Python

var_hola = 'Hola'
var_mundo = 'Mundo'

# Imprimir los valores
print(var_hola, var_mundo)

# Concacatenación de cadenas (unir dos o mas cadenas, +)
var_hola_mundo = var_hola + ' ' + var_mundo
print(var_hola_mundo)

# Interpolacion de cadenas, usando la letra f
var_hola_mundo = f'Mi cadena: {var_hola} {var_mundo}'
print(var_hola_mundo)

# Interpolacion con multilineas f''' '''
print(f'''Mi cadena: 
    {var_hola} 
        {var_mundo} ''')
