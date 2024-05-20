.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

データ型
===========

組み込みデータ型
---------------------
MicroPythonには次のようなデータ型があります：

* テキスト型: str
* 数値型: int, float, complex
* シーケンス型: list, tuple, range
* マッピング型: dict
* セット型: set, frozenset
* ブーリアン型: bool
* バイナリ型: bytes, bytearray, memoryview

データ型の取得
-----------------------------
``type()`` 関数を使用することで、任意のオブジェクトのデータ型を取得できます。



.. code-block:: python

    a = 6.8
    print(type(a))

>>> %Run -c $EDITOR_CONTENT
<class 'float'>

データ型の設定
----------------------
MicroPythonでは、変数に値を割り当てる際にデータ型が自動的に決定されるため、特に設定する必要はありません。



.. code-block:: python

    x = "welcome"
    y = 45
    z = ["apple", "banana", "cherry"]

    print(type(x))
    print(type(y))
    print(type(z))

>>> %Run -c $EDITOR_CONTENT
<class 'str'>
<class 'int'>
<class 'list'>
>>> 

特定のデータ型の設定
----------------------------------

データ型を明示的に指定したい場合は、以下のコンストラクタ関数を使用できます。

.. list-table:: 
    :widths: 25 10
    :header-rows: 1

    *   - 例
        - データ型
    *   - x = int(20)
        - int
    *   - x = float(20.5)
        - float
    *   - x = complex(1j)
        - complex
    *   - x = str("Hello World")
        - str
    *   - x = list(("apple", "banana", "cherry"))
        - list
    *   - x = tuple(("apple", "banana", "cherry"))
        - tuple
    *   - x = range(6)
        - range
    *   - x = dict(name="John", age=36)
        - dict
    *   - x = set(("apple", "banana", "cherry"))
        - set
    *   - x = frozenset(("apple", "banana", "cherry"))
        - frozenset
    *   - x = bool(5)
        - bool
    *   - x = bytes(5)
        - bytes
    *   - x = bytearray(5)
        - bytearray
    *   - x = memoryview(bytes(5))
        - memoryview

結果を確認するために、いくつかを出力してみましょう。



.. code-block:: python

    a = float(20.5)
    b = list(("apple", "banana", "cherry"))
    c = bool(5)

    print(a)
    print(b)
    print(c)

>>> %Run -c $EDITOR_CONTENT
20.5
['apple', 'banana', 'cherry']
True
>>> 

型変換
----------------
int(), float(), complex()メソッドを使用して、一つの型から別の型に変換できます。
Pythonにおけるキャスティングは、コンストラクタ関数を使用して行われます：

* int() - 整数リテラル、浮動小数点リテラル（小数部分をすべて削除）、文字列リテラル（文字列が整数を表している場合）から整数を生成
* float() - 整数リテラル、浮動小数点リテラル、または文字列リテラル（文字列が浮動小数点数または整数を表す場合）から浮動小数点数を生成
* str() - 文字列、整数リテラル、浮動小数点リテラルを含む多様なデータ型から文字列を生成



.. code-block:: python

    a = float("5")
    b = int(3.7)
    c = str(6.0)

    print(a)
    print(b)
    print(c)

注：複素数を別の数値型に変換することはできません。
