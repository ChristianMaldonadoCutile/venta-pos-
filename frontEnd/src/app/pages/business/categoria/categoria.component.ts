import { CommonModule, NgFor } from '@angular/common';
import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { CategoriaService } from '../../../service/categoriaService/categoria.service';
import { Categoria } from '../../../model/categoria';

@Component({
  selector: 'app-categoria',
  imports: [FormsModule, CommonModule, NgFor,],
  templateUrl: './categoria.component.html',
  styleUrl: './categoria.component.css'
})
export default class CategoriaComponent {

  constructor(private categoriaService: CategoriaService) { }

  categorias: Categoria[] = [];

  nombre: string = '';
  descripcion: string = '';

  ngOnInit(): void {
    this.mostrarCategorias();
  }

  mostrarCategorias() {
    this.categoriaService.mostrarCategorias().subscribe(categorias => {
      this.categorias = categorias;
    });
  }

  crearCategoria() {
    const categoria = { nombre: this.nombre, descripcion: this.descripcion };
    this.categoriaService.crearCategoria(categoria).subscribe(() => {
      this.mostrarCategorias();
      this.nombre = '';
      this.descripcion = '';
      this.cerrarModal();
    });
  }

  eliminarCategoria(id: number) {
    this.categoriaService.eliminarCategoria(id).subscribe(() => {
      this.mostrarCategorias();
      console.log("eliminado");
    });
  }

  mostrarModal = false;

  abrirModal() {
    this.mostrarModal = true;
  }

  cerrarModal() {
    this.mostrarModal = false;
  }
}
