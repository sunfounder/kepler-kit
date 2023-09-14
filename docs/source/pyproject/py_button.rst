.. _py_button:

2.5 ボタンの値を読み取る
==============================================

これらのピンは、その名前が示すようにGPIO（汎用入出力）として、入力と出力の両方の機能を持っています。以前は出力機能を使用しましたが、この章では入力機能を使用してボタンの値を入力します。

* :ref:`cpn_button`

**必要なコンポーネント**

このプロジェクトでは、以下のコンポーネントが必要です。

まとめてキットを購入する方が便利です、リンクはこちら：

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
        - Micro USBケーブル
        - 1
        - 
    *   - 3
        - :ref:`cpn_breadboard`
        - 1
        - |link_breadboard_buy|
    *   - 4
        - :ref:`cpn_wire`
        - いくつか
        - |link_wires_buy|
    *   - 5
        - :ref:`cpn_resistor`
        - 1(10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_button`
        - 1
        - |link_button_buy|

**回路図**

|sch_button|

ボタンの片側ピンが3.3vに、もう一方のピンがGP14に接続されていれば、ボタンが押された状態でGP14がハイレベルになります。しかし、ボタンが押されていない場合、GP14は未定義状態となり、ハイかローかが不明です。ボタンが押されていない時に安定したローレベルを得るためには、10Kのプルダウン抵抗を介してGP14をGNDに再接続する必要があります。

**配線**

|wiring_button|

.. note::
    4ピンのボタンはH型になっています。左の2ピンか右の2ピンが接続されており、中央のギャップを越えると、同じ行番号の2つの半行が接続されます。（例えば、私の回路では、E23とF23が接続されていますし、E25とF25も接続されています）。

    ボタンが押されるまで、左右のピンは互いに独立しており、一方から他方への電流の流れはありません。

**コード**

.. note::

    * ``kepler-kit-main/micropython`` パス下の ``2.5_read_button_value.py`` ファイルを開くか、このコードをThonnyにコピーしてから、「Run Current Script」をクリックするか、F5キーを押して実行してください。

    * 右下隅の「MicroPython（Raspberry Pi Pico）」インタープリタを選択することを忘れずに。

    * 詳細なチュートリアルについては、 :ref:`open_run_code_py` を参照してください。

.. code-block:: python

    import machine
    import utime
    button = machine.Pin(14, machine.Pin.IN)
    while True:
        if button.value() == 1:
            print("You pressed the button!")
            utime.sleep(1)

コードが実行されると、シェルに「You pressed the button!」と表示されます。

**プルアップ動作モード**

次は、プルアップモードでボタンを使用する場合の配線とコードです。

|sch_button_pullup|

|wiring_button_pullup|

プルダウンモードとの唯一の違いは、10Kの抵抗が3.3Vに接続され、ボタンはGNDに接続されているため、ボタンが押されるとGP14がローレベルになることです。これはプルダウンモードで得られる値とは逆です。
したがって、このコードを ``if button.value() == 0:`` に変更するだけです。

参考資料もご覧ください：

* `machine.Pin <https://docs.micropython.org/en/latest/library/machine.Pin.html>`_
