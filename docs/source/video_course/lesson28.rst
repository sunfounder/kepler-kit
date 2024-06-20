.. note::

    こんにちは、SunFounder Raspberry Pi & Arduino & ESP32 愛好者コミュニティへようこそ！仲間の愛好者たちと一緒に、Raspberry Pi、Arduino、ESP32 の世界をより深く探求しましょう。

    **参加する理由**

    - **専門サポート**: コミュニティとチームの助けを借りて、購入後の問題や技術的な課題を解決できます。
    - **学びと共有**: スキル向上のためのヒントやチュートリアルを交換できます。
    - **限定プレビュー**: 新製品の発表やプレビューに早期アクセスできます。
    - **特別割引**: 最新の製品に対して、限定の割引を享受できます。
    - **フェスティブプロモーションとギブアウェイ**: ギブアウェイやホリデープロモーションに参加できます。

    👉 一緒に探求し、創造する準備はできましたか？今すぐ[|link_sf_facebook|]をクリックして参加しましょう！

lesson 28: Raspberry Pi Pico WをWiFiに接続する
=============================================================================

このチュートリアルでは、Raspberry Pi Pico WとPCをWi-Fiを介してクライアント-サーバー関係に設定する方法を説明します。

* **導入**:
 - 目標を強調: Raspberry Pi Pico WをWi-Fiに接続し、PCとのクライアント-サーバー関係を作成する。
* **クライアント-サーバー関係の理解**:
 - マクドナルドのサーバーとクライアントのアナロジーを使って概念を説明。
 - PCがクライアント、Raspberry Pi Pico Wがサーバーになることを明確にする。
* **Raspberry Pi Pico Wをサーバーとして設定する**:
 - 必要なライブラリとWi-Fiネットワークを作成する手順を詳述。
 - Wi-Fiに接続し、IPアドレスを取得する方法を説明。
 - Raspberry Pi Pico W上でUDPサーバーを設定し、IPアドレスとポートにバインドする方法を説明。
* **PCにクライアントを作成する**:
 - PCクライアントがRaspberry Pi Pico Wサーバーに接続するためのコードを提供。
 - クライアントからサーバーにコマンドを送信する方法を説明。
* **データの送受信**:
 - サーバーがクライアントからコマンドを受信し、デコードする方法を示す。
 - サーバーからクライアントへの応答を送信する方法を実演。
* **実践デモ**:
 - サーバーとクライアントのプログラムを実行し、相互作用とデータ交換を示す。
 - バッテリー駆動のRaspberry Pi Pico WがOLEDディスプレイにIPアドレスを表示する様子を表示。

**ビデオ**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/UR_p4QchMYY?si=V5vRZw4R_UFDwt36" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

