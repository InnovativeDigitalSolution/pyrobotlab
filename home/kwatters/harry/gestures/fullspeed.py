def fullspeed():
  if isRightHandActivated:
    i01.setHandVelocity("right", -1, -1, -1, -1, -1, -1)
      
  if isLeftHandActivated:
    i01.setHandVelocity("left", -1, -1, -1, -1, -1, -1)
      
  if isRightArmActivated:
    i01.setArmVelocity("right", -1, -1, -1, -1)
    
  if isLeftArmActivated:
    i01.setArmVelocity("left", -1, -1, -1, -1)
  
  if isHeadActivated:
    i01.setHeadVelocity(-1, -1, -1)
  
  if isTorsoActivated:
    i01.setTorsoVelocity(-1, -1, -1)
      
  if isEyeLidsActivated:
    i01.setEyelidsVelocity(-1,-1)

