.. note::

    こんにちは、SunFounder Raspberry Pi & Arduino & ESP32 愛好者コミュニティへようこそ！Raspberry Pi、Arduino、ESP32 の世界をさらに深く探求しましょう。

    **参加する理由**

    - **専門サポート**: コミュニティとチームの助けを借りて、購入後の問題や技術的な課題を解決できます。
    - **学びと共有**: スキル向上のためのヒントやチュートリアルを交換できます。
    - **限定プレビュー**: 新製品の発表やプレビューに早期アクセスできます。
    - **特別割引**: 最新の製品に対して、限定の割引を享受できます。
    - **フェスティブプロモーションとギブアウェイ**: ギブアウェイやホリデープロモーションに参加できます。

    👉 一緒に探求し、創造する準備はできましたか？今すぐ[|link_sf_facebook|]をクリックして参加しましょう！

lesson 67 : MicroPythonでPi Picoの両方のコアを使用する方法
===================================================================================

このチュートリアルでは、Raspberry Pi Pico Wの両方のコアを使用する方法を紹介します。

* **配線設定**:
- 緑色のLEDをGPIOピン14に接続し、330オームの抵抗を介してグランドに接続します。
- 赤色のLEDをGPIOピン15に接続し、330オームの抵抗を介してグランドに接続します。
* **コード実装**:
- 必要なライブラリ（`machine`、`time`、`_thread`）をインポートします。
- LED用のピンを設定します。
- LEDの点滅時間のパラメータを定義します。
- LEDの点滅を制御する関数を作成します:
   - `other_core`関数は赤色のLEDをセカンドコアで制御します。
   - `green_blink`関数はメインコアで緑色のLEDを制御します。
- `_thread.start_new_thread`を使用して、セカンドコアで`other_core`関数を実行します。
* **宿題**:
- サーボを接続します。
- サーボとLEDを制御します:
  - サーボが後退する際に赤色のLEDを点滅させます。
  - サーボが前進する際に緑色のLEDを点滅させます。

**ビデオ**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/mm1EoNqjd4c?si=RHZLX39PpGDbAFuM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

