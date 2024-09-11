.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好者コミュニティへようこそ！仲間の愛好者と共に、Raspberry Pi、Arduino、ESP32の世界に深く飛び込みましょう。

    **なぜ参加するのか？**

    - **専門家のサポート**: コミュニティやチームの助けを借りて、購入後の問題や技術的な課題を解決しましょう。
    - **学びと共有**: スキルを向上させるためのヒントやチュートリアルを交換しましょう。
    - **独占プレビュー**: 新製品の発表やプレビューにいち早くアクセスできます。
    - **特別割引**: 最新の製品に対する特別割引をお楽しみください。
    - **フェスティバルプロモーションとギブアウェイ**: ギブアウェイや休日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできましたか？ [|link_sf_facebook|]をクリックして、今すぐ参加しましょう！

Lesson 32: モバイル天気ステーションプロジェクト
=============================================================================

このチュートリアルでは、Raspberry Pi Pico Wを使用してポータブル天気ステーションを作成する方法を説明します。

* **WiFiへの接続**: ライブラリをインポートし、WLANオブジェクトを作成してWiFiに接続します。
* **天気データの取得**: OpenWeatherMap APIを使用してリアルタイムの天気データを取得し、APIキーが必要です。
* **JSONデータの解析**: JSONレスポンスから温度、湿度、気圧、日の出、日の入り時刻を抽出します。
* **OLEDにデータを表示**: OLEDディスプレイをセットアップして接続し、``ssd1306`` ライブラリを使用して天気データをループで画面に更新します。
* **デバイスに電源を供給**: Raspberry Pi Pico Wをバッテリーで動作させ、ポータブル化します。
* **コードの説明**: OLEDを初期化し、WiFiに接続し、天気データを取得して表示し、定期的に更新するループを設定します。
* **宿題**: 温度、湿度、または風速に基づいて天気条件を示すRGB LEDを追加します。


**ビデオ**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/zovC4CvR1Hw?si=d_lhJvfzTC3pR5cS" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
