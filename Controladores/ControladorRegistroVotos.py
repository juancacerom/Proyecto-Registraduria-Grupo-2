from Modelos.RegistroVotos import RegistroVotos
from Modelos.Partidos import Partidos
from Modelos.Candidatos import Candidatos
from Modelos.mesaVotacion import MesaVotacion

from Repositorios.repositorioMesaVotacion import RepositorioMesaVotacion
from Repositorios.repositorioPartidos import RepositorioPartidos
from Repositorios.repositorioCandidatos import RepositorioCandidatos
from Repositorios.repositorioRegistroVotos import RepositorioRegistroVotos
class ControladorRegistroVotos():
    def __init__(self):
        self.repositorioRegistro = RepositorioRegistroVotos()
        self.repositorioCandidatos = RepositorioCandidatos()
        self.repositorioPartidos = RepositorioPartidos()
        self.repositorioMesa = RepositorioMesaVotacion()
    def index(self):
        return self.repositorioRegistro.findAll()
    def create(self,infoRegistro,id_Cantidato,id_Partido, id_Mesa):
        nuevoRegistro=RegistroVotos(infoRegistro)
        nuevoRegistro.año = infoRegistro["numero Registro"]
        elCandidato= Candidatos(self.repositorioCandidatos.findById(id_Cantidato))
        elPartido=Partidos(self.repositorioPartidos.findById(id_Partido))
        laMesa = MesaVotacion(self.repositorioMesa.findById(id_Mesa))
        nuevoRegistro.Candidatos = elCandidato
        nuevoRegistro.Partidos = elPartido
        nuevoRegistro.MesaVotacion = laMesa
        return self.repositorioRegistro.save(nuevoRegistro)
    def show(self,id):
        Registro=RegistroVotos(self.repositorioRegistro.findById(id))
        return Registro.__dict__

    def update(self,id,id_Cantidato,id_Partido):
        elRegistro=RegistroVotos(self.repositorioRegistro.findById(id))
        elCandidato = Candidatos(self.repositorioCandidatos.findById(id_Cantidato))
        elPartido = Partidos(self.repositorioPartidos.findById(id_Partido))
        elRegistro.Candidatos = elCandidato
        elRegistro.Partidos = elPartido
        return self.repositorioRegistro.save(elRegistro)
    def delete(self, id):
        return self.repositorioRegistro.delete(id)
    def listadoIncritosMesa(self,id_Mesa):
        return self.repositorioRegistro.getlistadoInscritosMesa(id_Mesa)
    def nombrePartido(self,id_Partido):
        return self.repositorioRegistro.getNombrePartido(id_Partido)
    def nombreCandidato(self,id_Cantidato):
        return self.repositorioRegistro.getNombreCandidato(id_Cantidato)


