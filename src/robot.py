from vendor import DobotDllType as dType

CON_STR = {
    dType.DobotConnect.DobotConnect_NoError:  "DobotConnect_NoError",
    dType.DobotConnect.DobotConnect_NotFound: "DobotConnect_NotFound",
    dType.DobotConnect.DobotConnect_Occupied: "DobotConnect_Occupied"}

class RobotArm():
    homePos = [160, 0, 0, 0]

    def __init__(self):
        # robot arm initilize
        try:
            self.api = dType.load()
        except OSError as e:
            sys.exit(1)
        state = dType.ConnectDobot(self.api, "", 115200)[0]
        if CON_STR[state] != "DobotConnect_NoError":
            print('connection status: ' + CON_STR[state])
        dType.SetQueuedCmdClear(self.api)
        dType.SetHOMEParams(self.api,self.homePos[0], self.homePos[1], self.homePos[2], self.homePos[3], isQueued=1)
        dType.SetPTPJointParams(self.api,200,200,200,200,200,200,200,200, isQueued=1)
        dType.SetPTPCoordinateParams(self.api,200,200,200,200, isQueued=1)
        dType.SetPTPCommonParams(self.api, 100, 100, isQueued=1)
        lastIndex = dType.SetPTPCommonParams(self.api, 100, 100, isQueued=1)[0]

        dType.SetQueuedCmdStartExec(self.api)
        doSleep = False
        while lastIndex > dType.GetQueuedCmdCurrentIndex(self.api)[0]:
            doSleep = True
            dType.dSleep(100)
        if not doSleep:
            dType.dSleep(20000)
        dType.SetQueuedCmdStopExec(self.api)

    def __del__(self):
        # robot arm finshing
        if self.api is not None:
            dType.DisconnectDobot(self.api)

    def move_point(self, point):
        # moving point
        pass
