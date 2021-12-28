import { Component, Output, EventEmitter, NgModule } from '@angular/core';
import { User } from './tasks/task';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})


export class AppComponent {
  title = 'MyProject';
  items: User[] = []

  addTask(newItem: User[]) {
    this.items = newItem
  }




}
