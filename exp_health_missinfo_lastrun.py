#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.1.1),
    on Fri Dec  6 10:47:14 2024
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

import psychopy
psychopy.useVersion('2023.1.1')


# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# Run 'Before Experiment' code from ShufflerCode
from random import shuffle, sample
#random.seed(1)


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2023.1.1'
expName = 'exp_corregido'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
    'group': 'AB',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/guillermopuebla/Projects/health_missinformation/exp_health_missinfo_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1440, 900], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=True,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    backgroundImage='', backgroundFit='none',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "NewsLoader" ---
# Run 'Begin Experiment' code from LoaderCode
# Initialize lists of items and problems
data_list = []
problem_list = []


# --- Initialize components for Routine "NewsShuffler" ---

# --- Initialize components for Routine "IntroNews" ---
text = visual.TextStim(win=win, name='text',
    text='En este estudio tendrás que evaluar la veracidad de varias noticias. Además tendrás que memorizar una secuencia de números por un corto período de tiempo.\n\nEl estudio está dividido en dos bloques. Podrás tomar un descanzo al final del segundo bloque.\n\nPara empezar presiona ENTER.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "blank500" ---
text_2 = visual.TextStim(win=win, name='text_2',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "NumberA" ---
# Run 'Begin Experiment' code from NumberPresentCode
# Counter for items and problems
current_item = -1
text_number_a = visual.TextStim(win=win, name='text_number_a',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
number_presentation_key_a = keyboard.Keyboard()

# --- Initialize components for Routine "NewsTrial" ---
text_item = visual.TextStim(win=win, name='text_item',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
item_response = keyboard.Keyboard()

# --- Initialize components for Routine "blank500" ---
text_2 = visual.TextStim(win=win, name='text_2',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "TypedResponse" ---
textInput = visual.TextStim(win=win, name='textInput',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
textPrompt = visual.TextStim(win=win, name='textPrompt',
    text='Escribe el número presentado (sólo dígitos) y presiona ENTER para continuar...',
    font='Open Sans',
    pos=(0, 0.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
keyResp = keyboard.Keyboard()

# --- Initialize components for Routine "blank500" ---
text_2 = visual.TextStim(win=win, name='text_2',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "RestScreen" ---
rest_text = visual.TextStim(win=win, name='rest_text',
    text='Ahora puedes descansar...\n\nPresiona ESPACIO para continuar con el segundo bloque.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
rest_end_key = keyboard.Keyboard()

# --- Initialize components for Routine "NumberB" ---
text_number_b = visual.TextStim(win=win, name='text_number_b',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
number_presentation_key_b = keyboard.Keyboard()

# --- Initialize components for Routine "TypedResponse" ---
textInput = visual.TextStim(win=win, name='textInput',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
textPrompt = visual.TextStim(win=win, name='textPrompt',
    text='Escribe el número presentado (sólo dígitos) y presiona ENTER para continuar...',
    font='Open Sans',
    pos=(0, 0.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
keyResp = keyboard.Keyboard()

# --- Initialize components for Routine "blank500" ---
text_2 = visual.TextStim(win=win, name='text_2',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "NewsTrial" ---
text_item = visual.TextStim(win=win, name='text_item',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
item_response = keyboard.Keyboard()

# --- Initialize components for Routine "blank500" ---
text_2 = visual.TextStim(win=win, name='text_2',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "GoodbyeScreen" ---
text_3 = visual.TextStim(win=win, name='text_3',
    text='Felicitaciones! estas a punto de terminar el estudio.\n\nPresiona ESPACIO para terminar.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('items_noticias_2.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "NewsLoader" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from LoaderCode
    # Polulate items list
    data_list.append((item_id, item, criteria))
    
    # keep track of which components have finished
    NewsLoaderComponents = []
    for thisComponent in NewsLoaderComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "NewsLoader" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in NewsLoaderComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "NewsLoader" ---
    for thisComponent in NewsLoaderComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "NewsLoader" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials'


# --- Prepare to start Routine "NewsShuffler" ---
continueRoutine = True
# update component parameters for each repeat
# Run 'Begin Routine' code from ShufflerCode
# Polulate items list
# data_list.append((item_id, item, criteria))

# Randomize input data
shuffle(data_list)
print('data_list length: ', len(data_list))

# There are 10 true and 26 false items.
n_true = 16
half_true = int(n_true/2)
n_false = 16
half_false = int(n_false/2)

# Make two lists, randomize and then join together
data_true = [x for x in data_list if x[2] == 1]
data_false = [x for x in data_list if x[2] == 0]

data_a = data_true[0:half_true] + data_false[0:half_false]
data_b = data_true[half_true:n_true] + data_false[half_false:n_false]

for x, y, z in data_a:
    print(x, z)

print('')

for x, y, z in data_b:
    print(x, z)

print('')

shuffle(data_a)
shuffle(data_b)

for x, y, z in data_a:
    print(x, z)

print('')

for x, y, z in data_b:
    print(x, z)
data_list = data_a + data_b



# Get list sizes for blocks
n_a = len(data_a)
n_b = len(data_b)

print(f'n_a: {n_a}')
print(f'n_b: {n_b}')

# Get id, item and criteria
data_list = list(zip(*data_list))
id_list = list(data_list[0])
item_list = list(data_list[1])
criteria_list = list(data_list[2])

# Populate problem list
for i in range(len(item_list)):
    numbers = sample(range(1, 10), 5)
    string_numbers = ''.join(str(x) for x in numbers)
    problem_list.append(string_numbers)

# keep track of which components have finished
NewsShufflerComponents = []
for thisComponent in NewsShufflerComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "NewsShuffler" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in NewsShufflerComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "NewsShuffler" ---
for thisComponent in NewsShufflerComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "NewsShuffler" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "IntroNews" ---
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
IntroNewsComponents = [text, key_resp]
for thisComponent in IntroNewsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "IntroNews" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    
    # if text is starting this frame...
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text.started')
        # update status
        text.status = STARTED
        text.setAutoDraw(True)
    
    # if text is active this frame...
    if text.status == STARTED:
        # update params
        pass
    
    # *key_resp* updates
    waitOnFlip = False
    
    # if key_resp is starting this frame...
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp.started')
        # update status
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['return'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in IntroNewsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "IntroNews" ---
for thisComponent in IntroNewsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.nextEntry()
# the Routine "IntroNews" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "blank500" ---
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
blank500Components = [text_2]
for thisComponent in blank500Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "blank500" ---
routineForceEnded = not continueRoutine
while continueRoutine and routineTimer.getTime() < 0.5:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    
    # if text_2 is starting this frame...
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_2.started')
        # update status
        text_2.status = STARTED
        text_2.setAutoDraw(True)
    
    # if text_2 is active this frame...
    if text_2.status == STARTED:
        # update params
        pass
    
    # if text_2 is stopping this frame...
    if text_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_2.tStartRefresh + 0.5-frameTolerance:
            # keep track of stop time/frame for later
            text_2.tStop = t  # not accounting for scr refresh
            text_2.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_2.stopped')
            # update status
            text_2.status = FINISHED
            text_2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in blank500Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "blank500" ---
for thisComponent in blank500Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-0.500000)

# set up handler to look after randomisation of conditions etc
controlTaskOrder = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditions'+expInfo['group']+'.xlsx'),
    seed=None, name='controlTaskOrder')
thisExp.addLoop(controlTaskOrder)  # add the loop to the experiment
thisControlTaskOrder = controlTaskOrder.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisControlTaskOrder.rgb)
if thisControlTaskOrder != None:
    for paramName in thisControlTaskOrder:
        exec('{} = thisControlTaskOrder[paramName]'.format(paramName))

for thisControlTaskOrder in controlTaskOrder:
    currentLoop = controlTaskOrder
    # abbreviate parameter names if possible (e.g. rgb = thisControlTaskOrder.rgb)
    if thisControlTaskOrder != None:
        for paramName in thisControlTaskOrder:
            exec('{} = thisControlTaskOrder[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    block_a = data.TrialHandler(nReps=nRepsTask1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='block_a')
    thisExp.addLoop(block_a)  # add the loop to the experiment
    thisBlock_a = block_a.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisBlock_a.rgb)
    if thisBlock_a != None:
        for paramName in thisBlock_a:
            exec('{} = thisBlock_a[paramName]'.format(paramName))
    
    for thisBlock_a in block_a:
        currentLoop = block_a
        # abbreviate parameter names if possible (e.g. rgb = thisBlock_a.rgb)
        if thisBlock_a != None:
            for paramName in thisBlock_a:
                exec('{} = thisBlock_a[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "NumberA" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from NumberPresentCode
        # Update counter at each trial
        current_item += 1
        
        # Update item and problem variables
        item = item_list[current_item]
        item_id = id_list[current_item]
        item_target = criteria_list[current_item]
        
        number_string = problem_list[current_item]
        
        
        text_number_a.setText(f"Recuerda este número: {str(number_string)} \n \n Presiona ENTER para continuar.")
        number_presentation_key_a.keys = []
        number_presentation_key_a.rt = []
        _number_presentation_key_a_allKeys = []
        # keep track of which components have finished
        NumberAComponents = [text_number_a, number_presentation_key_a]
        for thisComponent in NumberAComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "NumberA" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_number_a* updates
            
            # if text_number_a is starting this frame...
            if text_number_a.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_number_a.frameNStart = frameN  # exact frame index
                text_number_a.tStart = t  # local t and not account for scr refresh
                text_number_a.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_number_a, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_number_a.started')
                # update status
                text_number_a.status = STARTED
                text_number_a.setAutoDraw(True)
            
            # if text_number_a is active this frame...
            if text_number_a.status == STARTED:
                # update params
                pass
            
            # *number_presentation_key_a* updates
            waitOnFlip = False
            
            # if number_presentation_key_a is starting this frame...
            if number_presentation_key_a.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                number_presentation_key_a.frameNStart = frameN  # exact frame index
                number_presentation_key_a.tStart = t  # local t and not account for scr refresh
                number_presentation_key_a.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(number_presentation_key_a, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'number_presentation_key_a.started')
                # update status
                number_presentation_key_a.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(number_presentation_key_a.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(number_presentation_key_a.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if number_presentation_key_a.status == STARTED and not waitOnFlip:
                theseKeys = number_presentation_key_a.getKeys(keyList=['return'], waitRelease=False)
                _number_presentation_key_a_allKeys.extend(theseKeys)
                if len(_number_presentation_key_a_allKeys):
                    number_presentation_key_a.keys = _number_presentation_key_a_allKeys[-1].name  # just the last key pressed
                    number_presentation_key_a.rt = _number_presentation_key_a_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
                if eyetracker:
                    eyetracker.setConnectionState(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in NumberAComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "NumberA" ---
        for thisComponent in NumberAComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from NumberPresentCode
        # Save item and math problem info to file
        thisExp.addData('item', item)
        thisExp.addData('item_id', item_id)
        thisExp.addData('item_target', item_target)
        thisExp.addData('number_string', number_string)
        # check responses
        if number_presentation_key_a.keys in ['', [], None]:  # No response was made
            number_presentation_key_a.keys = None
        block_a.addData('number_presentation_key_a.keys',number_presentation_key_a.keys)
        if number_presentation_key_a.keys != None:  # we had a response
            block_a.addData('number_presentation_key_a.rt', number_presentation_key_a.rt)
        # the Routine "NumberA" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "NewsTrial" ---
        continueRoutine = True
        # update component parameters for each repeat
        text_item.setText(f"{str(item)} \n \n Presiona 'q' para responder verdadero o 'p' para responder falso.")
        item_response.keys = []
        item_response.rt = []
        _item_response_allKeys = []
        # keep track of which components have finished
        NewsTrialComponents = [text_item, item_response]
        for thisComponent in NewsTrialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "NewsTrial" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_item* updates
            
            # if text_item is starting this frame...
            if text_item.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_item.frameNStart = frameN  # exact frame index
                text_item.tStart = t  # local t and not account for scr refresh
                text_item.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_item, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_item.started')
                # update status
                text_item.status = STARTED
                text_item.setAutoDraw(True)
            
            # if text_item is active this frame...
            if text_item.status == STARTED:
                # update params
                pass
            
            # *item_response* updates
            waitOnFlip = False
            
            # if item_response is starting this frame...
            if item_response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                item_response.frameNStart = frameN  # exact frame index
                item_response.tStart = t  # local t and not account for scr refresh
                item_response.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(item_response, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'item_response.started')
                # update status
                item_response.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(item_response.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(item_response.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if item_response.status == STARTED and not waitOnFlip:
                theseKeys = item_response.getKeys(keyList=['q', 'p'], waitRelease=False)
                _item_response_allKeys.extend(theseKeys)
                if len(_item_response_allKeys):
                    item_response.keys = _item_response_allKeys[-1].name  # just the last key pressed
                    item_response.rt = _item_response_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
                if eyetracker:
                    eyetracker.setConnectionState(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in NewsTrialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "NewsTrial" ---
        for thisComponent in NewsTrialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if item_response.keys in ['', [], None]:  # No response was made
            item_response.keys = None
        block_a.addData('item_response.keys',item_response.keys)
        if item_response.keys != None:  # we had a response
            block_a.addData('item_response.rt', item_response.rt)
        # the Routine "NewsTrial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "blank500" ---
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        blank500Components = [text_2]
        for thisComponent in blank500Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "blank500" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_2* updates
            
            # if text_2 is starting this frame...
            if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_2.frameNStart = frameN  # exact frame index
                text_2.tStart = t  # local t and not account for scr refresh
                text_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_2.started')
                # update status
                text_2.status = STARTED
                text_2.setAutoDraw(True)
            
            # if text_2 is active this frame...
            if text_2.status == STARTED:
                # update params
                pass
            
            # if text_2 is stopping this frame...
            if text_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_2.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    text_2.tStop = t  # not accounting for scr refresh
                    text_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_2.stopped')
                    # update status
                    text_2.status = FINISHED
                    text_2.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
                if eyetracker:
                    eyetracker.setConnectionState(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in blank500Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "blank500" ---
        for thisComponent in blank500Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.500000)
        
        # --- Prepare to start Routine "TypedResponse" ---
        continueRoutine = True
        # update component parameters for each repeat
        keyResp.keys = []
        keyResp.rt = []
        _keyResp_allKeys = []
        # Run 'Begin Routine' code from codeResp
        respDisplay = ""
        maxDigits = 5
        
        #key logger defaults
        last_len = 0
        key_list = []
        # keep track of which components have finished
        TypedResponseComponents = [textInput, textPrompt, keyResp]
        for thisComponent in TypedResponseComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "TypedResponse" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *textInput* updates
            
            # if textInput is starting this frame...
            if textInput.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                textInput.frameNStart = frameN  # exact frame index
                textInput.tStart = t  # local t and not account for scr refresh
                textInput.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textInput, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textInput.started')
                # update status
                textInput.status = STARTED
                textInput.setAutoDraw(True)
            
            # if textInput is active this frame...
            if textInput.status == STARTED:
                # update params
                textInput.setText(respDisplay, log=False)
            
            # *textPrompt* updates
            
            # if textPrompt is starting this frame...
            if textPrompt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                textPrompt.frameNStart = frameN  # exact frame index
                textPrompt.tStart = t  # local t and not account for scr refresh
                textPrompt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textPrompt, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textPrompt.started')
                # update status
                textPrompt.status = STARTED
                textPrompt.setAutoDraw(True)
            
            # if textPrompt is active this frame...
            if textPrompt.status == STARTED:
                # update params
                pass
            
            # *keyResp* updates
            waitOnFlip = False
            
            # if keyResp is starting this frame...
            if keyResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                keyResp.frameNStart = frameN  # exact frame index
                keyResp.tStart = t  # local t and not account for scr refresh
                keyResp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(keyResp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'keyResp.started')
                # update status
                keyResp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(keyResp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(keyResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if keyResp.status == STARTED and not waitOnFlip:
                theseKeys = keyResp.getKeys(keyList=['0','1','2','3','4','5','6','7','8','9','return','backspace'], waitRelease=False)
                _keyResp_allKeys.extend(theseKeys)
                if len(_keyResp_allKeys):
                    keyResp.keys = [key.name for key in _keyResp_allKeys]  # storing all keys
                    keyResp.rt = [key.rt for key in _keyResp_allKeys]
            # Run 'Each Frame' code from codeResp
            #if a new key has been pressed since last time
            
            if(len(keyResp.keys) > last_len):
                #increment the key logger length
                last_len = len(keyResp.keys)
                
                #grab the last key added to the keys list
                key_list.append(keyResp.keys.pop())
            
                #check for backspace
                if("backspace" in key_list):
                    key_list.remove("backspace")
            
                    #if we have at least 1 character, remove it
                    if(len(key_list) > 0):
                        key_list.pop()
                        
                #if enter is pressed then...
                elif("return" in key_list):
                    #remove the enter key
                    key_list.pop()
                    
                    #and end the trial if we have at least 2 digits
                    if(len(key_list) >= 2):
                        continueRoutine = False
            
                #now loop through and remove any extra characters that may exist
            
                while(len(key_list) > maxDigits):
                    key_list.pop()
            
                #create a variable to display
                respDisplay = ''.join(key_list)
            
            
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
                if eyetracker:
                    eyetracker.setConnectionState(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in TypedResponseComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "TypedResponse" ---
        for thisComponent in TypedResponseComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if keyResp.keys in ['', [], None]:  # No response was made
            keyResp.keys = None
        block_a.addData('keyResp.keys',keyResp.keys)
        if keyResp.keys != None:  # we had a response
            block_a.addData('keyResp.rt', keyResp.rt)
        # Run 'End Routine' code from codeResp
        thisExp.addData('subjResponse', respDisplay)
        # the Routine "TypedResponse" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "blank500" ---
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        blank500Components = [text_2]
        for thisComponent in blank500Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "blank500" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_2* updates
            
            # if text_2 is starting this frame...
            if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_2.frameNStart = frameN  # exact frame index
                text_2.tStart = t  # local t and not account for scr refresh
                text_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_2.started')
                # update status
                text_2.status = STARTED
                text_2.setAutoDraw(True)
            
            # if text_2 is active this frame...
            if text_2.status == STARTED:
                # update params
                pass
            
            # if text_2 is stopping this frame...
            if text_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_2.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    text_2.tStop = t  # not accounting for scr refresh
                    text_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_2.stopped')
                    # update status
                    text_2.status = FINISHED
                    text_2.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
                if eyetracker:
                    eyetracker.setConnectionState(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in blank500Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "blank500" ---
        for thisComponent in blank500Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.500000)
        thisExp.nextEntry()
        
    # completed nRepsTask1 repeats of 'block_a'
    
    
    # set up handler to look after randomisation of conditions etc
    rest = data.TrialHandler(nReps=nRepsTask2, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='rest')
    thisExp.addLoop(rest)  # add the loop to the experiment
    thisRest = rest.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisRest.rgb)
    if thisRest != None:
        for paramName in thisRest:
            exec('{} = thisRest[paramName]'.format(paramName))
    
    for thisRest in rest:
        currentLoop = rest
        # abbreviate parameter names if possible (e.g. rgb = thisRest.rgb)
        if thisRest != None:
            for paramName in thisRest:
                exec('{} = thisRest[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "RestScreen" ---
        continueRoutine = True
        # update component parameters for each repeat
        rest_end_key.keys = []
        rest_end_key.rt = []
        _rest_end_key_allKeys = []
        # keep track of which components have finished
        RestScreenComponents = [rest_text, rest_end_key]
        for thisComponent in RestScreenComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "RestScreen" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *rest_text* updates
            
            # if rest_text is starting this frame...
            if rest_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rest_text.frameNStart = frameN  # exact frame index
                rest_text.tStart = t  # local t and not account for scr refresh
                rest_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rest_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'rest_text.started')
                # update status
                rest_text.status = STARTED
                rest_text.setAutoDraw(True)
            
            # if rest_text is active this frame...
            if rest_text.status == STARTED:
                # update params
                pass
            
            # *rest_end_key* updates
            waitOnFlip = False
            
            # if rest_end_key is starting this frame...
            if rest_end_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rest_end_key.frameNStart = frameN  # exact frame index
                rest_end_key.tStart = t  # local t and not account for scr refresh
                rest_end_key.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rest_end_key, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'rest_end_key.started')
                # update status
                rest_end_key.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(rest_end_key.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(rest_end_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if rest_end_key.status == STARTED and not waitOnFlip:
                theseKeys = rest_end_key.getKeys(keyList=['space'], waitRelease=False)
                _rest_end_key_allKeys.extend(theseKeys)
                if len(_rest_end_key_allKeys):
                    rest_end_key.keys = _rest_end_key_allKeys[-1].name  # just the last key pressed
                    rest_end_key.rt = _rest_end_key_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
                if eyetracker:
                    eyetracker.setConnectionState(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in RestScreenComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "RestScreen" ---
        for thisComponent in RestScreenComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if rest_end_key.keys in ['', [], None]:  # No response was made
            rest_end_key.keys = None
        rest.addData('rest_end_key.keys',rest_end_key.keys)
        if rest_end_key.keys != None:  # we had a response
            rest.addData('rest_end_key.rt', rest_end_key.rt)
        # the Routine "RestScreen" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed nRepsTask2 repeats of 'rest'
    
    
    # set up handler to look after randomisation of conditions etc
    block_b = data.TrialHandler(nReps=nRepsTask3, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='block_b')
    thisExp.addLoop(block_b)  # add the loop to the experiment
    thisBlock_b = block_b.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisBlock_b.rgb)
    if thisBlock_b != None:
        for paramName in thisBlock_b:
            exec('{} = thisBlock_b[paramName]'.format(paramName))
    
    for thisBlock_b in block_b:
        currentLoop = block_b
        # abbreviate parameter names if possible (e.g. rgb = thisBlock_b.rgb)
        if thisBlock_b != None:
            for paramName in thisBlock_b:
                exec('{} = thisBlock_b[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "NumberB" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from NumberPresentCode_2
        # Update counter at each trial
        current_item += 1
        
        # Update item and problem variables
        item = item_list[current_item]
        item_id = id_list[current_item]
        item_target = criteria_list[current_item]
        
        number_string = problem_list[current_item]
        
        text_number_b.setText(f"Recuerda este número: {str(number_string)} \n \n Presiona ENTER para continuar.")
        number_presentation_key_b.keys = []
        number_presentation_key_b.rt = []
        _number_presentation_key_b_allKeys = []
        # keep track of which components have finished
        NumberBComponents = [text_number_b, number_presentation_key_b]
        for thisComponent in NumberBComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "NumberB" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_number_b* updates
            
            # if text_number_b is starting this frame...
            if text_number_b.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_number_b.frameNStart = frameN  # exact frame index
                text_number_b.tStart = t  # local t and not account for scr refresh
                text_number_b.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_number_b, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_number_b.started')
                # update status
                text_number_b.status = STARTED
                text_number_b.setAutoDraw(True)
            
            # if text_number_b is active this frame...
            if text_number_b.status == STARTED:
                # update params
                pass
            
            # *number_presentation_key_b* updates
            waitOnFlip = False
            
            # if number_presentation_key_b is starting this frame...
            if number_presentation_key_b.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                number_presentation_key_b.frameNStart = frameN  # exact frame index
                number_presentation_key_b.tStart = t  # local t and not account for scr refresh
                number_presentation_key_b.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(number_presentation_key_b, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'number_presentation_key_b.started')
                # update status
                number_presentation_key_b.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(number_presentation_key_b.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(number_presentation_key_b.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if number_presentation_key_b.status == STARTED and not waitOnFlip:
                theseKeys = number_presentation_key_b.getKeys(keyList=['return'], waitRelease=False)
                _number_presentation_key_b_allKeys.extend(theseKeys)
                if len(_number_presentation_key_b_allKeys):
                    number_presentation_key_b.keys = _number_presentation_key_b_allKeys[-1].name  # just the last key pressed
                    number_presentation_key_b.rt = _number_presentation_key_b_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
                if eyetracker:
                    eyetracker.setConnectionState(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in NumberBComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "NumberB" ---
        for thisComponent in NumberBComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from NumberPresentCode_2
        # Save item and math problem info to file
        thisExp.addData('item', item)
        thisExp.addData('item_id', item_id)
        thisExp.addData('item_target', item_target)
        thisExp.addData('number_string', number_string)
        
        # check responses
        if number_presentation_key_b.keys in ['', [], None]:  # No response was made
            number_presentation_key_b.keys = None
        block_b.addData('number_presentation_key_b.keys',number_presentation_key_b.keys)
        if number_presentation_key_b.keys != None:  # we had a response
            block_b.addData('number_presentation_key_b.rt', number_presentation_key_b.rt)
        # the Routine "NumberB" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "TypedResponse" ---
        continueRoutine = True
        # update component parameters for each repeat
        keyResp.keys = []
        keyResp.rt = []
        _keyResp_allKeys = []
        # Run 'Begin Routine' code from codeResp
        respDisplay = ""
        maxDigits = 5
        
        #key logger defaults
        last_len = 0
        key_list = []
        # keep track of which components have finished
        TypedResponseComponents = [textInput, textPrompt, keyResp]
        for thisComponent in TypedResponseComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "TypedResponse" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *textInput* updates
            
            # if textInput is starting this frame...
            if textInput.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                textInput.frameNStart = frameN  # exact frame index
                textInput.tStart = t  # local t and not account for scr refresh
                textInput.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textInput, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textInput.started')
                # update status
                textInput.status = STARTED
                textInput.setAutoDraw(True)
            
            # if textInput is active this frame...
            if textInput.status == STARTED:
                # update params
                textInput.setText(respDisplay, log=False)
            
            # *textPrompt* updates
            
            # if textPrompt is starting this frame...
            if textPrompt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                textPrompt.frameNStart = frameN  # exact frame index
                textPrompt.tStart = t  # local t and not account for scr refresh
                textPrompt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textPrompt, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textPrompt.started')
                # update status
                textPrompt.status = STARTED
                textPrompt.setAutoDraw(True)
            
            # if textPrompt is active this frame...
            if textPrompt.status == STARTED:
                # update params
                pass
            
            # *keyResp* updates
            waitOnFlip = False
            
            # if keyResp is starting this frame...
            if keyResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                keyResp.frameNStart = frameN  # exact frame index
                keyResp.tStart = t  # local t and not account for scr refresh
                keyResp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(keyResp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'keyResp.started')
                # update status
                keyResp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(keyResp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(keyResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if keyResp.status == STARTED and not waitOnFlip:
                theseKeys = keyResp.getKeys(keyList=['0','1','2','3','4','5','6','7','8','9','return','backspace'], waitRelease=False)
                _keyResp_allKeys.extend(theseKeys)
                if len(_keyResp_allKeys):
                    keyResp.keys = [key.name for key in _keyResp_allKeys]  # storing all keys
                    keyResp.rt = [key.rt for key in _keyResp_allKeys]
            # Run 'Each Frame' code from codeResp
            #if a new key has been pressed since last time
            
            if(len(keyResp.keys) > last_len):
                #increment the key logger length
                last_len = len(keyResp.keys)
                
                #grab the last key added to the keys list
                key_list.append(keyResp.keys.pop())
            
                #check for backspace
                if("backspace" in key_list):
                    key_list.remove("backspace")
            
                    #if we have at least 1 character, remove it
                    if(len(key_list) > 0):
                        key_list.pop()
                        
                #if enter is pressed then...
                elif("return" in key_list):
                    #remove the enter key
                    key_list.pop()
                    
                    #and end the trial if we have at least 2 digits
                    if(len(key_list) >= 2):
                        continueRoutine = False
            
                #now loop through and remove any extra characters that may exist
            
                while(len(key_list) > maxDigits):
                    key_list.pop()
            
                #create a variable to display
                respDisplay = ''.join(key_list)
            
            
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
                if eyetracker:
                    eyetracker.setConnectionState(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in TypedResponseComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "TypedResponse" ---
        for thisComponent in TypedResponseComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if keyResp.keys in ['', [], None]:  # No response was made
            keyResp.keys = None
        block_b.addData('keyResp.keys',keyResp.keys)
        if keyResp.keys != None:  # we had a response
            block_b.addData('keyResp.rt', keyResp.rt)
        # Run 'End Routine' code from codeResp
        thisExp.addData('subjResponse', respDisplay)
        # the Routine "TypedResponse" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "blank500" ---
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        blank500Components = [text_2]
        for thisComponent in blank500Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "blank500" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_2* updates
            
            # if text_2 is starting this frame...
            if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_2.frameNStart = frameN  # exact frame index
                text_2.tStart = t  # local t and not account for scr refresh
                text_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_2.started')
                # update status
                text_2.status = STARTED
                text_2.setAutoDraw(True)
            
            # if text_2 is active this frame...
            if text_2.status == STARTED:
                # update params
                pass
            
            # if text_2 is stopping this frame...
            if text_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_2.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    text_2.tStop = t  # not accounting for scr refresh
                    text_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_2.stopped')
                    # update status
                    text_2.status = FINISHED
                    text_2.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
                if eyetracker:
                    eyetracker.setConnectionState(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in blank500Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "blank500" ---
        for thisComponent in blank500Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.500000)
        
        # --- Prepare to start Routine "NewsTrial" ---
        continueRoutine = True
        # update component parameters for each repeat
        text_item.setText(f"{str(item)} \n \n Presiona 'q' para responder verdadero o 'p' para responder falso.")
        item_response.keys = []
        item_response.rt = []
        _item_response_allKeys = []
        # keep track of which components have finished
        NewsTrialComponents = [text_item, item_response]
        for thisComponent in NewsTrialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "NewsTrial" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_item* updates
            
            # if text_item is starting this frame...
            if text_item.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_item.frameNStart = frameN  # exact frame index
                text_item.tStart = t  # local t and not account for scr refresh
                text_item.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_item, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_item.started')
                # update status
                text_item.status = STARTED
                text_item.setAutoDraw(True)
            
            # if text_item is active this frame...
            if text_item.status == STARTED:
                # update params
                pass
            
            # *item_response* updates
            waitOnFlip = False
            
            # if item_response is starting this frame...
            if item_response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                item_response.frameNStart = frameN  # exact frame index
                item_response.tStart = t  # local t and not account for scr refresh
                item_response.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(item_response, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'item_response.started')
                # update status
                item_response.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(item_response.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(item_response.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if item_response.status == STARTED and not waitOnFlip:
                theseKeys = item_response.getKeys(keyList=['q', 'p'], waitRelease=False)
                _item_response_allKeys.extend(theseKeys)
                if len(_item_response_allKeys):
                    item_response.keys = _item_response_allKeys[-1].name  # just the last key pressed
                    item_response.rt = _item_response_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
                if eyetracker:
                    eyetracker.setConnectionState(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in NewsTrialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "NewsTrial" ---
        for thisComponent in NewsTrialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if item_response.keys in ['', [], None]:  # No response was made
            item_response.keys = None
        block_b.addData('item_response.keys',item_response.keys)
        if item_response.keys != None:  # we had a response
            block_b.addData('item_response.rt', item_response.rt)
        # the Routine "NewsTrial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "blank500" ---
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        blank500Components = [text_2]
        for thisComponent in blank500Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "blank500" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_2* updates
            
            # if text_2 is starting this frame...
            if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_2.frameNStart = frameN  # exact frame index
                text_2.tStart = t  # local t and not account for scr refresh
                text_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_2.started')
                # update status
                text_2.status = STARTED
                text_2.setAutoDraw(True)
            
            # if text_2 is active this frame...
            if text_2.status == STARTED:
                # update params
                pass
            
            # if text_2 is stopping this frame...
            if text_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_2.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    text_2.tStop = t  # not accounting for scr refresh
                    text_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_2.stopped')
                    # update status
                    text_2.status = FINISHED
                    text_2.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
                if eyetracker:
                    eyetracker.setConnectionState(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in blank500Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "blank500" ---
        for thisComponent in blank500Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.500000)
        thisExp.nextEntry()
        
    # completed nRepsTask3 repeats of 'block_b'
    
# completed 1.0 repeats of 'controlTaskOrder'


# --- Prepare to start Routine "GoodbyeScreen" ---
continueRoutine = True
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
GoodbyeScreenComponents = [text_3, key_resp_2]
for thisComponent in GoodbyeScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "GoodbyeScreen" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    
    # if text_3 is starting this frame...
    if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_3.frameNStart = frameN  # exact frame index
        text_3.tStart = t  # local t and not account for scr refresh
        text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_3.started')
        # update status
        text_3.status = STARTED
        text_3.setAutoDraw(True)
    
    # if text_3 is active this frame...
    if text_3.status == STARTED:
        # update params
        pass
    
    # *key_resp_2* updates
    waitOnFlip = False
    
    # if key_resp_2 is starting this frame...
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_2.started')
        # update status
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in GoodbyeScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "GoodbyeScreen" ---
for thisComponent in GoodbyeScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys = None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.nextEntry()
# the Routine "GoodbyeScreen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
