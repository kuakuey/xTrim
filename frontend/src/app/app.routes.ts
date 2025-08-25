import { Routes } from '@angular/router';
import { Consumo } from './consumo/consumo';
import { Home } from './home/home';

export const routes: Routes = [
  { path: '', component: Home },          // pantalla inicial
  { path: 'consumo', component: Consumo } // nueva página de consumo
];
