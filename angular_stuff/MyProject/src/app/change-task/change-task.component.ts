import { Component, Output, OnInit, Input, EventEmitter } from '@angular/core';
import { User } from '../tasks/task';
@Component({
  selector: 'app-change-task',
  templateUrl: './change-task.component.html',
  styleUrls: ['./change-task.component.css']
})


export class ChangeTaskComponent implements OnInit {
  SelectedTask: any
  @Input() item: User[] = [];

  constructor() { }
  onSelect(user: any): void {
    this.SelectedTask = user;

  }

  deleteTask(del:any,user_tasks:User[],del_task:any){
    var itemToDel = user_tasks.find(x => x.task_id == del_task.task_id)
    
    user_tasks.splice(del_task.itemToDel,1)
     del.value=''
    // del_task.task_name=''
  }

  UpdateTask(task: any) {
    this.item[task.task_id].task_name = task.task_name
  }
  ngOnInit(): void {

  }



}
