.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

.. _py_mpr121:

4.3 電極キーボード
================================

プロジェクトに多数のタッチスイッチを追加したい場合、MPR121は良い選択です。このモジュールには導体で拡張できる電極があります。
例えば、電極をバナナに接続すると、そのバナナをタッチスイッチに変えることができます。

* :ref:`cpn_mpr121`

**必要な部品**

このプロジェクトには、以下の部品が必要です。

全てを一つのキットで購入するのも便利です、リンクはこちら：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前
        - このキットに含まれるアイテム
        - リンク
    *   - ケプラーキット
        - 450以上
        - |link_kepler_kit|

もちろん、以下のリンクから個々の部品を購入することもできます。

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
        - :ref:`cpn_mpr121`
        - 1
        - 

**回路図**

|sch_mpr121|

**配線**

|wiring_mpr121|

**コード**

.. note::

    * ``kepler-kit-main/micropython`` パス下の ``4.3_electrode_keyboard.py`` ファイルを開くか、このコードをThonnyにコピーして、「Run Current Script」をクリックするか、単にF5キーを押して実行してください。

    * 画面の右下隅にある "MicroPython (Raspberry Pi Pico)" インタープリタをクリックするのを忘れないでください。

    * 詳細なチュートリアルは、 :ref:`open_run_code_py` を参照してください。

    * このプロジェクトでは ``mpr121.py`` というライブラリが必要です。Pico Wにアップロードされているか確認してください。詳細なチュートリアルは :ref:`add_libraries_py` を参照してください。

.. code-block:: python

    from mpr121 import MPR121
    from machine import Pin, I2C
    import time

    i2c = I2C(1, sda=Pin(6), scl=Pin(7))
    mpr = MPR121(i2c)

    # すべてのキーを確認
    while True:
        value = mpr.get_all_states()
        if len(value) != 0:
            print(value)
        time.sleep_ms(100)

プログラムが動作すると、MPR121の12個の電極に手を触れると、触れた電極が表示されます。

電極を他の導体、例えばフルーツやワイヤー、箔などに拡張して接続することで、これらの電極をトリガーするさまざまな方法が増えます。

**仕組みは？**

mpr121ライブラリには、 ``MPR121`` クラスに機能が統合されています。

.. code-block:: python

    from mpr121 import MPR121

MPR121はI2Cモジュールであり、 ``MPR121`` オブジェクトを初期化するためにI2Cピンのセットを定義する必要があります。この時点で、モジュールの電極の状態が初期値として記録されます。電極が拡張されている場合、初期値をリセットするために例を再実行する必要があります。

.. code-block:: python

    from machine import Pin, I2C
    i2c = I2C(1, sda=Pin(6), scl=Pin(7))
    mpr = MPR121(i2c)

* `Inter-Integrated Circuit - Wikipedia <https://ja.wikipedia.org/wiki/I2C>`_

その後、 ``mpr.get_all_states()`` を使用して電極がトリガーされたかどうかを読み取ります。もし電極2と3がトリガーされた場合、値 ``[2, 3]`` が生成されます。

.. code-block::

    while True:
        value = mpr.get_all_states()
        if len(value) != 0:
            print(value)
        time.sleep_ms(100)

特定の電極を検出するために ``mpr.is_touched(electrode)`` も使用できます。トリガーされた場合、 ``True`` を返し、そうでない場合は ``False`` を返します。

.. code-block:: python

    while True:
        value = mpr.is_touched(0)
        print(value)
        time.sleep_ms(100)
