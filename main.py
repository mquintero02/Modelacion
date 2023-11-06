import json

def introduce_Peso(i,j,w,z,peso):
    ruta1= {"origen": f'calle: {i} carrera: {j}', "destino": f'calle: {w} carrera: {z}', "tiempo": peso}
    return ruta1

def main():
    rutas = {
        "rutaJavier":[]
    }
    x=50
    while x<=55:
        y=10
        while y <=14:
            if x==51:
                ruta1 = introduce_Peso(x,y,x,y+1,10)
                ruta2 = introduce_Peso(x,y+1,x,y,10)
            elif y==11 or y==12 or y==13 or y==14:
                ruta1 = introduce_Peso(x,y,x,y+1,7)
                ruta2 = introduce_Peso(x,y+1,x,y,7)
            else:
                ruta1 = introduce_Peso(x,y,x,y+1,5)
                ruta2 = introduce_Peso(x,y+1,x,y,5)
            if x != 55:
                if x ==51 or x+1==51:
                    ruta3= introduce_Peso(x,y,x+1,y,10)
                    ruta4= introduce_Peso(x+1,y,x,y,10)
                elif y==12 or y==13 or y==14:
                    ruta3=introduce_Peso(x,y,x+1,y,7)
                    ruta4=introduce_Peso(x+1,y,x,y,7)
                else:
                    ruta3= introduce_Peso(x,y,x+1,y,5)
                    ruta4= introduce_Peso(x+1,y,x,y,5)
            rutas["rutaJavier"].append(ruta1)
            rutas["rutaJavier"].append(ruta2)
            rutas["rutaJavier"].append(ruta3)
            rutas["rutaJavier"].append(ruta4)
            y=y+1
        x=x+1
    print(len(rutas["rutaJavier"]))
    print(rutas["rutaJavier"])

main()