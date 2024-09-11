.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好者コミュニティへようこそ！仲間の愛好者と共に、Raspberry Pi、Arduino、ESP32の世界に深く飛び込みましょう。

    **なぜ参加するのか？**

    - **専門家のサポート**: コミュニティやチームの助けを借りて、購入後の問題や技術的な課題を解決しましょう。
    - **学びと共有**: スキルを向上させるためのヒントやチュートリアルを交換しましょう。
    - **独占プレビュー**: 新製品の発表やプレビューにいち早くアクセスできます。
    - **特別割引**: 最新の製品に対する特別割引をお楽しみください。
    - **フェスティバルプロモーションとギブアウェイ**: ギブアウェイや休日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできましたか？ [|link_sf_facebook|]をクリックして、今すぐ参加しましょう！

Lesson 31: センサーなしのリモート天気ステーションプロジェクト
=============================================================================

このチュートリアルでは、Raspberry Pi Pico Wを使用してセンサーなしの天気ステーションを作成する方法について説明します。

* **WiFiへの接続**: ライブラリをインポートし、WLANオブジェクトを使用してWiFiに接続します。
* **天気データの取得**: OpenWeatherMap APIを使用してリアルタイムの天気データを取得し、APIキーが必要です。
* **JSONデータの解析**: JSONレスポンスから温度、湿度、気圧、日の出、日の入り時刻を抽出します。
* **コードの説明**: ``urequests.get()`` を使用してデータを取得し、Unix時間を変換し、気圧の単位を調整します。
* **天気データの表示**: 温度、湿度、気圧、天気の状態、風速を表示します。
* **宿題**: ディスプレイを追加し、ポータブルでバッテリー駆動の天気ステーションを作成します。



**ビデオ**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/hbcA90S7Jtk?si=mHMxKUEEpqiYM7DA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
