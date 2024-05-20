.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

.. _py_led_bar:

2.2 レベルを表示
=============================

最初のプロジェクトはLEDを点滅させるだけのシンプルなものです。このプロジェクトでは、一般的に電力やボリュームレベルを表示するために使用される、プラスチックケースに10個のLEDを含むLEDバーグラフを使用します。

|img_led_bar_pin|

* :ref:`cpn_led_bar`

**必要なコンポーネント**

このプロジェクトでは、以下のコンポーネントが必要です。

全体のキットを購入する方が便利です、リンクは以下の通りです：

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
        - 複数
        - |link_wires_buy|
    *   - 5
        - :ref:`cpn_resistor`
        - 10(220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_led_bar`
        - 1
        - 

**回路図**

|sch_ledbar|

LEDバーグラフには10個のLEDがあり、それぞれが個別に制御できます。各LEDのアノードはGP6〜GP15に接続され、カソードは220オームの抵抗を介してGNDに接続されています。


**配線**

|wiring_ledbar|

**コード**

.. note::

    * ``kepler-kit-main/micropython`` のパス内の ``2.2_display_the_level.py`` ファイルを開くか、このコードをThonnyにコピーしてから「Run Current Script」をクリック、または単にF5キーを押して実行してください。

    * 右下隅にある「MicroPython（Raspberry Pi Pico）」インタープリタをクリックするのを忘れないでください。

    * 詳細なチュートリアルは :ref:`open_run_code_py` を参照してください。

.. code-block:: python

    import machine
    import utime

    pin = [6,7,8,9,10,11,12,13,14,15]
    led= []
    for i in range(10):
        led.append(None)
        led[i] = machine.Pin(pin[i], machine.Pin.OUT)

    while True:
        for i in range(10):
            led[i].toggle()
            utime.sleep(0.2)

プログラムが実行されていると、LEDバーグラフ上のLEDが順番に点灯し、その後消えます。

**動作の仕組みは？**

LEDバーは、10本のピンによって制御される10個のLEDで構成されています。つまり、これらのピンを定義する必要があります。
一つひとつ定義するのは煩雑な作業なので、ここでは ``Lists（リスト）`` を使用しています。

.. note::
    Pythonのリストは、一度に複数の要素を扱うことができる非常に多機能なデータ型であり、カンマで区切られた要素を角括弧[]内に配置することで作成されます。

.. code-block:: python

    pin = [6,7,8,9,10,11,12,13,14,15]    

このコード行によって ``pin`` というリストが定義され、10個の要素 ``6,7,8,9,10,11,12,13,14,15`` が含まれます。
インデックス演算子 [] を使用して、リスト内の項目にアクセスすることができます。Pythonでは、インデックスは0から始まります。したがって、10個の要素を持つリストは、0から9までのインデックスを持ちます。
このリストを例にすると、 ``pin[0]`` は ``6`` であり、 ``pin[4]`` は ``10`` です。

次に、10個のLEDオブジェクトを定義するために使用される空のリスト ``led`` を宣言します。

.. code-block:: python

    led = []    

リストの長さが0であるため、配列に対する直接的な操作、たとえばled[0]を出力するなど、は機能しません。新しい項目を追加する必要があります。

.. code-block:: python

    led.append(None)

この ``append()`` メソッドの結果として、リスト ``led`` には最初の項目が追加され、長さが1になり、 ``led[0]`` が ``None`` （nullを意味する）という現在の値にもかかわらず有効な要素になります。

次のステップは、ピン6に接続されている ``led[0]`` を、最初のLEDオブジェクトとして定義することです。

.. code-block:: python

    led[0] = machine.Pin(6, machine.Pin.OUT)

最初のLEDオブジェクトが定義されました。

以上から、10個のピン番号をリスト **pin** として作成しました。これにより、まとめて操作を行いやすくなります。

.. code-block:: python

    led[0] = machine.Pin(pin[0], machine.Pin.OUT)

``for`` 文を使用して、10本のピンすべてが上記の文を実行するようにします。

.. code-block:: python

    import machine

    pin = [6,7,8,9,10,11,12,13,14,15]
    led= []
    for i in range(10):
        led.append(None)
        led[i] = machine.Pin(pin[i], machine.Pin.OUT)

* :ref:`syntax_list`
* :ref:`syntax_forloop`

もう一つの ``for`` ループを使用して、LEDバーの10個のLEDが順番に状態を切り替えるようにします。

.. code-block:: python

    for i in range(10):
        led[i].toggle()
        utime.sleep(0.2)

このコード片をwhileループ内に配置することで、コードの完成です。

.. code-block:: python

    import machine
    import utime

    pin = [6,7,8,9,10,11,12,13,14,15]
    led= []
    for i in range(10):
        led.append(None)
        led[i] = machine.Pin(pin[i], machine.Pin.OUT)

    while True:
        for i in range(10):
            led[i].toggle()
            utime.sleep(0.2)

