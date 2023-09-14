.. _py_keypad:

4.2 4x4キーパッド
========================

4x4キーボード、別名マトリックスキーボードは、単一のパネルに16キーが配置されたマトリックスです。

このキーパッドは、主にデジタル入力が必要なデバイスに見られます。例えば、電卓、テレビのリモートコントロール、押しボタン式の電話、自動販売機、ATM、ダイヤル錠、デジタルドアロックなどです。

このプロジェクトでは、押されたキーを特定し、関連するキーの値を取得する方法を学びます。

* :ref:`cpn_keypad`
* `E.161 - Wikipedia <https://en.wikipedia.org/wiki/E.161>`_

**必要なコンポーネント**

このプロジェクトでは、以下のコンポーネントが必要です。

一式を購入するのは確かに便利です、リンクはこちら：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前	
        - このキットに含まれるアイテム
        - リンク
    *   - ケプラーキット	
        - 450以上
        - |link_kepler_kit|

以下のリンクから個別にも購入可能です。

.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - コンポーネント	
        - 数量
        - リンク
    *   - 1
        - :ref:`cpn_pico_w`
        - 1
        - |link_picow_buy|
    *   - 2
        - マイクロUSBケーブル
        - 1
        - 
    *   - 3
        - :ref:`cpn_breadboard`
        - 1
        - |link_breadboard_buy|
    *   - 4
        - :ref:`cpn_wire`
        - 数本
        - |link_wires_buy|
    *   - 5
        - :ref:`cpn_resistor`
        - 4(10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_keypad`
        - 1
        - |link_keypad_buy|

**回路図**

|sch_keypad|

マトリックスキーボードの各列には4つのプルダウン抵抗が接続されており、キーが押されていない場合にG6〜G9が安定した低レベルになるようにしています。

キーボードの行（G2〜G5）は高レベルに設定されています。もしG6〜G9のいずれかが高レベルで読み取られた場合、どのキーが押されたかがわかります。

例えば、G6が高レベルで読み取られた場合、数字のキー1が押されています。これは、数字のキー1の制御ピンがG2とG6であり、数字のキー1が押されたときにG2とG6が接続され、G6も高レベルになるからです。

**配線**

|wiring_keypad|

配線を容易にするため、上記の図では、マトリックスキーボードの列と10K抵抗が同時にG6〜G9の位置にある穴に挿入されています。

**コード**

.. note::

    * ``kepler-kit-main/micropython`` のパスにある ``4.2_4x4_keypad.py`` ファイルを開くか、このコードをThonnyにコピーして、「Run Current Script」をクリックするか、単にF5キーを押して実行します。

    * 右下隅にある「MicroPython（Raspberry Pi Pico）」のインタープリタをクリックするのを忘れないでください。

    * 詳細なチュートリアルについては、 :ref:`open_run_code_py` を参照してください。

.. code-block:: python

    import machine
    import time

    characters = [["1","2","3","A"],["4","5","6","B"],["7","8","9","C"],["*","0","#","D"]]

    pin = [2,3,4,5]
    row = []
    for i in range(4):
        row.append(None)
        row[i] = machine.Pin(pin[i], machine.Pin.OUT)

    pin = [6,7,8,9]
    col = []
    for i in range(4):
        col.append(None)
        col[i] = machine.Pin(pin[i], machine.Pin.IN)

    def readKey():
        key = []
        for i in range(4):
            row[i].high()
            for j in range(4):
                if(col[j].value() == 1):
                    key.append(characters[i][j])
            row[i].low()
        if key == [] :
            return None
        else:
            return key

    last_key = None
    while True:
        current_key = readKey()
        if current_key == last_key:
            continue
        last_key = current_key
        if current_key != None:
            print(current_key)
        time.sleep(0.1)

プログラムを実行すると、Shellがキーパッドで押したキーを出力します。

**仕組み**

.. code-block:: python

    import machine
    import time

    characters = [["1","2","3","A"],["4","5","6","B"],["7","8","9","C"],["*","0","#","D"]]

    pin = [2,3,4,5]
    row = []
    for i in range(4):
        row.append(None)
        row[i] = machine.Pin(pin[i], machine.Pin.OUT)

    pin = [6,7,8,9]
    col = []
    for i in range(4):
        col.append(None)
        col[i] = machine.Pin(pin[i], machine.Pin.IN)

マトリックスキーボードの各キーを配列 ``characters[]`` に宣言し、各行と列のピンを定義します。

.. code-block:: python

    last_key = None
    while True:
        current_key = readKey()
        if current_key == last_key:
            continue
        last_key = current_key
        if current_key != None:
            print(current_key)
        time.sleep(0.1)

これは、ボタンの値を読み取り、出力するメイン関数の一部です。

関数 ``readKey()`` は、各ボタンの状態を読み取ります。

``if current_key != None`` および ``if current_key == last_key`` の文は、キーが押されているかどうかと、押されたボタンの状態を判断するために使用されます。
（例えば、'1'を押しているときに'3'を押すと、判断が成立します。）

条件が成立すると、現在押されているキーの値を出力します。

``last_key = current_key`` の文は、各判断の状態を配列 ``last_key`` に割り当て、次の条件判断に備えます。

.. code-block:: python

    def readKey():
        key = []
        for i in range(4):
            row[i].high()
            for j in range(4):
                if(col[j].value() == 1):
                    key.append(characters[i][j])
            row[i].low()
        if key == [] :
            return None
        else:
            return key

この関数は、各行に順番に高レベルを割り当てます。ボタンが押されると、キーの位置する列が高レベルになります。
二層のループの判断後、状態が1のボタンの値が配列 ``key`` に格納されます。

キー'3'を押す場合：

|img_keypad_pressed|

``row[0]`` が高レベルに書き込まれ、 ``col[2]`` が高レベルになります。

``col[0]`` 、 ``col[1]`` 、 ``col[3]`` は低レベルになります。

四つの状態があります：0、0、1、0；そして、'3'を ``pressed_keys`` に書き込みます。

``row[1]`` 、 ``row[2]`` 、 ``row[3]`` が高レベルに書き込まれると、
``col[0]`` ~ ``col[4]`` は低レベルになります。

ループが停止し、key = '3'が返されます。

ボタン'1'と'3'を押すと、key = ['1','3']が返されます。
