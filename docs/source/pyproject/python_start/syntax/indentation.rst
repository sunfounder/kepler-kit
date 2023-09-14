インデント
=============

インデントとは、コード行の先頭にあるスペースのことです。
標準的なPythonプログラムと同様に、MicroPythonプログラムも通常は上から下に実行されます：
それは一行ずつ解釈され、インタープリタで実行され、次の行に進むのです。
まるでシェルで一行ずつ入力するかのように。
ただし、命令リストを一行ずつ見ていくだけのプログラムはあまり賢くありません。そのため、MicroPythonもPythonと同様に、プログラムの実行順序を制御する独自の方法があります：それがインデントです。

print()の前には少なくとも1つのスペースを入れなければならず、そうでないと「Invalid syntax（無効な構文）」というエラーメッセージが表示されます。通常は、Tabキーを一様に押すことでスペースを標準化することが推奨されます。

.. code-block:: python

    if 8 > 5:
    print("Eight is greater than Five!")

>>> %Run -c $EDITOR_CONTENT
Traceback (most recent call last):
  File "<stdin>", line 2
SyntaxError: invalid syntax

同じブロックのコード内でスペースの数を揃えなければ、Pythonはエラーを出します。

.. code-block:: python

    if 8 > 5:
    print("Eight is greater than Five!")
            print("Eight is greater than Five")

>>> %Run -c $EDITOR_CONTENT
Traceback (most recent call last):
  File "<stdin>", line 2
SyntaxError: invalid syntax
