.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

関数
==============

MicroPythonにおいて、関数（function）は特定のタスクを実行するための関連するステートメント（命令）のグループです。

関数はプログラムをより小さなモジュラーなブロックに分割するのに役立ちます。プランが大きくなるにつれて、関数はそれをより整理されたものにし、管理しやすくします。

さらに、コードの重複を避け、再利用可能にします。

関数の作成
------------------

.. code-block::

    def function_name(parameters): 
        """docstring"""
        statement(s)

* 関数は ``def`` キーワードを使用して定義されます。

* 関数名は、関数を一意に識別するためのものです。関数名の命名規則は変数のそれと同じで、以下のルールに従います。
    
   * 数字、文字、アンダースコアのみを含めることができます。
   * 最初の文字は文字またはアンダースコアでなければなりません。
   * 大文字と小文字は区別されます。

* パラメータ（arguments）は、関数に値を渡すためのものです。これはオプションです。

* コロン（:）は、関数ヘッダの終わりを示します。

* オプションのdocstring（ドキュメント文字列）は、関数の機能を説明するために使用されます。通常は三重引用符を使用して、docstringを複数行に拡張できるようにします。

* 関数の本体を構成する一つ以上の有効なMicroPythonのステートメント。ステートメントは同じインデントレベル（通常は4つのスペース）を持つ必要があります。

* 各関数には少なくとも一つのステートメントが必要ですが、何らかの理由でステートメントを含まない関数がある場合は、エラーを避けるためにpass文を入れてください。

* 関数から値を返すためのオプションの ``return`` ステートメント。


関数の呼び出し
-------------------

関数を呼び出すには、関数名の後に括弧を追加します。



.. code-block:: python

    def my_function():
        print("Your first function")

    my_function()

>>> %Run -c $EDITOR_CONTENT
Your first function

return ステートメント
-----------------------

return ステートメントは、関数を終了し、それが呼び出された場所に戻るために使用されます。

**return の構文**

.. code-block:: python

    return [expression_list]

このステートメントには、評価されて値が返される式を含めることができます。ステートメントに式がない場合、または ``return`` ステートメント自体が関数に存在しない場合、関数は ``None`` オブジェクトを返します。



.. code-block:: python

    def my_function():
            print("Your first function")

    print(my_function())

>>> %Run -c $EDITOR_CONTENT
Your first function
None

ここでは、 ``None`` が返り値です。これは、 ``return`` ステートメントが使用されていないからです。

引数
-------------

情報は引数として関数に渡すことができます。

引数は、関数名の後の括弧内で指定します。必要な数だけ引数を追加でき、それらをコンマで区切ります。



.. code-block:: python

    def welcome(name, msg):
        """This is a welcome function for
        the person with the provided message"""
        print("Hello", name + ', ' + msg)

    welcome("Lily", "Welcome to China!")

>>> %Run -c $EDITOR_CONTENT
Hello Lily, Welcome to China!


引数の数
*************************

デフォルトでは、関数は正確な数の引数で呼び出される必要があります。つまり、関数が2つのパラメータを期待している場合、関数は2つの引数で呼び出さなければならず、それ以上でもそれ以下でもありません。



.. code-block:: python

    def welcome(name, msg):
        """This is a welcome function for
        the person with the provided message"""
        print("Hello", name + ', ' + msg)

    welcome("Lily", "Welcome to China!")

ここでは、welcome()関数には2つのパラメータがあります。

この関数を二つの引数で呼び出しているので、関数はスムーズに動作し、エラーは発生しません。

異なる数の引数で呼び出された場合、インタープリタはエラーメッセージを表示します。

以下は、この関数への呼び出しで、一つとゼロの引数を含んでいる場合と、それぞれのエラーメッセージです。

.. code-block::

    welcome("Lily")＃引数が一つだけ

>>> %Run -c $EDITOR_CONTENT
Traceback (most recent call last):
  File "<stdin>", line 6, in <module>
TypeError: function takes 2 positional arguments but 1 were given

.. code-block::

    welcome()＃引数がない

>>> %Run -c $EDITOR_CONTENT
Traceback (most recent call last):
  File "<stdin>", line 6, in <module>
TypeError: function takes 2 positional arguments but 0 were given


デフォルト引数
*************************

MicroPythonでは、パラメータにデフォルト値を設定するために代入演算子（=）を使用できます。

引数なしで関数を呼び出した場合、デフォルト値が使用されます。



.. code-block:: python

    def welcome(name, msg = "Welcome to China!"):
        """This is a welcome function for
        the person with the provided message"""
        print("Hello", name + ', ' + msg)
    welcome("Lily")

>>> %Run -c $EDITOR_CONTENT
Hello Lily, Welcome to China!

この関数では、パラメータ ``name`` にはデフォルト値が設定されておらず、呼び出し時に必須（必須）です。

一方で、パラメータ ``msg`` のデフォルト値は "Welcome to China!" です。したがって、呼び出し時にはオプションです。値が提供された場合、デフォルト値は上書きされます。

関数内の任意の数の引数にデフォルト値を設定できます。ただし、一度デフォルト引数が設定されると、その右側のすべての引数にもデフォルト値が必要です。

これは、デフォルト引数に続く非デフォルト引数は許可されていないことを意味します。

例えば、上記の関数ヘッダを以下のように定義した場合：

.. code-block:: python

    def welcome(name = "Lily", msg):

次のエラーメッセージが表示されます：

>>> %Run -c $EDITOR_CONTENT
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
SyntaxError: non-default argument follows default argument


キーワード引数
**************************

関数を特定の値で呼び出した場合、これらの値は位置に基づいて引数に割り当てられます。

例えば、上記の関数 welcome() で、それを welcome("Lily", "Welcome to China") として呼び出した場合、値 "Lily" は ``name`` に、同様に "Welcome to China" はパラメータ ``msg`` に割り当てられます。

MicroPythonでは、キーワード引数を使用して関数を呼び出すことができます。この方法で関数を呼び出すと、引数の順序（位置）を変更できます。

.. code-block:: python

    # keyword arguments
    welcome(name = "Lily",msg = "Welcome to China!")

    # keyword arguments (out of order)
    welcome(msg = "Welcome to China！",name = "Lily") 

    #1 positional, 1 keyword argument
    welcome("Lily", msg = "Welcome to China!")

ここでわかるように、関数呼び出し時に位置引数とキーワード引数を混在させることができます。ただし、キーワード引数は位置引数の後に来る必要があります。

キーワード引数の後に位置引数があるとエラーが発生します。

例えば、関数の呼び出しが以下のような場合：

.. code-block:: python

    welcome(name="Lily","Welcome to China!")

次のエラーが発生します：

>>> %Run -c $EDITOR_CONTENT
Traceback (most recent call last):
  File "<stdin>", line 5, in <module>
SyntaxError: non-keyword arg after keyword arg


任意の引数
********************

事前に関数に渡される引数の数を知らない場合があります。

関数定義で、パラメータ名の前にアスタリスク（*）を追加できます。



.. code-block:: python

    def welcome(*names):
        """This function welcomes all the person
        in the name tuple"""
        #names is a tuple with arguments
        for name in names:
            print("Welcome to China!", name)
            
    welcome("Lily","John","Wendy")

>>> %Run -c $EDITOR_CONTENT
Welcome to China! Lily
Welcome to China! John
Welcome to China! Wendy

ここでは、関数を複数の引数で呼び出しています。これらの引数は、関数に渡される前にタプルにパックされます。

関数内部で、すべての引数を取得するためにforループを使用しています。


再帰
----------------
Pythonでは、関数が他の関数を呼び出すことができることはよく知られています。さらに、関数が自分自身を呼び出すことも可能です。このような構造を再帰関数と呼びます。

この特性の利点は、データをループ処理して結果に到達できることです。

開発者は再帰に非常に慎重である必要があります。無限ループに陥ったり、過度なメモリやプロセッサのリソースを消費する関数を書いてしまう可能性があります。しかし、正確に書かれた再帰は、非常に効率的で数学的に優雅なプログラミング手法となることもあります。



.. code-block:: python

    def rec_func(i):
        if(i > 0):
            result = i + rec_func(i - 1)
            print(result)
        else:
            result = 0
        return result

    rec_func(6)

>>> %Run -c $EDITOR_CONTENT
1
3
6
10
15
21

この例では、rec_func()は自分自身を呼び出す（「再帰」）関数として定義しています。 ``i`` 変数をデータとして使用し、再帰するたびにデクリメント（-1）します。条件が0より大きくない場合（つまり、0の場合）、再帰は終了します。

新しい開発者にとっては、その動作を理解するのに時間がかかることがあります。最良のテスト方法は、テストして修正することです。

**再帰の利点**

* 再帰関数はコードをクリーンでエレガントに見せます。
* 再帰を使用すると、複雑なタスクをより単純なサブプロブレムに分解できます。
* ネストされた反復を使用するよりも、再帰を使用した方がシーケンス生成が容易です。

**再帰の欠点**

* 再帰の背後にあるロジックは、理解が難しい場合があります。
* 再帰呼び出しはメモリと時間を大量に消費するため、効率が悪いです。
* 再帰関数はデバッグが困難です。

