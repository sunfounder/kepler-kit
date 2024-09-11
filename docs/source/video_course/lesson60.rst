.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好者コミュニティへようこそ！仲間の愛好者と共に、Raspberry Pi、Arduino、ESP32の世界に深く飛び込みましょう。

    **なぜ参加するのか？**

    - **専門家のサポート**: コミュニティやチームの助けを借りて、購入後の問題や技術的な課題を解決しましょう。
    - **学びと共有**: スキルを向上させるためのヒントやチュートリアルを交換しましょう。
    - **独占プレビュー**: 新製品の発表やプレビューにいち早くアクセスできます。
    - **特別割引**: 最新の製品に対する特別割引をお楽しみください。
    - **フェスティバルプロモーションとギブアウェイ**: ギブアウェイや休日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできましたか？ [|link_sf_facebook|]をクリックして、今すぐ参加しましょう！

Lesson 60: MicroPythonでジョイスティックを使用してNeoPixelの色を制御する
=============================================================================

このチュートリアルでは、Raspberry Pi Pico Wを使用してジョイスティックでLEDストリップを制御する方法を説明します。

* **配線セットアップ**:

    - ジョイスティックのグランドをピン38、3.3Vをピン36、VRXをGPIOピン27、VRYをGPIOピン26に接続します。
    - Neopixelのグランドをピン38、5Vをピン40、データピンをGPIOピン0に接続します。
    
* **コードの実装**:

    - ライブラリ（``machine``, ``time``, ``math``, ``neopixel``）をインポートします。
    - ジョイスティック用のADCとNeopixelを設定します。ジョイスティックの値を読み取り、角度を計算します。
    - 角度をRGBに変換し、Neopixelに適用します。

* **宿題**: ジョイスティックの角度と中心からの距離に基づいて、NeoPixelの色と明るさを制御するプログラムを作成します。


**ビデオ**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/8UCJHY7uTH4?si=BKJ8lYNz1kF4w9wm" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
