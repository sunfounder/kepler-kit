.. note::

    こんにちは、SunFounder Raspberry Pi & Arduino & ESP32 愛好者コミュニティへようこそ！Raspberry Pi、Arduino、ESP32 の世界をさらに深く探求しましょう。

    **参加する理由**

    - **専門サポート**: コミュニティとチームの助けを借りて、購入後の問題や技術的な課題を解決できます。
    - **学びと共有**: スキル向上のためのヒントやチュートリアルを交換できます。
    - **限定プレビュー**: 新製品の発表やプレビューに早期アクセスできます。
    - **特別割引**: 最新の製品に対して、限定の割引を享受できます。
    - **フェスティブプロモーションとギブアウェイ**: ギブアウェイやホリデープロモーションに参加できます。

    👉 一緒に探求し、創造する準備はできましたか？今すぐ[|link_sf_facebook|]をクリックして参加しましょう！

lesson 74 :  MicroPythonでRGB LEDを制御するクラスを作成する
===================================================================================

このチュートリアルでは、Raspberry Pi Pico W を使用してRGB LEDを制御するMicroPythonライブラリの作成方法について説明します。

* **配線設定**:
  - RGB LED を Raspberry Pi Pico W に接続:
  - R ピンを 330 オームの抵抗を通して GPIO ピン 14 に接続。
  - G ピンを GPIO ピン 13 に接続。
  - B ピンを 330 オームの抵抗を通して GPIO ピン 12 に接続。
  - グランドピンをグランドレールに接続。

* **コード実装**:
* **ライブラリの作成**:
   - `RGB_LED` クラスを定義し、RGB LED を操作するためのMicroPythonライブラリを作成。
   - クラス内にカラー値の辞書を含める。
   - LED ピンの初期化と PWM を使用したカラー設定のためのメソッドを作成。
* **ライブラリのインポート**:
   - 必要なライブラリ（`machine`, `time`）をインポート。
   - クラスメソッド内で RGB LED ピンの PWM を設定。
* **メインプログラム**:
   - カスタムライブラリをインポートし、RGB LED のオブジェクトを作成。
   - ユーザーに希望するカラーの入力を促すために while ループを使用。
   - 入力を検証し、適切に LED のカラーを設定。
   - 無効な入力に対するエラーハンドリングと、キーボード割り込みを使用したクリーンな終了機能を実装。
* **宿題**:
   - MicroPython ライブラリに追加のカラー設定やパターンなどの機能を追加し、メインプログラムがシンプルで読みやすい状態を保つようにプログラムを拡張。

**ビデオ**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/tw-mXURNEUc?si=Ja75F1-I6MYwJgEh" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

