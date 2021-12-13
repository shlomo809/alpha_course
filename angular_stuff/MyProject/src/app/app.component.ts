import { Component, Output, EventEmitter } from '@angular/core';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'MyProject';
  message=''

  @Output() ShowMassage = new EventEmitter();


  Show(){
    this.message="Hello World!!!!"
  }

}
