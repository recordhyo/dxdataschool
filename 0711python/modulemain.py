import sys
import module #내가만든 module.py를 import 

#sys.path.append("./") 현재디렉토리에서 모듈이나 패키지 검색하도록 설정

print(module.myPI)
module.func("모듈 사용")