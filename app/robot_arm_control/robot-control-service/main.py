from fastapi import FastAPI
from ControlArm import ControlArmController
from .ControlRequest import ControlRequestData

app = FastAPI()

@app.get("/")
async def root():
    """return a welcome message

    Returns:
        _type_: string welcome message
    """
    return {"message": "Welcome, to the Robot Manipulation API!"}

@app.post("/robot/control/{servo}")
async def move_robot(request: ControlRequestData):
    """send a servo command to the robot arm

    Returns:
        _type_: void
    """
    # create controller
    arm_controller = ControlArmController()
    arm_controller.control_single_servo(request.servo, request.angle, request.time)
    return {"message": "command sent to robot arm"}

@app.post("/robot/control/")
async def move_robot_all(request: ControlRequestData):
    """send a move command to the robot arm

    Returns:
        _type_: string move command
    """
    # create controller
    arm_controller = ControlArmController()
    arm_controller.control_all_servo(request.angle, request.time)
    return {"message": "command sent to robot arm"}

@app.post("/robot/control/stop")
async def stop():
    """send a stop command to the robot arm

    Returns:
        _type_: string stop command
    """
    return {"message": "stop command sent"}

@app.post("/robot/control/reset")
async def reset():
    """send a reset command to the robot arm

    Returns:
        _type_: string reset command
    """
    return {"message": "reset command sent"}

@app.get("/robot/control/status")
async def status():
    """send a status command to the robot arm

    Returns:
        _type_: string status command
    """
    return {"message": "status command sent"}

@app.get("/robot/control/version")
async def version():
    """send a version command to the robot arm

    Returns:
        _type_: string version command
    """
    return {"message": "version command sent"}
