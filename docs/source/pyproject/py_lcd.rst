.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

.. _py_lcd:

3.4 液晶ディスプレイ
===============================

LCD1602は、キャラクタ型の液晶ディスプレイで、同時に32（16×2）文字を表示することができます。

ご存知のように、LCDやその他のディスプレイは人間とマシンの対話を大いに豊かにしていますが、一つの弱点があります。
それは、コントローラに接続すると、多くのIOポートが占有されてしまうことです。特に、外部ポートの少ないコントローラではこの問題は顕著です。
そのため、この問題を解決するためにI2Cバスを備えたLCD1602が開発されました。

* :ref:`cpn_i2c_lcd`
* `Inter-Integrated Circuit - Wikipedia <https://ja.wikipedia.org/wiki/I2C>`_

|pin_i2c|

このセクションでは、I2C0インターフェースを使用してLCD1602を制御し、テキストを表示します。

**必要なコンポーネント**

このプロジェクトには、以下のコンポーネントが必要です。

一式を購入する方が便利です、リンクはこちら：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前
        - このキットに含まれるアイテム
        - リンク
    *   - ケプラーキット
        - 450以上
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
        - :ref:`cpn_i2c_lcd`
        - 1
        - |link_i2clcd1602_buy|

**回路図**

|sch_lcd|

**配線**

|wiring_lcd|

**コード**

.. note::

    * ``kepler-kit-main/micropython`` フォルダ内の ``3.4_liquid_crystal_display.py`` ファイルを開くか、このコードをThonnyにコピーしてから「Run Current Script」をクリック、または単にF5キーを押して実行してください。

    * 右下隅にある「MicroPython（Raspberry Pi Pico）」インタープリタをクリックするのを忘れないでください。

    * 詳細なチュートリアルは :ref:`open_run_code_py` を参照してください。
    
    * ここでは ``lcd1602.py`` というライブラリが必要です。Pico Wにアップロードされているか確認してください。詳細なチュートリアルは  :ref:`add_libraries_py` を参照してください。


.. code-block:: python

    from lcd1602 import LCD
    import utime

    from machine import I2C, Pin
    from lcd1602 import LCD
    import time

    # Initialize I2C communication;
    i2c = I2C(1, sda=Pin(6), scl=Pin(7), freq=400000)

    # Create an LCD object for interfacing with the LCD1602 display
    lcd = LCD(i2c)

    # Display the first message on the LCD
    # Use '\n' to create a new line.
    string = "SunFounder\n    LCD Tutorial"
    lcd.message(string)
    # Wait for 2 seconds
    time.sleep(2)
    # Clear the display
    lcd.clear()

    # Display the second message on the LCD
    string = "Hello\n  World!"
    lcd.message(string)
    # Wait for 5 seconds
    time.sleep(5)
    # Clear the display before exiting
    lcd.clear()  

プログラムを実行すると、LCDには順番に2行のテキストが表示され、その後消えます。

.. note:: コードが実行されているときに画面が真っ白な場合、背面のポテンショメータを回してコントラストを調整できます。

**動作原理は？**

#. I2C通信の設定

   ``machine``モジュールはI2C通信を設定するために使用されます。 SDA（シリアルデータ）とSCL（シリアルクロック）ピン（それぞれピン20と21）が定義され、I2Cの周波数（400kHz）も設定されます。

   .. code-block:: python
      
      from machine import I2C, Pin
      i2c = I2C(1, sda=Pin(6), scl=Pin(7), freq=400000)

#. LCDディスプレイの初期化

   ``lcd1602``モジュールの``LCD``クラスがインスタンス化されます。このクラスは、I2Cを介してLCDディスプレイとの通信を処理します。 ``i2c``オブジェクトを使用して``LCD``オブジェクトが作成されます。

   ``lcd1602``ライブラリの詳細な使用方法については、``lcd1602.py``を参照してください。

   .. code-block:: python
      
      from lcd1602 import LCD
      lcd = LCD(i2c)

#. LCDにメッセージを表示

   ``LCD``オブジェクトの``message``メソッドは、画面にテキストを表示するために使用されます。 ``\n``文字はLCD上に新しい行を作成します。 ``time.sleep()``関数は、指定された秒数だけ実行を一時停止します。

   .. code-block:: python
      
      string = "SunFounder\n    LCD Tutorial"
      lcd.message(string)
      time.sleep(2)
      lcd.clear()

#. ディスプレイのクリア

   ``LCD``オブジェクトの``clear``メソッドが呼び出され、ディスプレイからテキストが消去されます。

   .. code-block:: python
      
      lcd.clear()

#. 2つ目のメッセージの表示

   新しいメッセージが表示され、その後遅延が発生し、画面が再びクリアされます。

   .. code-block:: python
      
      string = "Hello\n  World!"
      lcd.message(string)
      time.sleep(5)
      lcd.clear()