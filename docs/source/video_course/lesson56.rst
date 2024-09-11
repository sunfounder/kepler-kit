.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好者コミュニティへようこそ！仲間の愛好者と共に、Raspberry Pi、Arduino、ESP32の世界に深く飛び込みましょう。

    **なぜ参加するのか？**

    - **専門家のサポート**: コミュニティやチームの助けを借りて、購入後の問題や技術的な課題を解決しましょう。
    - **学びと共有**: スキルを向上させるためのヒントやチュートリアルを交換しましょう。
    - **独占プレビュー**: 新製品の発表やプレビューにいち早くアクセスできます。
    - **特別割引**: 最新の製品に対する特別割引をお楽しみください。
    - **フェスティバルプロモーションとギブアウェイ**: ギブアウェイや休日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできましたか？ [|link_sf_facebook|]をクリックして、今すぐ参加しましょう！

Lesson 56: MicroPythonでジョイスティックを使用する
=============================================================================

このチュートリアルでは、Raspberry Pi Pico Wを使用してジョイスティックを操作する方法を説明します。

* **配線セットアップ**: グランド、3.3V、VRXをGPIOピン27、VRYをGPIOピン26に接続します。
* **コードの実装**: ``machine``, ``time``, ``math`` をインポートし、ジョイスティック軸のためにADCを設定して、ジョイスティックの値を読み取り表示します。
* **キャリブレーション**: 読み取り値を-100から+100のスケールに変換して、直感的に解釈できるようにします。
* **宿題**: ジョイスティックをキャリブレーションするプログラムを作成し、中央が (0,0)、端が±100を示すようにします。

**ビデオ**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/0W8XSJhGux0?si=DO3JL-oMiMfbXF_e" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
