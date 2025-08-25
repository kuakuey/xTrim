import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { FormsModule } from '@angular/forms';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { CommonModule } from '@angular/common';
// Import Bootstrap JS
declare var bootstrap: any;

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [FormsModule, HttpClientModule, CommonModule],
  templateUrl: './home.html',
  styleUrl: './home.css',
})
export class Home {
  cedula: string = '';
  cargando = false;
  error = '';

  constructor(private http: HttpClient, private router: Router) {}

  mostrarModal = false;

  consultarConsumo() {
    this.error = '';
    this.cargando = true;

    this.http.get(`http://127.0.0.1:5000/consumo/${this.cedula}`).subscribe({
      next: (data) => {
        this.cargando = false;
        this.router.navigate(['/consumo'], { state: { resultado: data } });
      },
      error: () => {
        this.cargando = false;
        this.mostrarModal = true; // Mostrar modal
      },
    });
  }

  cerrarModal() {
    this.mostrarModal = false; // Ocultar modal
  }
}
