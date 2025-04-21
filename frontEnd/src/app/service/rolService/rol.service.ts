import { Injectable } from '@angular/core';
import { environment } from '../../environments/environment.development';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Rol } from '../../model/rol';

@Injectable({
  providedIn: 'root'
})
export class RolService {
  private apiUrl = environment.endpoint;
  constructor(private http: HttpClient) { }

  mostrarRoles(): Observable<Rol[]> {
    return this.http.get<Rol[]>(`${this.apiUrl}/api/usuarios/roles/`);
  }

  crearRol(rol: Rol): Observable<Rol> {
    return this.http.post<Rol>(`${this.apiUrl}/api/usuarios/roles/crear/`, rol);
  }

  eliminarRol(id: number): Observable<Rol> {
    return this.http.delete<Rol>(`${this.apiUrl}/api/usuarios/roles/eliminar/${id}${`/`}`);
  }
}
