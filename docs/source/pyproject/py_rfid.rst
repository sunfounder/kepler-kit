.. _py_rfid:


6.5 無線周波識別（RFID）
================================================

無線周波識別（RFID）は、オブジェクト（またはタグ）と問い合わせ装置（またはリーダー）との間で無線通信を使用して、それを追跡および識別する技術です。タグの送信範囲は数メートルに限られています。リーダーとタグは、必ずしも視界を必要としません。

ほとんどのタグには、通常、集積回路（IC）とアンテナが搭載されています。
このマイクロチップは、無線周波（RF）を介してリーダーとの通信を管理するだけでなく、情報も保存します。
パッシブタグには独立したエネルギー源がなく、リーダーからの外部電磁信号に電力供給を依存しています。
アクティブタグは、バッテリーなどの独立したエネルギー源で動作し、その結果、処理、送信、範囲の面でより高性能かもしれません。


* :ref:`cpn_mfrc522`

**必要なコンポーネント**

このプロジェクトでは、以下のコンポーネントが必要です。

全体のキットを購入すると非常に便利です、リンクはこちら：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前
        - このキットに含まれるアイテム
        - リンク
    *   - ケプラーキット	
        - 450以上
        - |link_kepler_kit|

以下のリンクから個別にも購入できます。

.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - コンポーネント	
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
        - 数本
        - |link_wires_buy|
    *   - 5
        - :ref:`cpn_mfrc522`
        - 1
        - |link_rfid_buy|

**回路図**

|sch_rfid|

**配線**

|wiring_rfid|


**コード**

ここでは、 ``mfrc522`` フォルダ内のライブラリを使用する必要があります。Pico Wにアップロードされているかどうか確認してください。詳細なチュートリアルは :ref:`add_libraries_py` を参照してください。

主要な関数は二つに分かれています：

* ``6.5_rfid_write.py`` ：カード（またはキー）に情報を書き込むために使用されます。
* ``6.5_rfid_read.py`` ：カード（またはキー）に格納されている情報を読み取るために使用されます。

``kepler-kit-main/micropython`` のパスの下で ``6.5_rfid_write.py`` ファイルを開くか、このコードをThonnyにコピーしてから、「現在のスクリプトを実行」をクリックするか、単にF5を押して実行します。

実行後、シェルでメッセージを入力し、その後MFRC522モジュールに近づけてメッセージを書き込むことができます。

.. code-block:: python

    from mfrc522 import SimpleMFRC522

    reader = SimpleMFRC522(spi_id=0,sck=2,miso=4,mosi=3,cs=5,rst=0)

    def write():
        to_write = input("Please enter the message: ")
        print("Writing...Please place the card...")
        id, text = reader.write(to_write)
        print("ID: %s\nText: %s" % (id,text))

    write()

``kepler-kit-main/micropython`` のパスの下で ``6.5_rfid_read.py`` ファイルを開くか、このコードをThonnyにコピーしてから、「現在のスクリプトを実行」をクリックするか、単にF5を押して実行します。

実行後、カード（またはキー）に格納されたメッセージを読み取ることができます。

.. code-block:: python

    from mfrc522 import SimpleMFRC522

    reader = SimpleMFRC522(spi_id=0,sck=2,miso=4,mosi=3,cs=5,rst=0)

    def read():
        print("Reading...Please place the card...")
        id, text = reader.read()
        print("ID: %s\nText: %s" % (id,text))

    read()

**どのように動作するか？**

.. code-block:: python

    from mfrc522 import SimpleMFRC522

    reader = SimpleMFRC522(spi_id=0,sck=2,miso=4,mosi=3,cs=5,rst=0)

``SimpleMFRC522()`` クラスをインスタンス化します。

.. code-block:: python

    id, text = reader.read()

この関数はカードデータを読み取るために使用されます。読み取りが成功すると、idとtextが返されます。

.. code-block:: python

    id, text = reader.write("text")

この関数は、カードに情報を書き込むために使用されます。 **Enter** キーを押して書き込みを完了します。
``text`` はカードに書き込む情報です。
