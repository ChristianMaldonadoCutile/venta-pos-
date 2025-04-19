import { CommonModule, NgFor } from '@angular/common';
import { Component } from '@angular/core';
import { Usuario } from '../../../model/usuario';
import { UsuarioService } from '../../../service/usuarioservice/usuario.service';
import { Rol } from '../../../model/rol';
import { RolService } from '../../../service/rolService/rol.service';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-usuario',
  imports: [CommonModule,NgFor,FormsModule],
  templateUrl: './usuario.component.html',
  styleUrl: './usuario.component.css'
})
export default class UsuarioComponent {

  
  constructor(private usuarioService: UsuarioService, private rolService: RolService) { }

  usuario : Usuario = {} as Usuario;
 
  usuarios : Usuario[] = [];
  roles :  Rol[] = [];

  ngOnInit(): void {
    this.mostrarUsuarios();
    this.cargarRoles();
  }

  mostrarUsuarios() {
    this.usuarioService.mostrarUsuario().subscribe((usuarios) => {
      this.usuarios = usuarios;
      console.log(usuarios)
    })
  }

  crearUsuario() {
    this.usuarioService.crearUsuario(this.usuario).subscribe(() => {
      this.mostrarUsuarios();
      this.cerrarModal();
    });
  }

  cargarRoles() {
    this.rolService.mostrarRoles().subscribe((roles) => {
      this.roles = roles;
    })
  }

  mostrarModal = false;

  abrirModal() {
    this.mostrarModal = true;
  }

  cerrarModal() {
    this.mostrarModal = false;
  }

}
