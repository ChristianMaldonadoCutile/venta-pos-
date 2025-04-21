import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { AuthService } from '../../../service/authService/auth.service';
import { Route, Router, RouterModule } from '@angular/router';
import { UsuarioService } from '../../../service/usuarioservice/usuario.service';

@Component({
  selector: 'ecommerce-login',
  standalone: true,
  imports: [FormsModule, CommonModule, ReactiveFormsModule,RouterModule],
  templateUrl: './registrar.component.html',
})
export default class RegistrarClienteComponent {
    nombre : String = '';
    email : string = '';
    password : string = ''; 

    constructor(private readonly usuarioService: UsuarioService, private router:Router ) { }

    registrar() {
      const usuario ={email : this.email, password: this.password, nombre: this.nombre, rol: "Cliente", nit: "", estado: true}
      this.usuarioService.crearUsuario(usuario).subscribe((response: any) => {
        localStorage.setItem('token', response.token);
        this.router.navigate(['ecommerce']);
      });
    }
}
