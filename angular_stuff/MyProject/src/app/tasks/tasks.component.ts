import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';
import { User } from './task';
@Component({
  selector: 'app-tasks',
  templateUrl: './tasks.component.html',
  styleUrls: ['./tasks.component.css']
})
export class TasksComponent implements OnInit {
  id: number = 0

  username = ''
  SelectedTask_test: any
  user_tasks: User[] = []
  @Output() addNewTask = new EventEmitter<User[]>();
  UserInput(box: any, value2: string) {


    const task: User = {
      task_name: box.value,
      task_priority: value2,
      task_id: this.id

    }

    this.user_tasks.push(task)
    this.addNewTask.emit(this.user_tasks)
    

    this.id++;



    box.value = ''
  }
  constructor() { }

  ngOnInit(): void {
  }

}
