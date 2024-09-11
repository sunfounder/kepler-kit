.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好者コミュニティへようこそ！仲間の愛好者と共に、Raspberry Pi、Arduino、ESP32の世界に深く飛び込みましょう。

    **なぜ参加するのか？**

    - **専門家のサポート**: コミュニティやチームの助けを借りて、購入後の問題や技術的な課題を解決しましょう。
    - **学びと共有**: スキルを向上させるためのヒントやチュートリアルを交換しましょう。
    - **独占プレビュー**: 新製品の発表やプレビューにいち早くアクセスできます。
    - **特別割引**: 最新の製品に対する特別割引をお楽しみください。
    - **フェスティバルプロモーションとギブアウェイ**: ギブアウェイや休日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできましたか？ [|link_sf_facebook|]をクリックして、今すぐ参加しましょう！

Lesson 47: ローパスフィルターを使用してセンサーデータを改善する
=============================================================================
このチュートリアルでは、Raspberry Pi Pico WとMPU6050センサーを使用して、ローパスフィルターを実装することで安定した2軸傾斜計を作成する方法を説明します。

* **セットアップ**: MPU6050をRaspberry Pi Pico Wに接続します。
* **概念**: 加速度計データを使用して傾きを測定し、加速による誤差に対処します。
* **ローパスフィルター**: データを平滑化するために以下の式を使用してフィルターを実装します: ``\(\text{new value} = \text{confidence} \times \text{measurement} + (1 - \text{confidence}) \times \text{old value}\)``。
* **コード**: X、Y、Zの測定値をフィルターにかけ、ピッチとロール角を表示します。
* **宿題**: ローパスフィルターをテストし、信頼度の値を調整して実験します。

**ビデオ**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/3YqGIg4crEk?si=rwiDFcJ98nlj_Sg3" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
