import suds

class Client:
    #conocido como constructor establese la conexion
    def __init__(self):
        self.client = suds.client.Client("http://Develop:8080/proyectFinal/QuerysService?wsdl")

    def insertar_usuarios(self,name,user,password):
        return self.client.service.insertarUsuario(name,user,password)

    def verificar_usuario(self,username,password):
        return self.client.service.verificarUsuario(username,password)

    def insertar_comentario(self,title,description,user):
        return self.client.service.comentarios(title,description,user)

#metodo main
#if(__name__ == "__main__"):
#    client = Client()
#    if client.verificar_usuario("bogarin","bogarin10"):
#        print 'jalo'
#    else:
#        print 'no jalo'
