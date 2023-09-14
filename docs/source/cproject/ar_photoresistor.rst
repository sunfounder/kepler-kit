.. _ar_photoresistor:

2.12 - 光を感じる
=================================

フォトレジスタは、アナログ入力に典型的に使用されるデバイスであり、ポテンショメータと非常に似た方法で使用されます。その抵抗値は光の強度に依存し、照射される光が強ければ抵抗値は小さくなり、逆に、光が弱ければ抵抗値は増加します。

* :ref:`cpn_photoresistor`

**必要なコンポーネント**

このプロジェクトで必要なコンポーネントは以下の通りです。

一式をまとめて購入すると便利です、そのためのリンクはこちら：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前
        - このキットに含まれるアイテム
        - 購入リンク
    *   - ケプラーキット
        - 450+
        - |link_kepler_kit|

以下のリンクから個別にも購入できます。

.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - コンポーネント紹介
        - 数量
        - 購入リンク
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
        - 数本
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

この回路では、10KΩの抵抗器とフォトレジスタが直列に接続され、流れる電流は同じです。10KΩの抵抗器は保護として機能し、GP28はフォトレジスタの電圧変換後の値を読み取ります。

光が強くなると、フォトレジスタの抵抗が減少し、その結果、電圧が低下し、GP28からの値も低下します。光が十分に強いと、フォトレジスタの抵抗はほぼ0に近く、GP28の値もほぼ0に近くなります。このとき、10KΩの抵抗器は、3.3VとGNDが直接接続されて短絡するのを防ぐ保護役となります。

フォトレジスタを暗い状況に置くと、GP28の値は上昇します。十分に暗い状況では、フォトレジスタの抵抗は無限大になり、その電圧はほぼ3.3V（10KΩの抵抗は無視できる）に近く、GP28の値は最大値65535に近くなります。

計算式は以下の通りです。

    (Vp/3.3V) x 65535 = Ap

**配線**

|wiring_photoresistor|

**コード**

.. note::

   * ファイル ``2.12_feel_the_light.ino`` は、 ``kepler-kit-main/arduino/2.12_feel_the_light`` のパスで開くことができます。
   * または、このコードを **Arduino IDE** にコピーしてください。

   * **アップロード** ボタンをクリックする前に、ボード（Raspberry Pi Pico）と正しいポートを選択してください。

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/44074b9e-3e4e-475b-af37-689254f87ab2/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

プログラムが実行された後、シリアルモニターはフォトレジスタの値を出力します。手で覆うか、フラッシュライトで照らして、値がどのように変わるかを確認できます。
