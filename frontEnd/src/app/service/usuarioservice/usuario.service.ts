import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from '../../environments/environment.development';
import { Rol } from '../../model/rol';
import { Usuario } from '../../model/usuario';


@Injectable({
  providedIn: 'root'
})

export class UsuarioService {
  private apiUrl = environment.endpoint;
  constructor(private http: HttpClient) {
    
  }
  mostrarUsuario(): Observable<Usuario[]> {
    return this.http.get<Usuario[]>(`${this.apiUrl}/api/usuarios/usuarios/todos/`);
  }

  crearUsuario(usuario: Usuario): Observable<Usuario> {
    return this.http.post<Usuario>(`${this.apiUrl}/api/usuarios/registro/`, usuario);
  }

  eliminarUSuario(id: number): Observable<Usuario> {
    return this.http.delete<Usuario>(`${this.apiUrl}/api/usuarios/eliminar/${id}/`);
  }
  actualizarUsuario(id: number, usuario: Usuario): Observable<Usuario> {
    return this.http.put<Usuario>(`${this.apiUrl}/api/usuarios/actualizar_usuario/${id}/`, usuario);
  }
}
