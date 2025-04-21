import { Routes } from '@angular/router';
import LoginComponent from './pages/business/login/login.component';
import { AuthGuard } from './guards/auth.guards';
import { InicioComponent } from './pages/cliente/inicio/inicio.component';
import RegistrarClienteComponent from './pages/cliente/registrar/registrar.component';


export const routes: Routes = [
  {
    path: '',
    redirectTo: 'login',
    pathMatch: 'full'
  },
  {
    path: 'login',
    component: LoginComponent
  },
  {
    path: 'ecommerce',
    component: InicioComponent
  },
  {
    path: 'ecommerce/registrar',
    component: RegistrarClienteComponent
  },
  {
    path: '',
    canActivate: [AuthGuard],
    loadComponent: () => import('./pages/panelAdm/layout/layout.component'),

    children: [
      {
        path: 'dashboard',
        loadComponent: () => import('./pages/business/dashboard/dashboard.component')
      },
      {
        path: 'inventario',
        loadComponent: () => import('./pages/business/inventario/inventario.component')
      },
      {
        path: 'categoria',
        loadComponent: () => import('./pages/business/categoria/categoria.component')
      },
      {
        path: 'marca',
        loadComponent: () => import('./pages/business/marca/marca.component')
      },
      {
        path: 'producto',
        loadComponent: () => import('./pages/business/producto/producto.component')
      },
      {
        path: 'usuario',
        loadComponent: () => import('./pages/business/usuario/usuario.component')
      },
      {
        path: 'ventas',
        loadComponent: () => import('./pages/business/ventas/ventas.component')
      },
      {
        path: 'roles',
        loadComponent: () => import('./pages/business/roles-permisos/roles-permisos.component'),
      },
    ],

  },
  {
    path: '**',
    redirectTo: 'dashboard'
  }
];
