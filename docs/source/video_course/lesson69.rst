.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好者コミュニティへようこそ！仲間の愛好者と共に、Raspberry Pi、Arduino、ESP32の世界に深く飛び込みましょう。

    **なぜ参加するのか？**

    - **専門家のサポート**: コミュニティやチームの助けを借りて、購入後の問題や技術的な課題を解決しましょう。
    - **学びと共有**: スキルを向上させるためのヒントやチュートリアルを交換しましょう。
    - **独占プレビュー**: 新製品の発表やプレビューにいち早くアクセスできます。
    - **特別割引**: 最新の製品に対する特別割引をお楽しみください。
    - **フェスティバルプロモーションとギブアウェイ**: ギブアウェイや休日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできましたか？ [|link_sf_facebook|]をクリックして、今すぐ参加しましょう！

Lesson 69: MicroPythonスレッドをプログラム終了時にクリーンに終了する方法
===================================================================================

このチュートリアルでは、Raspberry Pi Pico Wの両方のコアを使用してサーボとLEDを制御する方法を説明します。

* **配線セットアップ**: 赤LEDをGPIOピン15、緑LEDをGPIOピン14、サーボをGPIOピン17に接続し、電源をピン40、グランドをピン38に接続します。
* **コードの実装**: ``machine``, ``time``, ``_thread``, ``Servo`` をインポートします。LEDとサーボ用のピンを設定し、サーボの動きに基づいてLEDを点滅させる ``other_core`` 関数を定義します。サーボとLEDを制御するためのループを作成します。
* **宿題**: サーボの時計回りの動作には赤LED、反時計回りの動作には緑LEDが点滅するようにコードを修正します。


**ビデオ**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/mcXxqx0lZYo?si=tIek_zJ4EMuZ3bC4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
