.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

.. _ar_motor:

3.5 - 小型ファン
=======================

今回はTA6586を用いて、DCモーターを時計回りと反時計回りに回転させます。
DCモーターは比較的大きな電流を必要とするため、安全上の理由で、ここでは電源モジュールを使ってモーターに電力を供給します。

* :ref:`cpn_motor`
* :ref:`cpn_ta6586`
* :ref:`cpn_power_module`

**必要な部品**

このプロジェクトでは、以下のコンポーネントが必要です。

一式を購入することは非常に便利です、リンクはこちらです：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前	
        - このキットに含まれるアイテム
        - 購入リンク
    *   - Kepler Kit	
        - 450+
        - |link_kepler_kit|

以下のリンクから個別にも購入できます。

.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - コンポーネントの説明
        - 数量
        - 購入リンク

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

    * DCモーターは高電流を必要とするため、安全のためにここではLi-poチャージャーモジュールを使用してモーターに電力を供給します。
    * 図に示されているようにLi-poチャージャーモジュールが接続されていることを確認してください。そうでなければ、短絡が起きる可能性があり、バッテリーと回路が損傷する可能性があります。

|wiring_motor|

**コード**

.. note::

   * ファイル ``3.5_small_fan.ino`` は、 ``kepler-kit-main/arduino/3.5_small_fan`` のパスの下で開くことができます。
   * または、このコードを **Arduino IDE** にコピーしてください。

   * **アップロード** ボタンをクリックする前に、ボード（Raspberry Pi Pico）と正確なポートを選択することを忘れないでください。

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/26d75a18-6b91-40f4-80ab-f2cdf58644ac/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

プログラムが実行されると、モーターは規則的なパターンで前後に回転します。

.. note::

    * もしコードを再度アップロードできない場合は、今回はPico Wの **RUN** ピンをGNDにワイヤで接続してリセットし、その後このワイヤを抜いてコードを再実行してください。
    * これは、モーターが大量の電流を使用しているため、Pico Wがコンピュータから切断される可能性があるからです。

    |wiring_run_reset|
