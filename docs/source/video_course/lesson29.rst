.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好者コミュニティへようこそ！仲間の愛好者と共に、Raspberry Pi、Arduino、ESP32の世界に深く飛び込みましょう。

    **なぜ参加するのか？**

    - **専門家のサポート**: コミュニティやチームの助けを借りて、購入後の問題や技術的な課題を解決しましょう。
    - **学びと共有**: スキルを向上させるためのヒントやチュートリアルを交換しましょう。
    - **独占プレビュー**: 新製品の発表やプレビューにいち早くアクセスできます。
    - **特別割引**: 最新の製品に対する特別割引をお楽しみください。
    - **フェスティバルプロモーションとギブアウェイ**: ギブアウェイや休日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできましたか？ [|link_sf_facebook|]をクリックして、今すぐ参加しましょう！

Lesson 29: Wi-Fiを使用してRGB LEDをリモート制御するシンプルなクライアントサーバープロジェクト
=================================================================================================

このチュートリアルでは、Wi-Fiを通じてRaspberry Pi Pico WとPCを使用してリモートでRGB LEDを制御する方法を説明します。

* **イントロダクション**: Wi-Fiを使用してRaspberry Pi Pico W上のRGB LEDをリモートで制御することを目標とします。
* **配線図とセットアップ**: RGB LEDをGPIOピン16、17、18に接続し、OLEDをGPIOピン2（SDA）と3（SCL）に接続します。
* **サーバー側のセットアップ**: ライブラリをインポートし、GPIOピンを初期化し、Wi-Fiに接続してUDPサーバーを作成し、OLEDにIPアドレスを表示します。
* **クライアント側のセットアップ**: PC上でUDPクライアントを作成し、サーバーにカラーコマンドを送信します。
* **実践的なデモンストレーション**: PCから送信されたコマンドでRGB LEDの色を変更し、OLEDにコマンドとIPアドレスを表示する様子を紹介します。
* **最終セットアップとテスト**: Raspberry Pi Pico Wにバッテリーを接続し、コードを ``main.py`` として保存して、ワイヤレス操作を実演します。


**ビデオ**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/eZTETVkX-N8?si=TtZ6B4-Ljm75rhPB" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
