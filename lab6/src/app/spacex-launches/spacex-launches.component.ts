import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http'; 
import { LaunchFilterComponent } from '../launch-filter/launch-filter.component';
import { CommonModule } from '@angular/common';



@Component({
  selector: 'app-spacex-launches',
  standalone: true,
  imports: [CommonModule, LaunchFilterComponent],
  templateUrl: './spacex-launches.component.html',
  styleUrls: ['./spacex-launches.component.css']
})
export class SpacexLaunchesComponent implements OnInit {
  launches: any[] = [];  // Массив для хранения всех запусков
  filteredLaunches: any[] = [];  // Массив для хранения отфильтрованных запусков

  constructor(private http: HttpClient) {}  // Внедрение HttpClient

  ngOnInit() {
    // Делаем запрос к API SpaceX
    this.http.get<any[]>('https://api.spacexdata.com/v4/launches')  // URL для запроса
      .subscribe(data => {
        this.launches = data;  // Сохраняем все данные о запусках
        this.filteredLaunches = data;  // Изначально показываем все запуски
      });
  }

  // Метод для фильтрации успешных запусков
  filterSuccessfulLaunches() {
    this.filteredLaunches = this.launches.filter(launch => launch.success);  // Фильтрация по успешным запускам
  }
  
  onFilterSuccess(successOnly: boolean) {
    if (successOnly) {
      this.filteredLaunches = this.launches.filter(launch => launch.success);
    } else {
      this.filteredLaunches = [...this.launches];
    }
  }
  
}
