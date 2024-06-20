.. note::

    こんにちは、SunFounder Raspberry Pi & Arduino & ESP32 愛好者コミュニティへようこそ！Raspberry Pi、Arduino、ESP32 の世界をさらに深く探求しましょう。

    **参加する理由**

    - **専門サポート**: コミュニティとチームの助けを借りて、購入後の問題や技術的な課題を解決できます。
    - **学びと共有**: スキル向上のためのヒントやチュートリアルを交換できます。
    - **限定プレビュー**: 新製品の発表やプレビューに早期アクセスできます。
    - **特別割引**: 最新の製品に対して、限定の割引を享受できます。
    - **フェスティブプロモーションとギブアウェイ**: ギブアウェイやホリデープロモーションに参加できます。

    👉 一緒に探求し、創造する準備はできましたか？今すぐ[|link_sf_facebook|]をクリックして参加しましょう！

lesson 58 : MicroPythonでジョイスティックの角度を測定する
=============================================================================

このチュートリアルでは、Raspberry Pi Pico Wでジョイスティックをキャリブレーションする方法について説明します。

* **配線設定**: グラウンドをピン38に、3.3Vをピン36に、VRXをGPIOピン27に、VRYをGPIOピン26に接続します。
* **コードの実装**: 必要なライブラリをインポートします。ジョイスティック軸のADCを設定し、キャリブレーション用の値を読み取ります。
* **キャリブレーション**: 生のADC値を-100から+100のスケールに変換します。三角法を使用してジョイスティックの角度を計算します。
* **宿題**: ジョイスティックの角度に基づいてサーボモーターを制御するプログラムを書き、0から180度までの正確な追跡を確保します。

**ビデオ**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/KpDIv0i41Tw?si=PUEInyKbRTIUcvCa" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

