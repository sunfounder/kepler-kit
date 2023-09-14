.. _py_music_player:

7.8 RFID音楽プレーヤー
==========================

前回のプロジェクト、     で、MFRC522モジュールを使ってカード（またはキー）に最大48文字の情報を書き込むことができることを学びました。この情報には、キーとID情報の他にも、楽譜が含まれます。

例えば、 ``EEFGGFEDCCDEEDD EEFGGFEDCCDEDCC`` と書き込んだ場合、カード（またはキー）を再度読み取ったときにブザーが音楽を再生します。WS2812も装備することで、素晴らしいエフェクトを表示することもできます。

インターネットでさまざまな楽譜を見つけたり、自分自身で音楽を作曲して、それをカード（またはキー）に保存し、友達と共有することもできます！

|rfid_player|

**必要なコンポーネント**

このプロジェクトでは、以下のコンポーネントが必要です。

一式をまとめて購入するのが便利です。リンクはこちら：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前	
        - このキットに含まれるアイテム
        - リンク
    *   - Kepler Kit	
        - 450+
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
        - 複数
        - |link_wires_buy|
    *   - 5
        - :ref:`cpn_transistor`
        - 1(S8050)
        - |link_transistor_buy|
    *   - 6
        - :ref:`cpn_resistor`
        - 1(1KΩ)
        - |link_resistor_buy|
    *   - 7
        - パッシブ :ref:`cpn_buzzer`
        - 1
        - |link_passive_buzzer_buy|
    *   - 8
        - :ref:`cpn_mfrc522`
        - 1
        - |link_rfid_buy|
    *   - 9
        - :ref:`cpn_ws2812`
        - 1
        - |link_ws2812_buy|

**回路図**

|sch_music_player|

**配線図**

|wiring_rfid_music_player| 


**コード**

#. ``kepler-kit-main/micropython`` フォルダ内の ``6.5_rfid_write.py`` ファイルを開いて、「Run Current Script」をクリックするか、単にF5キーを押して実行します。

#. 実行後、シェルに ``EEFGGFEDCCDEEDD EEFGGFEDCCDEDCC`` と入力し、カード（またはキー）をMFRC522モジュールに近づけます。これで、歓喜の歌の楽譜が保存されます。

#. ``kepler-kit-main/micropython`` フォルダ内の ``7.8_rfid_music_player.py`` ファイルを開くか、このコードをThonnyにコピーして、「Run Current Script」をクリックするか、単にF5キーを押して実行します。

    .. code-block:: python

        from mfrc522 import SimpleMFRC522
        import machine
        import time
        from ws2812 import WS2812
        import urandom

        # ws2812
        ws = WS2812(machine.Pin(16), 8)

        # mfrc522
        reader = SimpleMFRC522(spi_id=0, sck=2, miso=4, mosi=3, cs=5, rst=0)

        # ブザー
        NOTE_C4 = 262
        NOTE_D4 = 294
        NOTE_E4 = 330
        NOTE_F4 = 349
        NOTE_G4 = 392
        NOTE_A4 = 440
        NOTE_B4 = 494
        NOTE_C5 = 523

        buzzer = machine.PWM(machine.Pin(15))
        note = [NOTE_C4, NOTE_D4, NOTE_E4, NOTE_F4, NOTE_G4, NOTE_A4, NOTE_B4, NOTE_C5]

        def tone(pin, frequency, duration):
            pin.freq(frequency)
            pin.duty_u16(30000)
            time.sleep_ms(duration)
            pin.duty_u16(0)

        # 明るくする
        def lumi(index):
            for i in range(8):
                ws[i] = 0x0000FF
            ws[index] = 0xFF0000  # int(urandom.uniform(0, 0xFFFFFF))
            ws.write()

        # テキストをインデックスにエンコード
        words = ["C", "D", "E", "F", "G", "A", "B", "N"]
        def take_text(text):
            string = text.replace(' ', '').upper()
            while len(string) > 0:
                index = words.index(string[0])
                tone(buzzer, note[index], 250)
                lumi(index)
                new_str = ""
                for i in range(0, len(string)):
                    if i != 0:
                        new_str = new_str + string[i]
                string = new_str

        # カードを読む
        def read():
            print("Reading...Please place the card...")
            id, text = reader.read()
            print("ID: %s\nText: %s" % (id,text))
            take_text(text)

        read()

#. カード（またはキー）を再度MFRC522モジュールに近づけると、ブザーがカード（またはキー）に保存された音楽を再生し、RGBストリップがランダムな色で点灯します。
