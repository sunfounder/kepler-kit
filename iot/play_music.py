# Thanks to Robson Couto for open-sourced these scores.
# You can access his github from here: https://github.com/robsoncouto/arduino-songs 

NOTE_B0 =  31
NOTE_C1 =  33
NOTE_CS1 = 35
NOTE_D1 =  37
NOTE_DS1 = 39
NOTE_E1 =  41
NOTE_F1 =  44
NOTE_FS1 = 46
NOTE_G1 =  49
NOTE_GS1 = 52
NOTE_A1 =  55
NOTE_AS1 = 58
NOTE_B1 =  62
NOTE_C2 =  65
NOTE_CS2 = 69
NOTE_D2 =  73
NOTE_DS2 = 78
NOTE_E2 =  82
NOTE_F2 =  87
NOTE_FS2 = 93
NOTE_G2 =  98
NOTE_GS2 = 104
NOTE_A2 =  110
NOTE_AS2 = 117
NOTE_B2 =  123
NOTE_C3 =  131
NOTE_CS3 = 139
NOTE_D3 =  147
NOTE_DS3 = 156
NOTE_E3 =  165
NOTE_F3 =  175
NOTE_FS3 = 185
NOTE_G3 =  196
NOTE_GS3 = 208
NOTE_A3 =  220
NOTE_AS3 = 233
NOTE_B3 =  247
NOTE_C4 =  262
NOTE_CS4 = 277
NOTE_D4 =  294
NOTE_DS4 = 311
NOTE_E4 =  330
NOTE_F4 =  349
NOTE_FS4 = 370
NOTE_G4 =  392
NOTE_GS4 = 415
NOTE_A4 =  440
NOTE_AS4 = 466
NOTE_B4 =  494
NOTE_C5 =  523
NOTE_CS5 = 554
NOTE_D5 =  587
NOTE_DS5 = 622
NOTE_E5 =  659
NOTE_F5 =  698
NOTE_FS5 = 740
NOTE_G5 =  784
NOTE_GS5 = 831
NOTE_A5 =  880
NOTE_AS5 = 932
NOTE_B5 =  988
NOTE_C6 =  1047
NOTE_CS6 = 1109
NOTE_D6 =  1175
NOTE_DS6 = 1245
NOTE_E6 =  1319
NOTE_F6 =  1397
NOTE_FS6 = 1480
NOTE_G6 =  1568
NOTE_GS6 = 1661
NOTE_A6 =  1760
NOTE_AS6 = 1865
NOTE_B6 =  1976
NOTE_C7 =  2093
NOTE_CS7 = 2217
NOTE_D7 =  2349
NOTE_DS7 = 2489
NOTE_E7 =  2637
NOTE_F7 =  2794
NOTE_FS7 = 2960
NOTE_G7 =  3136
NOTE_GS7 = 3322
NOTE_A7 =  3520
NOTE_AS7 = 3729
NOTE_B7 =  3951
NOTE_C8 =  4186
NOTE_CS8 = 4435
NOTE_D8 =  4699
NOTE_DS8 = 4978
REST =      0

# notes of the moledy followed by the duration.
# a 4 means a quarter note, 8 an eighteenth , 16 sixteenth, so on
# !!negative numbers are used to represent dotted notes,
# so -4 means a dotted quarter note, that is, a quarter plus an eighteenth!!
song = {
    "nokia":[NOTE_E5, 8, NOTE_D5, 8, NOTE_FS4, 4, NOTE_GS4, 4, NOTE_CS5, 8, NOTE_B4, 8, NOTE_D4, 4, 
                NOTE_E4, 4,NOTE_B4, 8, NOTE_A4, 8, NOTE_CS4, 4, NOTE_E4, 4, NOTE_A4, 2],
    "starwars":[NOTE_AS4,8, NOTE_AS4,8, NOTE_AS4,8,
                    NOTE_F5,2, NOTE_C6,2,
                    NOTE_AS5,8, NOTE_A5,8, NOTE_G5,8, NOTE_F6,2, NOTE_C6,4,  
                    NOTE_AS5,8, NOTE_A5,8, NOTE_G5,8, NOTE_F6,2, NOTE_C6,4,  
                    NOTE_AS5,8, NOTE_A5,8, NOTE_AS5,8, NOTE_G5,2, NOTE_C5,8, 
                    NOTE_C5,8, NOTE_C5,8,NOTE_F5,2, NOTE_C6,2,
                    NOTE_AS5,8, NOTE_A5,8, NOTE_G5,8, NOTE_F6,2, NOTE_C6,4,  
                    
                    NOTE_AS5,8, NOTE_A5,8, NOTE_G5,8, NOTE_F6,2, NOTE_C6,4, 
                    NOTE_AS5,8, NOTE_A5,8, NOTE_AS5,8, NOTE_G5,2, NOTE_C5,-8, NOTE_C5,16, 
                    NOTE_D5,-4, NOTE_D5,8, NOTE_AS5,8, NOTE_A5,8, NOTE_G5,8, NOTE_F5,8,
                    NOTE_F5,8, NOTE_G5,8, NOTE_A5,8, NOTE_G5,4, NOTE_D5,8, NOTE_E5,4,NOTE_C5,-8, NOTE_C5,16,
                    NOTE_D5,-4, NOTE_D5,8, NOTE_AS5,8, NOTE_A5,8, NOTE_G5,8, NOTE_F5,8,
                    
                    NOTE_C6,-8, NOTE_G5,16, NOTE_G5,2, REST,8, NOTE_C5,8,
                    NOTE_D5,-4, NOTE_D5,8, NOTE_AS5,8, NOTE_A5,8, NOTE_G5,8, NOTE_F5,8,
                    NOTE_F5,8, NOTE_G5,8, NOTE_A5,8, NOTE_G5,4, NOTE_D5,8, NOTE_E5,4,NOTE_C6,-8, NOTE_C6,16,
                    NOTE_F6,4, NOTE_DS6,8, NOTE_CS6,4, NOTE_C6,8, NOTE_AS5,4, NOTE_GS5,8, NOTE_G5,4, NOTE_F5,8,
                    NOTE_C6,1],
    "nevergonnagiveyouup":[NOTE_D5,-4, NOTE_E5,-4, NOTE_A4,4, 
                            NOTE_E5,-4, NOTE_FS5,-4, NOTE_A5,16, NOTE_G5,16, NOTE_FS5,8,
                            NOTE_D5,-4, NOTE_E5,-4, NOTE_A4,2,
                            NOTE_A4,16, NOTE_A4,16, NOTE_B4,16, NOTE_D5,8, NOTE_D5,16,
                            NOTE_D5,-4, NOTE_E5,-4, NOTE_A4,4,  
                            NOTE_E5,-4, NOTE_FS5,-4, NOTE_A5,16, NOTE_G5,16, NOTE_FS5,8,
                            NOTE_D5,-4, NOTE_E5,-4, NOTE_A4,2,
                            NOTE_A4,16, NOTE_A4,16, NOTE_B4,16, NOTE_D5,8, NOTE_D5,16,
                            REST,4, NOTE_B4,8, NOTE_CS5,8, NOTE_D5,8, NOTE_D5,8, NOTE_E5,8, NOTE_CS5,-8,
                            NOTE_B4,16, NOTE_A4,2, REST,4, 

                            REST,8, NOTE_B4,8, NOTE_B4,8, NOTE_CS5,8, NOTE_D5,8, NOTE_B4,4, NOTE_A4,8, 
                            NOTE_A5,8, REST,8, NOTE_A5,8, NOTE_E5,-4, REST,4, 
                            NOTE_B4,8, NOTE_B4,8, NOTE_CS5,8, NOTE_D5,8, NOTE_B4,8, NOTE_D5,8, NOTE_E5,8, REST,8,
                            REST,8, NOTE_CS5,8, NOTE_B4,8, NOTE_A4,-4, REST,4,
                            REST,8, NOTE_B4,8, NOTE_B4,8, NOTE_CS5,8, NOTE_D5,8, NOTE_B4,8, NOTE_A4,4,
                            NOTE_E5,8, NOTE_E5,8, NOTE_E5,8, NOTE_FS5,8, NOTE_E5,4, REST,4,
                            
                            NOTE_D5,2, NOTE_E5,8, NOTE_FS5,8, NOTE_D5,8, 
                            NOTE_E5,8, NOTE_E5,8, NOTE_E5,8, NOTE_FS5,8, NOTE_E5,4, NOTE_A4,4,
                            REST,2, NOTE_B4,8, NOTE_CS5,8, NOTE_D5,8, NOTE_B4,8,
                            REST,8, NOTE_E5,8, NOTE_FS5,8, NOTE_E5,-4, NOTE_A4,16, NOTE_B4,16, NOTE_D5,16, NOTE_B4,16,
                            NOTE_FS5,-8, NOTE_FS5,-8, NOTE_E5,-4, NOTE_A4,16, NOTE_B4,16, NOTE_D5,16, NOTE_B4,16,

                            NOTE_E5,-8, NOTE_E5,-8, NOTE_D5,-8, NOTE_CS5,16, NOTE_B4,-8, NOTE_A4,16, NOTE_B4,16, NOTE_D5,16, NOTE_B4,16, 
                            NOTE_D5,4, NOTE_E5,8, NOTE_CS5,-8, NOTE_B4,16, NOTE_A4,8, NOTE_A4,8, NOTE_A4,8, 
                            NOTE_E5,4, NOTE_D5,2, NOTE_A4,16, NOTE_B4,16, NOTE_D5,16, NOTE_B4,16,
                            NOTE_FS5,-8, NOTE_FS5,-8, NOTE_E5,-4, NOTE_A4,16, NOTE_B4,16, NOTE_D5,16, NOTE_B4,16,
                            NOTE_A5,4, NOTE_CS5,8, NOTE_D5,-8, NOTE_CS5,16, NOTE_B4,8, NOTE_A4,16, NOTE_B4,16, NOTE_D5,16, NOTE_B4,16,

                            NOTE_D5,4, NOTE_E5,8, NOTE_CS5,-8, NOTE_B4,16, NOTE_A4,4, NOTE_A4,8,  
                            NOTE_E5,4, NOTE_D5,2, REST,4,
                            REST,8, NOTE_B4,8, NOTE_D5,8, NOTE_B4,8, NOTE_D5,8, NOTE_E5,4, REST,8,
                            REST,8, NOTE_CS5,8, NOTE_B4,8, NOTE_A4,-4, REST,4,
                            REST,8, NOTE_B4,8, NOTE_B4,8, NOTE_CS5,8, NOTE_D5,8, NOTE_B4,8, NOTE_A4,4,
                            REST,8, NOTE_A5,8, NOTE_A5,8, NOTE_E5,8, NOTE_FS5,8, NOTE_E5,8, NOTE_D5,8,
                            
                            REST,8, NOTE_A4,8, NOTE_B4,8, NOTE_CS5,8, NOTE_D5,8, NOTE_B4,8, 
                            REST,8, NOTE_CS5,8, NOTE_B4,8, NOTE_A4,-4, REST,4,
                            NOTE_B4,8, NOTE_B4,8, NOTE_CS5,8, NOTE_D5,8, NOTE_B4,8, NOTE_A4,4, REST,8,
                            REST,8, NOTE_E5,8, NOTE_E5,8, NOTE_FS5,4, NOTE_E5,-4, 
                            NOTE_D5,2, NOTE_D5,8, NOTE_E5,8, NOTE_FS5,8, NOTE_E5,4, 
                            NOTE_E5,8, NOTE_E5,8, NOTE_FS5,8, NOTE_E5,8, NOTE_A4,8, NOTE_A4,4,

                            REST,-4, NOTE_A4,8, NOTE_B4,8, NOTE_CS5,8, NOTE_D5,8, NOTE_B4,8, 
                            REST,8, NOTE_E5,8, NOTE_FS5,8, NOTE_E5,-4, NOTE_A4,16, NOTE_B4,16, NOTE_D5,16, NOTE_B4,16,
                            NOTE_FS5,-8, NOTE_FS5,-8, NOTE_E5,-4, NOTE_A4,16, NOTE_B4,16, NOTE_D5,16, NOTE_B4,16,
                            NOTE_E5,-8, NOTE_E5,-8, NOTE_D5,-8, NOTE_CS5,16, NOTE_B4,8, NOTE_A4,16, NOTE_B4,16, NOTE_D5,16, NOTE_B4,16,
                            NOTE_D5,4, NOTE_E5,8, NOTE_CS5,-8, NOTE_B4,16, NOTE_A4,4, NOTE_A4,8, 

                            NOTE_E5,4, NOTE_D5,2, NOTE_A4,16, NOTE_B4,16, NOTE_D5,16, NOTE_B4,16, 
                            NOTE_FS5,-8, NOTE_FS5,-8, NOTE_E5,-4, NOTE_A4,16, NOTE_B4,16, NOTE_D5,16, NOTE_B4,16,
                            NOTE_A5,4, NOTE_CS5,8, NOTE_D5,-8, NOTE_CS5,16, NOTE_B4,8, NOTE_A4,16, NOTE_B4,16, NOTE_D5,16, NOTE_B4,16,
                            NOTE_D5,4, NOTE_E5,8, NOTE_CS5,-8, NOTE_B4,16, NOTE_A4,4, NOTE_A4,8,  
                            NOTE_E5,4, NOTE_D5,2, NOTE_A4,16, NOTE_B4,16, NOTE_D5,16, NOTE_B4,16,
                            
                            NOTE_FS5,-8, NOTE_FS5,-8, NOTE_E5,-4, NOTE_A4,16, NOTE_B4,16, NOTE_D5,16, NOTE_B4,16, 
                            NOTE_A5,4, NOTE_CS5,8, NOTE_D5,-8, NOTE_CS5,16, NOTE_B4,8, NOTE_A4,16, NOTE_B4,16, NOTE_D5,16, NOTE_B4,16,
                            NOTE_D5,4, NOTE_E5,8, NOTE_CS5,-8, NOTE_B4,16, NOTE_A4,4, NOTE_A4,8,  
                            NOTE_E5,4, NOTE_D5,2, NOTE_A4,16, NOTE_B4,16, NOTE_D5,16, NOTE_B4,16,
                            NOTE_FS5,-8, NOTE_FS5,-8, NOTE_E5,-4, NOTE_A4,16, NOTE_B4,16, NOTE_D5,16, NOTE_B4,16, 
                            
                            NOTE_A5,4, NOTE_CS5,8, NOTE_D5,-8, NOTE_CS5,16, NOTE_B4,8, NOTE_A4,16, NOTE_B4,16, NOTE_D5,16, NOTE_B4,16,
                            NOTE_D5,4, NOTE_E5,8, NOTE_CS5,-8, NOTE_B4,16, NOTE_A4,4, NOTE_A4,8, 

                            NOTE_E5,4, NOTE_D5,2, REST,4],
    "gameofthrone":[NOTE_G4,8, NOTE_C4,8, NOTE_DS4,16, NOTE_F4,16, NOTE_G4,8, NOTE_C4,8, NOTE_DS4,16, NOTE_F4,16, #1
                    NOTE_G4,8, NOTE_C4,8, NOTE_DS4,16, NOTE_F4,16, NOTE_G4,8, NOTE_C4,8, NOTE_DS4,16, NOTE_F4,16,
                    NOTE_G4,8, NOTE_C4,8, NOTE_E4,16, NOTE_F4,16, NOTE_G4,8, NOTE_C4,8, NOTE_E4,16, NOTE_F4,16,
                    NOTE_G4,8, NOTE_C4,8, NOTE_E4,16, NOTE_F4,16, NOTE_G4,8, NOTE_C4,8, NOTE_E4,16, NOTE_F4,16,
                    NOTE_G4,-4, NOTE_C4,-4,#5

                    NOTE_DS4,16, NOTE_F4,16, NOTE_G4,4, NOTE_C4,4, NOTE_DS4,16, NOTE_F4,16, #6
                    NOTE_D4,-1, #7 and 8
                    NOTE_F4,-4, NOTE_AS3,-4,
                    NOTE_DS4,16, NOTE_D4,16, NOTE_F4,4, NOTE_AS3,-4,
                    NOTE_DS4,16, NOTE_D4,16, NOTE_C4,-1, #11 and 12

                    #repeats from 5
                    NOTE_G4,-4, NOTE_C4,-4,#5

                    NOTE_DS4,16, NOTE_F4,16, NOTE_G4,4, NOTE_C4,4, NOTE_DS4,16, NOTE_F4,16, #6
                    NOTE_D4,-1, #7 and 8
                    NOTE_F4,-4, NOTE_AS3,-4,
                    NOTE_DS4,16, NOTE_D4,16, NOTE_F4,4, NOTE_AS3,-4,
                    NOTE_DS4,16, NOTE_D4,16, NOTE_C4,-1, #11 and 12
                    NOTE_G4,-4, NOTE_C4,-4,
                    NOTE_DS4,16, NOTE_F4,16, NOTE_G4,4,  NOTE_C4,4, NOTE_DS4,16, NOTE_F4,16,

                    NOTE_D4,-2,#15
                    NOTE_F4,-4, NOTE_AS3,-4,
                    NOTE_D4,-8, NOTE_DS4,-8, NOTE_D4,-8, NOTE_AS3,-8,
                    NOTE_C4,-1,
                    NOTE_C5,-2,
                    NOTE_AS4,-2,
                    NOTE_C4,-2,
                    NOTE_G4,-2,
                    NOTE_DS4,-2,
                    NOTE_DS4,-4, NOTE_F4,-4, 
                    NOTE_G4,-1,
                    
                    NOTE_C5,-2,#28
                    NOTE_AS4,-2,
                    NOTE_C4,-2,
                    NOTE_G4,-2, 
                    NOTE_DS4,-2,
                    NOTE_DS4,-4, NOTE_D4,-4,
                    NOTE_C5,8, NOTE_G4,8, NOTE_GS4,16, NOTE_AS4,16, NOTE_C5,8, NOTE_G4,8, NOTE_GS4,16, NOTE_AS4,16,
                    NOTE_C5,8, NOTE_G4,8, NOTE_GS4,16, NOTE_AS4,16, NOTE_C5,8, NOTE_G4,8, NOTE_GS4,16, NOTE_AS4,16,
                    
                    REST,4, NOTE_GS5,16, NOTE_AS5,16, NOTE_C6,8, NOTE_G5,8, NOTE_GS5,16, NOTE_AS5,16,
                    NOTE_C6,8, NOTE_G5,16, NOTE_GS5,16, NOTE_AS5,16, NOTE_C6,8, NOTE_G5,8, NOTE_GS5,16, NOTE_AS5,16,  ],
    "songofstorms":[  NOTE_D4,4, NOTE_A4,4, NOTE_A4,4,
                    REST,8, NOTE_E4,8, NOTE_B4,2,
                    NOTE_F4,4, NOTE_C5,4, NOTE_C5,4,
                    REST,8, NOTE_E4,8, NOTE_B4,2,
                    NOTE_D4,4, NOTE_A4,4, NOTE_A4,4,
                    REST,8, NOTE_E4,8, NOTE_B4,2,
                    NOTE_F4,4, NOTE_C5,4, NOTE_C5,4,
                    REST,8, NOTE_E4,8, NOTE_B4,2,
                    NOTE_D4,8, NOTE_F4,8, NOTE_D5,2,
                    
                    NOTE_D4,8, NOTE_F4,8, NOTE_D5,2,
                    NOTE_E5,-4, NOTE_F5,8, NOTE_E5,8, NOTE_E5,8,
                    NOTE_E5,8, NOTE_C5,8, NOTE_A4,2,
                    NOTE_A4,4, NOTE_D4,4, NOTE_F4,8, NOTE_G4,8,
                    NOTE_A4,-2,
                    NOTE_A4,4, NOTE_D4,4, NOTE_F4,8, NOTE_G4,8,
                    NOTE_E4,-2,
                    NOTE_D4,8, NOTE_F4,8, NOTE_D5,2,
                    NOTE_D4,8, NOTE_F4,8, NOTE_D5,2,

                    NOTE_E5,-4, NOTE_F5,8, NOTE_E5,8, NOTE_E5,8,
                    NOTE_E5,8, NOTE_C5,8, NOTE_A4,2,
                    NOTE_A4,4, NOTE_D4,4, NOTE_F4,8, NOTE_G4,8,
                    NOTE_A4,2, NOTE_A4,4,
                    NOTE_D4,1,],     
    "zeldatheme":[  NOTE_AS4,-2,  NOTE_F4,8,  NOTE_F4,8,  NOTE_AS4,8,#1
                    NOTE_GS4,16,  NOTE_FS4,16,  NOTE_GS4,-2,
                    NOTE_AS4,-2,  NOTE_FS4,8,  NOTE_FS4,8,  NOTE_AS4,8,
                    NOTE_A4,16,  NOTE_G4,16,  NOTE_A4,-2,
                    REST,1, 

                    NOTE_AS4,4,  NOTE_F4,-4,  NOTE_AS4,8,  NOTE_AS4,16,  NOTE_C5,16, NOTE_D5,16, NOTE_DS5,16,#7
                    NOTE_F5,2,  NOTE_F5,8,  NOTE_F5,8,  NOTE_F5,8,  NOTE_FS5,16, NOTE_GS5,16,
                    NOTE_AS5,-2,  NOTE_AS5,8,  NOTE_AS5,8,  NOTE_GS5,8,  NOTE_FS5,16,
                    NOTE_GS5,-8,  NOTE_FS5,16,  NOTE_F5,2,  NOTE_F5,4, 

                    NOTE_DS5,-8, NOTE_F5,16, NOTE_FS5,2, NOTE_F5,8, NOTE_DS5,8, #11
                    NOTE_CS5,-8, NOTE_DS5,16, NOTE_F5,2, NOTE_DS5,8, NOTE_CS5,8,
                    NOTE_C5,-8, NOTE_D5,16, NOTE_E5,2, NOTE_G5,8, 
                    NOTE_F5,16, NOTE_F4,16, NOTE_F4,16, NOTE_F4,16,NOTE_F4,16,NOTE_F4,16,NOTE_F4,16,NOTE_F4,16,NOTE_F4,8, NOTE_F4,16,NOTE_F4,8,

                    NOTE_AS4,4,  NOTE_F4,-4,  NOTE_AS4,8,  NOTE_AS4,16,  NOTE_C5,16, NOTE_D5,16, NOTE_DS5,16,#15
                    NOTE_F5,2,  NOTE_F5,8,  NOTE_F5,8,  NOTE_F5,8,  NOTE_FS5,16, NOTE_GS5,16,
                    NOTE_AS5,-2, NOTE_CS6,4,
                    NOTE_C6,4, NOTE_A5,2, NOTE_F5,4,
                    NOTE_FS5,-2, NOTE_AS5,4,
                    NOTE_A5,4, NOTE_F5,2, NOTE_F5,4,

                    NOTE_FS5,-2, NOTE_AS5,4,
                    NOTE_A5,4, NOTE_F5,2, NOTE_D5,4,
                    NOTE_DS5,-2, NOTE_FS5,4,
                    NOTE_F5,4, NOTE_CS5,2, NOTE_AS4,4,
                    NOTE_C5,-8, NOTE_D5,16, NOTE_E5,2, NOTE_G5,8, 
                    NOTE_F5,16, NOTE_F4,16, NOTE_F4,16, NOTE_F4,16,NOTE_F4,16,NOTE_F4,16,NOTE_F4,16,NOTE_F4,16,NOTE_F4,8, NOTE_F4,16,NOTE_F4,8],
    "harrypotter":[  REST, 2, NOTE_D4, 4,
                    NOTE_G4, -4, NOTE_AS4, 8, NOTE_A4, 4,
                    NOTE_G4, 2, NOTE_D5, 4,
                    NOTE_C5, -2, 
                    NOTE_A4, -2,
                    NOTE_G4, -4, NOTE_AS4, 8, NOTE_A4, 4,
                    NOTE_F4, 2, NOTE_GS4, 4,
                    NOTE_D4, -1, 
                    NOTE_D4, 4,

                    NOTE_G4, -4, NOTE_AS4, 8, NOTE_A4, 4, #10
                    NOTE_G4, 2, NOTE_D5, 4,
                    NOTE_F5, 2, NOTE_E5, 4,
                    NOTE_DS5, 2, NOTE_B4, 4,
                    NOTE_DS5, -4, NOTE_D5, 8, NOTE_CS5, 4,
                    NOTE_CS4, 2, NOTE_B4, 4,
                    NOTE_G4, -1,
                    NOTE_AS4, 4,
                        
                    NOTE_D5, 2, NOTE_AS4, 4,#18
                    NOTE_D5, 2, NOTE_AS4, 4,
                    NOTE_DS5, 2, NOTE_D5, 4,
                    NOTE_CS5, 2, NOTE_A4, 4,
                    NOTE_AS4, -4, NOTE_D5, 8, NOTE_CS5, 4,
                    NOTE_CS4, 2, NOTE_D4, 4,
                    NOTE_D5, -1, 
                    REST,4, NOTE_AS4,4,  

                    NOTE_D5, 2, NOTE_AS4, 4,#26
                    NOTE_D5, 2, NOTE_AS4, 4,
                    NOTE_F5, 2, NOTE_E5, 4,
                    NOTE_DS5, 2, NOTE_B4, 4,
                    NOTE_DS5, -4, NOTE_D5, 8, NOTE_CS5, 4,
                    NOTE_CS4, 2, NOTE_AS4, 4,
                    NOTE_G4, -1, ],
}


import time
import machine

# change this to make the song slower or faster
tempo = 220

# this calculates the duration of a whole note in ms
wholenote = (60000 * 4) / tempo

def tone(pin,frequency,duration):
    if frequency is 0:
        pass
    else:
        pin.freq(frequency)
        pin.duty_u16(30000)
    time.sleep_ms(duration)
    pin.duty_u16(0)

def noTone(pin):
    tone(pin,0,100)

def play(pin,melody):

    # iterate over the notes of the melody.
    # Remember, the array is twice the number of notes (notes + durations)
    for thisNote in range(0,len(melody),2):
        # calculates the duration of each note
        divider = melody[thisNote+1]
        if divider > 0:
            noteDuration = wholenote/divider
        elif divider < 0:
            noteDuration = wholenote/-(divider)
            noteDuration *= 1.5

        # we only play the note for 90% of the duration, leaving 10% as a pause
        tone(pin,melody[thisNote],int(noteDuration*0.9))

        # Wait for the specief duration before playing the next note.
        time.sleep_ms(int(noteDuration))

        # stop the waveform generation before the next note.
        noTone(pin)
    

if __name__=='__main__':
    buzzer = machine.PWM(machine.Pin(15))
    melody=melody = song["gameofthrone"]
    play(buzzer,melody)