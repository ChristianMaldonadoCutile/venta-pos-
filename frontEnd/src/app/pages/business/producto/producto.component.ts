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

  previewUrl: string | ArrayBuffer | null = null;
  private db: IDBDatabase | null = null;

  producto: Producto = {} as Producto;

/*************  ✨ Windsurf Command ⭐  *************/
/**
 * Lifecycle hook that is called after the component's data-bound properties are initialized.
 * This method loads the initial data for the component by fetching and displaying
 * the list of productos and categorias.
 */

/*******  2749d807-2adc-4d84-bd58-c5112da403e0  *******/
  ngOnInit() {
    this.initDB();
    this.mostrarProductos();
    this.cargarCategoria();
  }

  private initDB(): void {
    const request = indexedDB.open('ImageStorageDB', 1);

    request.onupgradeneeded = (event) => {
      this.db = (event.target as IDBOpenDBRequest).result;
      if (!this.db.objectStoreNames.contains('images')) {
        this.db.createObjectStore('images', { keyPath: 'id' });
      }
    };

    request.onsuccess = (event) => {
      this.db = (event.target as IDBOpenDBRequest).result;
      this.loadImage();
    };
  }

  onFileSelected(event: any): void {
    const file: File = event.target.files[0];

    if (file) {
      const reader = new FileReader();
      reader.onload = () => {
        this.previewUrl = reader.result;
        this.saveImage(reader.result as string);
      };
      reader.readAsDataURL(file);
    }
  }

  private saveImage(imageData: string): void {
    if (!this.db) return;

    const transaction = this.db.transaction('images', 'readwrite');
    const store = transaction.objectStore('images');
    store.put({ id: 'profile', data: imageData });
  }

  private loadImage(): void {
    if (!this.db) return;

    const transaction = this.db.transaction('images');
    const store = transaction.objectStore('images');
    const request = store.get('profile');

    request.onsuccess = (event) => {
      const result = (event.target as IDBRequest).result;
      if (result) {
        this.previewUrl = result.data;
      }
    };
  }

  deleteImage(): void {
    // Para localStorage
    localStorage.removeItem('userProfileImage');

    // Para IndexedDB
    if (this.db) {
      const transaction = this.db.transaction('images', 'readwrite');
      const store = transaction.objectStore('images');
      store.delete('profile');
    }

    this.previewUrl = null;
  }


  cargarCategoria() {
    this.categoriaService.mostrarCategorias().subscribe(categorias => {
      this.categorias = categorias;
    })
  }

  mostrarProductos() {
    this.productoService.mostrarProductos().subscribe(productos => {
      this.productos = productos;
      this.productosFiltrados = [...this.productos];
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
    this.producto = { ...producto }; // <- esto crea una copia del objeto
    this.crear = false;
    this.abrirModal();
  }

  mostrarModal = false;

  abrirModal() {
    this.mostrarModal = true;
  }

  cerrarModal() {
    this.mostrarModal = false;
    this.producto = {} as Producto;
  }

  // ----------------Busqueda por filtros-------------------
  busqueda: string = '';
  productosFiltrados: Producto[] = [];
  filtrarProductos(termino: string): void {
    if (!termino) {
      this.productosFiltrados = [...this.productos];
      return;
    }

    this.productosFiltrados = this.productos.filter(producto =>
      producto.nombre.toLowerCase().includes(termino.toLowerCase())
    );
  }

//---------------------------------------------------------
}
