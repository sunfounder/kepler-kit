.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好者コミュニティへようこそ！仲間の愛好者と共に、Raspberry Pi、Arduino、ESP32の世界に深く飛び込みましょう。

    **なぜ参加するのか？**

    - **専門家のサポート**: コミュニティやチームの助けを借りて、購入後の問題や技術的な課題を解決しましょう。
    - **学びと共有**: スキルを向上させるためのヒントやチュートリアルを交換しましょう。
    - **独占プレビュー**: 新製品の発表やプレビューにいち早くアクセスできます。
    - **特別割引**: 最新の製品に対する特別割引をお楽しみください。
    - **フェスティバルプロモーションとギブアウェイ**: ギブアウェイや休日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできましたか？ [|link_sf_facebook|]をクリックして、今すぐ参加しましょう！

Lesson 64: MicroPythonでLEDを使ったオブジェクト指向プログラミングの例
===================================================================================

このチュートリアルでは、Raspberry Pi Pico Wを使用して、オブジェクト指向プログラミング（OOP）を学び、LEDを制御する方法を説明します。

* **配線セットアップ**: 赤色LEDをGPIOピン15、緑色LEDをGPIOピン14に接続し、330オームの抵抗をグランドに接続します。
* **クラスとメソッド**: 

   1. ``LED`` クラスを定義します。
   2. ``__init__`` メソッドでピンを設定します。
   3. LEDを制御する ``blink`` メソッドを実装します。

* **コードの実装**: 

   1. ``machine`` と ``time`` をインポートします。
   2. ``__init__`` と ``blink`` を持つ ``LED`` クラスを作成します。
   3. 赤と緑のLEDをインスタンス化します。

  

**ビデオ**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/3wyCL9QK_uY?si=G0GXEHqdo2jQ_F-5" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
