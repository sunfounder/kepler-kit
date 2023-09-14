.. _py_pa_buz:

3.2 カスタムトーン
==========================================

前回のプロジェクトではアクティブブザーを使用しましたが、今回はパッシブブザーを使用します。

アクティブブザーと同様に、パッシブブザーも電磁誘導の現象を利用して動作します。違いは、パッシブブザーには振動源がないため、直流信号を使っても音を出さない点です。
しかし、これによりパッシブブザーは自分自身の振動周波数を調整し、"ド、レ、ミ、ファ、ソ、ラ、シ"などの異なる音を出すことができます。

パッシブブザーでメロディを鳴らしましょう！

* :ref:`cpn_buzzer`

**必要な部品**

このプロジェクトで必要な部品は以下の通りです。

全体のキットを購入すると非常に便利です。リンクはこちら：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前
        - このキットに含まれるアイテム
        - リンク
    *   - ケプラーキット
        - 450+
        - |link_kepler_kit|

以下のリンクから個別に購入することもできます。

.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - 部品
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
        - :ref:`cpn_transistor`
        - 1(S8050)
        - |link_transistor_buy|
    *   - 6
        - :ref:`cpn_resistor`
        - 1(1KΩ)
        - |link_resistor_buy|
    *   - 7
        - パッシブ :ref:`cpn_buzzer`
        - 1
        - |link_passive_buzzer_buy|

**回路図**

|sch_buzzer|

GP15出力が高い場合、1Kの電流制限抵抗を経て（トランジスタを保護するため）、S8050（NPNトランジスタ）が導通し、ブザーが鳴ります。

S8050（NPNトランジスタ）の役割は、電流を増幅してブザーの音を大きくすることです。実際、GP15に直接ブザーを接続することもできますが、ブザーの音が小さくなることに気づくでしょう。

**配線**

|img_buzzer|

キットには2つのブザーが含まれていますが、ここではパッシブブザー（背面に露出したPCBがあるもの）を使用します。

ブザーはトランジスタが必要なため、ここではS8050を使用します。

|wiring_buzzer|


**コード**

.. note::

    * ``kepler-kit-main/micropython`` のパス下にある ``3.2_custom_tone.py`` ファイルを開くか、このコードをThonnyにコピーして、"Run Current Script"をクリックするか、単にF5キーを押して実行します。

    * 右下隅の"MicroPython（Raspberry Pi Pico）"インタープリターをクリックするのを忘れないでください。

    * 詳細なチュートリアルは、 :ref:`open_run_code_py` を参照してください。

.. code-block:: python

    import machine
    import utime

    buzzer = machine.PWM(machine.Pin(15))

    def tone(pin, frequency, duration):
        pin.freq(frequency)
        pin.duty_u16(30000)
        utime.sleep_ms(duration)
        pin.duty_u16(0)

    tone(buzzer, 440, 250)
    utime.sleep_ms(500)
    tone(buzzer, 494, 250)
    utime.sleep_ms(500)
    tone(buzzer, 523, 250)


**動作原理**

パッシブブザーにデジタル信号が与えられると、振動板を押し続けるだけで音は発生しません。

したがって、 ``tone()`` 関数を使用して、PWM信号を生成し、パッシブブザーに音を出させます。

この関数には3つのパラメーターがあります：

* **pin** 、ブザーを制御するGPIOピン。
* **frequency** 、ブザーの音程は周波数で決まり、周波数が高いほど音程も高くなります。
* **duration** 、音の持続時間。

``duty_u16()`` 関数を使用して、デューティーサイクルを30000（約50%）に設定します。他の数値でも構いませんが、振動させるためには不連続な電気信号を生成する必要があります。



**詳細**

ピアノの基本周波数に従って特定の音をシミュレートし、完全な楽曲を演奏することができます。

* `Piano key frequencies - Wikipedia <https://en.wikipedia.org/wiki/Piano_key_frequencies>`_



.. note::

    * ``kepler-kit-main/micropython`` のパス下にある ``3.2_custom_tone_2.py`` ファイルを開くか、このコードをThonnyにコピーして、"Run Current Script"をクリックするか、単にF5キーを押して実行します。

    * 右下隅の"MicroPython（Raspberry Pi Pico）"インタープリターをクリックするのを忘れないでください。

    * 詳細なチュートリアルは、 :ref:`open_run_code_py` を参照してください。

.. code-block:: python

    import machine
    import utime

    NOTE_C4 = 262
    NOTE_G3 = 196
    NOTE_A3 = 220
    NOTE_B3 = 247

    melody = [NOTE_C4, NOTE_G3, NOTE_G3, NOTE_A3, NOTE_G3, NOTE_B3, NOTE_C4]

    buzzer = machine.PWM(machine.Pin(15))

    def tone(pin, frequency, duration):
        pin.freq(frequency)
        pin.duty_u16(30000)
        utime.sleep_ms(duration)
        pin.duty_u16(0)

    for note in melody:
        tone(buzzer, note, 250)
        utime.sleep_ms(150)

