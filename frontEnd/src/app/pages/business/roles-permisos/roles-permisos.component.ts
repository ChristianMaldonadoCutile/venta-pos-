import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { RolService } from '../../../service/rolService/rol.service';
import { Rol } from '../../../model/rol';

@Component({
  selector: 'app-roles-permisos',
  standalone: true,
  imports: [FormsModule, CommonModule, ReactiveFormsModule],
  templateUrl: './roles-permisos.component.html',
  styleUrl: './roles-permisos.component.css'
})
export default class RolesPermisosComponent implements OnInit{

  roles: Rol[] = [];
  nombre:string = '';
  descripcion:string = '';

  constructor(private rolService: RolService) { }

  ngOnInit(): void {
      this.mostrarRoles();
  }

  mostrarRoles() {
    this.rolService.mostrarRoles().subscribe((roles) => {
      this.roles = roles;
    });
  }

  crearRol() {
    const rol = { nombre: this.nombre, descripcion: this.descripcion };
    console.log(rol);
    this.rolService.crearRol(rol).subscribe(() => {
      this.mostrarRoles();
      this.nombre = '';
      this.descripcion = '';
      this.cerrarModal();
    });
  }

  eliminarRol(id: number) {
    this.rolService.eliminarRol(id).subscribe(() => {
      this.mostrarRoles();
    });
  }

  // Modal de guardar
  mostrarModal: boolean = false;
  abrirModal() {
    this.mostrarModal = true;
  }

  cerrarModal() {
    this.mostrarModal = false;
    // this.nuevoRol = { nombre: '', descripcion: '' , estado: true };
  }
}
