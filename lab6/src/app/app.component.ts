import { Component } from '@angular/core';
import {RouterLink, RouterOutlet} from '@angular/router';
import {HomePageComponent} from "./home-page/home-page.component";
import {AlbumsPageComponent} from "./albums-page/albums-page.component";
import {NgIf} from "@angular/common";
import {AlbumDetailComponent} from "./album-detail/album-detail.component";
import {FormsModule} from "@angular/forms";
import {TopBarComponent} from "./top-bar/top-bar.component";

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, HomePageComponent, AlbumsPageComponent, RouterLink, NgIf, AlbumDetailComponent, FormsModule, TopBarComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'lab6';
  isAlbum = true;
  isAlbums = false;

  clickAlbum(){
    this.isAlbum = !this.isAlbums;
    this.isAlbum = !this.isAlbum;
  }
}
