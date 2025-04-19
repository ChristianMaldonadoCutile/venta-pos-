import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { AuthService } from '../../../service/authService/auth.service';
import { Route, Router, RouterModule } from '@angular/router';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [FormsModule, CommonModule, ReactiveFormsModule,RouterModule],
  templateUrl: './login.component.html',
  styleUrl: './login.component.css'
})
export default class LoginComponent {
    email : string = '';
    password : string = ''; 

    constructor(private readonly authService: AuthService, private router:Router ) { }

    login() {
      this.authService.login(this.email, this.password).subscribe((response: any) => {
        localStorage.setItem('token', response.token);
        this.router.navigate(['dashboard']);
      });
    }
}
