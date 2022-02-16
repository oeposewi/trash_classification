import time
from gpiozero import OutputDevice as stepper

# Set up pins
IN1 = stepper(17)
IN2 = stepper(27)
IN3 = stepper(22)
IN4 = stepper(23)
step_pins = [IN1,IN2,IN3,IN4] # Motor GPIO pins</p><p>

def stepperTurn(direction, power, step_wait, duration, rotations):
    # Full sequence has more power but rotates slower
    seq = [[1,0,0,1],
           [1,0,0,0],
           [1,1,0,0],
           [0,1,0,0],
           [0,1,1,0],
           [0,0,1,0],
           [0,0,1,1],
           [0,0,0,1]]
    # Direction
    if direction == 'ccw':
        seq.reverse()
    # Half sequence rotates faster with less power
    if power == 'half':
        seq = seq[1::2]
      
    # Set time between steps
    wait_time = 0.004
    if step_wait > 0.002:
        wait_time = step_wait
    
    total_steps = int(rotations * 512)
    step_counter = 0
    time_start = time.time()
    
    while True:
        for pins in seq:     # iterates through sequence
            for pin_num,pin_state in enumerate(pins):                 # iterates through pins
                
                x_pin=step_pins[pin_num]           # Get GPIO
                if pin_state == 1:
                    x_pin.on()
                else:
                    x_pin.off()
            time.sleep(wait_time)                         

        step_counter += 1        
        # end by time
        if type(duration) == int:    
            if (time.time() > (time_start + duration)):
                print('stepper stopped by time')
                for pin in range(0,4):
                    x_pin = step_pins[pin]
                    x_pin.off()
                break
        # End By Rotation
        if type(total_steps) == int:
            if step_counter >= total_steps:
                print('stepper stopped by step count')
                for pin in range(0,4):
                    step_pins[pin].off()
                break
#stepperTurn(direction='cw', power='full', step_wait= .005, duration='off', rotations=1) 

