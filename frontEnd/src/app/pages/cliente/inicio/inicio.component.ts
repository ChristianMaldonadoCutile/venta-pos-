import { Component } from '@angular/core';
import { NavBarComponent } from '../componentes/nav-bar/nav-bar.component';
import { FooterComponent } from '../componentes/footer/footer.component';
import { CardComponent } from '../componentes/card/card.component';

@Component({
  selector: 'app-inicio',
  imports: [NavBarComponent,FooterComponent,CardComponent,],
  templateUrl: './inicio.component.html',
  styleUrl: './inicio.component.css'
})
export class InicioComponent {

}
