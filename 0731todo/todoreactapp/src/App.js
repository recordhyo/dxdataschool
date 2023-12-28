//import logo from './logo.svg';
import './App.css';
import React from 'react';
import ToDo from './ToDo';
import AddToDo from './AddToDo';
import {Paper, List, Container} from "@material-ui/core"
import { call } from './service/ApiService';

class App extends React.Component {
  constructor(props){
    super(props);
    this.state = {items:[]};
  }


  componentDidMount() {
    call("/todo","GET",null).then((response)=> this.setState({items:response.list}))
  }



  //데이터 추가를 위한 함수 - item 1개 받아서 items에 추가하는 함수
  add = (item) => {
    item.userid="parkhs";
    call("/todo","POST", item).then((response)=> this.setState({items:response.list}))

  /*  
    //기존 items를 thisItems에 복제 
    const thisItems = this.state.items
    //추가할 item을 생성 
    item.id = "ID-" + thisItems.length;
    item.done = false;
    //복제본에 데이터를 추가 - 배열이나 객체에 바로 데이터 넣는것 안됨
    thisItems.push(item);
    //items에 복제본을 추가
    //react는 props나 state가 변경되면 컴포넌트 자동 재출력
    this.setState({item:thisItems});*/
  }

  //데이터 삭제하는 함수 
  delete = (item) => {
    item.userid="parkhs";
    call("/todo","DELETE", item).then((response)=> this.setState({items:response.list}))

    /*
    const thisItems = this.state.items;
    //thisItems 에서 itme 삭제하기 - id가 구별하는 속성 - 원본은 그대로 두기
    const newItems = thisItems.filter((e) => e.id !== item.id);
    //state를 newItems로 변경해서 데이터를 재출력
    this.setState({items:newItems},() => {
      console.log(item.id +"가 삭제되었습니다.")
    })*/
  }

  //데이터를 수정하는 함수
  update = (item) => {
    item.userid="parkhs";
    call("/todo", "PUT", item).then((response) => this.setState({items:response.list}))
  }


  render(){
    var todoItems = this.state.items.length > 0 && (
      <Paper style={{margin:16}}>
        <List> {this.state.items.map((item,idx) => (
          <ToDo item={item} key={item.id} delete={this.delete} update={this.update}/>
        ))}
        </List>
      </Paper>
    )
    
    return (
      <div className='App'>
        <Container maxWidth="md">
          <AddToDo add={this.add}/>
          {todoItems}

        </Container>
        
      </div>
    )
  }
}

export default App;
