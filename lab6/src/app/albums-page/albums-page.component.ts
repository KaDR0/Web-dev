import {Component, OnInit} from '@angular/core';
import {album, albums} from "../db";
import {postIds} from "../live";
import {CommonModule, NgForOf, NgIf} from "@angular/common";
import {PostService} from "../post.service";
import {RouterModule} from "@angular/router";
import {FormsModule} from "@angular/forms";
@Component({
  selector: 'app-albums-page',
  standalone: true,
  imports: [RouterModule, CommonModule, FormsModule, NgForOf, NgIf],
  templateUrl: './albums-page.component.html',
  styleUrl: './albums-page.component.css'
})
export class AlbumsPageComponent implements OnInit{
  albumId= 0;
  Posts!: album[];
  PostIds!: number[];
  newPost: album;
  isAdd = false;
  id = 120;
  constructor(private postService: PostService) {
    this.newPost = {
      userId: 120,
      id: this.id,
      title: '',
    }
  }
  ngOnInit() {
    this.getPosts();
    this.getPostIds();
  }
  addPost() {
    this.postService.createPost(this.newPost).subscribe(
      (album) => {
        this.Posts.unshift(album);
        alert('Post created');
        this.newPost = {} as album;
        this.id++;
      }
    );
  }
  getPosts(){
    this.Posts = albums;
    this.postService.getPosts().subscribe((Posts) => {
      this.Posts = Posts;
    });
  }
  getPostIds(){
    this.PostIds = postIds;
  }
  NewPost(){
    this.isAdd = !this.isAdd;
  }
  nextAlbum(isNext: boolean)
  {
    if(isNext)this.albumId++;
    else this.albumId--;

    if(this.albumId < 0)this.albumId = 9;
    else if(this.albumId > 9)this.albumId = 0;
  }
  deletePost(id: number) {
    this.Posts = this.Posts.filter((p) => p.id !== id);
    this.postService.deletePost(id).subscribe(() => {
      console.log('deleted');
    });
  }
}
