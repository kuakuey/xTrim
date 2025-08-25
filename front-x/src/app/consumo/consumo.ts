import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Router } from '@angular/router';
import { Location } from '@angular/common';

@Component({
  selector: 'app-consumo',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './consumo.html',
  styleUrl: './consumo.css'
})
export class Consumo {
  consumo: any;

  constructor(private router: Router, private location: Location) {
    // Recibir los datos desde history.state
    this.consumo = history.state.resultado;

    // Si no hay datos, volver al inicio
    if (!this.consumo) {
      this.router.navigate(['/']);
    }
  }

  // Método para regresar
  regresar() {
    // Puedes usar location.back() o router.navigate(['/'])
    this.location.back();  // Vuelve a la página anterior
    // o this.router.navigate(['/']); // Vuelve siempre al inicio
  }
}
