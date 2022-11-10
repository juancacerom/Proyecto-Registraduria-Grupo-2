from Repositorios.repositorioMesaVotacion import RepositorioMesaVotacion
from Modelos.mesaVotacion import MesaVotacion
class ControladorMesa():
    def __init__(self):
        self.repositorioMesaVotacion = RepositorioMesaVotacion()
    def index(self):
        return self.repositorioMesaVotacion.findAll()
    def create(self,infoMesaVotacion):
        nuevaMesaVotacion=MesaVotacion(infoMesaVotacion)
        return self.repositorioMesaVotacion.save(nuevaMesaVotacion)
    def show(self,id):
        laMesaVotacion=MesaVotacion(self.repositorioMesaVotacion.findById(id))
        return laMesaVotacion.__dict__
    def update(self,id,infoMesaVotacion):
        MesaActual=MesaVotacion(self.repositorioMesaVotacion.findById(id))
        MesaActual.Cedula=infoMesaVotacion["CedulaInscrita"]
        return self.repositorioMesaVotacion.save(MesaActual)
    def delete(self,id):
        return self.repositorioMesaVotacion.delete(id)