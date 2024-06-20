.. note::

    こんにちは、SunFounder Raspberry Pi & Arduino & ESP32 愛好者コミュニティへようこそ！Raspberry Pi、Arduino、ESP32 の世界をさらに深く探求しましょう。

    **参加する理由**

    - **専門サポート**: コミュニティとチームの助けを借りて、購入後の問題や技術的な課題を解決できます。
    - **学びと共有**: スキル向上のためのヒントやチュートリアルを交換できます。
    - **限定プレビュー**: 新製品の発表やプレビューに早期アクセスできます。
    - **特別割引**: 最新の製品に対して、限定の割引を享受できます。
    - **フェスティブプロモーションとギブアウェイ**: ギブアウェイやホリデープロモーションに参加できます。

    👉 一緒に探求し、創造する準備はできましたか？今すぐ[|link_sf_facebook|]をクリックして参加しましょう！

lesson 69 : MicroPythonスレッドをクリーンに終了させる方法
===================================================================================

このチュートリアルでは、Raspberry Pi Pico Wの両方のコアを使用してサーボとLEDを制御する方法を紹介します。

* **配線設定**:
 - 赤色のLEDをGPIOピン15に接続し、330オームの抵抗を介してグランドに接続します。
 - 緑色のLEDをGPIOピン14に接続し、330オームの抵抗を介してグランドに接続します。
 - サーボの制御線をGPIOピン17に、電源線を物理ピン40に、グランド線を物理ピン38に接続します。
* **コード実装**:
 - 必要なライブラリ（`machine`、`time`、`_thread`、`Servo`）をインポートします。
 - LEDとサーボのピンを設定します。
 - グローバル変数を使用してサーボの方向に基づいてLEDを点滅させる関数`other_core`を定義します。
 - サーボを動かし、LEDの方向を設定するループを作成します。
* **宿題**:
 - コードを拡張して、サーボが時計回りに動くときに赤色のLEDを点滅させ、反時計回りに動くときに緑色のLEDを点滅させるようにします。


**ビデオ**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/mcXxqx0lZYo?si=tIek_zJ4EMuZ3bC4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

