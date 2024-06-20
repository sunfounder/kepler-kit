.. note::

    こんにちは、SunFounder Raspberry Pi & Arduino & ESP32 愛好者コミュニティへようこそ！Raspberry Pi、Arduino、ESP32 の世界をさらに深く探求しましょう。

    **参加する理由**

    - **専門サポート**: コミュニティとチームの助けを借りて、購入後の問題や技術的な課題を解決できます。
    - **学びと共有**: スキル向上のためのヒントやチュートリアルを交換できます。
    - **限定プレビュー**: 新製品の発表やプレビューに早期アクセスできます。
    - **特別割引**: 最新の製品に対して、限定の割引を享受できます。
    - **フェスティブプロモーションとギブアウェイ**: ギブアウェイやホリデープロモーションに参加できます。

    👉 一緒に探求し、創造する準備はできましたか？今すぐ[|link_sf_facebook|]をクリックして参加しましょう！

lesson 64 : MicroPythonを使用したオブジェクト指向プログラミングの例 - LEDの制御
===================================================================================

このチュートリアルでは、Raspberry Pi Pico Wを使用したオブジェクト指向プログラミング（OOP）を紹介し、LEDの制御に焦点を当てます。

* **配線設定**: 赤色LEDをGPIOピン15に、緑色LEDをGPIOピン14に接続し、それぞれに330オームの抵抗を接地します。
* **クラスとメソッド**:
  1. LEDオブジェクトを管理する`LED`クラスを定義します。
  2. `__init__`メソッドでピンを設定し、LEDを初期化します。
  3. LEDの点滅を制御する`blink`メソッドを実装します。
* **コード実装**:
  1. 必要なライブラリ（`machine`と`time`）をインポートします。
  2. `LED`クラスを`__init__`および`blink`メソッドで作成します。
  3. 赤色と緑色のLEDオブジェクトをインスタンス化します。
  4. 指定されたパラメータに従ってLEDを点滅させるループを使用します。
* **宿題**: サーボモーターを簡単に制御できるクラスを作成します。このクラスには、サーボの初期化と角度を設定するメソッドを含めます。MicroPythonでサーボモーターを操作する詳細は、レッスン36を参照してください。

**ビデオ**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/3wyCL9QK_uY?si=G0GXEHqdo2jQ_F-5" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

