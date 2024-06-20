.. note::

    こんにちは、SunFounder Raspberry Pi & Arduino & ESP32 愛好者コミュニティへようこそ！Raspberry Pi、Arduino、ESP32 の世界をさらに深く探求しましょう。

    **参加する理由**

    - **専門サポート**: コミュニティとチームの助けを借りて、購入後の問題や技術的な課題を解決できます。
    - **学びと共有**: スキル向上のためのヒントやチュートリアルを交換できます。
    - **限定プレビュー**: 新製品の発表やプレビューに早期アクセスできます。
    - **特別割引**: 最新の製品に対して、限定の割引を享受できます。
    - **フェスティブプロモーションとギブアウェイ**: ギブアウェイやホリデープロモーションに参加できます。

    👉 一緒に探求し、創造する準備はできましたか？今すぐ[|link_sf_facebook|]をクリックして参加しましょう！

lesson 32: モバイル気象ステーションプロジェクト
=============================================================================

このチュートリアルでは、Raspberry Pi Pico Wを使用してポータブル気象ステーションを作成する方法を説明します。

* **WiFiへの接続**:
 - 必要なライブラリをインポートします。
 - WLANオブジェクトを作成し、WiFiネットワークに接続します。
* **天気データの取得**:
 - OpenWeatherMap APIを使用してリアルタイムの天気データを取得します。
 - 無料アカウントにサインアップしてOpenWeatherMapからAPIキーを取得します。
* **JSONデータの解析**:
 - 気温、湿度、気圧、日の出と日の入りの時刻などの関連する天気情報を抽出します。
* **OLEDにデータを表示する**:
 - OLEDディスプレイを設定し、Raspberry Pi Pico Wに接続します。
 - `ssd1306`ライブラリを使用して天気データをOLED画面に表示します。
 - 定期的に天気データを画面に更新するループを作成します。
* **デバイスへの電源供給**:
 - ポータブル使用のためにRaspberry Pi Pico Wをバッテリーに接続します。
* **コードの説明**:
 - OLEDディスプレイの初期化とWiFiへの接続手順を説明します。
 - 天気データを取得して解析し、OLED画面に表示します。
 - 数分ごとに天気データを更新するループを実装します。
* **宿題**:
 - プロジェクトを強化するために、RGB LEDを追加して、気温、湿度、風速などの天気条件を視覚的に示します。


**ビデオ**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/zovC4CvR1Hw?si=d_lhJvfzTC3pR5cS" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

