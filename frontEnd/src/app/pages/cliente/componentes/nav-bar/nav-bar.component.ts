import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from '../../../../service/authService/auth.service';
import { NgIf } from '@angular/common';


@Component({
  selector: 'app-nav-bar',
  standalone : true,
  imports: [NgIf],
  templateUrl: './nav-bar.component.html',
  styleUrl: './nav-bar.component.css'
})
export class NavBarComponent {
   login(){
    this.router.navigate(["/login"])
   }
   registrar(){
    this.router.navigate(["/ecommerce/registrar"])
   }
   nombreUsuario : string | null = null;
   cargar(){
    this.nombreUsuario = localStorage.getItem("nombre")!;
   }
   ngOnInit(){
    if(this.authService.isAuthenticated()){
      this.isLogin = true;
      this.cargar();
    }
   }
   isLogin : boolean = false;
   constructor(private router : Router,private authService : AuthService){
   }
   cerrarSesion(){
    localStorage.clear();
    this.nombreUsuario = null;
    this.isLogin = false;
    window.location.reload();
   }
}
