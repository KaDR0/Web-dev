import { Component, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'app-launch-filter',
  templateUrl: './launch-filter.component.html',
  styleUrls: ['./launch-filter.component.css']
})
export class LaunchFilterComponent {
  @Output() filterSuccess: EventEmitter<boolean> = new EventEmitter();

  onSuccessFilter(): void {
    this.filterSuccess.emit(true);  // Передаем значение для успешных запусков
  }

  onFailureFilter(): void {
    this.filterSuccess.emit(false);  // Передаем значение для неуспешных запусков
  }
}
