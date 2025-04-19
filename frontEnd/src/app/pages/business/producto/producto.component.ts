import { CommonModule, NgFor } from '@angular/common';
import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { RouterLink } from '@angular/router';
import { ProductoService } from '../../../service/productoService/producto.service';
import { Producto } from '../../../model/producto';
import { CategoriaService } from '../../../service/categoriaService/categoria.service';
import { Categoria } from '../../../model/categoria';

@Component({
  selector: 'app-producto',
  imports: [FormsModule, CommonModule, NgFor],
  templateUrl: './producto.component.html',
  styleUrl: './producto.component.css'
})
export default class ProductoComponent {

  constructor(private productoService: ProductoService, private categoriaService: CategoriaService) { }

  productos: Producto[] = [];
  categorias: Categoria[] = [];
  crear : boolean = true;

  producto: Producto = {} as Producto;

  ngOnInit() {
    this.mostrarProductos();
    this.cargarCategoria();
  }

  cargarCategoria() {
    this.categoriaService.mostrarCategorias().subscribe(categorias => {
      this.categorias = categorias;
    })
  }

  mostrarProductos() {
    this.productoService.mostrarProductos().subscribe(productos => {
      this.productos = productos;
    });
  }

  crearProducto() {
    if (this.crear == true) {
      this.producto.categoria = this.categorias.find(categoria => categoria.id == this.producto.idcategoria)!.nombre;
      this.productoService.crearPruducto(this.producto).subscribe(producto => {
        this.mostrarProductos();
        this.cerrarModal();
      });
    }else{
      this.producto.categoria = this.categorias.find(categoria => categoria.id == this.producto.idcategoria)!.nombre;
      this.productoService.actualizarProducto(this.producto).subscribe(producto => {
        this.mostrarProductos();
        this.crear = true;
        this.cerrarModal();
      });
    }
  }

  eliminarProducto(id: number) {
    this.productoService.eliminarProducto(id).subscribe(producto => {
      this.mostrarProductos();
    });
  }

  editarProducto(producto: Producto) {
    this.producto = producto;
    this.crear = false;
    this.abrirModal();
  }

  mostrarModal = false;

  abrirModal() {
    this.mostrarModal = true;
  }

  cerrarModal() {
    this.mostrarModal = false;
  }
}
