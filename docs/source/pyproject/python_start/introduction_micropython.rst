1.1 MicroPythonの紹介
======================================

MicroPythonは、C言語で書かれた、Python 3とほぼ互換性のあるプログラミング言語のソフトウェア実装です。これは、マイクロコントローラ上で動作するように最適化されています。

MicroPythonは、Pythonのバイトコードへのコンパイラと、そのバイトコードのランタイムインタプリターで構成されています。ユーザーには、対話型のプロンプト（REPL）が提供され、サポートされているコマンドを即座に実行できます。コアPythonライブラリの一部が含まれており、MicroPythonには、プログラマーが低レベルハードウェアにアクセスできるモジュールも含まれています。

* 参照： `MicroPython - Wikipedia <https://ja.wikipedia.org/wiki/MicroPython>`_

物語はここから始まります
--------------------------------

2013年、ダミアン・ジョージがクラウドファンディング（Kickstarter）を立ち上げたことで、状況が変わりました。

ダミアンはケンブリッジ大学の学部生で、ロボティクスプログラミングに熱心でした。彼はPythonの世界をギガバイトマシンからキロバイトへと縮小したいと考えていました。Kickstarterキャンペーンは、彼が概念実証を完成した実装に変えるための開発をサポートするものでした。

MicroPythonは、プロジェクトの成功に熱心な多様なPythonistaコミュニティによってサポートされています。

開発者たちは、コードベースのテストとサポートだけでなく、チュートリアル、コードライブラリ、ハードウェアのポーティングも提供しているため、ダミアンはプロジェクトの他の側面に集中することができました。

* 参照： `realpython <https://realpython.com/micropython/>`_

なぜMicroPythonなのか？
--------------------------

オリジナルのKickstarterキャンペーンでは、MicroPythonはSTM32F4を搭載した開発ボード「pyboard」としてリリースされましたが、多くのARMベースの製品アーキテクチャをサポートしています。主にサポートされているポートには、ARM Cortex-M（多くのSTM32ボード、TI CC3200/WiPy、Teensyボード、Nordic nRFシリーズ、SAMD21およびSAMD51）、ESP8266、ESP32、16ビットPIC、Unix、Windows、Zephyr、JavaScriptがあります。
また、MicroPythonは高速なフィードバックを可能にします。これは、REPLを使用して対話的にコマンドを入力し、レスポンスを得ることができるためです。コードを微調整してすぐに実行することもできます。これにより、コード-コンパイル-アップロード-実行のサイクルを経なくても済みます。

Pythonにも同様の利点がありますが、Raspberry Pi Picoのような一部のマイクロコントローラボードは、小さくて単純で、Python言語を全体的に実行するためのメモリが非常に少ないです。それが、MicroPythonが主要なPythonの機能を維持しつつ、これらのマイクロコントローラボードで動作する新しい機能を多数追加して進化した理由です。

次に、Raspberry Pi PicoにMicroPythonをインストールする方法を学びます。

* 参照： `MicroPython - Wikipedia <https://ja.wikipedia.org/wiki/MicroPython>`_
* 参照： `realpython <https://realpython.com/micropython/>`_

