.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好者コミュニティへようこそ！仲間の愛好者と共に、Raspberry Pi、Arduino、ESP32の世界に深く飛び込みましょう。

    **なぜ参加するのか？**

    - **専門家のサポート**: コミュニティやチームの助けを借りて、購入後の問題や技術的な課題を解決しましょう。
    - **学びと共有**: スキルを向上させるためのヒントやチュートリアルを交換しましょう。
    - **独占プレビュー**: 新製品の発表やプレビューにいち早くアクセスできます。
    - **特別割引**: 最新の製品に対する特別割引をお楽しみください。
    - **フェスティバルプロモーションとギブアウェイ**: ギブアウェイや休日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできましたか？ [|link_sf_facebook|]をクリックして、今すぐ参加しましょう！

Lesson 45: 自由落下で物体の高さを計算する
=============================================================================
このチュートリアルでは、Raspberry Pi Pico WとMPU6050センサーを使用して垂直距離を測定する方法を説明します。

* **セットアップ**: MPU6050とOLED 1306をRaspberry Pi Pico Wに接続し、ノイズを減らすために確実に接続します。
* **概念**: 自由落下中の時間（T_drop）を測定し、それを使用して落下した高さを計算します。
* **方程式**: ``高さ（H）を \( H = 16 \times (T_{drop})^2 \)`` の式で計算し、時間をミリ秒から秒に変換します。
* **コードの実装**: ライブラリを設定し、Z軸加速度で0Gを検出し、自由落下中にタイマーを開始して、OLEDに高さと落下時間を表示します。
* **実践的なデモンストレーション**: 既知の高さからセンサーを落としてテストし、必要に応じて精度を調整します。

**ビデオ**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/xpHDAcdrTF0?si=NdmV4J5G6DhJ4f6M" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
