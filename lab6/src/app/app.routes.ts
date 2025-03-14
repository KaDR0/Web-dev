import { Routes } from '@angular/router';
import {HomePageComponent} from "./home-page/home-page.component";
import {AlbumsPageComponent} from "./albums-page/albums-page.component";
import {AlbumDetailComponent} from "./album-detail/album-detail.component";
import {AboutPageComponent} from  "./about-page/about-page.component";
import {NotFoundComponent} from "./not-found/not-found.component";
import {AlbumPhotosComponent} from "./album-photos/album-photos.component";

export const routes: Routes = [
  {path: '', redirectTo: 'home', pathMatch: 'full'},
  {path: 'home', component: HomePageComponent, title: 'Home'},
  {path: 'about', component: AboutPageComponent, title: 'About'},
  {path: 'albums', component: AlbumsPageComponent, title: 'Albums'},
  {path: 'albums/:id', component: AlbumDetailComponent, title: 'Album Detail'},
  {path: 'albums/:id/photos', component: AlbumPhotosComponent, title: 'Album photos'},
  {path: '**', component: NotFoundComponent, title: '404 Not Found'}
];
