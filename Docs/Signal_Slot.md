### Signal / Slot

- Signal: 위젯에 정의된 이벤트
- Slot: 이벤트가 발생할 때 호출되는 함수나 메서드
- 사용자 정의 시그널: PyQt에서 제공하지 않는 이벤트(시그널)을 직접 정의할 수 있다.

- 왜 필요할까?
  - 지금 시리얼 통신 프로그램을 만들고 있는데 다른 작업도 처리하면서 통신을 해야하기 때문에 스레드를 사용해야한다. 스레드를 사용하게 되면 시그널 클래스에서 받은 값을 GUI클래스로 보내주는 방법이 필요한데 이때 시그널/슬로을 사용하면 된다.
  - 시그널을 통해 한 객체에서 다른 객체로 값을 보내줄 수 있다.



출처: [https://pystock.atlassian.net/wiki/spaces/FIN/pages/393838/7+-+PyQt#id-7%EA%B5%90%EC%8B%9C-PyQt%EC%8B%9C%EA%B7%B8%EB%84%90/%EC%8A%AC%EB%A1%AF(%EC%8B%AC%ED%99%94)-PyQt%EC%82%AC%EC%9A%A9%EC%9E%90%EC%A0%95%EC%9D%98%EC%8B%9C%EA%B7%B8%EB%84%90/%EC%8A%AC%EB%A1%AF](https://pystock.atlassian.net/wiki/spaces/FIN/pages/393838/7+-+PyQt#id-7교시-PyQt시그널/슬롯(심화)-PyQt사용자정의시그널/슬롯)