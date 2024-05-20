.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

.. _py_ultrasonic:

6.1 距離の測定
======================================

超音波センサーモジュールは、物体までの距離を決定するために、ソナーおよびレーダーシステムの原理に基づいて動作します。

* :ref:`cpn_ultrasonic`

**必要なコンポーネント**

このプロジェクトには、以下のコンポーネントが必要です。

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前
        - このキットに含まれるアイテム
        - リンク
    *   - Keplerキット
        - 450以上
        - |link_kepler_kit|

以下のリンクから個別にも購入可能です。

.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - S/N
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
        - :ref:`cpn_ultrasonic`
        - 1
        - |link_ultrasonic_buy|

**回路図**

|sch_ultrasonic|

**配線**

|wiring_ultrasonic|


**コード**

.. note::

    * ``kepler-kit-main/micropython`` のパスの下にある ``6.1_measuring_distance.py`` ファイルを開くか、このコードをThonnyにコピーしてから、「Run Current Script」をクリックするか、単にF5キーを押して実行してください。

    * 画面右下隅の「MicroPython（Raspberry Pi Pico）」インタプリタをクリックするのを忘れないでください。

    * 詳細なチュートリアルは、 :ref:`open_run_code_py` を参照してください。

.. code-block:: python

    import machine
    import time

    TRIG = machine.Pin(17, machine.Pin.OUT)
    ECHO = machine.Pin(16, machine.Pin.IN)

    def distance():
        TRIG.low()
        time.sleep_us(2)
        TRIG.high()
        time.sleep_us(10)
        TRIG.low()
        while not ECHO.value():
            pass
        time1 = time.ticks_us()
        while ECHO.value():
            pass
        time2 = time.ticks_us()
        during = time.ticks_diff(time2, time1)
        return during * 340 / 2 / 10000

    while True:
        dis = distance()
        print('Distance: %.2f' % dis)
        time.sleep_ms(300)

プログラムが動作すると、シェルは前方の障害物からの超音波センサーの距離を出力します。

**動作原理は？**

超音波センサーは、送信プローブによって発生された高周波の音波（超音波）を生成します。この超音波が物体に衝突すると、エコーとして反射され、受信プローブによって検出されます。送信から受信までの時間を計算することで、距離を求めることができます。
この原理に基づいて、 ``distance()`` 関数が導出されます。

.. code-block:: python

    def distance():
        TRIG.low()
        time.sleep_us(2)
        TRIG.high()
        time.sleep_us(10)
        TRIG.low()
        while not ECHO.value():
            pass
        time1 = time.ticks_us()
        while ECHO.value():
            pass
        time2 = time.ticks_us()
        during = time.ticks_diff(time2, time1)
        return during * 340 / 2 / 10000

* その中で、最初の数行は10usの超音波を送信するために使用されます。

.. code-block:: python

    TRIG.low()
    time.sleep_us(2)
    TRIG.high()
    time.sleep_us(10)
    TRIG.low()

* 次に、超音波が発射された瞬間にプログラムが一時停止し、現在の時間が記録されます。

.. code-block:: python

        while not ECHO.value():
            pass
        time1 = time.ticks_us()

* その後、プログラムは再び一時停止します。エコーが受信された後、再度現在の時間が記録されます。

.. code-block:: python

        while ECHO.value():
            pass
        time2 = time.ticks_us()

* 最後に、2つの記録の時間差に音速（340m/s）を掛けて、超音波モジュールと障害物の間の距離（すなわち、モジュールから障害物までの超音波の往復）を2倍にします。単位をセンチメートルに変換すると、必要な戻り値が得られます。

.. code-block:: python

        during = time.ticks_diff(time2, time1)
        return during * 340 / 2 / 10000

注意：超音波センサーが動作している間、プログラムは一時停止するため、複雑なプロジェクトを作成する際には遅延が発生する可能性があります。

