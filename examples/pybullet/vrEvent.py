# See pybullet quickstart guide here:
# https://docs.google.com/document/d/10sXEhzFRSnvFcl3XxNGhnD4N2SedqwdAvK3dsihxVUA/edit#
# Create a Tiltbrush-like app, drawing lines using any controller
# Line width can be changed

import pybullet as p

CONTROLLER_ID = 0
POSITION=1
BUTTONS=6

#assume that the VR physics server is already started before
p.connect(p.SHARED_MEMORY)
p.setInternalSimFlags(0)#don't load default robot assets etc
p.resetSimulation()
p.loadURDF("plane.urdf")

prev=[None]*p.VR_MAX_CONTROLLERS
colors=[0.,0.5,0.5]*p.VR_MAX_CONTROLLERS
widths = [3]*p.VR_MAX_CONTROLLERS

#use a few default colors
colors[0] = [0,0,0]
colors[1] = [0.5,0,0]
colors[2] = [0,0.5,0]
colors[3] = [0,0,0.5]
colors[4] = [0.5,0.5,0.]
colors[5] = [.5,.5,.5]

while True:
	events = p.getVREvents()

	for e in (events):
		if (e[BUTTONS][33]&2):
			prev[e[CONTROLLER_ID]] = e[POSITION]
		if (e[BUTTONS][32]&2):
			widths[e[CONTROLLER_ID]]=widths[e[0]]+1
			if (widths[e[CONTROLLER_ID]]>20):
				widths[e[CONTROLLER_ID]] = 1
		if (e[BUTTONS][1]&2):
			p.resetSimulation()
			#p.setGravity(0,0,-10)
			p.removeAllUserDebugItems()
			p.loadURDF("plane.urdf")
		if (e[BUTTONS][33]==1):
			pt = prev[e[CONTROLLER_ID]]
			
			#print(prev[e[0]])
			#print(e[1])
			diff = [pt[0]-e[POSITION][0],pt[1]-e[POSITION][1],pt[2]-e[POSITION][2]]
			lenSqr =	diff[0]*diff[0]+diff[1]*diff[1]+diff[2]*diff[2]
			ptDistThreshold = 0.01
			if (lenSqr>(ptDistThreshold*ptDistThreshold)):
				p.addUserDebugLine(e[POSITION],prev[e[CONTROLLER_ID]],colors[e[CONTROLLER_ID]],widths[e[CONTROLLER_ID]])
				#p.loadURDF("cube_small.urdf",e[1])
				colors[e[CONTROLLER_ID]] = [1-colors[e[CONTROLLER_ID]][0],1-colors[e[CONTROLLER_ID]][1],1-colors[e[CONTROLLER_ID]][2]]
				prev[e[CONTROLLER_ID]] = e[POSITION]			