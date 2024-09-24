.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _py_guess_number:

7.7 Guess Number
==============================


Guessing Numbers is a fun party game where you and your friends input numbers (0-99). With each input of the number, the range will shrink until a player answers the riddle correctly. Then the player is defeated and punished. 

As an example, if the lucky number is 51, which the players cannot see, and the player 1 inputs 50, the prompt changes to 50 - 99; if the player 2 inputs 70, the range changes to 50 - 70; if the player 3 inputs 51, the player is unlucky. In this case, numbers are inputted through the keypad, and outcomes are displayed on a LCD screen.

|guess_number|

**Required Components**

In this project, we need the following components. 

It's definitely convenient to buy a whole kit, here's the link: 

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name	
        - ITEMS IN THIS KIT
        - LINK
    *   - Kepler Kit	
        - 450+
        - |link_kepler_kit|

You can also buy them separately from the links below.


.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - COMPONENT	
        - QUANTITY
        - LINK

    *   - 1
        - :ref:`cpn_pico_w`
        - 1
        - |link_picow_buy|
    *   - 2
        - Micro USB Cable
        - 1
        - 
    *   - 3
        - :ref:`cpn_breadboard`
        - 1
        - |link_breadboard_buy|
    *   - 4
        - :ref:`cpn_wire`
        - Several
        - |link_wires_buy|
    *   - 5
        - :ref:`cpn_resistor`
        - 4(10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_keypad`
        - 1
        - |link_keypad_buy|
    *   - 7
        - :ref:`cpn_i2c_lcd`
        - 1
        - |link_i2clcd1602_buy|


**Schematic**


|sch_guess_number|

This circuit is based on :ref:`py_keypad` with the addition of an I2C LCD1602 to display the pressed keys.


**Wiring**

|wiring_game_guess_number| 

To make the wiring easier, in the above diagram, the column row of the matrix keyboard and the 10K resistors are inserted into the holes where G10 ~ G13 are located at the same time.


**Code**

.. note::

    * Open the ``7.7_game_guess_number.py`` file under the path of ``kepler-kit-main/micropython`` or copy this code into Thonny, then click "Run Current Script" or simply press F5 to run it.

    * Don't forget to click on the "MicroPython (Raspberry Pi Pico)" interpreter in the bottom right corner. 

    * For detailed tutorials, please refer to :ref:`open_run_code_py`.

.. code-block:: python

    from lcd1602 import LCD
    from machine import I2C, Pin
    import time
    import urandom

    # Initialize I2C communication for the LCD1602 display
    i2c = I2C(1, sda=Pin(6), scl=Pin(7), freq=400000)

    # Create an LCD object for controlling the LCD1602 display
    lcd = LCD(i2c)

    # Keypad character mapping for a 4x4 matrix keypad
    characters = [["1", "2", "3", "A"], 
                ["4", "5", "6", "B"], 
                ["7", "8", "9", "C"], 
                ["*", "0", "#", "D"]]

    # Define row pins for the keypad
    pin = [21, 20, 19, 18]
    row = []
    for i in range(4):
        row.append(None)
        row[i] = machine.Pin(pin[i], machine.Pin.OUT)  # Set row pins as output

    # Define column pins for the keypad
    pin = [13, 12, 11, 10]
    col = []
    for i in range(4):
        col.append(None)
        col[i] = machine.Pin(pin[i], machine.Pin.IN)  # Set column pins as input

    # Function to read a key from the keypad
    def readKey():
        key = []
        for i in range(4):
            row[i].high()  # Set the row pin high
            for j in range(4):
                if col[j].value() == 1:  # Check if any column is pressed
                    key.append(characters[i][j])  # Record the corresponding key
            row[i].low()  # Set the row pin low
        if key == []:
            return None  # Return None if no key is pressed
        else:
            return key  # Return the pressed key

    # Initialize and reset the game variables (random pointValue, upper/lower limits)
    def init_new_value():
        global pointValue, upper, count, lower
        pointValue = int(urandom.uniform(0, 99))  # Generate a random number between 0 and 99
        print(pointValue)  # Print the target number (for debugging)
        upper = 99  # Set initial upper bound
        lower = 0  # Set initial lower bound
        count = 0  # Reset the player's guess count
        return False  # Indicate that the game has not ended

    # Function to display the game information on the LCD
    # If the player has guessed correctly, show "GAME OVER"
    # Otherwise, show the current guess and range
    def lcd_show(result):
        lcd.clear()  # Clear the LCD display
        if result == True:  # If the player guessed correctly
            string = "GAME OVER!\n"
            string += "Point is " + str(pointValue)  # Display the correct number
        else:
            string = "Enter number: " + str(count) + "\n"  # Show the player's current guess
            string += str(lower) + " < Point < " + str(upper)  # Show the range of possible values
        lcd.message(string)  # Send the string to the LCD
        return

    # Process the player's guess and update the upper or lower bound
    # If the guess matches the pointValue, return True to indicate the game is over
    # Otherwise, update the bounds and return False
    def number_processing():
        global upper, count, lower
        if count > pointValue:
            if count < upper:
                upper = count  # Update the upper bound if the guess is too high
        elif count < pointValue:
            if count > lower:
                lower = count  # Update the lower bound if the guess is too low
        elif count == pointValue:
            return True  # Return True if the guess matches the pointValue
        count = 0  # Reset the guess count for the next attempt
        return False

    ## Main game setup and loop
    # Display a welcome message and prompt the user to press 'A' to start
    string = "Press A to Start!"
    lcd.message(string)
    result = init_new_value()  # Initialize game variables

    # Main loop to handle keypad input and update the display
    last_key = None
    while True:
        current_key = readKey()  # Read the current key pressed
        if current_key == last_key:
            continue  # Skip processing if the same key is still pressed
        last_key = current_key  # Update the last pressed key
        
        if current_key != None:
            # If 'A' is pressed, restart the game with a new target number
            if current_key == ["A"]:
                result = init_new_value()
            # If 'D' is pressed, check if the current guess is correct
            elif current_key == ["D"]:
                result = number_processing()
            # If a number is pressed and the count is less than 10 digits
            elif current_key[0] in list("1234567890") and count < 10:
                count = count * 10 + int(current_key[0])  # Add the digit to the current guess
            lcd_show(result)  # Update the LCD with the current game state
        time.sleep(0.1)  # Small delay for key debounce


* After the code runs, press ``A`` to start the game. A random number ``point`` is produced but not displayed on the LCD, and what you need to do is to guess it. 
* The number you have typed appears at the end of the first line till the final calculation is finished. (Press ``D`` to start the comparation.)
* The number range of ``point`` is displayed on the second line. And you must type the number within the range. 
* When you type a number, the range narrows; if you got the lucky number luckily or unluckily, there will appear ``GAME OVER!``.

.. note:: 
    If the code and wiring are fine, but the LCD still does not display content, you can turn the potentiometer on the back to increase the contrast.
