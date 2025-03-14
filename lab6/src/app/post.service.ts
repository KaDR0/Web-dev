import {Injectable} from "@angular/core";
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";
import {album} from "./db"

@Injectable({
  providedIn: 'root'
})

export class PostService{
  BASE_URL: string = 'https://jsonplaceholder.typicode.com'
  constructor(private http: HttpClient) {
  }
  getPosts(): Observable<album[]>{
    return this.http.get<album[]>(`${this.BASE_URL}/posts`);
  }
  createPost(newPost: album): Observable<album> {
    return this.http.post<album>(`${this.BASE_URL}/posts`, newPost);
  }
  getPost(id: number): Observable<album> {
    return this.http.get<album>(`${this.BASE_URL}/posts/${id}`);
  }
  deletePost(id: number) {
    return this.http.delete(`${this.BASE_URL}/posts/${id}`);
  }
}
