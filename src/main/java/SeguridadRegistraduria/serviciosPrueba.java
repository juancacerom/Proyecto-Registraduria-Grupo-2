package SeguridadRegistraduria;


import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class serviciosPrueba {

    @GetMapping("/saludo")
    public String hello() {
        return "HOLA MUNDO";
    }

}