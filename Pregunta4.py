"""Iterando una lista con los tres valores posibles de temperatura que recibe la 
función del punto 5, hacer un print para cada combinación de los mismos"""

temperaturas = ["alta", "media", "baja"]

for temp1 in temperaturas:
    for temp2 in temperaturas:
        for temp3 in temperaturas:
            print(f"Combination: {temp1}, {temp2}, {temp3}")



