.. _py_guess_number:

7.7 数字当てゲーム
==============================

数字当ては楽しいパーティーゲームで、友達と一緒に0～99の数字を入力します。各プレイヤーが数字を入力する度に、範囲が狭まり、誰かが正解するとそのプレイヤーは敗北し、罰を受けます。

例えば、運の良い数字が51で、プレイヤーはそれを見ることができない場合、プレイヤー1が50を入力すると、プロンプトは50 - 99に変わります。プレイヤー2が70を入力すると、範囲は50 - 70に変わります。プレイヤー3が51を入力した場合、そのプレイヤーは不運です。このケースでは、数字はキーパッドを通じて入力され、結果はLCDスクリーンに表示されます。

|guess_number|

**必要なコンポーネント**

このプロジェクトでは、以下のコンポーネントが必要です。

一式を購入する方が便利です、リンクはこちら：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前	
        - このキットに含まれるアイテム
        - リンク
    *   - ケプラーキット	
        - 450+ 
        - |link_kepler_kit|

以下のリンクから個別にも購入できます。

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
    *   - 7
        - :ref:`cpn_i2c_lcd`
        - 1
        - |link_i2clcd1602_buy|

**回路図**

|sch_guess_number|

この回路は、 :ref:`py_keypad` を基にしており、押されたキーを表示するためのI2C LCD1602が追加されています。

**配線**

|wiring_game_guess_number|

配線を簡単にするために、上記の図では、マトリックスキーボードの列行と10Kの抵抗器が同時にG10～G13の穴に挿入されています。


**コード**

.. note::

    * ``kepler-kit-main/micropython`` のパスの下にある ``7.7_game_guess_number.py`` ファイルを開くか、このコードをThonnyにコピーしてから「Run Current Script」をクリックするか、単純にF5キーを押して実行します。

    * 右下隅の「MicroPython（Raspberry Pi Pico）」インタープリタをクリックするのを忘れないでください。

    * 詳細なチュートリアルは、 :ref:`open_run_code_py` を参照してください。

.. code-block:: python

    from lcd1602 import LCD
    import machine
    import time
    import urandom


    # keypad function
    characters = [["1","2","3","A"],["4","5","6","B"],["7","8","9","C"],["*","0","#","D"]]

    pin = [21,20,19,18]
    row = []
    for i in range(4):
        row.append(None)
        row[i] = machine.Pin(pin[i], machine.Pin.OUT)

    pin = [13,12,11,10]
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

    # init/reset number
    # reset the result as False for lcd show
    def init_new_value():
    global pointValue,upper,count,lower
    pointValue = int(urandom.uniform(0, 99))
    print(pointValue)
    upper = 99
    lower = 0
    count = 0
    return False


    # lcd show message
    # If target, show game over.
    # If not target, or not detected, show guess number.
    def lcd_show(result):
        lcd.clear()
        if result == True: 
            string ="GAME OVER!\n"
            string +="Point is "+ str(pointValue)
        else : 
            string ="Enter number: " + str(count) +"\n"
            string += str(lower)+ " < Point < " + str(upper)
        lcd.message(string)
        return  

    # detect number & reflesh show message 
    # if not target, reflesh number (upper or lower) and return False
    # if target, return True 
    def number_processing():
        global upper,count,lower
        if count > pointValue:
            if count < upper:
                upper = count
        elif count < pointValue:
            if count > lower:
                lower = count
        elif count == pointValue:
            return True
        count = 0
        return False 

    ## start
    lcd = LCD()
    string = "Welcome!\n"
    string = "Press A to Start!"
    lcd.message(string)
    result=init_new_value()

    # read key & display
    last_key = None
    while True:
        current_key = readKey()
        if current_key == last_key:
            continue
        last_key = current_key
        if current_key != None:
            # print(current_key)
            if current_key ==["A"]: # reset number
                result=init_new_value() 
            elif current_key==["D"]: # check
                result=number_processing()
            elif current_key[0] in list(["1","2","3","4","5","6","7","8","9","0"]) and count < 10: #check validity & limit digits
                count = count * 10 + int(current_key[0])
            lcd_show(result) # show 
        time.sleep(0.1)


* コードが実行された後、 ``A`` を押してゲームを開始します。ランダムな数字 ``point`` が生成されますが、LCDには表示されません。あなたがするべきことは、その数字を推測することです。
* 最終計算が終わるまで、最初の行の末尾に入力した数字が表示されます（比較を開始するには ``D`` を押します）。
* ``point`` の数字の範囲が2行目に表示されます。範囲内の数字を入力する必要があります。
* 数字を入力すると、範囲が狭まります。もし幸運な数字（または不運な数字）を当てた場合は、 ``GAME OVER!`` が表示されます。

.. note::
    コードと配線が問題ないが、LCDがまだ内容を表示しない場合は、裏側のポテンショメータを回してコントラストを上げることができます。

