import React ,{useState} from 'react';
import AWS from 'aws-sdk'

const S3_BUCKET ='hyobuckettest';
const REGION ='ap-northeast-2';
AWS.config.update({
  accessKeyId: 'AKIAXPYBCAWDFQIVVHWV',
  secretAccessKey: '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'
  })

  
const myBucket = new AWS.S3({
  params: { Bucket: S3_BUCKET},
  region: REGION,
  })

function App() {
  //파일 업로드 진행 상태를 저장할 상태 변수
  const [progress , setProgress] = useState(0);

  //업로드할 파일을 저장할 상태 변수
  const [selectedFile, setSelectedFile] = useState(null);

  //파일 선택 변경할 때 호출될 함수
  const handleFileInput = (e) => {
    //선택한 파일을 selectedFile에 저장 
    setSelectedFile(e.target.files[0]);
  }
  //업로드 버튼 눌렀을 때 전송하는 함수
  const uploadFile = (file) => {
    const params = {
      ACL: 'public-read',
      Body: file,
      Bucket: S3_BUCKET,
      Key: file.name
    };
    //전송함수 호출
    myBucket.putObject(params).on('httpUploadProgress', (evt) => {
      //중간에 전송 비율 출력
      setProgress(Math.round((evt.loaded / evt.total) * 100))
      }).send((err) => {
        if (err) console.log(err)})}

  return <div>
    <div>Native SDK File Upload Progress is {progress}%</div>
    <input type="file" onChange={handleFileInput}/>
    <button onClick={() => uploadFile(selectedFile)}> Upload to S3</button>
  </div>
}
export default App;