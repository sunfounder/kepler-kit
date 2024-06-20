.. note::

    こんにちは、SunFounder Raspberry Pi & Arduino & ESP32 愛好者コミュニティへようこそ！Raspberry Pi、Arduino、ESP32 の世界をさらに深く探求しましょう。

    **参加する理由**

    - **専門サポート**: コミュニティとチームの助けを借りて、購入後の問題や技術的な課題を解決できます。
    - **学びと共有**: スキル向上のためのヒントやチュートリアルを交換できます。
    - **限定プレビュー**: 新製品の発表やプレビューに早期アクセスできます。
    - **特別割引**: 最新の製品に対して、限定の割引を享受できます。
    - **フェスティブプロモーションとギブアウェイ**: ギブアウェイやホリデープロモーションに参加できます。

    👉 一緒に探求し、創造する準備はできましたか？今すぐ[|link_sf_facebook|]をクリックして参加しましょう！

lesson 73 :  MicroPythonで辞書を使ってRGB LEDを制御する方法
===================================================================================

このチュートリアルでは、Raspberry Pi Pico W を使用して辞書を用いた RGB LED の制御方法を説明します。

* **配線設定**:
- Raspberry Pi Pico W への RGB LED の接続:
  - R ピンを GPIO ピン 14 に 330 オームの抵抗を通して接続。
  - G ピンを GPIO ピン 13 に接続。
  - B ピンを GPIO ピン 12 に 330 オームの抵抗を通して接続。
  - グランドピンをグランドレールに接続。
* **コード実装**:
- **辞書の作成**:
   - カラー名をキーとして、その RGB 値をリストとして定義する辞書を作成。
- **ライブラリのインポート**:
   - 必要なライブラリ (`machine`, `time`) をインポート。
   - RGB LED ピンの PWM を設定。
- **メインプログラムループ**:
   - ユーザーに希望するカラーの入力を促すループを実装。
   - 入力を小文字に変換し、有効なカラーかどうかをチェック。
   - 有効であれば、辞書の値に基づいて PWM デューティサイクルを調整して LED の色を変更。
   - 無効な入力に対するエラーハンドリングを実装。
- **カラー設定関数**:
   - `make_color` 関数を定義し、希望するカラーを引数として受け取り、PWM を使用して RGB LED を適切に設定。

* **宿題**:
   - `make_color` 関数をライブラリに移動し、メインプログラムにインポートして使用するようにプログラムを拡張。

**ビデオ**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/1CHcjlaBvGY?si=feXCiEMKRkdsLx4y" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

