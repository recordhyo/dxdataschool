//import logo from './logo.svg';
import './App.css';
import MyComponent from './MyComponent';
import Sample from './Sample';
import EventComponent from './EventComponent';

function App() {
  return (
    <> 
      <MyComponent car = "genesis" /> 
      <Sample car = "bmw" car2 = "kia"> 샘플데이터 </Sample>
      <EventComponent />
    </>
  );
}

export default App;
