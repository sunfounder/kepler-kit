.. _py_led:

2.1 こんにちは、LED！ 
=======================================

"Hello, world!"を出力することがプログラミング学習の第一歩であるように、LEDをプログラムで制御することは、物理的なプログラミングを学ぶ際の伝統的な導入となっています。

* :ref:`cpn_led`

**必要な部品**

このプロジェクトでは、以下の部品が必要です。

キット全体を購入することは非常に便利です。リンクは以下になります：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前
        - このキットのアイテム
        - リンク
    *   - Kepler Kit	
        - 450以上
        - |link_kepler_kit|

以下のリンクから個別に購入することもできます。

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
        - Micro USBケーブル
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
        - 1(220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_led`
        - 1
        - |link_led_buy|

**回路図**

|sch_led|

この回路は単純な原理で動作し、図に示されているように電流の方向が示されています。GP15が高レベル（3.3v）を出力すると、220ohmの電流制限抵抗を経てLEDが点灯します。GP15が低レベル（0v）を出力すると、LEDは消灯します。


**配線**

|wiring_led|

回路を組む際は、電流の方向に従いましょう！

1. Pico WボードのGP15ピンでLEDが供給され、ここから回路が始まります。
#. LEDを保護するために、電流は220オームの抵抗器を通過しなければなりません。抵抗器の一方の端子はPico W GP15ピンと同じ行（私の回路では行20）に挿入し、他方の端子はブレッドボードの空いている行（行24）に挿入してください。

    .. note::
        220オームの抵抗器のカラーリングは赤、赤、黒、黒、茶です。

#. LEDを取り上げると、一方のリードが他方よりも長いことがわかります。長いリードを抵抗器と同じ行に、短いリードをブレッドボードの中央の隙間を挟んで同じ行に接続してください。

    .. note::
        長いリードは陽極であり、回路の正側を表します。短いリードは陰極であり、回路の負側を表します。
        
        陽極はGPIOピンに抵抗器を介して接続する必要があり、陰極はGNDピンに接続する必要があります。

#. オス-オス（M2M）ジャンパーワイヤーを使用して、LEDの短いピンをブレッドボードの負電源バスに接続します。
#. ジャンパーを使用して、Pico WのGNDピンを負の電源バスに接続します。

**コード**

.. note::
    
    * ``kepler-kit-main/micropython`` のパスの下で ``2.1_hello_led.py`` ファイルを開くか、このコードをThonnyにコピーしてから、"Run Current Script"をクリックするか、単にF5を押して実行してください。

    * 右下隅の"MicroPython（Raspberry Pi Pico）"インタプリターをクリックすることを忘れないでください。

    * 詳細なチュートリアルは、 :ref:`open_run_code_py` を参照してください。

.. code-block:: python

    import machine
    import utime
    
    led = machine.Pin(15, machine.Pin.OUT)
    while True:
        led.value(1)
        utime.sleep(2)
        led.value(0)
        utime.sleep(2)

コードが実行された後、LEDが点滅するのが見えるでしょう。



**動作の仕組みは？**

GPIOを使用するには、 ``machine`` ライブラリが必要です。

.. code-block:: python

    import machine

このライブラリには、MicroPythonとPico Wとの間で通信するために必要なすべての命令が含まれています。
このコード行がない場合、GPIOを制御することはできません。

次に注目するべき行は以下のとおりです。

.. code-block:: python

    led = machine.Pin(15, machine.Pin.OUT)

ここでオブジェクト ``led`` が定義されています。技術的には、x、y、banana、Michael_Jackson、または任意の文字など、任意の名前にすることができます。
プログラムを読みやすくするためには、目的を説明する名前を使用するのが最善です。

この行の第二部分（等号の後ろの部分）では、 ``machine`` ライブラリ内のPin関数を呼び出しています。これはPicoのGPIOピンに何をすべきかを指示するために使用されます。
``Pin`` 関数には2つのパラメーターがあります：最初の1つ（15）は設定するピンを表し、
第二のパラメーター（machine.Pin.OUT）は、ピンが入力ではなく出力であるべきことを指定します。

上記のコードではピンが「設定」されていますが、LEDを点灯させるわけではありません。これを行うためには、ピンを「使用」する必要もあります。

.. code-block:: python

    led.value(1)

GP15ピンは以前に設定され、 ``led`` と名付けられました。この文の機能は、 ``led`` の値を1に設定してLEDを点灯させることです。

全体として、GPIOを使用するには、以下のステップが必要です：

* **machineライブラリをインポートする** : これは必須であり、一度だけ実行されます。
* **GPIOを設定する** : 使用する前に、各ピンを設定する必要があります。
* **使用する** : ピンに値を割り当てることで、ピンの動作状態を変更します。

上記のステップに従って例を書くと、次のようなコードになります：

.. code-block:: python

    import machine
    led = machine.Pin(15, machine.Pin.OUT)
    led.value(1)

これを実行すると、LEDを点灯させることができます。

次に、"消灯"文を追加してみましょう：

.. code-block:: python

    import machine   
    led = machine.Pin(15, machine.Pin.OUT)
    led.value(1)
    led.value(0)

このコードに基づいて、このプログラムは最初にLEDを点灯させ、次に消灯させます。
しかし、実際に使用すると、このようにはなりません。
LEDから光が出ていないのは、2行の間の実行速度が非常に速いためであり、人間の目が反応するよりもはるかに速いからです。
LEDが点灯すると、私たちは即座に光を感じません。これはプログラムを遅くすることで修正できます。

プログラムの第二行には、以下の文が含まれるべきです：

.. code-block:: python

    import utime

``machine`` と同様に、ここでは ``utime`` ライブラリがインポートされており、時間に関連するすべてのことを処理します。
必要な遅延はこれに含まれています。 ``led.value(1)`` と ``led.value(0)`` の間に遅延文を追加し、それらを2秒間隔で分けます。

.. code-block:: python

    utime.sleep(2)

これでコードは次のようになります。
実行すると、LEDが最初に点灯し、次に消灯するのがわかります：

.. code-block:: python

    import machine 
    import utime  
    led = machine.Pin(15, machine.Pin.OUT)
    led.value(1)
    utime.sleep(2)
    led.value(0)

最後に、LEDを点滅させるようにしましょう。
ループを作成し、プログラムを書き直すと、この章の始めに見たものになります。

.. code-block:: python

    import machine
    import utime
    
    led = machine.Pin(15, machine.Pin.OUT)
    while True:
        led.value(1)
        utime.sleep(2)
        led.value(0)
        utime.sleep(2)

* :ref:`py_syntax_while_loops`

**さらに詳しく**

通常、ライブラリにはAPI（Application Programming Interface）ファイルが関連付けられています。
このファイルには、このライブラリを使用するために必要なすべての情報が含まれています。これには、関数、クラス、戻り値のタイプ、パラメータのタイプなどの詳細な説明もあります。

この記事では、MicroPythonの ``machine`` と ``utime`` ライブラリを使用しましたが、それらを使用するさまざまな方法は以下で見つけることができます。

* `machine.Pin <https://docs.micropython.org/en/latest/library/machine.Pin.html>`_

* `utime <https://docs.micropython.org/en/latest/library/utime.html>`_

LEDを点滅させるこの例を理解するためには、APIファイルを読むことをお勧めします！

.. note::

    * ``kepler-kit-main/micropython`` のパスの下にある ``2.1_hello_led_2.py`` ファイルを開くか、このコードをThonnyにコピーしてから、「Run Current Script」をクリックするか、単にF5を押して実行してください。

    * 右下隅の「MicroPython（Raspberry Pi Pico）」インタープリタをクリックするのを忘れないでください。

    * 詳細なチュートリアルについては、 :ref:`open_run_code_py` を参照してください。

.. code-block:: python

    import machine
    import utime

    led = machine.Pin(15, machine.Pin.OUT)
    while True:
        led.toggle()
        utime.sleep(1)
