package SeguridadRegistraduria.Repositorios;

import  org.springframework.data.mongodb.repository.MongoRepository;
import SeguridadRegistraduria.Modelos.Rol;

public interface repositorioRol extends MongoRepository<Rol, String> {
}
