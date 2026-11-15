
from controller import Robot

robot = Robot()
timestep = int(robot.getBasicTimeStep())

# Motors
left_motor = robot.getDevice("left wheel")
right_motor = robot.getDevice("right wheel")

left_motor.setPosition(float("inf"))
right_motor.setPosition(float("inf"))

left_motor.setVelocity(0.0)
right_motor.setVelocity(0.0)

# Sensor de distància
sensor = robot.getDevice("so0")
sensor.enable(timestep)

while robot.step(timestep) != -1:
    distance = sensor.getValue()
    print("Sensor so0:", distance)

    if distance > 500:
        # Girar
        left_motor.setVelocity(-3.0)
        right_motor.setVelocity(3.0)
    else:
        # Avançar
        left_motor.setVelocity(5.0)
        right_motor.setVelocity(5.0)
