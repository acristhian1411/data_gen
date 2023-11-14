import os

# Ejecutar los scripts uno por uno
script_files = [
    'client_gen.py',
    'seller_gen.py',
    'provider_gen.py',
    'product_gen.py',
    'purchases_gen.py',
    'sales_gen.py'
]

generated_files = [
    'clientes.sql',
    'vendedores.sql',
    'proveedores.sql',
    'productos.sql',
    'compras.sql',
    'ventas.sql'
]

for index, script_file in enumerate(script_files):
    print(f"Ejecutando: {script_file}")
    os.system(f"python {script_file}")
    generated_files[index] = f"{generated_files[index]}"

# Unificar los archivos SQL generados
unified_file = 'datos_prueba_unificado.sql'

with open(unified_file, 'w') as outfile:
    for generated_file in generated_files:
        with open(generated_file, 'r') as infile:
            outfile.write(f"-- Archivo: {generated_file}\n")
            outfile.write(infile.read())
            outfile.write("\n\n")

print(f"Se han unificado los archivos SQL generados en '{unified_file}'.")
