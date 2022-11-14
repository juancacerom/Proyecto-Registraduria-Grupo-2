package SeguridadRegistraduria.Repositorios;

import org.springframework.data.mongodb.repository.MongoRepository;
import SeguridadRegistraduria.Modelos.Permisos;

import java.util.Optional;

public interface repositorioPermisos extends MongoRepository<Permisos, String> {

    Optional<Permisos> findByUrlAndMetodo(String url, String metodo);

}
