.. note::

    こんにちは、SunFounder Raspberry Pi & Arduino & ESP32 愛好者コミュニティへようこそ！Raspberry Pi、Arduino、ESP32 の世界をさらに深く探求しましょう。

    **参加する理由**

    - **専門サポート**: コミュニティとチームの助けを借りて、購入後の問題や技術的な課題を解決できます。
    - **学びと共有**: スキル向上のためのヒントやチュートリアルを交換できます。
    - **限定プレビュー**: 新製品の発表やプレビューに早期アクセスできます。
    - **特別割引**: 最新の製品に対して、限定の割引を享受できます。
    - **フェスティブプロモーションとギブアウェイ**: ギブアウェイやホリデープロモーションに参加できます。

    👉 一緒に探求し、創造する準備はできましたか？今すぐ[|link_sf_facebook|]をクリックして参加しましょう！

lesson 60 : MicroPythonでジョイスティックを使ってNeoPixelの色を制御する
=============================================================================

このチュートリアルでは、Raspberry Pi Pico Wを使用してジョイスティックでLEDストリップを制御する方法を説明します。

* **配線設定**:
    - ジョイスティックのグラウンドをピン38、3.3Vをピン36、VRXをGPIOピン27、VRYをGPIOピン26に接続します。
    - NeoPixelのグラウンドをピン38、5Vをピン40、データをGPIOピン0に接続します。
* **コードの実装**:
    - 必要なライブラリ（`machine`、`time`、`math`、`neopixel`）をインポートします。
    - ジョイスティックとNeoPixelのADCを設定します。
    - ジョイスティックの値を読み取り、角度を計算します。
    - 角度をNeoPixelのRGB値に変換します。
* **宿題**:
    - ジョイスティックの角度と中心からの距離に基づいてNeoPixelの色と明るさを制御するプログラムを書いてみてください。


**ビデオ**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/8UCJHY7uTH4?si=BKJ8lYNz1kF4w9wm" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

