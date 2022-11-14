package SeguridadRegistraduria.Repositorios;

import org.springframework.data.mongodb.repository.MongoRepository;
import SeguridadRegistraduria.Modelos.Permisos;
import SeguridadRegistraduria.Modelos.PermisoRol;
import SeguridadRegistraduria.Modelos.Rol;

import java.util.Optional;

public interface repositorioPermisoRol extends MongoRepository<PermisoRol, String> {

    Optional<PermisoRol> findByRolAndPermiso(Rol rol, Permisos permiso);

}
