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

    lcd = LCD()
    string = " Hello!\n"
    lcd.message(string)
    utime.sleep(2)
    string = "    Sunfounder!"   
    lcd.message(string)
    utime.sleep(2)
    lcd.clear()   

プログラムを実行すると、LCDには順番に2行のテキストが表示され、その後消えます。

.. note:: コードが実行されているときに画面が真っ白な場合、背面のポテンショメータを回してコントラストを調整できます。

**動作原理は？**

lcd1602ライブラリでは、lcd1602に関連する機能をLCDクラスに統合しています。

lcd1602ライブラリをインポート

.. code-block:: python

    from lcd1602 import LCD    

LCDクラスのオブジェクトを宣言し、それにlcdという名前を付けます。

.. code-block:: python

    lcd = LCD()

このステートメントはLCDにテキストを表示します。引数は文字列型でなければならない点に注意が必要です。整数や浮動小数点数を渡したい場合は、強制的に変換する ``str()`` を使用する必要があります。

.. code-block:: python

    lcd.message(string)

このステートメントを複数回呼び出すと、lcdはテキストを重ねて表示します。そのため、次のステートメントを使用して表示をクリアする必要があります。

.. code-block:: python

    lcd.clear()

