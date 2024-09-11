.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好者コミュニティへようこそ！仲間の愛好者と共に、Raspberry Pi、Arduino、ESP32の世界に深く飛び込みましょう。

    **なぜ参加するのか？**

    - **専門家のサポート**: コミュニティやチームの助けを借りて、購入後の問題や技術的な課題を解決しましょう。
    - **学びと共有**: スキルを向上させるためのヒントやチュートリアルを交換しましょう。
    - **独占プレビュー**: 新製品の発表やプレビューにいち早くアクセスできます。
    - **特別割引**: 最新の製品に対する特別割引をお楽しみください。
    - **フェスティバルプロモーションとギブアウェイ**: ギブアウェイや休日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできましたか？ [|link_sf_facebook|]をクリックして、今すぐ参加しましょう！

Lesson 57: MicroPythonでジョイスティックをキャリブレーションする
=============================================================================

このチュートリアルでは、Raspberry Pi Pico Wを使用してジョイスティックをキャリブレーションする方法を説明します。

* **配線セットアップ**: グランドをピン38、3.3Vをピン36、VRXをGPIOピン27、VRYをGPIOピン26に接続します。
* **コードの実装**: ``machine``, ``time``, ``math`` をインポートし、ジョイスティック軸のためにADCを設定して、ジョイスティックの値を読み取り表示します。
* **キャリブレーション**: 生のADC値を-100から+100のスケールに変換し、ニュートラルポジションのノイズを調整します。
* **宿題**: ジョイスティックの位置に基づいて角度を計算し、報告するプログラムを作成します。


**ビデオ**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/rRHyho4vwIQ?si=cV75rrwEWSYoKhAN" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
