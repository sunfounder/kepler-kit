
# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import sphinx_rtd_theme
import time

# -- Project information -----------------------------------------------------

project = 'SunFounder Kepler Kit for Raspberry Pi Pico W'
copyright = f'{time.localtime().tm_year}, SunFounder'
author = 'www.sunfounder.com'


# The full version, including alpha/beta/rc tags
release = '1.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

extensions = [
    'sphinx.ext.autosectionlabel',
    'sphinx_copybutton'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_js_files = [
    'https://ezblock.cc/readDocFile/custom.js',
    './lang.js',
]
html_css_files = [
    'https://ezblock.cc/readDocFile/custom.css',
]


# new
rst_epilog = """
.. |img_take_color| image:: /img/edit_colors.png
.. |img_keypad_pressed| image:: /img/keypad_pressed.png
"""

# component pic
rst_epilog += """

.. |compoents_list| image:: /img/component/compoents_list.jpg
    :width: 800
.. |img_wire| image:: /img/component/wire.png
.. |img_buzzer| image:: /img/component/buzzer.png
    :width: 600
.. |img_rgb_pin| image:: /img/component/rgb_pin.jpg
    :width: 200
.. |img_buzzer_symbol| image:: /img/component/buzzer_symbol.png
.. |img_7seg| image:: /img/component/7_segment.png
    :width: 300
.. |img_7seg_cathode| image:: /img/component/segment_cathode.png
    :width: 400
.. |img_1_segment| image:: /img/component/1_segment.png
    :width: 200    
.. |img_74hc595| image:: /img/component/74HC595.png
.. |img_74jc595_1| image:: /img/component/74hc595_1.png
.. |img_74jc595_pin| image:: /img/component/74hc595_pin.png
.. |img_bb| image:: /img/component/breadboard.png
.. |img_bbi| image:: /img/component/breadboard_internal.png
.. |img_button| image:: /img/component/button.png
.. |img_button_symbol| image:: /img/component/button_symbol.png
.. |img_button2| image:: /img/component/button2.jpg
.. |img_4-digit-sche| image:: /img/component/4-digit-sche.png
.. |img_4-digit-sche-ca| image:: /img/component/4-digit-sche-ca.png

.. |img_led_matrix| image:: /img/component/led_matrix.png
    :width: 300
.. |img_788bs_i| image:: /img/component/image84.png
.. |img_788bs_sche| image:: /img/component/image85.png
.. |img_capacitor| image:: /img/component/capacitor.png
    :width: 100
.. |img_103_capacitor| image:: /img/component/103_capacitor.png
.. |img_dc_motor| image:: /img/component/motor.png
    :width: 600
.. |img_dc_motor_sche| image:: /img/component/motor_sche.png
.. |img_max7219| image:: /img/component/max7219_sche.png
.. |img_encoder| image:: /img/component/encoder205.jpeg
.. |img_encoder_timing| image:: /img/component/encoder206.png
.. |img_Hum-sch| image:: /img/component/Hum-sch.png
.. |img_Dht11| image:: /img/component/Dht11.png
.. |img_joystick_pic| image:: /img/component/joystick_pic.png
    :width: 600
.. |img_joystick| image:: /img/component/joystick318.png
.. |img_keypad| image:: /img/component/keypad314.png
.. |img_l293d0| image:: /img/component/l293d.png
    :width: 400
.. |img_l293d1| image:: /img/component/l293d111.png
.. |img_l293d2| image:: /img/component/l293d334.png
.. |img_mpr121| image:: /img/component/mpr121.png
    :width: 400
.. |img_mpu6050| image:: /img/component/mpu6050.png   
.. |img_mpu6050_a| image:: /img/component/mpu223.png
.. |img_mpu6050_a2| image:: /img/component/mpu224.png
.. |img_mpu6050_g| image:: /img/component/mpu225.png

.. |img_reed| image:: /img/component/reed.png
.. |img_reed_sche| image:: /img/component/reed_sche.png

.. |img_relay_sche| image:: /img/component/relay142.jpeg
.. |img_relay| image:: /img/component/relay12.png
    :width: 200
.. |ultrasonic_pic| image:: /img/component/ultrasonic_pic.png
    :width: 200
.. |ultrasonic_prin| image:: /img/component/ultrasonic_prin.jpg
    :width: 800
.. |img_i2c_lcd| image:: /img/component/i2c_lcd1602.png
.. |img_led| image:: /img/component/LED.png
    :width: 500
.. |img_led_symbol| image:: /img/component/led_symbol.png
.. |img_photoresistor| image:: /img/component/photoresistor.png
    :width: 100
.. |img_photoresistor_symbol| image:: /img/component/photoresistor_symbol.png
    :width: 200
.. |img_pir| image:: /img/component/pir.png
    :width: 300
.. |img_PIR_working_principle| image:: /img/component/PIR_working_principle.jpg
.. |img_pir_back| image:: /img/component/pir_back.png
.. |img_pot| image:: /img/component/potentiometer.png
    :width: 200
.. |img_pot_symbol| image:: /img/component/potentiometer_symbol.png
.. |img_res| image:: /img/component/resistor.png
    :width: 300
.. |img_res_symbol| image:: /img/component/resistor_symbol.png
.. |img_res_card| image:: /img/component/resistance_card.jpg
.. |img_220ohm| image:: /img/component/220ohm.jpg
    :width: 600
.. |img_rgb| image:: /img/component/rgb_led.png
    :width: 100
.. |img_rgb_light| image:: /img/component/rgb_light.png
.. |img_rgb_symbol| image:: /img/component/rgb_symbol.png
    :width: 300
.. |img_servo| image:: /img/component/servo.png
.. |img_servo_i| image:: /img/component/servo_internal.png
.. |img_servo_duty| image:: /img/component/servo_duty.png
.. |img_slide| image:: /img/component/slide_switch.png
.. |img_slide_prin| image:: /img/component/slide_principle.png
.. |img_slide_symbol| image:: /img/component/slide_symbol.png
.. |img_thermistor| image:: /img/component/thermistor.png
    :width: 100
.. |img_thermistor_symbol| image:: /img/component/thermistor_symbol.png
    :width: 600
.. |img_tilt| image:: /img/component/tilt_switch.png
    :width: 100
.. |img_tilt_symbol| image:: /img/component/tilt_symbol.png
.. |img_NPN&PNP| image:: /img/component/NPN&PNP.png
    :width: 300
.. |img_ebc| image:: /img/component/ebc.png
.. |img_transistor_symbol| image:: /img/component/transistor_symbol.png
.. |img_ws2812| image:: /img/component/ws2812b.png
.. |img_mfrc522| image:: /img/component/mfrc522.png
.. |img_power_module| image:: /img/component/power_module.png
.. |img_micro_switch| image:: /img/component/micro_pic.png
    :width: 200
.. |img_micro_switch1| image:: /img/component/micro_switch1.png
.. |img_micro_switch2| image:: /img/component/micro_switch2.png

.. |img_led_bar_pin| image:: /img/component/led_bar_pin.png
.. |img_led_bar_sche1| image:: /img/component/led_bar_sche1.png
    :width: 800

.. |img_led_bar| image:: /img/component/bar_graph.png
    :width: 300
.. |img_irrecv| image:: /img/component/infrared-receiver_01.jpg

.. |img_controller| image:: /img/component/image186.jpeg
    :width: 600
.. |img_pump| image:: /img/component/pump.png
    :width: 300
.. |img_water_sensor| image:: /img/component/water_sensor.png
    :width: 600
.. |img_diode| image:: /img/component/Diodes-symbol.png
.. |img_PIR_TTE| image:: /img/component/PIR_TTE.png
    :width: 400
.. |img_ta6586| image:: /img/component/ta6586.png    
.. |img_ta6586_pin| image:: /img/component/ta6586_pin.png  
.. |img_ta6586_priciple| image:: /img/component/ta6586_priciple.png  

.. |sch_lipo_charger| image:: /img/component/sch_lipo_charger.png 
    :width: 800
    
.. |lipo_module| image:: /img/component/lipo_module.png 

.. |lipo_wire| image:: /img/component/lipo_wire.png 

.. |i2c_lcd1602| image:: /img/component/i2c_lcd1602.png 

.. |i2c_address| image:: /img/component/i2c_address.jpg 

.. |back_lcd1602| image:: /img/component/back_lcd1602.jpg 



"""






# wiring pic
rst_epilog += """
.. |wiring_74hc_7seg| image:: /img/wiring/wiring_led_segment_display.png
    :width: 800
.. |wiring_74hc_led| image:: /img/wiring/wiring_microchip_74hc595.png
    :width: 800
.. |wiring_buzzer| image:: /img/wiring/wiring_custom_tone.png
    :width: 800
.. |wiring_beep| image:: /img/wiring/wiring_beep.png
    :width: 800    
.. |wiring_button| image:: /img/wiring/wiring_read_button_value.png
    :width: 600
.. |wiring_button_pullup| image:: /img/wiring/wiring_read_button_value_2.png
.. |wiring_tilt| image:: /img/wiring/wiring_read_button_value_4.png
.. |wiring_slide| image:: /img/wiring/wiring_read_button_value_3.png   
.. |wiring_limit_sw| image:: /img/wiring/wiring_read_button_value_5.png 
.. |wiring_led| image:: /img/wiring/wiring_led.png   
    :width: 800
.. |wiring_lcd| image:: /img/wiring/wiring_lcd.png
    :width: 800
.. |wiring_lcd_ar| image:: /img/wiring/wiring_lcd_ar.png
    :width: 800
.. |wiring_ws2812| image:: /img/wiring/wiring_rgb_strip.png
    :width: 800
.. |wiring_pot| image:: /img/wiring/wiring_turn_the_knob.png
.. |wiring_rgb| image:: /img/wiring/wiring_colorful_light.png
.. |wiring_servo| image:: /img/wiring/wiring_swing_servo.png
.. |wiring_temp| image:: /img/wiring/wiring_thermometer.png
.. |wiring_ultrasonic| image:: /img/wiring/wiring_ultrasonic.png
.. |wiring_4dig| image:: /img/wiring/wiring_4dig.png
    :width: 800
.. |wiring_keypad| image:: /img/wiring/wiring_keypad.png
.. |wiring_keypad_ar| image:: /img/wiring/wiring_keypad_ar.png
.. |wiring_joystick| image:: /img/wiring/wiring_joystick.png
.. |wiring_motor| image:: /img/wiring/wiring_motor.png
    :width: 800
.. |wiring_water| image:: /img/wiring/wiring_water.png
.. |wiring_photoresistor| image:: /img/wiring/wiring_photoresistor.png
.. |wiring_pir| image:: /img/wiring/wiring_pir.png
.. |wiring_ledbar| image:: /img/wiring/wiring_ledbar.png
    :width: 800
.. |wiring_reed| image:: /img/wiring/wiring_reed.png
.. |wiring_mpr121| image:: /img/wiring/wiring_mpr121.png
.. |wiring_mpr121_ar| image:: /img/wiring/wiring_mpr121_ar.png
.. |wiring_mpu6050| image:: /img/wiring/wiring_mpu6050.png
.. |wiring_mpu6050_ar| image:: /img/wiring/wiring_mpu6050_ar.png
.. |wiring_rfid| image:: /img/wiring/wiring_rfid.png
.. |wiring_dht11| image:: /img/wiring/wiring_dht11.png
.. |wiring_ledmatrix_1| image:: /img/wiring/wiring_matrix_1.png
    :width: 800
.. |wiring_ledmatrix_2| image:: /img/wiring/wiring_matrix_2.png
    :width: 800
.. |wiring_ledmatrix_3| image:: /img/wiring/wiring_matrix_3.png
    :width: 800
.. |wiring_ledmatrix_4| image:: /img/wiring/wiring_matrix_4.png
    :width: 800
.. |wiring_irrecv| image:: /img/wiring/wiring_irrecv.png
.. |wiring_pump| image:: /img/wiring/wiring_pump.png
.. |wiring_s8050| image:: /img/wiring/wiring_transistor_s8050.png
.. |wiring_s8550| image:: /img/wiring/wiring_transistor_s8550.png
.. |wiring_relay_1| image:: /img/wiring/wiring_relay_1.png
.. |wiring_relay_2| image:: /img/wiring/wiring_relay_2.png
    :width: 800
.. |wiring_light_theremin| image:: /img/wiring/wiring_light_theremin.png
.. |wiring_room_temp|  image:: /img/wiring/wiring_room_temp.png
.. |wiring_alarm_siren_lamp| image:: /img/wiring/wiring_alarm_siren_lamp.png
.. |wiring_digital_bubble_level|  image:: /img/wiring/wiring_digital_bubble_level.png
    :width: 800
.. |wiring_fruit_piano|  image:: /img/wiring/wiring_fruit_piano.png
    :width: 800
.. |wiring_game_10_second|  image:: /img/wiring/wiring_game_10_second.png
    :width: 800
.. |wiring_game_guess_number|  image:: /img/wiring/wiring_game_guess_number.png
    :width: 800
.. |wiring_somatosensory_controller|  image:: /img/wiring/wiring_motion_control.png
.. |wiring_passager_counter|  image:: /img/wiring/wiring_passager_counter.png
.. |wiring_reversing_aid|  image:: /img/wiring/wiring_reversing_aid.png
.. |wiring_rfid_music_player|  image:: /img/wiring/wiring_rfid_music_player.png
    :width: 800
.. |wiring_traffic_light|  image:: /img/wiring/wiring_traffic_light.png
    :width: 800
.. |wiring_run_reset|  image:: /img/wiring/wiring_run_reset.png



"""


# schematic pic
rst_epilog += """
.. |sch_74hc_7seg| image:: /img/schematic/sch_number_display.png
    :width: 800
.. |sch_74hc_led| image:: /img/schematic/sch_microchip_74hc595.png
.. |sch_buzzer| image:: /img/schematic/sch_custom_tone.png
.. |sch_button| image:: /img/schematic/sch_reading_button_value.png
.. |sch_button_pullup| image:: /img/schematic/sch_reading_button_value2.png
.. |sch_tilt| image:: /img/schematic/sch_reading_button_value3.png
.. |sch_slide| image:: /img/schematic/sch_reading_button_value4.png   
.. |sch_limit_sw| image:: /img/schematic/sch_reading_button_value5.png 
.. |sch_led| image:: /img/schematic/sch_hello_led.png   
.. |sch_lcd| image:: /img/schematic/sch_lcd.png
.. |sch_lcd_ar| image:: /img/schematic/sch_lcd_ar.png
.. |sch_ws2812| image:: /img/schematic/sch_rgb_led_strip.png
.. |sch_pot| image:: /img/schematic/sch_turn_the_knob.png
.. |sch_rgb| image:: /img/schematic/sch_colorful_light.png
.. |sch_servo| image:: /img/schematic/sch_swinging_servo.png
.. |sch_temp| image:: /img/schematic/sch_thermometer.png
.. |sch_ultrasonic| image:: /img/schematic/sch_measuring_distance.png
.. |sch_4dig| image:: /img/schematic/sch_time_counter.png
    :width: 800
.. |sch_keypad| image:: /img/schematic/sch_keypad.png
.. |sch_keypad_ar| image:: /img/schematic/sch_keypad_ar.png
.. |sch_joystick| image:: /img/schematic/sch_toggle_the_joystick.png
.. |sch_motor| image:: /img/schematic/sch_small_fan.png
.. |sch_water| image:: /img/schematic/sch_feel_the_water_level.png
.. |sch_photoresistor| image:: /img/schematic/sch_feel_the_light.png
.. |sch_pir| image:: /img/schematic/sch_detect_human_movement.png
.. |sch_ledbar| image:: /img/schematic/sch_display_the_level.png
.. |sch_reed| image:: /img/schematic/sch_feel_the_magnetism.png
.. |sch_mpr121| image:: /img/schematic/sch_mpr121.png
.. |sch_mpr121_ar| image:: /img/schematic/sch_mpr121_ar.png
.. |sch_mpu6050| image:: /img/schematic/sch_mpu6050.png
.. |sch_mpu6050_ar| image:: /img/schematic/sch_mpu6050_ar.png
.. |sch_rfid| image:: /img/schematic/sch_rfid.png
.. |sch_irremote| image:: /img/schematic/sch_ir_remote_control.png
.. |sch_dht11| image:: /img/schematic/sch_dht11.png
.. |sch_ledmatrix| image:: /img/schematic/sch_8x8_pixel_graphics.png
    :width: 800
.. |sch_irrecv| image:: /img/schematic/sch_ir_remote_control.png
.. |sch_pump| image:: /img/schematic/sch_pumping.png
.. |sch_s8050| image:: /img/schematic/sch_transistor_s8050.png
.. |sch_s8550| image:: /img/schematic/sch_transistor_s8550.png
.. |sch_relay_1| image:: /img/schematic/sch_control_another_circuit.png
.. |sch_relay_2| image:: /img/schematic/sch_control_another_circuit2.png
.. |sch_light_theremin| image:: /img/schematic/sch_light_theremin.png
.. |sch_room_temp|  image:: /img/schematic/sch_room_temp.png

.. |sch_alarm_siren_lamp| image:: /img/schematic/sch_alarm_siren_lamp.png
.. |sch_passager_counter| image:: /img/schematic/sch_passager_counter.png
.. |sch_10_second| image:: /img/schematic/sch_10_second.png
.. |sch_traffic_light| image:: /img/schematic/sch_traffic_light.png
.. |sch_guess_number| image:: /img/schematic/sch_guess_number.png
.. |sch_music_player| image:: /img/schematic/sch_music_player.png
.. |sch_fruit_piano| image:: /img/schematic/sch_fruit_piano.png
    :width: 800
.. |sch_reversing_aid| image:: /img/schematic/sch_reversing_aid.png
.. |sch_somato| image:: /img/schematic/sch_somato.png
.. |sch_bubble_level| image:: /img/schematic/sch_bubble_level.png
    :width: 800
"""

# phonomenon pic
rst_epilog += """

.. |rfid_player| image:: /img/rfid_player.png
.. |fruit_piano| image:: /img/fruit_piano.png
.. |sirem_alarm| image:: /img/sirem_alarm.png
.. |guess_number| image:: /img/guess_number.png
.. |setup_web| image:: /img/setup_web.jpg
.. |anvil| image:: /img/anvil.jpg
.. |plant_monitor| image:: /img/plant_monitor.jpg


"""

# pico micropython start
rst_epilog += """
.. |bootsel_onboard| image:: /img/micropython_start/bootsel_onboard.png
.. |th_files| image:: /img/micropython_start/th_files .png
.. |th_path| image:: /img/micropython_start/th_path.png
.. |th_pico| image:: /img/micropython_start/th_pico.png
.. |th_upload| image:: /img/micropython_start/th_upload.png
.. |th_done| image:: /img/micropython_start/th_done.png
.. |interpreter| image:: /img/micropython_start/interpreter.png
.. |index_htm| image:: /img/micropython_start/index_htm.png
.. |welcome_pico| image:: /img/micropython_start/welcome_pico.png
.. |download_uf2| image:: /img/micropython_start/download_uf2.png
.. |move_uf2| image:: /img/micropython_start/move_uf2.png
.. |download_thonny| image:: /img/micropython_start/download_thonny.png
.. |thonny_ide.jpg| image:: /img/micropython_start/thonny_ide.jpg
.. |hello_shell| image:: /img/micropython_start/hello_shell.png
.. |hello_world_script| image:: /img/micropython_start/hello_world_script.png
.. |where_save| image:: /img/micropython_start/where_save.png
.. |hello_world_save| image:: /img/micropython_start/hello_world_save.png
.. |open_code| image:: /img/micropython_start/open_code.png
.. |sec_inter| image:: /img/micropython_start/sec_inter.png
.. |run_it| image:: /img/micropython_start/run_it.png
.. |stop_it| image:: /img/micropython_start/stop_it.png
.. |save_as| image:: /img/micropython_start/save_as.png
.. |sec_pico| image:: /img/micropython_start/sec_pico.png
.. |sec_name| image:: /img/micropython_start/sec_name.png
.. |new_file| image:: /img/micropython_start/new_file.png
.. |copy_file| image:: /img/micropython_start/copy_file.png

"""

# # pico arduino start
# rst_epilog += """
# .. |ars_arduino_setup1| image:: /img/arduino_start/arduino_setup1.png
# .. |ars_boards_manager| image:: /img/arduino_start/boards_manager.png
# .. |ars_install_pico| image:: /img/arduino_start/install_pico.png
# .. |ars_pico_board| image:: /img/arduino_start/pico_board.png
# .. |ars_test_blink| image:: /img/arduino_start/test_blink.png
# .. |ars_upload_blink| image:: /img/arduino_start/upload_blink.png
# .. |ars_upload_process| image:: /img/arduino_start/upload_process.png
# .. |ars_done_uploading| image:: /img/arduino_start/done_uploading.png
# .. |ars_arduino_ide| image:: /img/arduino_start/arduino_ide.png
# .. |ars_serial_monitor| image:: /img/arduino_start/serial_monitor.png
# .. |ars_baud_rate| image:: /img/arduino_start/baud_rate.png
# .. |ars_open_code| image:: /img/arduino_start/ar_open_code.png

# """

# appenx arduino add lib
rst_epilog += """
.. |apx_add_lib1| image:: /img/appenx_add_lib/image291.png
.. |apx_add_lib2| image:: /img/appenx_add_lib/image292.png
.. |apx_add_lib3| image:: /img/appenx_add_lib/image293.png
.. |apx_add_lib4| image:: /img/appenx_add_lib/image294.png
.. |apx_add_lib5| image:: /img/appenx_add_lib/image295.png
.. |apx_add_lib6| image:: /img/appenx_add_lib/image296.png
.. |apx_add_lib7| image:: /img/appenx_add_lib/image297.png

"""

# faq
rst_epilog += """
.. |save_to_pico| image:: /img/faq/save_to_pico.png
.. |interepter_thonny| image:: /img/faq/interepter_thonny.png


"""

# pico pin
rst_epilog += """
.. |pico_w_side| image:: /img/pico_w_side.png
.. |pico_pin| image:: /img/pico_pin.jpg
    :width: 800
.. |pin_adc| image:: /img/pin_pic3.png
.. |pin_pwm| image:: /img/pin_pic.png
.. |pin_i2c| image:: /img/pin_pic2.png
"""

# basic circuit
rst_epilog += """
.. |bc1| image:: /img/bc1.png
.. |bc2| image:: /img/bc2.png
.. |bc2.5| image:: /img/bc2.5.png
.. |bc3| image:: /img/bc3.png
"""


# piper start
rst_epilog += """

.. |save_download| image:: /img/piper_start/save_download.png
.. |download_per| image:: /img/piper_start/download_per.png
.. |per_home| image:: /img/piper_start/per_home.png
.. |per_import| image:: /img/piper_start/per_import.png
.. |choose_file| image:: /img/piper_start/choose_file.png
.. |import_led| image:: /img/piper_start/import_led.png
.. |media1| image:: /img/piper_start/media1.png
    :width: 800
.. |media2| image:: /img/piper_start/media2.png
.. |media3| image:: /img/piper_start/media3.png
.. |media4| image:: /img/piper_start/media4.png
.. |media5| image:: /img/piper_start/media5.png
.. |media6| image:: /img/piper_start/media6.png
.. |media7| image:: /img/piper_start/media7.png
.. |media8| image:: /img/piper_start/media8.png
.. |media9| image:: /img/piper_start/media9.png
.. |media11| image:: /img/piper_start/media11.png
.. |piper_intro1| image:: /img/piper_start/piper_intro1.png
.. |media12| image:: /img/piper_start/media12.png
.. |media14| image:: /img/piper_start/media14.png
.. |media15| image:: /img/piper_start/media15.png
.. |media16| image:: /img/piper_start/media16.png
.. |media166| image:: /img/piper_start/media166.png
.. |media17| image:: /img/piper_start/media17.png
.. |pico_port| image:: /img/piper_start/pico_port.png
.. |disconnect_per| image:: /img/piper_start/disconnect_per.png
.. |media2-s| image:: /img/piper_start/media2-s.png
.. |media9-s| image:: /img/piper_start/media9-s.png
.. |media11-s| image:: /img/piper_start/media11-s.png
.. |per_import-s| image:: /img/piper_start/per_import-s.png

"""


# piper
rst_epilog += """

.. |blink1| image:: /img/piper/2.1_blink_led.png
    :width: 300
.. |button_race0| image:: /img/piper/button_race0.png
    :width: 800
.. |button_race| image:: /img/piper/2.13_reaction_game.png
    :width: 800
.. |button_race1| image:: /img/piper/button_race1.png
.. |button_race2| image:: /img/piper/button_race2.png
.. |button_race3| image:: /img/piper/button_race3.png
.. |button_race4| image:: /img/piper/button_race4.png
.. |button_race5| image:: /img/piper/button_race5.png
.. |button0| image:: /img/piper/button0.png
    :width: 800
.. |2.2_button| image:: /img/piper/2.2_button.png
    :width: 400
.. |controllable_servo0| image:: /img/piper/controllable_servo0.png
    :width: 800
.. |controllable_servo| image:: /img/piper/2.7_swing_servo.png
    :width: 800
.. |controllable_servo1| image:: /img/piper/controllable_servo1.png
.. |controllable_servo2| image:: /img/piper/controllable_servo2.png
.. |controllable_servo3| image:: /img/piper/controllable_servo3.png
.. |drum_kit0| image:: /img/piper/drum_kit0.png
    :width: 800
.. |drum_kit| image:: /img/piper/2.5_drum_kit.png
    :width: 400
.. |drum_kit1| image:: /img/piper/drum_kit1.png
.. |drum_kit2| image:: /img/piper/drum_kit2.png
.. |light_intensity_display0| image:: /img/piper/light_intensity_display0.png
.. |light_intensity_display| image:: /img/piper/2.8_light_intensity_display.png
    :width: 800
.. |light_intensity_display1| image:: /img/piper/light_intensity_display1.png
.. |light_intensity_display2| image:: /img/piper/light_intensity_display2.png
.. |light_intensity_display3| image:: /img/piper/light_intensity_display3.png
.. |lucky_cat0| image:: /img/piper/lucky_cat0.png
    :width: 800
.. |lucky_cat| image:: /img/piper/2.9_lucky_cat.png
    :width: 800
.. |lucky_cat1| image:: /img/piper/lucky_cat1.png
.. |lucky_cat2| image:: /img/piper/lucky_cat2.png
.. |lucky_cat3| image:: /img/piper/lucky_cat3.png

.. |WS2812_Flow_friz| image:: /img/piper/WS2812_Flow_friz.png
    :width: 800
.. |neopixel| image:: /img/piper/2.10_flowing_led.png
    :width: 500
.. |neo1| image:: /img/piper/neo1.png
.. |neo2| image:: /img/piper/neo2.png
.. |neo3| image:: /img/piper/neo3.png
.. |neo4| image:: /img/piper/neo4.png
.. |neo5| image:: /img/piper/neo5.png
.. |overcrowd0| image:: /img/piper/overcrowd0.png
    :width: 800
.. |overcrowd| image:: /img/piper/overcrowd.png
    :width: 800
.. |overcrowd1| image:: /img/piper/overcrowd1.png
.. |overcrowd2| image:: /img/piper/overcrowd2.png
.. |overcrowd3| image:: /img/piper/overcrowd3.png
.. |overcrowd4| image:: /img/piper/overcrowd4.png
.. |reversing_system0| image:: /img/piper/reversing_system0.png
    :width: 800
.. |reversing_system| image:: /img/piper/2.11_reversing_system.png
    :width: 800
.. |reversing_system1| image:: /img/piper/reversing_system1.png
.. |reversing_system2| image:: /img/piper/reversing_system2.png
.. |reversing_system3| image:: /img/piper/reversing_system3.png
.. |reversing_system4| image:: /img/piper/reversing_system4.png
.. |reversing_system5| image:: /img/piper/reversing_system5.png
.. |rgb0| image:: /img/piper/rgb0.png
    :width: 800
.. |rgb_pin| image:: /img/piper/rgb_pin.jpg
.. |rgb_led| image:: /img/piper/2.4_rainbow_light.png
    :width: 300
.. |service_bell0| image:: /img/piper/service_bell0.png
    :width: 800
.. |service_bell| image:: /img/piper/2.3_service_bell.png
    :width: 400
.. |temperature_controlled_fan0| image:: /img/piper/temperature_controlled_fan0.png
    :width: 800
.. |temperature_controlled_fan| image:: /img/piper/2.12_smart_fan.png
    :width: 800
.. |temperature_controlled_fan1| image:: /img/piper/temperature_controlled_fan1.png
.. |temperature_controlled_fan2| image:: /img/piper/temperature_controlled_fan2.png
.. |temperature_controlled_fan5| image:: /img/piper/temperature_controlled_fan5.png
.. |water_tank| image:: /img/piper/2.6_smart_water_tank.png
    :width: 600
.. |water_tank0| image:: /img/piper/water_tank0.png
    :width: 800    
.. |water_tank1| image:: /img/piper/water_tank1.png
.. |water_tank2| image:: /img/piper/water_tank2.png
.. |water_tank3| image:: /img/piper/water_tank3.png

"""

# open link in a new window

rst_epilog += """

.. |link_heat_index| raw:: html

    <a href="https://en.wikipedia.org/wiki/Heat_index" target="_blank">heat index</a>
    
.. |link_sf_facebook| raw:: html

    <a href="https://bit.ly/raphaelkit " target="_blank">ここ</a>

.. |link_german_tutorials| raw:: html

    <a href="https://docs.sunfounder.com/projects/kepler-kit/de/latest/" target="_blank">Deutsch Online-Kurs</a>

.. |link_jp_tutorials| raw:: html

    <a href="https://docs.sunfounder.com/projects/kepler-kit/ja/latest/" target="_blank">日本語オンライン教材</a>

.. |link_en_tutorials| raw:: html

    <a href="https://docs.sunfounder.com/projects/kepler-kit/en/latest/" target="_blank">English Online-tutorials</a>

.. |link_fr_tutorials| raw:: html

    <a href="https://docs.sunfounder.com/projects/kepler-kit/fr/latest/" target="_blank">Didacticiels en ligne en français</a>

.. |link_es_tutorials| raw:: html

    <a href="https://docs.sunfounder.com/projects/kepler-kit/es/latest/" target="_blank">Tutoriales en línea en español</a>

.. |link_it_tutorials| raw:: html

    <a href="https://docs.sunfounder.com/projects/kepler-kit/it/latest/" target="_blank">Tutorial online in italiano</a>

.. |link_download_arduino|  raw:: html

    <a href="https://www.arduino.cc/en/software" target="_blank">Arduino Software</a>
    

.. |link_micropython| raw:: html

    <a href="https://en.wikipedia.org/wiki/MicroPython" target="_blank">MicroPython - Wikipedia</a>
    
.. |link_thonny| raw:: html

    <a href="https://thonny.org/" target="_blank">Thonny</a>

.. |link_sunfounder_controller| raw:: html

    <a href="https://docs.sunfounder.com/projects/sf-controller/en/latest/" target="_blank">SunFounder Control</a>

.. |link_realpython| raw:: html

    <a href="https://realpython.com/micropython/" target="_blank">realpython</a>

.. |link_micropython_pi| raw:: html

    <a href="https://www.raspberrypi.com/documentation/microcontrollers/micropython.html#drag-and-drop-micropython" target="_blank">method</a>

.. |link_cheerlights| raw:: html

    <a href="https://twitter.com/cheerlights" target="_blank">@CheerLights - Twitter</a>

.. |link_ifttt| raw:: html

    <a href="https://ifttt.com/explore" target="_blank">IFTTT</a>

.. |link_webhooks| raw:: html

    <a href="https://ifttt.com/maker_webhooks/settings" target="_blank">Webhooks Settings</a>

.. |link_openweather| raw:: html

    <a href="https://openweathermap.org/" target="_blank">OpenWeather</a>


.. |link_openweather_api| raw:: html

    <a href="https://home.openweathermap.org/api_keys" target="_blank">OpenWeatherMap Api Keys</a>

.. |link_hivemq| raw:: html

    <a href="http://www.hivemq.com/demos/websocket-client/" target="_blank">HiveMQ Web Client</a>
    
.. |link_piano_frequency| raw:: html

    <a href="https://en.wikipedia.org/wiki/Piano_key_frequencies" target="_blank">Piano key frequencies</a>

.. |link_port| raw:: html

    <a href="https://en.wikipedia.org/wiki/Port_(computer_networking)" target="_blank">port</a>

.. |link_html| raw:: html

    <a href="https://html.com/" target="_blank">HTML.COM</a>

.. |link_anvil| raw:: html

    <a href="https://anvil.works/" target="_blank">Anvil website</a>

.. |link_anvil_docs| raw:: html

    <a href="https://anvil.works/docs/server" target="_blank">Anvil Docs</a>


.. |link_anvil_firmware| raw:: html

    <a href="https://github.com/anvil-works/anvil-pico/releases" target="_blank">firmware from Anvil</a>

.. |link_paul_course| raw:: html

    <a href="https://www.youtube.com/playlist?list=PLGs0VKk2DiYz8js1SJog21cDhkBqyAhC5" target="_blank">Raspberry Pi Pico W Lessons for Absolute Beginners</a>

"""

# Purchase links of components

rst_epilog += """

.. |link_Kepler_Ultimate_Kit| raw:: html

    <a href="https://www.sunfounder.com/collections/raspberry-pi-kit-for-beginner-1/products/sunfounder-raspberry-pi-pico-w-ultimate-starter-kit" target="_blank">Purchase Link for Kepler Ultimate Kit</a>

.. |link_kepler_Mlimate_kit| raw:: html

    <a href="https://www.sunfounder.com/collections/raspberry-pi-kit-for-beginner-1/products/sunfounder-raspberry-pi-pico-w-ultimate-starter-kit" target="_blank">Purchase Link for Kepler Ultimate Kit</a>

.. |link_kepler_kit| raw:: html

    <a href="https://www.sunfounder.com/collections/raspberry-pi-kit-for-beginner-1/products/sunfounder-raspberry-pi-pico-w-ultimate-starter-kit" target="_blank">Kepler Ultimate Kit</a>

.. |link_picow_buy| raw:: html

    <a href="https://www.sunfounder.com/products/raspberry-pi-pico-w" target="_blank">BUY</a>
    
.. |link_led_buy| raw:: html

    <a href="https://www.sunfounder.com/products/500pcs-5-colors-x-100pcs-5mm-leds-with-white-red-yellow-green-blue-colors-kit-box" target="_blank">BUY</a>

.. |link_resistor_buy| raw:: html

    <a href="https://www.sunfounder.com/products/1-4w-resistor-assortment-kit-40-values-400pcs" target="_blank">BUY</a>

.. |link_wires_buy| raw:: html

    <a href="https://www.sunfounder.com/products/560pcs-jumper-wire-kit-with-14-lengths" target="_blank">BUY</a>

.. |link_breadboard_buy| raw:: html

    <a href="https://www.sunfounder.com/products/sunfounder-breadboard-kit" target="_blank">BUY</a>

.. |link_rgb_led_buy| raw:: html

    <a href="https://www.sunfounder.com/products/100pcs-5mm-4-pin-rgb-common-cathode-led" target="_blank">BUY</a>

.. |link_button_buy| raw:: html

    <a href="https://www.sunfounder.com/products/100pcs-6x6x5-mm-miniature-push-button" target="_blank">BUY</a>

.. |link_capacitor_buy| raw:: html

    <a href="https://www.sunfounder.com/products/ceramic-capacitor-assortment-kit-set-of-600-small-assorted-capacitors" target="_blank">BUY</a>

.. |link_potentiometer_buy| raw:: html

    <a href="https://www.sunfounder.com/products/10pcs-10k-ohm-trim-potentiometer-breadboard" target="_blank">BUY</a>

.. |link_photoresistor_buy| raw:: html

    <a href="https://www.sunfounder.com/products/100pcs-photoresistor-photo-light-sensitive-resistor-5516" target="_blank">BUY</a>

.. |link_thermistor_buy| raw:: html

    <a href="https://www.sunfounder.com/products/50pcs-ntc-thermistor-mf11-103-10k-ohm" target="_blank">BUY</a>

.. |link_transistor_buy| raw:: html

    <a href="https://www.sunfounder.com/products/10-values-200pcs-power-supply-general-transistor-npn-pnp-assortment-kit-bc337-bc327-2n2222-2n2907-2n3904-2n3906-s8050-s8550-a1015-c1815-set" target="_blank">BUY</a>

.. |link_relay_buy| raw:: html

    <a href="https://www.sunfounder.com/products/10pcs-srs-05vdc-sl-c-5v-relay-coil-spdt-6-pin-pcb-electromagnetic-power-relay" target="_blank">BUY</a>

.. |link_passive_buzzer_buy| raw:: html

    <a href="https://www.sunfounder.com/products/20pcs-3-5v-2-terminals-passive-buzzer" target="_blank">BUY</a>

.. |link_ws2812_buy| raw:: html

    <a href="https://www.sunfounder.com/products/2pcs-8-bit-ws2812b-rgb-led-strip-5050smd-individual-addressable-60pixels-m" target="_blank">BUY</a>

.. |link_i2clcd1602_buy| raw:: html

    <a href="https://www.sunfounder.com/products/i2c-lcd1602-module" target="_blank">BUY</a>

.. |link_motor_buy| raw:: html

    <a href="https://www.sunfounder.com/products/5pcs-1-5v-6v-type-miniature-dc-motors" target="_blank">BUY</a>

.. |link_servo_buy| raw:: html

    <a href="https://www.sunfounder.com/products/sg90-micro-digital-servo" target="_blank">BUY</a>

.. |link_keypad_buy| raw:: html

    <a href="https://www.sunfounder.com/products/membrane-switch-keypad" target="_blank">BUY</a>

.. |link_74hc595_buy| raw:: html

    <a href="https://www.sunfounder.com/products/10-pcs-ic-74hc595-74595-sn74hc595n-8-bit-shift-register-dip-16" target="_blank">BUY</a>

.. |link_7segment_buy| raw:: html

    <a href="https://www.sunfounder.com/products/30pcs-0-56-7-segment-led" target="_blank">BUY</a>

.. |link_ultrasonic_buy| raw:: html

    <a href="https://www.sunfounder.com/products/5pcs-hc-sr04-ultrasonic-module-distance-sensor" target="_blank">BUY</a>

.. |link_dht22_buy| raw:: html

    <a href="https://www.sunfounder.com/products/dht22-am2302-digital-temperature-and-humidity-sensor" target="_blank">BUY</a>

.. |link_receiver_buy| raw:: html

    <a href="https://www.sunfounder.com/products/infrared-receiver-module" target="_blank">BUY</a>

.. |link_rfid_buy| raw:: html

    <a href="https://www.sunfounder.com/products/rfid-kit-blue" target="_blank">BUY</a>


.. |link_pir_buy| raw:: html

    <a href="https://www.sunfounder.com/products/hcsr501-human-sensor" target="_blank">BUY</a>



"""
