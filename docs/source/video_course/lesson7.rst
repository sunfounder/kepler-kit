.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好者コミュニティへようこそ！仲間の愛好者と共に、Raspberry Pi、Arduino、ESP32の世界に深く飛び込みましょう。

    **なぜ参加するのか？**

    - **専門家のサポート**: コミュニティやチームの助けを借りて、購入後の問題や技術的な課題を解決しましょう。
    - **学びと共有**: スキルを向上させるためのヒントやチュートリアルを交換しましょう。
    - **独占プレビュー**: 新製品の発表やプレビューにいち早くアクセスできます。
    - **特別割引**: 最新の製品に対する特別割引をお楽しみください。
    - **フェスティバルプロモーションとギブアウェイ**: ギブアウェイや休日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできましたか？ [|link_sf_facebook|]をクリックして、今すぐ参加しましょう！

Lesson 7: MicroPythonでポテンショメーターを使って3つのLEDを制御
====================================================================

このチュートリアルでは、Raspberry Pi Pico Wを使用してポテンショメーターで3つのLED（緑、黄色、赤）を制御する方法について説明します。

* **宿題の解答レビュー**: ポテンショメーターと3つのLEDを接続し、読み取り値を0から100にマッピングする方法の復習。
* **回路のセットアップ**: ポテンショメーターとLEDをRaspberry Pi Pico Wに接続する配線図。
* **値の読み取りとマッピング**: アナログ値を読み取り、432〜65,535の範囲を0〜100にマッピングする方法。
* **LEDの制御**: ifステートメントを使用して、ポテンショメーターの位置に基づいてLEDを制御（0-79で緑、80-94で黄色、95-100で赤）。
* **実践的なデモンストレーション**: 回路とコードの動作例を紹介。

**ビデオ**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/YqvcSnGd_HQ?si=igsP6I-k3FhYA7Go" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

