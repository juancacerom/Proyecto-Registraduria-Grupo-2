from Repositorios.repositorioCandidatos import RepositorioCandidatos
from Modelos.Candidatos import Candidatos
class ControladorCandidatos():
    def __init__(self):
        self.repositorioCandidatos = RepositorioCandidatos()
    def index(self):
        return self.repositorioCandidatos.findAll()
    def create(self,infoCandidatos):
        nuevoCandidato=Candidatos(infoCandidatos)
        return self.repositorioCandidatos.save(nuevoCandidato)
    def show(self,id):
        elCandidato=Candidatos(self.repositorioCandidatos.findById(id))
        return elCandidato.__dict__
    def update(self,id,infoCandidatos):
        CandidatoActual=Candidatos(self.repositorioCandidatos.findById(id))
        CandidatoActual.cedula=infoCandidatos["cedula"]
        CandidatoActual.nombre = infoCandidatos["nombre"]
        CandidatoActual.apellido = infoCandidatos["apellido"]
        CandidatoActual.numeroResolucion = infoCandidatos["Numero Resolucion"]
        return self.repositorioCandidatos.save(CandidatoActual)
    def delete(self,id):
        return self.repositorioCandidatos.delete(id)