.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好者コミュニティへようこそ！仲間の愛好者と共に、Raspberry Pi、Arduino、ESP32の世界に深く飛び込みましょう。

    **なぜ参加するのか？**

    - **専門家のサポート**: コミュニティやチームの助けを借りて、購入後の問題や技術的な課題を解決しましょう。
    - **学びと共有**: スキルを向上させるためのヒントやチュートリアルを交換しましょう。
    - **独占プレビュー**: 新製品の発表やプレビューにいち早くアクセスできます。
    - **特別割引**: 最新の製品に対する特別割引をお楽しみください。
    - **フェスティバルプロモーションとギブアウェイ**: ギブアウェイや休日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできましたか？ [|link_sf_facebook|]をクリックして、今すぐ参加しましょう！

Lesson 37: MicroPythonでポテンショメーターを使用してサーボを制御する
=============================================================================
このチュートリアルでは、Raspberry Pi Pico Wとポテンショメーターを使用してサーボモーターを制御する方法を説明します。

* **サーボモーター制御**: SG90サーボをRaspberry Pi Pico Wに接続し、GND、電源（5V）、制御信号をGPIOピン15に接続します。
* **配線セットアップ**: ポテンショメーターを3.3V、GND、信号をGPIOピン26に接続します。
* **PWMの基本**: 50HzのPWMを使用してサーボの位置を制御します。
* **コードの説明**: GPIOピン15でPWMを設定し、ポテンショメーターの入力をサーボの角度に変換します。
* **実践的なデモンストレーション**: コードを実行して、ポテンショメーターでサーボを制御し、サーボホーンの手動回転を避けます。
* **応用アイデア**: 大型サーボを制御するために外部電源を使用し、より高度なプロジェクトに応用します。


**ビデオ**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/iiJasGsLTrQ?si=f-avwQIJNypRuh4t" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
