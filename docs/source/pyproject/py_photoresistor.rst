.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

.. _py_photoresistor:

2.12 光を感じる
=============================

フォトレジスタは典型的なアナログ入力デバイスであり、ポテンショメータと非常に類似した方法で使用されます。その抵抗値は光の強度に依存し、照射される光が強いほど抵抗値が小さくなり、逆に、光が弱いと抵抗値が増加します。

* :ref:`cpn_photoresistor`

**必要な部品**

このプロジェクトでは、以下の部品が必要です。

全体のキットを購入することは非常に便利です、以下がそのリンクです：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前
        - このキットのアイテム
        - リンク
    *   - ケプラーキット
        - 450以上
        - |link_kepler_kit|

下記のリンクから個々の部品も購入可能です。

.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - S/N
        - 部品
        - 数量
        - リンク

    *   - 1
        - :ref:`cpn_pico_w`
        - 1
        - |link_picow_buy|
    *   - 2
        - マイクロUSBケーブル
        - 1
        - 
    *   - 3
        - :ref:`cpn_breadboard`
        - 1
        - |link_breadboard_buy|
    *   - 4
        - :ref:`cpn_wire`
        - 複数
        - |link_wires_buy|
    *   - 5
        - :ref:`cpn_resistor`
        - 1(10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_photoresistor`
        - 1
        - |link_photoresistor_buy|


**回路図**

|sch_photoresistor|

この回路では、10KΩの抵抗とフォトレジスタが直列に接続され、両方を流れる電流は同じです。10KΩの抵抗は保護として機能し、GP28はフォトレジスタの電圧変換後の値を読み取ります。

光が強くなると、フォトレジスタの抵抗が減少し、その電圧も減少します。その結果、GP28からの値も減少します。光が十分に強い場合、フォトレジスタの抵抗はほぼ0になり、GP28の値もほぼ0になります。この時、10KΩの抵抗が保護役割を果たし、3.3VとGNDが短絡するのを防ぎます。

フォトレジスタを暗い状況に置くと、GP28の値が増加します。十分に暗い状況では、フォトレジスタの抵抗は無限大になり、その電圧はほぼ3.3V（10KΩの抵抗は無視できる）になり、GP28の値は最大値65535に近づきます。

計算式は以下の通りです。

    (Vp/3.3V) x 65535 = Ap


**配線**

|wiring_photoresistor|

**コード**

.. note::

    * ``kepler-kit-main/micropython`` のパスの下にある ``2.12_feel_the_light.py`` ファイルを開くか、このコードをThonnyにコピーして、"Run Current Script"をクリックするか、F5を押して実行してください。

    * 右下隅の"MicroPython (Raspberry Pi Pico)" インタープリターをクリックするのを忘れないでください。

    * 詳細なチュートリアルについては、 :ref:`open_run_code_py` を参照してください。

.. code-block:: python

    import machine
    import utime

    photoresistor = machine.ADC(28)

    while True:
        light_value  = photoresistor.read_u16()
        print(light_value)
        utime.sleep_ms(10)

プログラムが実行された後、Shellにはフォトレジスタの値が出力されます。懐中電灯で照らすか、手で覆って値がどのように変わるかを確認できます。
