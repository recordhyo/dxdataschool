//react.js 에서 exprot한 객체를 React로 받아서 사용 
import React from 'react';
import { ListItem, ListItemText, InputBase, Checkbox, ListItemSecondaryAction, IconButton } from "@material-ui/core";
import DeleteOutlined from "@material-ui/icons/DeleteOutlined"

class ToDo extends React.Component{
    constructor(props){
        super(props);
        //props는 읽기전용이라서 수정하고자 하는 경우 state에 복사해서 사용해야함
        this.state = {item:props.item, readOnly:true} //속성추가는 여기서
        this.delete = props.delete
        this.update = props.update
    }

    //Event 발생하면 readOnly의 값을 false로 수정 
    offReadOnlyMode = (e) => {
        this.setState({readOnly:false})
    }

    //Enter를 눌렀을 때 동작하는 메서드
    enterKeyEventHandler = (e) => {
        if(e.key === "Enter"){
            this.setState({readOnly:true})
            //데이터수정
            this.update(this.state.item)
        }
    }

    //체크박스 값 변경할 때 호출되는 메서드
    checkboxEventHandler = (e) => {
        const thisItem = this.state.item
        thisItem.done = !thisItem.done
        this.setState({item:thisItem})
        this.update(this.state.item)
    }

    //Input의 내용을 변경했을 때 호출될 메서드
    editEventHandler = (e) => {
        const thisItem = this.state.item;
        thisItem.title = e.target.value;
        this.setState({item:thisItem})
        this.update(this.state.item)
    }

    //삭제 아이콘 눌렀을 때 호출될 함수 
    deleteEventHandler = (e) => {
        this.delete(this.state.item);
    }

    
    render(){
        const item = this.state.item
        return (
            <ListItem>
                <Checkbox checked={item.done} onChange={this.checkboxEventHandler}/>
                <ListItemText>
                    <InputBase 
                        inputProps = {{"aria-lable":"naked", readOnly:this.state.readOnly}}
                        type="text"
                        id = {item.id}
                        name = {item.id}
                        value = {item.title}
                        multiline = {true}
                        fullWidth = {true} 
                        onClick={this.offReadOnlyMode}
                        onKeyPress={this.enterKeyEventHandler}
                        onChange={this.editEventHandler}/>
                </ListItemText>
                <ListItemSecondaryAction>
                    <IconButton aria-label='Delete ToDo' onClick={this.deleteEventHandler}>
                        <DeleteOutlined />
                    </IconButton>
                </ListItemSecondaryAction>

            </ListItem>
        )
    }
}
export default ToDo;