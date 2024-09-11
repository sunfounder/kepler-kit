.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好者コミュニティへようこそ！仲間の愛好者と共に、Raspberry Pi、Arduino、ESP32の世界に深く飛び込みましょう。

    **なぜ参加するのか？**

    - **専門家のサポート**: コミュニティやチームの助けを借りて、購入後の問題や技術的な課題を解決しましょう。
    - **学びと共有**: スキルを向上させるためのヒントやチュートリアルを交換しましょう。
    - **独占プレビュー**: 新製品の発表やプレビューにいち早くアクセスできます。
    - **特別割引**: 最新の製品に対する特別割引をお楽しみください。
    - **フェスティバルプロモーションとギブアウェイ**: ギブアウェイや休日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできましたか？ [|link_sf_facebook|]をクリックして、今すぐ参加しましょう！

Lesson 16: MicroPythonでRGB LEDの色のシーケンスを制御
=============================================================================

このチュートリアルでは、Raspberry Pi Pico Wを使用して、MicroPythonでforループを使ってRGB LEDを制御する方法について説明します。

* **イントロダクション**: forループとPWMを使用してRGB LEDの明るさと色を制御する概要を説明します。
* **回路のセットアップ**: 330オームの抵抗を使用してRGB LEDをGPIOピン13、14、15に接続します。
* **PWMのセットアップ**: 各LEDチャネルでPWMを設定し、スムーズな色の変化のために1000Hzの周波数を使用します。
* **カラーシーケンスの入力**: ユーザーにカラーシーケンスを入力させ、入力を配列に保存します。
* **カラー制御ロジック**: ifステートメントを使用して、赤、緑、青、シアン、マゼンタ、黄色、オレンジ、オフなどの色に対応するPWM値を割り当てます。
* **連続ループ**: while trueループとスリープステートメントを使用して、カラーシーケンスを繰り返し表示します。



**ビデオ**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/VivNlgYg3wY?si=ECUsRAWanIAShyxk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

