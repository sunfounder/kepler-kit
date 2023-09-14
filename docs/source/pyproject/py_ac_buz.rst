.. _py_ac_buz:

3.1 ビープ音
==================

アクティブブザーは、LEDを点灯させるのと同じくらい使いやすい典型的なデジタル出力デバイスです！

* :ref:`cpn_buzzer`

**必要なコンポーネント**

このプロジェクトで必要なコンポーネントは以下の通りです。

全てのキットをまとめて購入するのが便利です。リンクはこちら：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前
        - キット内容
        - リンク
    *   - Keplerキット
        - 450+点
        - |link_kepler_kit|

以下のリンクから個別にも購入できます。

.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - コンポーネント
        - 個数
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
        - :ref:`cpn_transistor`
        - 1(S8050)
        - |link_transistor_buy|
    *   - 6
        - :ref:`cpn_resistor`
        - 1(1KΩ)
        - |link_resistor_buy|
    *   - 7
        - アクティブ :ref:`cpn_buzzer`
        - 1
        - 

**回路図**

|sch_buzzer|

GP15の出力が高い場合、1Kの電流制限抵抗を経て（トランジスタを保護するため）、S8050（NPNトランジスタ）が導通し、ブザーが鳴ります。

S8050（NPNトランジスタ）の役割は、電流を増幅してブザーの音を大きくすることです。実際には、GP15に直接ブザーを接続しても、ブザーの音は小さいことに気付くでしょう。

**配線**

キットには2種類のブザーが含まれています。
アクティブブザーを使用する必要があります。裏返して、封じられた裏側（露出したPCBではない方）が必要なものです。

|img_buzzer|

ブザーは動作時にトランジスタが必要で、ここではS8050（NPNトランジスタ）を使用しています。

|wiring_beep|

**コード**

.. note::

    * ``kepler-kit-main/micropython`` のパスの下で ``3.1_beep.py`` ファイルを開くか、このコードをThonnyにコピーして、"Run Current Script"をクリックするか、F5キーを押すだけで実行できます。

    * 右下の"MicroPython (Raspberry Pi Pico)"インタプリタをクリックするのを忘れないでください。

    * 詳しいチュートリアルは、 :ref:`open_run_code_py` を参照してください。

.. code-block:: python

    import machine
    import utime

    buzzer = machine.Pin(15, machine.Pin.OUT)
    while True:
        for i in range(4):
            buzzer.value(1)
            utime.sleep(0.3)
            buzzer.value(0)
            utime.sleep(0.3)
        utime.sleep(1)

コードを実行すると、毎秒ビープ音が聞こえます。

