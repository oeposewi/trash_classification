import time
from gpiozero import OutputDevice as stepper

# Set up pins
IN1 = stepper(17)
IN2 = stepper(27)
IN3 = stepper(22)
IN4 = stepper(23)
stepPins = [IN1,IN2,IN3,IN4] # Motor GPIO pins</p><p>

def stepperTurn(direction, stepSeqLength, stepWait, duration):
    # Direction
    stepDir = 1        # Set to 1 for clockwise
    if direction == 'ccw':
        stepDir = -1         # Set to -1 for anti-clockwise
    
    # Full sequence has more power but rotates slower
    seq = [[1,0,0,1],
           [1,0,0,0],
           [1,1,0,0],
           [0,1,0,0],
           [0,1,1,0],
           [0,0,1,0],
           [0,0,1,1],
           [0,0,0,1]]
    
    # Half sequence rotates faster with less power
    if stepSeqLength == 'half':
        seq = seq[1::2]
      
    # Set time between steps
    waitTime = 0.004
    if stepWait > 0.002:
        waitTime = stepWait

    stepCounter = 0    
    stepCount = len(seq)
    timeStart = time.time()
    
    while True:
        for pin in range(0,4):
            xPin=stepPins[pin]          # Get GPIO
            if seq[stepCounter][pin]!=0:
                xPin.on()
            else:
                xPin.off()
        stepCounter += stepDir
        if (stepCounter >= stepCount):
            stepCounter = 0
        if (stepCounter < 0):
            stepCounter = stepCount+stepDir
        print(stepCounter)
        time.sleep(waitTime)     # Wait before moving on
        if (time.time() > (timeStart+ duration)):
            for pin in range(0,4):
                xPin = stepPins[pin]
                xPin.off()
            break
        
#stepperTurn(direction='cw', stepSeqLength='full', stepWait= .006, duration=60)
