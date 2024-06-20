.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好者コミュニティへようこそ！仲間の愛好者と共に、Raspberry Pi、Arduino、ESP32の世界に深く飛び込みましょう。

    **参加する理由**

    - **専門家のサポート**: コミュニティやチームの助けを借りて、購入後の問題や技術的な課題を解決します。
    - **学びと共有**: スキルを向上させるためのヒントやチュートリアルを交換します。
    - **独占プレビュー**: 新製品の発表やプレビューにいち早くアクセスできます。
    - **特別割引**: 最新の製品に対する特別割引を楽しめます。
    - **フェスティブプロモーションとギブアウェイ**: ギブアウェイや休日のプロモーションに参加できます。

    👉 私たちと一緒に探索し、創造する準備はできましたか？ [|link_sf_facebook|]をクリックして、今すぐ参加しましょう！

lesson 13:  ユーザー指定のRGB LEDカラーをMicropythonで実現
==========================================================================

このチュートリアルでは、SunFounder Kepler KitとRaspberry Pi Pico Wを使用してRGB LEDを制御する方法について説明します。

* **RGB LEDの制御**: PWM（パルス幅変調）を使用してRGB LEDを制御し、さまざまな色を実現する方法を説明します。RGB LEDの構造についても説明し、赤、緑、青、グランドの4本の足があることを解説します。
* **配線図とセットアップ**: RGB LEDをRaspberry Pi Pico Wに接続するための詳細な配線図を提供します。各色チャネル（赤、緑、青）はGPIOピン（13, 14, 15）に接続され、それぞれ220オームの抵抗が電流を制限するために使用されます。
* **コードの説明**: 各GPIOピンでPWMを設定し、各色チャネルの明るさを制御するためのMicroPythonコードを説明します。ユーザーの入力に基づいて特定の色（赤、緑、青、シアン、マゼンタ、黄、オレンジ、白）を点灯させるコードを含みます。
* **実践デモ**: コードを実行し、RGB LEDの色を変更する方法を示します。色を入力し、RGB LEDがその色に変わる様子を観察するプロセスを実演します。
* **宿題**: プロジェクトを拡張し、3つのポテンショメータを接続して手動でRGB LEDの色を制御するようにします。ポテンショメータの値を混ぜ合わせて、任意の色を達成することを推奨します。

**ビデオ**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/FLMPjwXqXVw?si=laOuij3khzBg5Uac" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

