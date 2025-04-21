import { Component } from '@angular/core';
import { NavBarComponent } from '../componentes/nav-bar/nav-bar.component';
import { FooterComponent } from '../componentes/footer/footer.component';
import { CardComponent } from '../componentes/card/card.component';
import { Producto } from '../../../model/producto';
import { ProductoService } from '../../../service/productoService/producto.service';
import { read } from 'fs';
import { NgFor } from '@angular/common';

@Component({
  selector: 'app-inicio',
  imports: [NavBarComponent,FooterComponent,CardComponent,NgFor],
  templateUrl: './inicio.component.html',
  styleUrl: './inicio.component.css'
})
export class InicioComponent {
  productos : Producto[]=[];
  constructor(private readonly productoService: ProductoService){
    this.cargarProductos();
  }

  cargarProductos(){
    this.productoService.mostrarProductos().subscribe(productos =>{this.productos = productos; })
  }

}


