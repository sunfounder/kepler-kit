If Else
============= 

特定の条件が満たされた場合にのみコードを実行したいときに、判断（デシジョンメイキング）が必要です。

if
-------------------- 
.. code-block:: python

    if テスト式:
        ステートメント

この場合、プログラムは ``テスト式`` を評価し、 ``テスト式`` がTrueである場合にのみ ``ステートメント`` を実行します。

``テスト式`` がFalseの場合、 ``ステートメント`` は実行されません。

MicroPythonでは、インデントは ``if`` ステートメントの本体を意味します。本体はインデントで始まり、最初の非インデントされた行で終わります。

Pythonは非ゼロの値を「True」と解釈します。Noneと0は「False」と解釈されます。

**if文のフローチャート**

.. image:: img/if_statement.png

**例**

.. code-block:: python

    num = 8
    if num > 0:
        print(num, "は正の数です。")
    print("この行で終わり")

>>> %Run -c $EDITOR_CONTENT
8 は正の数です。
この行で終わり


if...else
----------------------- 

.. code-block:: python

    if テスト式:
        ifの本体
    else:
        elseの本体

``if..else`` ステートメントは ``テスト式`` を評価し、テスト条件が ``True`` の場合にのみ ``if`` の本体を実行します。

条件が ``False`` の場合、 ``else`` の本体が実行されます。インデントはブロックを区別するために使用されます。

**if...else文のフローチャート**

.. image:: img/if_else.png

**例**

.. code-block:: python

    num = -8
    if num > 0:
        print(num, "は正の数です。")
    else:
        print(num, "は負の数です。")

>>> %Run -c $EDITOR_CONTENT
-8 は負の数です。


if...elif...else
-------------------- 

.. code-block:: python

    if テスト式:
        ifの本体
    elif テスト式:
        elifの本体
    else: 
        elseの本体

``Elif`` は ``else if`` の省略形です。複数の式をチェックすることができます。

``if`` の条件がFalseの場合、次のelifブロックの条件がチェックされ、以降続きます。

すべての条件が ``False`` の場合、 ``else`` の本体が実行されます。

いくつかの ``if...elif...else`` ブロックのうち、条件に従って一つだけが実行されます。

``if`` ブロックは一つの ``else`` ブロックしか持つことができませんが、複数の ``elif`` ブロックを持つことができます。

**if...elif...else文のフローチャート**

.. image:: img/if_elif_else.png

**例**

.. code-block:: python

    x = 10
    y = 9

    if x > y:
        print("xはyより大きい")
    elif x == y:
        print("xとyは等しい")
    else:
        print("xはyより大きい")

>>> %Run -c $EDITOR_CONTENT
xはyより大きい


ネストしたif
--------------------- 

if文を別のif文に埋め込むことができ、それをネストしたif文と呼びます。

**例**

.. code-block:: python

    x = 67

    if x > 10:
        print("10より上で、")
        if x > 20:
            print("さらに20よりも上です！")
        else:
            print("しかし20より上ではありません。")

>>> %Run -c $EDITOR_CONTENT
10より上で、
さらに20よりも上です！
