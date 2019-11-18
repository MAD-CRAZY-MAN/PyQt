### Table Widget

- 행: 줄을 의미, 열: 칸을 의미

- QListWidget과 마찬가지로 QAbstracItemView를 상속받는 위젯이다.

- QAbstracltimeView속성 https://wikidocs.net/35496#qlistwidget_1

  - autoScroll: ListWidget에 항목이 많아졌을 때, 자동으로 스크롤을 할 수 있도록 만들어줌
  - dragEnabled: ListWidget의 항목을 드래그 할 수 있게 할지를 결정한다.
  - dragDropMode: Drag & Drop을 허용할지, Drag만 허용할지 등을 결정한다.
  - defaultDropAction: Drop했을 때, 어떤 행동을 할지를 결정한다. 기본값은 CopyAction
  - alternatingRowColor: 줄을 구분하기 쉽게 짝수 번째 줄의 배경색을 변경한다.
  - selectionMode: 선택 모드를 결정한다. 기본값은 ExtendedSelection이며, MultiSelection등을 선택할 수 있습니다.
  - selectionBehavior : 선택 방법을 결정합니다. 기본값은 SelectItems이며, SelectRow, SelectColumns등을 선택할 수 있습니다.

- QTableView의 속성

  - ShowGrid: 표의 선을 보여줄지를 결정한다.
  - gridStyle: showGrid를 체크했을 때, 표의 선을 어떤 모양으로 할지 결정한다. (기본값, 실선)

- QTableWidget의 속성

  - rowCount: QTableWidget의 행의 개수를 결정
  - columnCount: QTableWidget의 열의 개수를 결정

- QTableWidget의 시그널과 함수

  - 시그널

    - ableWidget의 Cell의 내용이 바뀌었을 때 기능 실행
      **self.TableWidget이름.cellChanged.connect(함수)**
    - TableWidget에서 선택된 Cell이 바뀌었을 때 기능 실행
      **self.TableWidget이름.currentCellChanged.connect(함수)**
    - TableWidget에서 Cell이 클릭 되었을 때 기능 실행
      **self.TableWidget이름.cellClicked.connect(함수)**
    - TableWidget에서 Cell이 더블클릭 되었을 때 기능 실행
      **self.TableWidget이름.cellDoubleClicked.connect(함수)**

  - 함수

    - 현재 상태의 반환
      - .item(row, col): row번쨰 줄, col번째 열의 항목을 반환한다. 이때, 반환된 항목을 QTableWidgetItem의 형식으로 반환된다.
      - .currentItem(): 현재 선택하고 있는 항목을 반환한다. 이때, 반환된 항목을 QTableWidgetItem의 형식으로 반환한다.
      - .currentRow(): 현재 선택하고 있는 항목의 행을 반환한다.
      - .currentColumn(): 현재 선택하고 있는 항목의 열을 반환한다.
      - .selectedItems(): 선택한 항목들을 리스트 형식으로 반환한다. 리스트 안에는 선택된 항목들이 QTableWidgetItem의 형식으로 포함되어있다.
      - .selectedRanges(): 현재 선택한 범위를 QTableWidgetSelectionRange의 형식으로 반환한다.

  - 항목의 추가, 삭제와 관련된 함수

    - .setItem(row, col, item): row번째 줄, col번쨰 칸에 Item이라는 항목을 추가한다.
    - .takeItem(row, col): row번째 줄, col번째 칸에 있는 항목을 삭제한다.
    - .clear(): 행과 열의 Header를 포함한 모든 항목을 삭제한다.
    - .clearContents(): 행과 열의 Header를 제외한 모든 항목을 삭제한다.

  - Table의 행과 열에 관련된 함수

    - .currentColumnCount():  현재 Table Widget에 존재하는 열의 개수를 반환합니다.
    - .currentRowCount(): 현재 Table Widget에 존재하는 행의 개수를 반환합니다.
    - .setColumnCount(col): 현재 Table Widget의 열의 개수를 col개로 설정합니다.
    - .setRowCount(row): 현재 Table Widget의 행의 개수를 row개로 설정합니다.
    - .horizontalHeaderItem(col):  col번째 열의 Header를 QTableWidgetItem 형식의 객체로 반환합니다
    - .takeHorizontalHeader(col): col번째 열의 Header를 삭제합니다. 이때 삭제된 항목은 QTableWidgetItem형식의 객체로 반환됩니다.
    - .setHorizontalHeaderItem(col, item): col번째 열의 Header를 Item이 가지고 있는 글자로 바꿉니다. 이때, Item은 QTableWidgetItem 형식의 객체여야 합니다.
    - .setHorizontalHeaderLabels(List): 열들의 Header를 일괄적으로 변경합니다. Parameter로 새로운 Header가 될 문자열이 들어있는 List가 필요하며, List의 0번째 항목이 0번째 열의 Header가 됩니다.

    

    - .verticalHeaderItem(row): row번째 줄의 Header를 QTableWidgetItem 형식의 객체로 반환합니다
    - .takeVerticalHeader(row):  row번째 줄의 Header를 삭제합니다. 이때 삭제된 항목은 QTableWidgetItem형식의 객체로 반환됩니다.
    - .setVerticalHeaderItem(row, item): row번째 줄의 Header를 Item이 가지고 있는 글자로 바꿉니다. 이때, Item은 QTableWidgetItem 형식의 객체여야 합니다.
    - .setVerticalHeaderLabels(List): 행들의 Header를 일괄적으로 변경합니다. Parameter로 새로운 Header가 될 문자열이 들어있는 List가 필요하며, List의 0번째 항목이 0번째 행의 Header가 됩니다.

    출처: https://wikidocs.net/35498

