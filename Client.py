import suds

class Client:
    #conocido como constructor establese la conexion
    def __init__(self):
        self.client = suds.client.Client("http://develop:8080/finalProyect/QuerysService?wsdl")

    def insertar_usuarios(self,name,user,password):
        return self.client.service.insertarUsuario(name,user,password)

    def verificar_usuario(self,username,password):
        return self.client.service.verificarUsuario(username,password)



#metodo main
#if(__name__ == "__main__"):
#    client = Client()
#    client.registros()
