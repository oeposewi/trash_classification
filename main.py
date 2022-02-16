#from cameraCtrl import take_still
from stepperCtrl import stepperTurn


#take_still()


#stepperTurn(direction='cw', stepSeqLength='full', stepWait= .01, duration='off', totalSteps=256)
stepperTurn(direction='ccw', power='full', step_wait= .008, duration='off', rotations=1) 
