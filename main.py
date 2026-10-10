class ADN:
    def __init__(self,id,nombre,secuencia,riesgo):
        self.id = id
        self.nombre = nombre
        self.secuencia = secuencia
        self.riesgo = riesgo
    
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

    def Contar_ocurrencias(self, secuencia, i=0,contador=0):
        if i == len(self.secuencias):
            return contador
        if self.secuencias[i].secuencia == secuencia:
            contador += 1
        return self.Contar_ocurrencias(secuencia,i+1,contador)