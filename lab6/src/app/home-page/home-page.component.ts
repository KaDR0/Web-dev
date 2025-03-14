import { Component } from '@angular/core';
import {NgIf} from "@angular/common";
import {RouterLink} from "@angular/router";
import {FormsModule} from "@angular/forms";

@Component({
  selector: 'app-home-page',
  standalone: true,
  imports: [
    NgIf,
    RouterLink,
    FormsModule
  ],
  templateUrl: './home-page.component.html',
  styleUrl: './home-page.component.css'
})
export class HomePageComponent {

}
