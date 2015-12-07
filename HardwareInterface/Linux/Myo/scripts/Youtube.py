
scriptTitle = "YouTube Controller"

def onPoseEdge(pose, edge):
	myo.setLockingPolicy("none")
	if myo.title_contains("YouTube"):
		if (pose == "waveOut"):
			if (edge == "on"): myo.keyboard("right_arrow","down","")
			if (edge == "off"): myo.keyboard("right_arrow","up","")
		if (pose == "waveIn"):
			if (edge == "on"): myo.keyboard("left_arrow","down","")
			if (edge == "off"): myo.keyboard("left_arrow","up","")
		if (pose == "fist") and (edge == "on"): 
			myo.keyboard("space","press","")


