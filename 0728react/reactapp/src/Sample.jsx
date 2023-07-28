
function Sample(props) {
    //자바스크립트의 구조 분해 할당
    // = 오른쪽에 객체 설정, 왼쪽 {}안에 변수 설정하면 변수 이름과 동일한 객체 속성이 분해되어 대입됨
  const {car, children, car2} = props;
    return (<> 
    <div> 자동차 {car} </div>
    <div> 자동차2 : {car2}</div>
    <div> 태그 사이 문자열 출력 : {children}</div>
    </>)
}
export default Sample