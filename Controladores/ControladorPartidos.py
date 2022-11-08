from Repositorios.repositorioPartidos import RepositorioPartidos
from Modelos.Partidos import Partidos
class ControladorPartidos():
    def __init__(self):
        self.repositorioPartidos = RepositorioPartidos()
    def index(self):
        return self.repositorioPartidos.findAll()
    def create(self,infoPartidos):
        nuevoPartidos=Partidos(infoPartidos)
        return self.repositorioPartidos.save(nuevoPartidos)
    def show(self,id):
        elPartido=Partidos(self.repositorioPartidos.findById(id))
        return elPartido.__dict__
    def update(self,id,infoPartidos):
        PartidoActual=Partidos(self.repositorioPartidos.findById(id))
        PartidoActual.nombre=infoPartidos["nombre"]
        PartidoActual.lema = infoPartidos["lema"]
        return self.repositorioPartidos.save(PartidoActual)
    def delete(self,id):
        return self.repositorioPartidos.delete(id)