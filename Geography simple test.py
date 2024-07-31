print('---Welcome to this test---') #Heading/greeting 

#initialize the test by asking the user to begin
playing = input('Do  you want to play? (y/n)')
if playing != 'y':
    quit()

print('---The following will be a quick test to gauge your understanding in Geography---\n') #Subheading

score = 0 #Score counter 

print('Question 1: Which are the forces which have contributed to the geoid shape of the Earth \n A. Centrifugal \n B. Centripetal \n C. Gravity \n D. Friction') #only one answer is correct

answer = input('Answer is ').upper() 
if answer == 'A':
    print ('Correct')
    score += 2
else:
    print('Incorrect')

print('Question 2: Three divisions of physical geography \n A. Geomorphology \n B. Climatology \n C. Rockology \n D. Meteorology \n E. Volcanology \n F. Seismology') #multiple answers will be correct

answer = input('Answer is ').upper()
if answer == 'A' or 'B' or 'D':
    print ('Correct')
    score += 2
else:
    print('Incorrect')

print('Question 3: Two types of igneous rocks \n A. Extrusive \n B. Metamorphic  \n C. Intrusive \n D. Sedimentary \n E. Conglomerate') 

answer = input('Answer is ').upper()
if answer == 'A' or 'C':
    print ('Correct')
    score += 2 
else:
    print('Incorrect')

print('-----Your final score is---- \n '+  str(score)+' Out of 6')


