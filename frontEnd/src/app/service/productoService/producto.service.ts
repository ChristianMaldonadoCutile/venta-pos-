import { Injectable } from '@angular/core';
import { environment } from '../../environments/environment.development';
import { HttpClient } from '@angular/common/http';
import { Producto } from '../../model/producto';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ProductoService {

  private apiUrl = environment.endpoint;

  constructor(private http: HttpClient) { }

  crearPruducto(producto: Producto): Observable<Producto> {
    return this.http.post<Producto>(`${this.apiUrl}/productos/crear/`, producto);
  }

  mostrarProductos(): Observable<Producto[]> {
    return this.http.get<Producto[]>(`${this.apiUrl}/productos/obtener_todos/`);
  }

  eliminarProducto(id: number): Observable<Producto> {
    return this.http.delete<Producto>(`${this.apiUrl}/productos/eliminar/${id}/`);
  }

  actualizarProducto(producto: Producto): Observable<Producto> {
    return this.http.put<Producto>(`${this.apiUrl}/productos/actualizar/${producto.id}/`, producto);
  }
}
