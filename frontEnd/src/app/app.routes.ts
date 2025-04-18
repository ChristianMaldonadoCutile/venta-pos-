import { Routes } from '@angular/router';


export const routes: Routes = [
    {
        path: '',
        redirectTo: 'login',
        pathMatch: 'full'
    },
    {
        path: '',
        // canActivate:[authGuard],
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
