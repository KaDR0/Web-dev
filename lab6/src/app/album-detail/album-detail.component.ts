import {Component, OnInit} from '@angular/core';
import { album } from '../db';
import {ActivatedRoute, RouterLink} from "@angular/router";
import {PostService} from "../post.service";
import {NgIf} from "@angular/common";
import {FormsModule} from "@angular/forms";
import {NotFoundComponent} from "../not-found/not-found.component";

@Component({
  selector: 'app-album-detail',
  standalone: true,
  imports: [
    NgIf,
    FormsModule,
    RouterLink,
    NotFoundComponent
  ],
  templateUrl: './album-detail.component.html',
  styleUrl: './album-detail.component.css'
})
export class AlbumDetailComponent implements OnInit{
  Ialbum: album = {} as album;
  title: '';
  isChange = false;
  isloaded!: boolean;

  constructor(private activateRoute: ActivatedRoute, private postService: PostService){
    this.title = '';
  }

  saveTitle() {
    this.Ialbum.title = this.title;
    this.title = '';
  }
  isInput(){
    this.isChange = !this.isChange;
  }
  ngOnInit(): void {
  const id = this.activateRoute.snapshot.paramMap.get('id')!;
  this.isloaded = false;
  this.postService.getPost(+id).subscribe((Ialbum) => {
    this.Ialbum = Ialbum;
    this.isloaded = true;
  });
  }
}
