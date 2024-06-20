.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好者コミュニティへようこそ！仲間の愛好者と共に、Raspberry Pi、Arduino、ESP32の世界に深く飛び込みましょう。

    **参加する理由**

    - **専門家のサポート**: コミュニティやチームの助けを借りて、購入後の問題や技術的な課題を解決します。
    - **学びと共有**: スキルを向上させるためのヒントやチュートリアルを交換します。
    - **独占プレビュー**: 新製品の発表やプレビューにいち早くアクセスできます。
    - **特別割引**: 最新の製品に対する特別割引を楽しめます。
    - **フェスティブプロモーションとギブアウェイ**: ギブアウェイや休日のプロモーションに参加できます。

    👉 私たちと一緒に探索し、創造する準備はできましたか？ [|link_sf_facebook|]をクリックして、今すぐ参加しましょう！

lesson 11:  MicroPythonでRGB LEDを理解し制御する
==========================================================================

このチュートリアルでは、SunFounder Kepler KitとRaspberry Pi Pico Wを使用してRGB LEDを制御する方法を説明します。

* **RGB LEDの制御**: PWM（パルス幅変調）を使用してRGB LEDの色を制御する方法について説明します。RGB LEDは、共通のグランドを持つ赤、緑、青の3つのLEDで構成されています。各色チャネルに対して個別の電流制限抵抗を使用してクロストークを防ぐ重要性を強調します。
* **配線図とセットアップ**: RGB LEDと必要な抵抗器をRaspberry Pi Pico Wに接続するための詳細な配線図を提供します。ブレッドボード上での物理的なセットアップを示し、赤、緑、青の各チャネルをGPIOピン13、14、15にそれぞれ接続します。
* **コードの説明**: 各GPIOピンでPWMを設定し、各色チャネルの明るさを制御するコードについて説明します。PWM周波数、デューティサイクル、および赤、緑、青の各チャネルのGPIOピンの初期化をカバーします。
* **実践デモ**: RGB LEDの色を変更するコードを実行する方法を示します。個々の色チャネルをオン・オフし、明るさレベルを調整する様子を実演します。
* **宿題**: ユーザーに、色（赤、緑、青、シアン、マゼンタ、黄、オレンジ、白）を入力させ、RGB LEDを指定された色に調整するプログラムを作成するよう求めます。PWM値を組み合わせて正確な色再現を達成することを奨励します。

**ビデオ**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/MCo5nXAKyUU?si=VauJgWRltVnQpwz-" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

