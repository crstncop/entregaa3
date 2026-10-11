class ADN:
    def __init__(self,id,nombre,secuencia:str,riesgo:int):
        self.id = id
        self.nombre = nombre
        self.secuencia: str = secuencia
        self.riesgo: int = riesgo
    
    def __repr__(self):
        return(f"ID: {self.id}, Nombre: {self.nombre}, Secuencia: {self.secuencia}, Riesgo: {self.riesgo}")

class secuencias:
    def __init__(self):
            self.secuencias = []

    def registrar(self, ADN,id,i=0):
        if i == len(self.secuencias):
            self.secuencias.append(ADN)
            return "secuencia agregada correctamente"
        if self.secuencias[i].id == id:
            return "Secuencia ya existe"
        return self.registrar(ADN,id,i+1)

    def contar_patron(self, secuencia, patron, i=0):
        if patron == "":
            return 0

        if i + len(patron) > len(secuencia):
            return 0

        actual = secuencia[i:i + len(patron)]

        if actual == patron:
            return 1 + self.contar_patron(secuencia, patron, i + 1)
        
        return self.contar_patron(secuencia, patron, i + 1)

    
    def contar_en_todas(self, patron, i=0):
        if i == len(self.secuencias):
            return []

        muestra = self.secuencias[i]

        cantidad = self.contar_patron(muestra.secuencia, patron)

        resultado_actual = [
            (muestra.id, muestra.nombre, cantidad)
        ]

        return resultado_actual + self.contar_en_todas(patron, i + 1)

    
    def promedio_riesgo(self, i=0, suma=0, cantidad=0):
        if i == len(self.secuencias):
            if cantidad == 0:
                return None
            return suma / cantidad

        return self.promedio_riesgo(i + 1,suma + self.secuencias[i].riesgo,cantidad + 1)

    def generar_subcadenas(self, secuencia, n, i=0):
        if n <= 0 or i + n > len(secuencia):
            return []

        actual = secuencia[i:i+n]

        return [actual] + self.generar_subcadenas(secuencia, n, i+1)

    
    def comparar_a_t(self, secuencia, i=0):
        if i == len(secuencia):
            return (0, 0)

        a, t = self.comparar_a_t(secuencia, i + 1)

        if secuencia[i] == "A":
            a += 1
        elif secuencia[i] == "T":
            t += 1

        if i == 0:
            if a > t:
                return "Tiene más A que T"
            elif t > a:
                return "Tiene más T que A"
            return "Tiene igual cantidad de A y T"

        return (a, t)

    def mutar(self, secuencia, i=0):
        if i == len(secuencia):
            return ("", 0)

        resto, cantidad = self.mutar(secuencia, i + 1)

        if secuencia[i] == "A":
            return ("T" + resto, cantidad + 1)

        elif secuencia[i] == "T":
            return ("A" + resto, cantidad + 1)

        return (secuencia[i] + resto, cantidad)

    def buscar_por_criterios(self, riesgo_minimo, longitud_minima, patron, i=0):
        if i == len(self.secuencias):
            return None

        muestra = self.secuencias[i]

        if (muestra.riesgo >= riesgo_minimo
            and len(muestra.secuencia) >= longitud_minima
            and self.contar_patron(muestra.secuencia, patron) > 0):
            return muestra

        return self.buscar_por_criterios(riesgo_minimo, longitud_minima, patron, i + 1)

    def eliminar_bajo_riesgo(self, riesgo_minimo, i=0):
        if i == len(self.secuencias):
            return 0

        if self.secuencias[i].riesgo < riesgo_minimo:
            del self.secuencias[i]
            return 1 + self.eliminar_bajo_riesgo(riesgo_minimo, i)

        return self.eliminar_bajo_riesgo(riesgo_minimo, i + 1)

# Crear el sistema
sistema = secuencias()

# Crear muestras de ADN
a1 = ADN(1, "Ana", "ATATCGAT", 7)
a2 = ADN(2, "Luis", "TTATATCC", 9)
a3 = ADN(3, "Mia", "CCGGAT", 4)
a4 = ADN(4, "Sol", "ATATATAT", 8)

# 1. Registrar
print("\n--- REGISTRAR ---")
print(sistema.registrar(a1, 1))
print(sistema.registrar(a2, 2))
print(sistema.registrar(a3, 3))
print(sistema.registrar(a4, 4))
print(sistema.registrar(a1, 1))  # ID duplicado

# 2. Contar un patrón
print("\n--- CONTAR PATRÓN ---")
print(sistema.contar_patron("ATAT", "AT"))  # 2

# Contar en todas las muestras
print("\n--- CONTAR EN TODAS ---")
print(sistema.contar_en_todas("AT"))

# 3. Promedio de riesgo
print("\n--- PROMEDIO ---")
print(sistema.promedio_riesgo())  # 7.0

# 4. Generar subcadenas
print("\n--- SUBCADENAS ---")
print(sistema.generar_subcadenas("ATCG", 2))
# ['AT', 'TC', 'CG']

# 5. Comparar A y T
print("\n--- COMPARAR A Y T ---")
print(sistema.comparar_a_t("AATTG"))
# Tiene igual cantidad de A y T

# 6. Mutar ADN
print("\n--- MUTAR ---")
print(sistema.mutar("ATCG"))
# ('TAGC', 2)

# 7. Buscar por criterios
print("\n--- BUSCAR ---")
print(sistema.buscar_por_criterios(7, 8, "AT"))
# Debe devolver la primera muestra que cumpla los criterios.

# 8. Eliminar bajo riesgo
print("\n--- ELIMINAR ---")
print("Eliminadas:", sistema.eliminar_bajo_riesgo(6))
print("Muestras restantes:", sistema.secuencias)