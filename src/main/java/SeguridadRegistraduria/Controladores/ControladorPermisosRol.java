package SeguridadRegistraduria.Controladores;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import SeguridadRegistraduria.Modelos.Permisos;
import SeguridadRegistraduria.Modelos.PermisoRol;
import SeguridadRegistraduria.Modelos.Rol;
import SeguridadRegistraduria.Repositorios.repositorioPermisos;
import SeguridadRegistraduria.Repositorios.repositorioPermisoRol;
import SeguridadRegistraduria.Repositorios.repositorioRol;

import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.util.List;
import java.util.Optional;

@RestController
@RequestMapping("/Permisos-rol")
public class ControladorPermisosRol {

    @Autowired
    private repositorioPermisoRol permisoRolRepo;

    @Autowired
    private repositorioPermisos permisoRepo;

    @Autowired
    private repositorioRol rolRepo;

    @GetMapping("")
    public List<PermisoRol> index() {
        return this.permisoRolRepo.findAll();
    }

    @GetMapping("{id}")
    public PermisoRol show(@PathVariable String id) {
        Optional<PermisoRol> optPermiso = this.permisoRolRepo.findById(id);
        return optPermiso.orElse(null);
    }

    @PostMapping("")
    public PermisoRol create(@RequestBody PermisoRol p) {

        Optional<Permisos> optPermiso = this.permisoRepo.findById(p.getPermiso().get_id());
        if(optPermiso.isEmpty())
        {
            return null;
        }

        Optional<Rol> rolOpt = this.rolRepo.findById(p.getRol().get_id());

        if(rolOpt.isEmpty())
        {
            return null;
        }

        return this.permisoRolRepo.save(p);
    }

    @PutMapping("{id}")
    public PermisoRol update(@PathVariable String id, @RequestBody PermisoRol p) {
        Optional<PermisoRol> optPermiso = this.permisoRolRepo.findById(id);
        if(optPermiso.isPresent())
        {
            PermisoRol actual = optPermiso.get();

            return this.permisoRolRepo.save(actual);
        }
        return null;
    }

    @DeleteMapping("{id}")
    public void delete(@PathVariable String id)
    {
        this.permisoRolRepo.deleteById(id);
    }

    @PostMapping("/validar-permiso/rol/{id_rol}")
    public PermisoRol getPermiso(@PathVariable String id_rol, @RequestBody Permisos infoPermiso,
                                 final HttpServletResponse response) throws IOException {

        Optional<Permisos> opt = this.permisoRepo.findByUrlAndMetodo(infoPermiso.getUrl(), infoPermiso.getMetodo());

        if(!opt.isPresent())
        {
            response.sendError(HttpServletResponse.SC_UNAUTHORIZED);
            return null;
        }

        Permisos p = opt.get();

        Optional<Rol> optRol = this.rolRepo.findById(id_rol);

        if(!optRol.isPresent())
        {
            response.sendError(HttpServletResponse.SC_UNAUTHORIZED);
            return null;
        }

        Rol r = optRol.get();

        Optional<PermisoRol> optPermisoRol = this.permisoRolRepo.findByRolAndPermiso(r, p);

        if(!optPermisoRol.isPresent())
        {
            response.sendError(HttpServletResponse.SC_UNAUTHORIZED);
            return null;
        }

        return optPermisoRol.get();

    }

}
