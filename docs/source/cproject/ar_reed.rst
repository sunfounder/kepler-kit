.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

.. _ar_reed:

2.9 - 磁気を感じる
===============================

最も一般的なタイプのリードスイッチには、スイッチが開いているときに小さなギャップで隔てられた、磁気化可能な柔軟な金属製のリードのペアが含まれています。

電磁石または永久磁石からの磁場がリードを引きつけることで、電気回路が完成します。
磁場が消えると、リードのばね力によってそれらが離れ、回路が開きます。

リードスイッチの一般的な用途の一例は、セキュリティアラームのためのドアや窓の開閉を検出することです。

* :ref:`cpn_reed`

**必要なコンポーネント**

このプロジェクトで必要なコンポーネントは以下の通りです。

全体のキットを購入すると非常に便利です。リンクはこちら：

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

    *   - 番号
        - コンポーネント紹介	
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
        - :ref:`cpn_resistor`
        - 1（10KΩ）
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_reed`
        - 1
        - 

**回路図**

|sch_reed|

デフォルトでは、GP14は低く、磁石がリードスイッチに近づくと高くなります。

10KΩの抵抗器の目的は、磁石が近くにないときにGP14を安定した低レベルに保つことです。

**配線**

|wiring_reed|

**コード**

.. note::

   * ファイル ``2.9_feel_the_magnetism.ino`` は、パス ``kepler-kit-main/arduino/2.9_feel_the_magnetism`` で開くことができます。
   * または、このコードを **Arduino IDE** にコピーしてください。

   * **Upload** ボタンをクリックする前に、ボード（Raspberry Pi Pico）と正確なポートを選択することを忘れないでください。

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/62bba18c-7921-4df9-806f-deffce17de9a/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

磁石が近づくと、回路が閉じます。 :ref:`ar_button` 章のボタンと同じように動作します。

