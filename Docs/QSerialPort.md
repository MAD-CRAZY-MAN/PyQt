### QSerialPort

- bool QSerialPort::flush()
  - 이 함수는 잠금없이 시리얼포트 아래에 내부 쓰기 버퍼로부터 가능한 많이 내 쓴다 .
  - 만약 어떤 데이터를 썼다면, 이 함수는 True를 반환하고 , 그렇지않으면 False를 반환한다.
  - 시리얼 포트로 즉시 버퍼 데이터를 보내기위해 이 함수를 호출하시오.
- qint64 QSerialPort::bytesToWrite() const
  - 쓰여지길 기다리는 바이트 수를 반환한다. 그 바이트 들은 이벤트 루프로 돌아가 제어 될 때 또는 flush()를 호출 할 때 쓰여진다.
- bool QSerialPort::waitForBytesWritten(int msecs)
  - 직렬 포트에 하나 이상의 바이트가 기록되고 바이트Written() 신호가 방출될 때까지 차단한다. 이 기능은 msec 밀리초 후에 시간 초과되며, 기본 시간 초과 시간은 30000밀리초입니다. msec가 -1이면 이 기능은 시간 초과되지 않는다.
  - 바이트Written() 신호가 방출되면 true를 반환하고, 그렇지 않으면 false(오류 발생 또는 작업 시간 초과)를 반환한다.

출처 https://doc.qt.io/qt-5/qserialport.html#flush