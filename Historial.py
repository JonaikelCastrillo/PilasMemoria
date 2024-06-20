from PaginaWeb import PaginaWeb

class Historial:
    def __init__(self):
        self.cima = None
    def esta_vacia(self):
        return self.cima is None 
    def apilar(self, url):
        nuevo_url = PaginaWeb(url)
        if self.cima is None:
            self.cima = nuevo_url
        else:
            nuevo_url.siguiente = self.cima #aquí el siguiente es el que está debajo 
            self.cima = nuevo_url
    def desapilar(self):
        if self.cima is None:
            print("El historial está vacío")
        else:
            valor = self.cima.url
            self.cima = self.cima.siguiente
            return valor 
    def ver_cima(self):
        if self.cima is None:
            print("El historial está vacío")
        else:
            return self.cima.url
    def mostrar_elementos(self):
        url_actual = self.cima
        end = False
        while url_actual and not end:
            print(url_actual.url)
            url_actual = url_actual.siguiente
            if url_actual == self.cima:
                end = True
        if self.cima is None:
            print("El historial está vacío")
    def vaciar(self):
        while self.cima:
            self.cima = self.cima.siguiente
        if self.cima is None:
            print("Historial eliminado")
    def buscar(self, url):
        url_actual = self.cima
        encontrado = False
        while url_actual and not encontrado:
            if url_actual.url == url:
                encontrado = True
            url_actual = url_actual.siguiente
        if self.cima is None:
            print("El historial está vacío")   
        if encontrado:
            print("El url está en el historial")
        else:
            print("El url no está en el historial")
       
            
                
    