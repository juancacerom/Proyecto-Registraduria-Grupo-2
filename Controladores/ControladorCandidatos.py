from Repositorios.repositorioCandidatos import RepositorioCandidatos
from Repositorios.repositorioPartidos import RepositorioPartidos
from Modelos.Candidatos import Candidatos
from Modelos.Partidos import Partidos
class ControladorCandidatos():
    def __init__(self):
        self.repositorioCandidatos = RepositorioCandidatos()
        self.repositorioPartidos = RepositorioPartidos()
    def index(self):
        return self.repositorioCandidatos.findAll()
    def create(self,infoCandidato):
        nuevoCandidato=Candidatos(infoCandidato)
        return self.repositorioCandidatos.save(nuevoCandidato)
    def show(self,id):
        elCandidato=Candidatos(self.repositorioCandidatos.findById(id))
        return elCandidato.__dict__
    def update(self,id,infoCandidato):
        CandidatoActual=Candidatos(self.repositorioCandidatos.findById(id))
        CandidatoActual.cedula=infoCandidato["cedula"]
        CandidatoActual.nombre = infoCandidato["nombre"]
        CandidatoActual.apellido = infoCandidato["apellido"]
        CandidatoActual.numeroResolucion = infoCandidato["numeroResolucion"]

        return self.repositorioCandidatos.save(CandidatoActual)
    def delete(self,id):
        return self.repositorioCandidatos.delete(id)

    def asignarPartido(self, id, id_partido):
        CandidatoActual = Candidatos(self.repositorioCandidatos.findById(id))
        partidoActual = Partidos(self.repositorioPartidos.findById(id_partido))
        CandidatoActual.partido = partidoActual
        return self.repositorioCandidatos.save(CandidatoActual)
