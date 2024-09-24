.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

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
    from machine import I2C, Pin
    import time
    import urandom

    # Initialize I2C communication for the LCD1602 display
    i2c = I2C(1, sda=Pin(6), scl=Pin(7), freq=400000)

    # Create an LCD object for controlling the LCD1602 display
    lcd = LCD(i2c)

    # Keypad character mapping for a 4x4 matrix keypad
    characters = [["1", "2", "3", "A"], 
                ["4", "5", "6", "B"], 
                ["7", "8", "9", "C"], 
                ["*", "0", "#", "D"]]

    # Define row pins for the keypad
    pin = [21, 20, 19, 18]
    row = []
    for i in range(4):
        row.append(None)
        row[i] = machine.Pin(pin[i], machine.Pin.OUT)  # Set row pins as output

    # Define column pins for the keypad
    pin = [13, 12, 11, 10]
    col = []
    for i in range(4):
        col.append(None)
        col[i] = machine.Pin(pin[i], machine.Pin.IN)  # Set column pins as input

    # Function to read a key from the keypad
    def readKey():
        key = []
        for i in range(4):
            row[i].high()  # Set the row pin high
            for j in range(4):
                if col[j].value() == 1:  # Check if any column is pressed
                    key.append(characters[i][j])  # Record the corresponding key
            row[i].low()  # Set the row pin low
        if key == []:
            return None  # Return None if no key is pressed
        else:
            return key  # Return the pressed key

    # Initialize and reset the game variables (random pointValue, upper/lower limits)
    def init_new_value():
        global pointValue, upper, count, lower
        pointValue = int(urandom.uniform(0, 99))  # Generate a random number between 0 and 99
        print(pointValue)  # Print the target number (for debugging)
        upper = 99  # Set initial upper bound
        lower = 0  # Set initial lower bound
        count = 0  # Reset the player's guess count
        return False  # Indicate that the game has not ended

    # Function to display the game information on the LCD
    # If the player has guessed correctly, show "GAME OVER"
    # Otherwise, show the current guess and range
    def lcd_show(result):
        lcd.clear()  # Clear the LCD display
        if result == True:  # If the player guessed correctly
            string = "GAME OVER!\n"
            string += "Point is " + str(pointValue)  # Display the correct number
        else:
            string = "Enter number: " + str(count) + "\n"  # Show the player's current guess
            string += str(lower) + " < Point < " + str(upper)  # Show the range of possible values
        lcd.message(string)  # Send the string to the LCD
        return

    # Process the player's guess and update the upper or lower bound
    # If the guess matches the pointValue, return True to indicate the game is over
    # Otherwise, update the bounds and return False
    def number_processing():
        global upper, count, lower
        if count > pointValue:
            if count < upper:
                upper = count  # Update the upper bound if the guess is too high
        elif count < pointValue:
            if count > lower:
                lower = count  # Update the lower bound if the guess is too low
        elif count == pointValue:
            return True  # Return True if the guess matches the pointValue
        count = 0  # Reset the guess count for the next attempt
        return False

    ## Main game setup and loop
    # Display a welcome message and prompt the user to press 'A' to start
    string = "Press A to Start!"
    lcd.message(string)
    result = init_new_value()  # Initialize game variables

    # Main loop to handle keypad input and update the display
    last_key = None
    while True:
        current_key = readKey()  # Read the current key pressed
        if current_key == last_key:
            continue  # Skip processing if the same key is still pressed
        last_key = current_key  # Update the last pressed key
        
        if current_key != None:
            # If 'A' is pressed, restart the game with a new target number
            if current_key == ["A"]:
                result = init_new_value()
            # If 'D' is pressed, check if the current guess is correct
            elif current_key == ["D"]:
                result = number_processing()
            # If a number is pressed and the count is less than 10 digits
            elif current_key[0] in list("1234567890") and count < 10:
                count = count * 10 + int(current_key[0])  # Add the digit to the current guess
            lcd_show(result)  # Update the LCD with the current game state
        time.sleep(0.1)  # Small delay for key debounce



* コードが実行された後、 ``A`` を押してゲームを開始します。ランダムな数字 ``point`` が生成されますが、LCDには表示されません。あなたがするべきことは、その数字を推測することです。
* 最終計算が終わるまで、最初の行の末尾に入力した数字が表示されます（比較を開始するには ``D`` を押します）。
* ``point`` の数字の範囲が2行目に表示されます。範囲内の数字を入力する必要があります。
* 数字を入力すると、範囲が狭まります。もし幸運な数字（または不運な数字）を当てた場合は、 ``GAME OVER!`` が表示されます。

.. note::
    コードと配線が問題ないが、LCDがまだ内容を表示しない場合は、裏側のポテンショメータを回してコントラストを上げることができます。

