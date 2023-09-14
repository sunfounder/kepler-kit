.. _cpn_pico_w:

Raspberry Pi Pico W
=======================================

|pico_w_side|

Raspberry Pi Pico Wは、ベストセラーであるRaspberry Pi Pico製品ラインに無線接続性をもたらします。私たちのRP2040シリコンプラットフォームを基盤に、Pico製品は高性能、低コスト、使いやすさといった私たちの特長をマイクロコントローラー領域に展開します。

Raspberry Pi Pico Wは、オンボードアンテナとモジュラーなコンプライアンス認証を備えた2.4GHz 802.11 b/g/nの無線LANをサポートします。ステーションモードとアクセスポイントモードの両方で動作可能です。C言語およびMicroPythonの開発者には、ネットワーク機能へのフルアクセスが可能です。
RP2040と2MBのフラッシュメモリ、1.8–5.5Vの入力電圧をサポートする電源チップを搭載。26個のGPIOピンを提供し、そのうち3つはアナログ入力として機能可能です。これらは0.1インチピッチのスルーホールパッドにキャステラーションエッジを備えています。
Raspberry Pi Pico Wは、個々のユニットまたは480ユニットのリールで、自動組立て用に提供されています。

特長
--------------

* 21 mm x 51 mmのフォームファクタ
* Raspberry Piによって英国で設計されたRP2040マイクロコントローラーチップ
* デュアルコアArm Cortex-M0+プロセッサ、最大133MHzまでの柔軟なクロック
* 264kBのオンチップSRAM
* 2MBのオンボードQSPIフラッシュ
* 2.4GHz 802.11n無線LAN
* 26個のマルチファンクションGPIOピン、うち3つはアナログ入力
* 2 x UART、2 x SPIコントローラー、2 x I2Cコントローラー、16 x PWMチャンネル
* 1 x USB 1.1コントローラーおよびPHY、ホストとデバイスのサポートあり
* 8 x プログラマブルI/O（PIO）ステートマシン、カスタム周辺機器のサポート
* サポートする入力電力 1.8-5.5V DC
* 動作温度 -20°C から +70°C
* キャステラーションモジュールにより、キャリアボードへの直接はんだ付けが可能
* USB経由のマスストレージを使ったドラッグアンドドロッププログラミング
* 低消費電力のスリープモードとドーマントモード
* 高精度なオンチップクロック
* 温度センサー
* オンチップでの整数および浮動小数点ライブラリの高速化

Picoのピン配置
----------------

|pico_pin|


.. list-table::
    :widths: 3 5 10
    :header-rows: 1

    *   - 名前
        - 説明
        - 機能
    *   - GP0-GP28
        - 汎用入出力ピン
        - 入力または出力として動作し、特定の用途はない
    *   - GND
        - 0ボルトのグラウンド
        - Pico W周囲にいくつかのGNDピンがあり、配線が容易である。
    *   - RUN
        - Picoの有効/無効
        - 別のマイクロコントローラーからPico Wを開始および停止。
    *   - GPxx_ADCx
        - 汎用入出力またはアナログ入力
        - アナログ入力としても、デジタル入出力としても使用できるが、同時には使用できない。
    *   - ADC_VREF
        - アナログ-デジタル変換器（ADC）の電圧基準
        - 任意のアナログ入力の基準電圧を設定する特別な入力ピン。
    *   - AGND
        - ADC用の0ボルトのグラウンド
        - ADC_VREFピンと一緒に使用するための特別なグラウンド接続。
    *   - 3V3(O)
        - 3.3ボルト電源
        - Pico Wが内部で動作するのと同じ3.3Vの電源供給。
    *   - 3v3(E)
        - 電源の有効/無効
        - 3V3(O)電源をオン/オフするとともに、Pico Wもオフにすることができる。
    *   - VSYS
        - 2-5ボルト電源
        - Picoの内部電源供給に直接接続されたピン、Pico Wをオフにしない限りオフにできない。
    *   - VBUS
        - 5ボルト電源
        - PicoのマイクロUSBポートから取得した5Vの電源、3.3V以上の電力が必要なハードウェアに使用。

Raspberry Pi Pico Wを始めるために必要なすべては、`こちら <https://www.raspberrypi.org/documentation/pico/getting-started/>`_ で見つかります。

また、以下のリンクも参考にしてください：

* `Raspberry Pi Pico W製品概要 <https://datasheets.raspberrypi.com/picow/pico-w-product-brief.pdf>`_
* `Raspberry Pi Pico Wデータシート <https://datasheets.raspberrypi.com/picow/pico-w-datasheet.pdf>`_
* `Raspberry Pi Picoで始める：C/C++開発 <https://datasheets.raspberrypi.org/pico/getting-started-with-pico.pdf>`_
* `Raspberry Pi Pico C/C++ SDK <https://datasheets.raspberrypi.com/pico/raspberry-pi-pico-c-sdk.pdf>`_
* `Raspberry Pi Pico C/C++ SDKのAPIレベルDoxygenドキュメンテーション <https://raspberrypi.github.io/pico-sdk-doxygen/>`_
* `Raspberry Pi Pico Python SDK <https://datasheets.raspberrypi.com/pico/raspberry-pi-pico-python-sdk.pdf>`_
* `Raspberry Pi RP2040データシート <https://datasheets.raspberrypi.org/rp2040/rp2040-datasheet.pdf>`_
* `RP2040を用いたハードウェア設計 <https://datasheets.raspberrypi.com/rp2040/hardware-design-with-rp2040.pdf>`_
* `Raspberry Pi Pico W設計ファイル <https://datasheets.raspberrypi.com/picow/RPi-PicoW-PUBLIC-20220607.zip>`_
* `Raspberry Pi Pico W STEPファイル <https://datasheets.raspberrypi.com/picow/PicoW-step.zip>`_
