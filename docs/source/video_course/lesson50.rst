.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好者コミュニティへようこそ！仲間の愛好者と共に、Raspberry Pi、Arduino、ESP32の世界に深く飛び込みましょう。

    **なぜ参加するのか？**

    - **専門家のサポート**: コミュニティやチームの助けを借りて、購入後の問題や技術的な課題を解決しましょう。
    - **学びと共有**: スキルを向上させるためのヒントやチュートリアルを交換しましょう。
    - **独占プレビュー**: 新製品の発表やプレビューにいち早くアクセスできます。
    - **特別割引**: 最新の製品に対する特別割引をお楽しみください。
    - **フェスティバルプロモーションとギブアウェイ**: ギブアウェイや休日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできましたか？ [|link_sf_facebook|]をクリックして、今すぐ参加しましょう！

Lesson 50: センサーデータから長期的な定常誤差を除去する
=============================================================================
このチュートリアルでは、MPU6050センサーとRaspberry Pi Pico Wを使用して、傾き測定の精度を向上させる方法を説明します。

* **セットアップ**: MPU6050をRaspberry Pi Pico Wに接続します。
* **課題**: 加速度計はノイズが多く、ジャイロスコープは時間とともにドリフトします。
* **解決策**: 補完フィルターとローパスフィルターを使用して加速度計とジャイロスコープのデータを組み合わせ、誤差補正を行います。
* **結果**: 正確で高速、かつノイズの少ない傾き測定が実現します。
* **宿題**: フィルターと誤差補正を実装し、傾きデータをOLEDスクリーンに表示します。




**ビデオ**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/VdTBBUKH43k?si=oJ64AlVvQejBBR2R" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
