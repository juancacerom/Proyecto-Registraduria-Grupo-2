package SeguridadRegistraduria.Controladores;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import SeguridadRegistraduria.Modelos.Permisos;
import SeguridadRegistraduria.Repositorios.repositorioPermisos;

import java.util.List;
import java.util.Optional;

@RestController
@RequestMapping("/Permisos")
public class ControladorPermisos {

    @Autowired
    private repositorioPermisos PermisoRepo;

    @GetMapping("")
    public List<Permisos> index() {
        return this.PermisoRepo.findAll();
    }

    @GetMapping("{id}")
    public Permisos show(@PathVariable String id) {
        Optional<Permisos> optPermiso = this.PermisoRepo.findById(id);
        return optPermiso.orElse(null);
    }

    @PostMapping("")
    public Permisos create(@RequestBody Permisos p) {
        return this.PermisoRepo.save(p);
    }

    @PutMapping("{id}")
    public Permisos update(@PathVariable String id, @RequestBody Permisos p) {
        Optional<Permisos> optPermiso = this.PermisoRepo.findById(id);
        if(optPermiso.isPresent())
        {
            Permisos actual = optPermiso.get();
            actual.setUrl(p.getUrl());
            actual.setMetodo(p.getMetodo());
            return this.PermisoRepo.save(actual);
        }
        return null;
    }

    @DeleteMapping("{id}")
    public void delete(@PathVariable String id)
    {
        this.PermisoRepo.deleteById(id);
    }

}