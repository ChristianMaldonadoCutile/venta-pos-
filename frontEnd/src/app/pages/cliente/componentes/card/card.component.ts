import { Component, Input, } from '@angular/core';
import { Producto } from '../../../../model/producto';

@Component({
  selector: 'app-card',
  imports: [],
  templateUrl: './card.component.html',
  styleUrl: './card.component.css'
})
export class CardComponent {
  @Input()
  producto! : Producto;
  
  
}
