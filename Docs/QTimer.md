### QTimer

- 생성 
  - from PyQt.QtCore import *
  - timeVal = QTimer()
- 함수
  - .start()
    - QTimer가 시간을 체크하기 시작한다.
  - .start(msec)
    - QTimer가 Parameter만큼의 시간이 지난 후 시간을 체크하기 시작한다. Parameter로 시간을 입력해야 하며, 단위는 ms이다.
  - .stop() 
    - QTimer를 중지한다.
- Interval과 관련된 함수
  - .setInterval(msec)
    - QTimer의 Interval을 설정한다. Parameter로 Interval을 ms단위로 입력한다.
  - .timeout.connect(함수)
    - 매 Interval마다 어떤 함수를 실행할지 결정한다. 만약 Interval을 설정하지 않은 경우 1ms마다 함수가 반복된다.
- 상태 반환
  - .interval()
    - QTimer의 Interval을 반환한다.
  - .isActive()
    - QTimer가 작동 중인지 체크한다. 작동중: True, 멈춤: False 반환



출처: https://wikidocs.net/38522