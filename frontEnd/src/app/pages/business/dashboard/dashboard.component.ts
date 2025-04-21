import { Component } from '@angular/core';
import { UsuarioService } from '../../../service/usuarioservice/usuario.service';
import { RolService } from '../../../service/rolService/rol.service';
import { Usuario } from '../../../model/usuario';
import { Rol } from '../../../model/rol';
import { CommonModule, NgFor, NgIf } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-dashboard',
  imports: [NgFor, NgIf, FormsModule, CommonModule],
  templateUrl: './dashboard.component.html',
  styleUrl: './dashboard.component.css'
})
export default class DashboardComponent {

  constructor(private usuarioService: UsuarioService, private rolService: RolService) { }

  usuario: Usuario = {} as Usuario;

  usuarios: Usuario[] = [];
  roles: Rol[] = [];

  ngOnInit(): void {
    this.mostrarUsuarios();
    this.cargarRoles();
  }

  mostrarUsuarios() {
    this.usuarioService.mostrarUsuario().subscribe((usuarios) => {
      this.usuarios = usuarios;
      console.log(usuarios);
      this.usuariosFiltrados = [...this.usuarios];
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

// --------------------Modal-------------------------------
  mostrarModal = false;

  abrirModal() {
    this.mostrarModal = true;
  }

  cerrarModal() {
    this.mostrarModal = false;
  }
// ---------------------------------------------------------

// ----------------Busqueda por filtros-------------------
  busqueda: string = '';
  usuariosFiltrados: Usuario[] = [];
  filtrarUsuarios(termino: string): void {
    if (!termino) {
      this.usuariosFiltrados = this.usuarios.filter(usuario => usuario.rol === 'Cliente');
      return;
    }

    this.usuariosFiltrados = this.usuarios.filter(usuario =>
      usuario.rol === 'Cliente' &&
      usuario.nombre.toLowerCase().includes(termino.toLowerCase())
    );
  }

//---------------------------------------------------------
}
