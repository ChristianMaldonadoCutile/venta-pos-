import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import LayoutComponent from './pages/panelAdm/layout/layout.component';
import LoginComponent from './pages/business/login/login.component';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet,],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'frontEnd';
}
