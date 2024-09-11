.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好者コミュニティへようこそ！仲間の愛好者と共に、Raspberry Pi、Arduino、ESP32の世界に深く飛び込みましょう。

    **なぜ参加するのか？**

    - **専門家のサポート**: コミュニティやチームの助けを借りて、購入後の問題や技術的な課題を解決しましょう。
    - **学びと共有**: スキルを向上させるためのヒントやチュートリアルを交換しましょう。
    - **独占プレビュー**: 新製品の発表やプレビューにいち早くアクセスできます。
    - **特別割引**: 最新の製品に対する特別割引をお楽しみください。
    - **フェスティバルプロモーションとギブアウェイ**: ギブアウェイや休日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできましたか？ [|link_sf_facebook|]をクリックして、今すぐ参加しましょう！

Lesson 46: MPU6050を使用してディスプレイ付き2軸傾斜計を作成する
=============================================================================
このチュートリアルでは、Raspberry Pi Pico WとMPU6050センサーを使用して、2軸傾斜計を作成する方法を説明します。

* **セットアップ**: MPU6050とOLED 1306をRaspberry Pi Pico Wに接続します。
* **概念**: ピッチとロール角度を使用して傾きを測定し、OLEDにバブルレベルを表示します。
* **方程式**: 
   - ピッチ: ``\(\arctan\left(\frac{Y}{Z}\right)\)``
   - ロール: ``\(\arctan\left(\frac{X}{Z}\right)\)``
   - ラジアンを度に変換します。
* **コード**: ライブラリを設定し、X、Y、Zの加速度を測定して角度を計算し、OLEDに表示します。
* **デモンストレーション**: 傾きをテストし、バブルの動きを応答性に合わせて調整します。
* **応用**: 加速度や振動による誤差を防ぐために、傾斜の読み取りを安定させます。

**ビデオ**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/wYv39RMwXvU?si=6gJoFFIa1HSdGIFt" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
