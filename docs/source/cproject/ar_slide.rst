.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

.. _ar_slide:

2.7 - 左右トグルスイッチ
====================================

|img_slide|

スライドスイッチは3ピンのデバイスで、ピン2（中央）が共通ピンです。スイッチを左にトグルすると、左側の2ピンが接続され、右にトグルすると、右側の2ピンが接続されます。

**必要なコンポーネント**

このプロジェクトには、以下のコンポーネントが必要です。

全体のキットを購入するのが便利です。リンクはこちら：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前	
        - このキットに含まれるアイテム
        - 購入リンク
    *   - ケプラーキット	
        - 450+
        - |link_kepler_kit|

以下のリンクから個別に購入することもできます。

.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - コンポーネント紹介	
        - 数量
        - 購入リンク

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
        - :ref:`cpn_resistor`
        - 1（10KΩ）
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_capacitor`
        - 1（104）
        - |link_capacitor_buy|
    *   - 7
        - :ref:`cpn_slide_switch`
        - 1
        - 

**回路図**

|sch_slide|

スライドスイッチを右か左にトグルすると、GP14は異なるレベルになります。

10KΩの抵抗器の目的は、トグル中（極端な左または右にトグルしていない状態で）GP14を低く保つことです。

ここで使用される104セラミックコンデンサは、ジッタを排除するためです。

* :ref:`cpn_slide_switch`
* :ref:`cpn_capacitor`

**配線**

|wiring_slide|

**コード**

.. note::

   * ファイル ``2.7_toggle_left_right.ino`` は、パス ``kepler-kit-main/arduino/2.7_toggle_left_right`` で開くことができます。
   * または、このコードを **Arduino IDE** にコピーしてください。

   * **アップロード** ボタンをクリックする前に、ボード（Raspberry Pi Pico）と正確なポートを選択してください。

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/a20c0733-f234-4d4b-862d-db87f2c249e9/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

プログラムが動作していると、シリアルモニターにはスイッチを左または右にトグルしたときに「ON」または「OFF」と表示されます。
