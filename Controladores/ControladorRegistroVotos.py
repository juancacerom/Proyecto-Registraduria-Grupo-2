from Repositorios.repositorioRegistroVotos import RepositorioRegistroVotos
from Modelos.RegistroVotos import RegistroVotos
class ControladorRegistro():
    def __init__(self):
        self.Repositorioregistrovotos = RepositorioRegistroVotos()
    def index(self):
        return self.Repositorioregistrovotos.findAll()
    def create(self,infoRegistro):
        nuevoRegistro=RegistroVotos(infoRegistro)
        return self.Repositorioregistrovotos.save(nuevoRegistro)
    def show(self,id):
        Registro=RegistroVotos(self.Repositorioregistrovotos.findById(id))
        return Registro.__dict__
    def update(self,id,infoRegistro):
        RegistroActual=RegistroVotos(self.Repositorioregistrovotos.findById(id))
        RegistroActual.nombre=infoRegistro["nombre"]
        return self.Repositorioregistrovotos.save(RegistroActual)
    def delete(self,id):
        return self.Repositorioregistrovotos.delete(id)