package SeguridadRegistraduria.Repositorios;
import org.springframework.data.mongodb.repository.MongoRepository;
import SeguridadRegistraduria.Modelos.Usuario;
import java.util.Optional;

public interface repositorioUsuario extends MongoRepository<Usuario, String> {

    Optional<Usuario> findByCorreoAndContrasena(String correo, String contrasena);

}
