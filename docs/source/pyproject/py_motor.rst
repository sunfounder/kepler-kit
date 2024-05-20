.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

.. _py_motor:

3.5 スモールファン
=======================

今回は、TA6586を用いてDCモーターを時計回りと反時計回りに回転させます。
DCモーターは比較的大きな電流を必要とするため、安全上の理由からここでは電源モジュールを用いてモーターに電力を供給します。

* :ref:`cpn_motor`
* :ref:`cpn_ta6586`
* :ref:`cpn_power_module`

**必要な部品**

このプロジェクトでは、以下の部品が必要です。

全ての部品が含まれるキットを購入するのは確かに便利です、リンクはこちら：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前
        - このキットに含まれるアイテム
        - リンク
    *   - ケプラーキット
        - 450以上
        - |link_kepler_kit|

以下のリンクから部品を個別に購入することもできます。

.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - 項番
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
        - :ref:`cpn_ta6586`
        - 1
        - 
    *   - 6
        - :ref:`cpn_motor`
        - 1
        - |link_motor_buy|
    *   - 7
        - :ref:`cpn_lipo_charger`
        - 1
        -  
    *   - 8
        - 18650バッテリー
        - 1
        -  
    *   - 9
        - バッテリーホルダー
        - 1
        -  

**回路図**

|sch_motor|



**配線**

.. note::

    * DCモーターは高電流が必要なため、安全のためここではLi-poチャージャーモジュールを用いてモーターに電力を供給します。
    * ダイアグラムに示されているようにLi-poチャージャーモジュールが接続されていることを確認してください。そうしないと、バッテリーと回路が短絡し、ダメージを受ける可能性があります。

|wiring_motor|


**コード**

.. note::

    * ``kepler-kit-main/micropython`` パス下の ``3.5_small_fan.py`` ファイルを開くか、このコードをThonnyにコピーして、「Run Current Script」をクリックするか、単にF5キーを押して実行してください。

    * 画面の右下隅にある "MicroPython (Raspberry Pi Pico)" インタープリタをクリックするのを忘れないでください。

    * 詳細なチュートリアルは、 :ref:`open_run_code_py` を参照してください。

.. code-block:: python

    import machine
    import utime

    motor1A = machine.Pin(14, machine.Pin.OUT)
    motor2A = machine.Pin(15, machine.Pin.OUT)

    def clockwise():
        motor1A.high()
        motor2A.low()

    def anticlockwise():
        motor1A.low()
        motor2A.high()

    def stopMotor():
        motor1A.low()
        motor2A.low()

    while True:
        clockwise()
        utime.sleep(1)
        stopMotor()
        utime.sleep(1)
        anticlockwise()
        utime.sleep(1)
        stopMotor()
        utime.sleep(1)

プログラムが動作すると、モーターは一定のパターンで前後に回転します。

.. note::

    * ストップボタンをクリックした後もモーターが回転し続ける場合は、この時点でGNDにワイヤーでPico Wの **RUN** ピンをリセットする必要があります。その後、このワイヤーを抜いて再度コードを実行してください。
    * これはモーターが大量の電流を使用しているため、Pico Wがコンピュータから切断される可能性があるためです。

    |wiring_run_reset|
