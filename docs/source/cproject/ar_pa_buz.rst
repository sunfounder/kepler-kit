.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

.. _ar_pa_buz:

3.2 - カスタムトーン
==========================================

前回のプロジェクトではアクティブブザーを使用しましたが、今回はパッシブブザーを使用します。

アクティブブザーと同様に、パッシブブザーも電磁誘導の現象を利用して動作します。違いは、パッシブブザーには振動源がないため、直流信号を使用しても音を出さない点です。
しかし、この特性により、パッシブブザー自体の振動周波数を調整し、"ド、レ、ミ、ファ、ソ、ラ、シ"などの異なる音階を出すことができます。

さあ、パッシブブザーにメロディーを鳴らしてみましょう！

* :ref:`cpn_buzzer`

**必要なコンポーネント**

このプロジェクトで必要なコンポーネントは以下の通りです。

一式をまとめて購入するのが便利です、そのためのリンクはこちら：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前	
        - このキットに含まれるアイテム
        - 購入リンク
    *   - ケプラーキット	
        - 450+
        - |link_kepler_kit|

下記のリンクから個別にも購入できます。

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

GP15の出力が高いと、1Kの電流制限抵抗を通過した後で、S8050（NPNトランジスター）が導通し、ブザーが鳴ります。

S8050（NPNトランジスター）の役割は、電流を増幅してブザーの音を大きくすることです。実際には、GP15に直接ブザーを接続することもできますが、ブザーの音が小さいことに気付くでしょう。

**配線**

|img_buzzer|

このキットには2つのブザーが含まれていますが、ここではパッシブブザー（背面に露出したPCBがあるもの）を使用します。

ブザーは動作するためにトランジスタが必要です、ここではS8050を使用します。

|wiring_buzzer|

**コード**

.. note::

   * ファイル ``3.2_custom_tone.ino`` は、 ``kepler-kit-main/arduino/3.2_custom_tone`` のパスで開くことができます。
   * または、このコードを **Arduino IDE** にコピーしてください。

   * **アップロード** ボタンをクリックする前に、ボード（Raspberry Pi Pico）と正しいポートを選択してください。

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/69c55e56-9eeb-46bb-b3a8-b354c500cc17/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>


**動作の仕組み**

パッシブブザーにデジタル信号を与えると、振動板を押し出すだけで音を出すことはありません。

そのため、 ``tone()`` 関数を使用してPWM信号を生成し、パッシブブザーに音を出させます。

この関数には3つのパラメーターがあります：

  * **pin** ：ブザーを制御するGPIOピン。
  * **frequency** ：ブザーの音程は周波数で決まります。周波数が高いほど音程も高くなります。
  * **Duration** ：音の持続時間。

* `tone <https://www.arduino.cc/reference/en/language/functions/advanced-io/tone/>`_

**さらに学ぶ**

ピアノの基本周波数に応じて特定の音を模倣し、完全な曲を演奏することができます。

* `Piano key frequencies - Wikipedia <https://en.wikipedia.org/wiki/Piano_key_frequencies>`_

.. note::

   * ファイル ``3.2_custom_tone_2.ino`` は、 ``kepler-kit-main/arduino/3.2_custom_tone_2`` のパスで開くことができます。
   * または、このコードを **Arduino IDE** にコピーしてください。

   * **アップロード** ボタンをクリックする前に、ボード（Raspberry Pi Pico）と正しいポートを選択してください。

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/f934c785-7204-4972-aae5-01edde3c79cc/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>
