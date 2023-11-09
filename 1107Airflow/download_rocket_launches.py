import json
import pathlib
import airflow.utils.dates
import requests
import requests.exceptions as requests_exceptions
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator


#인스턴스 생성 - 모든 워크플로의 시작점
#dag 이름 과 설명 그리고 시작 날짜 및 실행 간격 설정
dag = DAG(
    dag_id="download_rocket_launches",
    description="Download rocket pictures of recently launched rockets.",
    start_date=airflow.utils.dates.days_ago(14),
    schedule_interval=None
)

#리눅스 작업을 생성
#웹 서버 API 데이터는 되도록이면 curl을 이용해서 관리하는 것이 편리함
#bash 스크립트를 이용해서 curl로 URL 결과값 다운로드
download_launches = BashOperator(
    task_id="download_launches",
    bash_command="curl -o /tmp/launches.json -L'https://ll.thespacedevs.com/2.0.0/launch/upcoming'", # noqa: E501
    dag=dag,
)

#웹에서 가져온 데이터를 파싱하고 이미지 경로에서 이미지 다운받아서 저장
def _get_pictures():
    # 디렉토리 존재 여부를 확인해서 디렉토리를 생성
    pathlib.Path("/tmp/images").mkdir(parents=True, exist_ok=True)
    # 데이터를 파싱하고 이미지 경로를 추출
    with open("/tmp/launches.json") as f:
        launches = json.load(f)
        image_urls = [launch["image"] for launch in launches["results"]]
        for image_url in image_urls:
            try:
                response = requests.get(image_url)
                image_filename = image_url.split("/")[-1]
                target_file = f"/tmp/images/{image_filename}"
                with open(target_file, "wb") as f:
                    f.write(response.content)
                print(f"Downloaded {image_url} to {target_file}")
            except requests_exceptions.MissingSchema:
                print(f"{image_url} appears to be an invalid URL.")
            except requests_exceptions.ConnectionError:
                print(f"Could not connect to {image_url}.")
#DAG에서 파이썬 함수를 호출

#파이썬 명령을 쓰고 싶을 때 PythonOperator
get_pictures = PythonOperator(
    task_id="get_pictures",
    python_callable=_get_pictures,
    #함수를 먼저 작성하고 python_callable 로 호출
    dag=dag
)

#알림 설정
notify = BashOperator(
    task_id="notify",
    bash_command='echo "이미지 저장 성공"',
    dag=dag,
)
#태스크 실행 순서 설정
download_launches >> get_pictures >> notify