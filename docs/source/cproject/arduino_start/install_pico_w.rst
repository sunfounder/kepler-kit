.. _setup_pico_arduino:

1.3 Raspberry Pi Pico Wのセットアップ（重要）
==================================================

1. UF2ファームウェアのインストール
-------------------------------------

Raspberry Pi Pico Wを初めて接続する際、またはBOOTSELボタンを押しながら挿入すると、COMポートが割り当てられずにドライブとして認識されます。これではコードのアップロードができません。

この問題を解決するには、UF2ファームウェアをインストールする必要があります。このファームウェアはMicroPythonをサポートしており、Arduino IDEとも互換性があります。

1. 以下のリンクからUF2ファームウェアをダウンロードしてください。

    * :download:`Raspberry Pi Pico W UF2ファームウェア <https://micropython.org/download/rp2-pico-w/rp2-pico-w-latest.uf2>`

2. Micro USBケーブルを使用して、Raspberry Pi Pico Wをコンピュータに接続します。Pico Wは **RPI-RP2** という名前の大容量ストレージデバイスとしてマウントされます。

    .. image:: img/install_pico_plugin.png

3. ダウンロードしたUF2ファームウェアを **RPI-RP2** ドライブにドラッグアンドドロップします。

    .. image:: img/install_pico_uf2.png

4. これにより、 **RPI-RP2** ドライブは消失し、次のステップに進むことができます。


2. ボードパッケージのインストール
--------------------------------------

Raspberry Pi Pico Wをプログラムするには、Arduino IDEに対応するパッケージをインストールする必要があります。手順は以下の通りです：

1. **ボードマネージャー** ウィンドウで **pico** と検索し、 **インストール** ボタンをクリックしてインストールを開始します。これにより、Raspberry Pi Pico Wをサポートする **Arduino Mbed OS RP2040 Boards** パッケージがインストールされます。

    .. image:: img/install_pico.png

2. インストール過程で、特定のデバイスドライバーのインストールに関するポップアップが数回表示されます。 **「インストール」** を選択してください。

    .. image:: img/install_pico_sa.png

3. インストールが完了したという通知が表示されます。

3. ボードとポートの選択
------------------------------------------

1. 適切なボードを選ぶには、 **ツール** -> **ボード** -> **Arduino Mbed OS RP2040 Boards** -> **Raspberry Pi Pico** に移動します。

    .. image:: img/install_pico_tool_board.png

2. Raspberry Pi Pico Wがコンピュータに接続されている場合、 **ツール** -> **ポート** で正しいポートを設定します。

    .. image:: img/install_pico_tool_port.png

3. Arduino 2.0は新しいクイックセレクト機能を提供しています。Raspberry Pi Pico Wは通常自動認識されないため、 **その他のボードとポートを選択** をクリックします。

    .. image:: img/install_pico_select.png

4. 検索バーに **Raspberry Pi Pico** と入力し、表示されたら選択し、適切なポートを選んで **OK** をクリックします。

    .. image:: img/install_pico_board.png

5. このクイックアクセスウィンドウを通じて、後で簡単に再選択できます。

    .. image:: img/install_pico_quick.png

6. これらの手法のいずれかで、正確なボードとポートが設定されます。これでRaspberry Pi Pico Wにコードをアップロードする準備が整いました。

4. コードのアップロード
--------------------------

次に、Raspberry Pi Pico Wにコードをアップロードする方法について説明します。

1. 任意の ``.ino`` ファイルを開くか、現在表示されている空のスケッチを使用します。その後、 **アップロード** ボタンをクリックします。

    .. image:: img/install_pico_upload.png

2. アップロード中のメッセージが表示されるのを待ちます。

    .. image:: img/install_pico_upload_dot.png

3. **BOOTSEL** ボタンを押しながら、Raspberry Pi Pico Wの接続を素早く外し、再接続します。

    .. image:: img/led_onboard.png 

    .. note::
        
        * このステップは、特にArduino IDEを初めて使用するユーザーにとって重要です。このステップをスキップすると、アップロードに失敗します。

        * この回のコードアップロードが成功した場合、Pico Wはコンピュータに認識されます。次回以降は、単純にコンピュータに接続するだけで良いです。

4. アップロード成功のプロンプトが表示されます。

    .. image:: img/install_pico_upload_done.png
