.. note::

    こんにちは、SunFounder Raspberry Pi & Arduino & ESP32 愛好者コミュニティへようこそ！仲間の愛好者たちと一緒に、Raspberry Pi、Arduino、ESP32 の世界をより深く探求しましょう。

    **参加する理由**

    - **専門サポート**: コミュニティとチームの助けを借りて、購入後の問題や技術的な課題を解決できます。
    - **学びと共有**: スキル向上のためのヒントやチュートリアルを交換できます。
    - **限定プレビュー**: 新製品の発表やプレビューに早期アクセスできます。
    - **特別割引**: 最新の製品に対して、限定の割引を享受できます。
    - **フェスティブプロモーションとギブアウェイ**: ギブアウェイやホリデープロモーションに参加できます。

    👉 一緒に探求し、創造する準備はできましたか？今すぐ[|link_sf_facebook|]をクリックして参加しましょう！

lesson 29: Wi-Fiを介してRGB LEDを制御するシンプルなクライアントサーバープロジェクト
==================================================================================

このチュートリアルでは、Raspberry Pi Pico WとPCをWi-Fi経由で接続し、リモートでRGB LEDを制御する方法を説明します。

* **導入**:
 - 目標は、Wi-Fiを使用してPCからRaspberry Pi Pico W上のRGB LEDをリモート制御することです。
* **配線図とセットアップ**:
 - RGB LEDの赤、緑、青のチャネルはそれぞれGPIOピン16、17、18に接続されます。
 - OLEDディスプレイはI2Cを介してGPIOピン2（SDA）と3（SCL）に接続されます。
* **サーバー側のセットアップ (Raspberry Pi Pico W)**:
 - ライブラリのインポート: `socket`、`time`、`network`、`machine`、`ssd1306`。
 - RGB LEDとOLEDディスプレイ用のGPIOピンを初期化します。
 - Wi-Fiに接続し、IPアドレスを取得します。
 - UDPサーバーソケットを作成し、IPアドレスとポートにバインドします。
 - OLED画面にIPアドレスとポートを表示します。
 - 受信コマンドをリッスンし、デコードしてコマンドと送信者のアドレスを表示します。
* **クライアント側のセットアップ (PC)**:
 - `socket`ライブラリをインポートします。
 - サーバーのアドレスとポートを定義します。
 - UDPクライアントソケットを作成します。
 - LEDの色のユーザー入力を取得し、コマンドをエンコードしてサーバーに送信します。
 - サーバーの応答を待ち、印刷します。
* **実践デモ**:
 - クライアントからコマンドを送信してサーバー上のRGB LEDの色を変更するデモを行います。
 - OLEDディスプレイには受信したコマンドと送信者のIPアドレスが表示されます。
* **最終セットアップとテスト**:
 - Raspberry Pi Pico WをUSBから切断し、バッテリーで電源を供給します。
 - コードを`main.py`として保存し、起動時に実行されるようにします。
 - PCからコマンドを送信し、RGB LEDの変化とOLEDの更新を観察する完全にワイヤレスな動作を実演します。

**ビデオ**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/eZTETVkX-N8?si=TtZ6B4-Ljm75rhPB" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

