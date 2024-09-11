.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好者コミュニティへようこそ！仲間の愛好者と共に、Raspberry Pi、Arduino、ESP32の世界に深く飛び込みましょう。

    **なぜ参加するのか？**

    - **専門家のサポート**: コミュニティやチームの助けを借りて、購入後の問題や技術的な課題を解決しましょう。
    - **学びと共有**: スキルを向上させるためのヒントやチュートリアルを交換しましょう。
    - **独占プレビュー**: 新製品の発表やプレビューにいち早くアクセスできます。
    - **特別割引**: 最新の製品に対する特別割引をお楽しみください。
    - **フェスティバルプロモーションとギブアウェイ**: ギブアウェイや休日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできましたか？ [|link_sf_facebook|]をクリックして、今すぐ参加しましょう！

Lesson 70: MicroPythonでデュアルコアプログラムをクリーンに終了する例
===================================================================================

このチュートリアルでは、Raspberry Pi Pico Wでスレッドを使用してサーボとボタンを制御する方法を説明します。

* **配線セットアップ**: サーボ制御をGPIOピン17に接続し、電源をピン40、グランドをピン38に接続します。ボタンをGPIOピン16とグランドに接続します。
* **コードの実装**: ``machine``, ``time``, ``_thread``, ``Servo`` をインポートします。ボタンとサーボのピンを設定し、サーボの位置を制御するトグルスイッチを実装します。サーボの動作をスレッドで制御し、プログラムをクリーンに終了させる方法を実装します。
* **宿題**: サーボの動作中に割り込まれてもプログラムがクリーンに終了するようにコードを修正します。



**ビデオ**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/UHbboCxIOYE?si=eDDi-2mYO0LSWSLJ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
