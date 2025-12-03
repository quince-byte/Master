"""
Defino una función que reciba una cadena de texto
y vaya sumando +1 a cada key del diccionario cuando se encuentre cada letra"""
def counter(text) -> dict:
    dict = {}
    for char in text.replace(" ",""):
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
    return dict

asku = input("Ingrese un texto: ")
print(counter(asku))