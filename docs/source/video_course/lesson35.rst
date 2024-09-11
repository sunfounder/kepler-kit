.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好者コミュニティへようこそ！仲間の愛好者と共に、Raspberry Pi、Arduino、ESP32の世界に深く飛び込みましょう。

    **なぜ参加するのか？**

    - **専門家のサポート**: コミュニティやチームの助けを借りて、購入後の問題や技術的な課題を解決しましょう。
    - **学びと共有**: スキルを向上させるためのヒントやチュートリアルを交換しましょう。
    - **独占プレビュー**: 新製品の発表やプレビューにいち早くアクセスできます。
    - **特別割引**: 最新の製品に対する特別割引をお楽しみください。
    - **フェスティバルプロモーションとギブアウェイ**: ギブアウェイや休日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできましたか？ [|link_sf_facebook|]をクリックして、今すぐ参加しましょう！

Lesson 35: RGB LED温度インジケーター付きリモート天気ステーション
=============================================================================
このチュートリアルでは、Raspberry Pi Pico Wを使用して、天気ステーションに温度を表示するRGB LEDを統合する方法を説明します。

* **プロジェクト概要**: Raspberry Pi Pico W、OLEDディスプレイ、RGB LEDを使用して、温度を視覚的に表現するリモート天気ステーションを構築します。
* **HSVからRGBへの変換**: 温度を-20°F（バイオレット）から120°F（赤）までHSVカラーホイールの角度にマッピングします。
* **回路セットアップ**: OLEDディスプレイとRGB LEDをRaspberry Pi Pico Wに接続し、GPIOとPWMを設定します。
* **コーディング**: 温度データを取得し、色相を計算してRGBに変換し、HSVからRGBへの変換ライブラリを使用してRGB LEDを制御します。
* **デモンストレーション**: OLEDとRGB LEDに温度を表示し、バッテリー駆動でセットアップを実行します。
* **結論**: 異なる色のマッピングや温度範囲でプロジェクトをカスタマイズし、チュートリアルに対するインタラクションを促進します。



**ビデオ**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/c9tQHyQWIYk?si=ORHsIXt8eBGeXDdp" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
