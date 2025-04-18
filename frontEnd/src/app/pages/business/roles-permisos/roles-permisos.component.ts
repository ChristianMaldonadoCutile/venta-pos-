import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-roles-permisos',
  imports: [FormsModule, CommonModule],
  templateUrl: './roles-permisos.component.html',
  styleUrl: './roles-permisos.component.css'
})
export default class RolesPermisosComponent {
  mostrarModal: boolean = false;
  nuevoRol = {
    rol: '',
    descripcion: ''
  };

  abrirModal() {
    this.mostrarModal = true;
  }

  cerrarModal() {
    this.mostrarModal = false;
  }

  guardarRol() {
    // Aquí puedes manejar la lógica para agregar el nuevo rol
    console.log(this.nuevoRol);
    this.cerrarModal(); // Cerrar el modal después de guardar
  }

  editarRol(id: number) {
    // Lógica para editar rol
  }

  eliminarRol(id: number) {
    // Lógica para eliminar rol
  }
}
