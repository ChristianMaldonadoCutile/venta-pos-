import { CommonModule, NgFor, NgIf } from '@angular/common';
import { Component } from '@angular/core';
import { Usuario } from '../../../model/usuario';
import { UsuarioService } from '../../../service/usuarioservice/usuario.service';
import { Rol } from '../../../model/rol';
import { RolService } from '../../../service/rolService/rol.service';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-usuario',
  imports: [CommonModule,NgFor,FormsModule,NgIf],
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

  eliminarUSuario(id: number) {
    this.usuarioService.eliminarUSuario(id).subscribe(() => {
      this.mostrarUsuarios();
    });
  }

  actualizarUsuario(usuario: Usuario, id: number) {
    this.usuarioService.actualizarUsuario(id, usuario).subscribe(() => {
      this.usuario = usuario;
      this.abrirModal();
      this.mostrarUsuarios();
    });
  }

  mostrarModal = false;

  abrirModal() {
    this.mostrarModal = true;
  }

  cerrarModal() {
    this.mostrarModal = false;
    this.usuario = {} as Usuario;
  }

}
