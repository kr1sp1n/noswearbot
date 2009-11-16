from waveapi import events
from waveapi import model
from waveapi import robot
import re

def OnParticipantsChanged(properties, context):
  """Invoked when any participants have been added/removed."""
  added = properties['participantsAdded']
  for p in added:
    Notify(context)

def OnRobotAdded(properties, context):
  """Invoked when the robot has been added."""
  root_wavelet = context.GetRootWavelet()
  root_wavelet.CreateBlip().GetDocument().SetText("I'm alive!")

def OnBlipSubmitted(properties, context):
  """Invoked when a blip has been submitted."""
  root_wavelet = context.GetRootWavelet()
  blip = context.GetBlipById(properties['blipId'])
  contents = blip.GetDocument().GetText()
  p = re.compile( '(fuck|shit|damn)')
  contents = p.sub( '$%*&', contents)
  #root_wavelet.CreateBlip().GetDocument().SetText(contents)
  blip.GetDocument().SetText(contents)

def Notify(context):
  root_wavelet = context.GetRootWavelet()
  root_wavelet.CreateBlip().GetDocument().SetText("Swear filter active! Following words will be censored: 'shit', 'fuck' and 'damn'.")

def initRobot():
  myRobot = robot.Robot('noswearbot', image_url='http://noswearbot.appspot.com/assets/icon.png', version='1', profile_url='http://noswearbot.appspot.com/')
  myRobot.RegisterHandler(events.WAVELET_PARTICIPANTS_CHANGED, OnParticipantsChanged)
  myRobot.RegisterHandler(events.WAVELET_SELF_ADDED, OnRobotAdded)
  myRobot.RegisterHandler(events.BLIP_SUBMITTED, OnBlipSubmitted)
  myRobot.Run()

def main():
  initRobot()

if __name__ == "__main__":
  main()