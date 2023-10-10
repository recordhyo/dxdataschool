package com.example.springdockerfile;


import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class FrontController {
    @GetMapping("/")
    public String home(){
        return "Hello Spring Boot";
    }
}
