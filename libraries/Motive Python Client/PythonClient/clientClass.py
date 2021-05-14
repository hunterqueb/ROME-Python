from NatNetClient import NatNetClient


class NatNetClientClass(NatNetClient):
    def __init__(self):
        self.streamingClinet = super()
        self.streamingClient.newFrameListener = receiveNewFrame
        self.streamingClient.rigidBodyListener = receiveRigidBodyFrame

        self.RigidBodyPosition = 2*[None]
        self.RigidBodyOrientation = 2*[None]
        self.RigidBodyID = 2*[None]

        self.streamingClient.run()

    def initReceiveNewFrame(self, frameNumber, markerSetCount, unlabeledMarkersCount, rigidBodyCount, skeletonCount,
                        labeledMarkerCount, timecode, timecodeSub, timestamp, isRecording, trackedModelsChanged):

        pass

    def initReceiveRigidBodyFrame(self, id, position, rotation):
        # rotation is in the format of quaternion
        # print( "Received frame for rigid body", id )
        self.RigidBodyPosition = position


# Here, we should use this to define which robot is defined where based on the rigidbodyid
    def receiveNewFrame(self,frameNumber, markerSetCount, unlabeledMarkersCount, rigidBodyCount, skeletonCount,
                        labeledMarkerCount, timecode, timecodeSub, timestamp, isRecording, trackedModelsChanged):

        pass
    # print( "Received frame", frameNumber )
    # print( "Received rigidBodyCount", rigidBodyCount )


# This is a callback function that gets connected to the NatNet client. It is called once per rigid body per frame
    def receiveRigidBodyFrame(self,id, position, rotation):
        # rotation is in the format of quaternion
        # print( "Received frame for rigid body", id )
        self.RigidBodyPosition = position

    def findRigidBody(self,robot):
        # call this to return the id for the rigid body for any robot specified
        pass
    
