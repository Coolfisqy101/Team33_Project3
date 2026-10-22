
from buildhat import Motor
from buildhat import LineFinder
import time

def forward(speed):
    motor1.speed(speed)
    motor2.speed(-speed) 

def left(speed):
    motor1.speed(speed)
    motor2.speed(speed)

def right(speed):
    motor1.speed(-speed)
    motor2.speed(-speed)

def back(speed):
    motor1.speed(-speed)
    motor2.speed(speed)


def main():
    pinM1 = yyy
    pinM2 = www
    pinL1 = xxx
    pinL2 = zzz
    motor1 = motor(pinM1)
    motor2 = motor(pinM2)
    lineFinder1 = lineFinder(pinL1)
    lineFinder2 = lineFinder(pinL2)

    try:
        curValue1 = lineFinder1.value
        curValue2 = lineFinder2.value
        if curValue1=1:
            left(xxx)
        elif curValue2=1:
            right(xxx)
        else:
            forward(xxx)

if __name__ == "__main__":
    main()
