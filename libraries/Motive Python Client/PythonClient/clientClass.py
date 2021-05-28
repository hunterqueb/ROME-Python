from NatNetClient import NatNetClient

# we need to get a only a few things,
#   being able to determine which rigid body id is which
#   
#   position and orientation of every rigid body
#   ability to filter the data?

class NatNetClientClass(NatNetClient):
    def __init__(self):
        self.streamingClinet = super()
        self.streamingClient.newFrameListener = receiveNewFrame
        self.streamingClient.rigidBodyListener = initReceiveRigidBodyFrame

        #dictionary to get the id of whatever robot, set to none for now
        self.RigidBodyID = {'GV' : None, 'AR2' : None}

        #dictionary to get the pos and ori of whatever robot, set to none for now
        self.RigidBodyPosition = {'GV': None, 'AR2': None}
        self.RigidBodyOrientation = {'GV': None, 'AR2': None}
        
        #create temp files that will help us get the which robot is which
        self.tempID = 2 * [None]
        self.tempPos = 2 * [None]
        self.tempOri = 2 * [None]
        self.initCounter = 0

        self.streamingClient.run()

    def __del__(self):
        pass


# This is a callback function that gets connected to the NatNet client. It is called once frame

    def receiveNewFrame(self, frameNumber, markerSetCount, unlabeledMarkersCount, rigidBodyCount, skeletonCount,
                        labeledMarkerCount, timecode, timecodeSub, timestamp, isRecording, trackedModelsChanged):

        pass
    # print( "Received frame", frameNumber )
    # print( "Received rigidBodyCount", rigidBodyCount )


# This is a callback function that gets connected to the NatNet client. It is called once per rigid body per frame
    def receiveRigidBodyFrame(self,id, position, rotation):
        # rotation is in the format of quaternion
        # print( "Received frame for rigid body", id )
        self.RigidBodyPosition = position
        # we should format the rotation to the euler and give the option for quaternion
    

    def initReceiveRigidBodyFrame(self, id, position, rotation):
        # print( "Received frame for rigid body", id )
        # self.RigidBodyPosition = position
        # this will will run twice, to get the id of both rigid bodies

        # store the data of the rigid bodies in temp variables
        self.temp[self.initCounter] = id
        self.tempPos[self.initCounter] = position
        self.tempOri[self.initCounter] = rotation

        # counter to set make sure we do 2 loops of this function
        if self.initCounter == 0:
            self.initCounter += 1
        else:
            # one the second run of the function we compare the vertical axis values of the rigid bodies. from here, the arm will always have markers higher than the GV, 
            # so the depending on the value is what is stored in the dictonaries
            if tempPos[0].z > tempPos[1].z:
                self.RigidBodyID['AR2'] = self.tempID[0]
                self.RigidBodyID['GV'] = self.tempID[1]
                self.RigidBodyPos['AR2'] = self.tempPos[0]
                self.RigidBodyPos['GV'] = self.tempPos[1]
                self.RigidBodyOri['AR2'] = self.tempOri[0]
                self.RigidBodyOri['GV'] = self.tempOri[1]
            else:
                self.RigidBodyID['AR2'] = self.tempID[1]
                self.RigidBodyID['GV'] = self.tempID[0]
                self.RigidBodyPos['AR2'] = self.tempPos[1]
                self.RigidBodyPos['GV'] = self.tempPos[0]
                self.RigidBodyOri['AR2'] = self.tempOri[1]
                self.RigidBodyOri['GV'] = self.tempOri[0]
            
            # now we delete the temp variables
            del self.tempID
            del self.tempPos
            del self.tempOri
            del self.initCounter
                
            # set the listener to the regular rigidbodyframe listener
            self.streamingClient.rigidBodyListener = receiveRigidBodyFrame
