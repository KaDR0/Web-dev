import {Component, OnInit} from '@angular/core';
import {NgForOf} from "@angular/common";
import {album, photos} from "../db";
import {ActivatedRoute, RouterLink} from "@angular/router";
import {PostService} from "../post.service";

@Component({
  selector: 'app-album-photos',
  standalone: true,
  imports: [
    NgForOf,
    RouterLink
  ],
  templateUrl: './album-photos.component.html',
  styleUrl: './album-photos.component.css'
})
export class AlbumPhotosComponent implements OnInit{

  protected readonly photos = photos;
  Ialbum: album = {} as album;
  Num = '';

  constructor(private activateRoute: ActivatedRoute, private postService: PostService){
  }
  WhatNum(){
      if ((this.Ialbum.id%10) == 1)this.Num = 'st';
      else if ((this.Ialbum.id%10) == 2)this.Num = 'nd';
      else if ((this.Ialbum.id%10) == 3)this.Num = 'rd';
      else this.Num = 'th';
  }
  ngOnInit(): void {
    const id = this.activateRoute.snapshot.paramMap.get('id')!;
    this.postService.getPost(+id).subscribe((Ialbum) => {
      this.Ialbum = Ialbum;
    });
    this.WhatNum();
  }
}
