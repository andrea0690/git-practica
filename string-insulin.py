# Store the human preproinsulin sequence in a variable called preproinsulin:

#preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktr" \
#"reaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"

# Almacenamos cada secuencia de elementos
lsInsulin="malwmrllpllallalwgpdpaaa"
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"
aInsulin = "giveqcctsicslyqlenycn"
cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"

insulin = bInsulin + aInsulin

print("Imprimir el valor de la insulina sin procesar")

print("La secuencia de insulina, cadena a: " + aInsulin)

# Creating a list of the amino acid (AA) weights  
aaWeights = {'A': 89.09, 'C': 121.16, 'D': 133.10, 'E': 147.13, 'F': 165.19,
'G': 75.07, 'H': 155.16, 'I': 131.17, 'K': 146.19, 'L': 131.17, 'M': 149.21,
'N': 132.12, 'P': 115.13, 'Q': 146.15, 'R': 174.20, 'S': 105.09, 'T': 119.12,
'V': 117.15, 'W': 204.23, 'Y': 181.19} 


#contar las veces que aparece un aminoacido en la secuencia.

aminoacidos = ['A', 'C',
'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T',
'V', 'W', 'Y']


conteo = {}
for letra in aminoacidos:
    conteo[letra]= insulin.count(letra.lower())
print(conteo)

peso =0
for x in aminoacidos:
    peso += conteo[x]*aaWeights[x]
    
    print(peso)