.. note::

    こんにちは、SunFounder Raspberry Pi & Arduino & ESP32 愛好者コミュニティへようこそ！Raspberry Pi、Arduino、ESP32 の世界をさらに深く探求しましょう。

    **参加する理由**

    - **専門サポート**: コミュニティとチームの助けを借りて、購入後の問題や技術的な課題を解決できます。
    - **学びと共有**: スキル向上のためのヒントやチュートリアルを交換できます。
    - **限定プレビュー**: 新製品の発表やプレビューに早期アクセスできます。
    - **特別割引**: 最新の製品に対して、限定の割引を享受できます。
    - **フェスティブプロモーションとギブアウェイ**: ギブアウェイやホリデープロモーションに参加できます。

    👉 一緒に探求し、創造する準備はできましたか？今すぐ[|link_sf_facebook|]をクリックして参加しましょう！

lesson 53 : MicroPythonでのNeopixelストリップのアニメーション
=============================================================================

このチュートリアルでは、Raspberry Pi Pico Wを使用してNeoPixelアレイをMicroPythonで制御する方法について説明します。

* **イントロダクション**:
   - 8個のLEDを持つNeoPixelアレイの概要。
   - 簡単な配線: 5V、GND、データピンをGPIOピン0に接続。
* **プログラミングの基本**:
   - 必要なライブラリのインポート: `neopixel` と `machine`。
   - NeoPixelオブジェクトの設定、色の定義、個々のピクセルを制御するデモンストレーション。
* **NeoPixelアレイのアニメーション**:
   - カラーバックグラウンド上でのランニングピクセルアニメーションを作成するコード。
   - スムーズなアニメーションのための前進および後退ループの説明。
* **高度なアニメーション**:
   - 宿題: HSVカラーホイールを使用してスムーズなレインボーカラーの遷移を作成する。
   - 様々なアニメーションやパターンの実験を奨励。

**ビデオ**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/7IvAQJfU908?si=czJleyd0ri405vkg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

