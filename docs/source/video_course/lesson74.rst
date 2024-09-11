.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好者コミュニティへようこそ！仲間の愛好者と共に、Raspberry Pi、Arduino、ESP32の世界に深く飛び込みましょう。

    **なぜ参加するのか？**

    - **専門家のサポート**: コミュニティやチームの助けを借りて、購入後の問題や技術的な課題を解決しましょう。
    - **学びと共有**: スキルを向上させるためのヒントやチュートリアルを交換しましょう。
    - **独占プレビュー**: 新製品の発表やプレビューにいち早くアクセスできます。
    - **特別割引**: 最新の製品に対する特別割引をお楽しみください。
    - **フェスティバルプロモーションとギブアウェイ**: ギブアウェイや休日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできましたか？ [|link_sf_facebook|]をクリックして、今すぐ参加しましょう！

Lesson 74: RGB LEDを制御するMicroPythonクラスを作成する
===================================================================================

このチュートリアルでは、Raspberry Pi Pico Wを使用してRGB LEDを制御するMicroPythonライブラリを作成する方法を説明します。

* **コンセプト概要**: PWMを使用してカスタム ``RGB_LED`` クラスでRGB LEDを制御します。
* **実装例**: RGB LEDをGPIOピンに接続し、PWMで色の変更を管理するクラスを定義し、ユーザー入力でLEDの色を調整します。
* **宿題**: ``RGB_LED`` クラスを拡張して、カラーパターンや追加機能を実装します。メインプログラムがシンプルでライブラリを活用できるようにします。
* **重要なポイント**: ハードウェア制御のためにカスタムクラスを使ってコードを構築し、MicroPythonで効率的にユーザー入力を処理する方法を学びます。


**ビデオ**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/tw-mXURNEUc?si=Ja75F1-I6MYwJgEh" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
