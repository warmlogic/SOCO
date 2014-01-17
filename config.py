# SOCO configuration

expName = 'SOCO'

# Number of sessions per subject
numSessions = 1

isEEG = True
playAudio = False

#############################
# Exp organization
#############################

# Number of trials/lists per session
numLists = 4
# Number of target stimuli per trial/list
study_listLen = 100
# number of buffer stimuli to add to start and end of lists
study_bufferStart = 2
study_bufferEnd = 2
# Recognition & Source task
test_numLures = 50

# Do a practice trial?
practiceList = True
prac_numLists = 2
pracstudy_listLen = 12
pracstudy_bufferStart = 2
pracstudy_bufferEnd = 2
practest_numLures = 6

#############################
# Display setup
#############################

# Stim setup
PICTURE_SIZE = 0.3
mid_coord = 0.5
top_coord = 0.05
bot_coord = 0.95
fback_coord = 0.25
# 15" PowerBook (1280x800); E013 iMac (1440x900)
#left_coord = 0.31
#right_coord = 0.69
# Wide (1680x1050): 15" MBP, office display
#left_coord = 0.31
#right_coord = 0.69
# Square (1024x768): D458? linux EEG
#left_coord = 0.28
#right_coord = 0.72
# Square (1280x1024): D464 linux EEG
left_coord = 0.25
right_coord = 0.75

#KEYIMAGE_SIZE = (0.96,0.12)

# Word Font size (proportion of vertical screen)
test_wordHeight = .05
instruct_wordHeight = .05
fixation_wordHeight = .05

# Orienting Stimulus text
orientText = '+'

# color frame info
#colors_names = ('red','blue')
#colors_rgb = ((255,0,0,80),(0,0,255,80))
colors_rgb = [(126,30,156,255),(21,176,26,255),(3,67,223,255),(255,129,192,255),(229,0,0,255),(249,115,6,255),(255,255,20,255),(101,55,0,255)]
color_names = ('purple','green','blue','pink','red','orange','yellow','brown')
#(2,147,134,255),(0,255,255,255)
# color_names = ('teal','cyan')

color_frame_side_prop = 0.2 # proportion of image size
color_frame_top_prop = 0.2 # proportion of image size

test_rect_side_prop = 0.15 # proportion of image size
test_rect_top_prop = 0.15 # proportion of image size

#################################
# EEG setup
#################################

# initial resting period duration
restEEGDuration = 20000

# this is the key that the experimenter has to hit to continue after
# impedance check
endImpedanceKey = "G"
# choose a huge number for the impedance countdown
maxImpedanceTime = 100000000

# number of blink breaks
study_blinkBreaksPerList = 3
test_blinkBreaksPerList = 10
# EEG: Pause after a blinking period to subject can finish blinking
pauseAfterBlink = 2000
textAfterBlink = "Get ready..."

# BEHAVIORAL ONLY: amount of time to break between study and test (isEEG == False)
breakTime = 300000 # 300000ms=5min

################################
# Study period parameters
################################

# Pause+Jitter after orienting cross before first study stim; only
# happens once on each list
study_preStimDelay = 2000
study_preStimJitter = 500
# Duration that the study stim is on the screen
study_stimDuration = 1500
study_stimJitter = None
# ISI+Jitter after study stim is cleared from the screen
study_ISI = 500
study_ISIJitter = 250

############################################################
# Test period parameters
############################################################

# keys for the test period
leftKeys_test = ('Z','X')
rightKeys_test = ('.','/')

newText_test = "N"
rememSourceText_test = "RC"
rememOtherText_test = "RO"
knowText_test = "F"
sureText_test = "Sure"
maybeText_test = "Maybe"

# # widescreen
# test_color_left_x = (0.53, 0.47)
# test_color_right_x = (0.47, 0.53)
# test_new_x = (0.43, 0.57)
# test_rs_x = (0.535, 0.465)
# test_ro_x = (0.465, 0.535)
# test_k_x = (0.425, 0.575)
# test_sure_x = (0.445, 0.555)
# test_maybe_x = (0.57, 0.425)

# square screen
test_color_left_x = (0.54, 0.46)
test_color_right_x = (0.46, 0.54)
test_new_x = (0.41, 0.59)
test_rs_x = (0.545, 0.455)
test_ro_x = (0.455, 0.545)
test_k_x = (0.40, 0.595)
test_sure_x = (0.43, 0.57)
test_maybe_x = (0.59, 0.405)

# Pause+Jitter before test period begins; happens once per list
test_preStimDelay = 2000
test_preStimJitter = 500

# amount of time to show fixation cross
test_preview = 750
test_previewJitter = None
#test_preStimDelay = 500
#test_preStimJitter = 150
# amount of time to show test stimulus
test_stimDuration = 750
test_stimJitter = None
# delay after each stim before response period
test_preRespOrientDelay = 1500
test_preRespOrientJitter = None
#test_preRespBlankDelay = 900
# min and max response duration
test_minRespDuration = 100
test_maxRespDuration = 30000
# delay after response period
test_ISI = 500
test_ISIJitter = 250

#############################################
# Other experiment parameters
#############################################

# countdown timer between lists
ILI_timer = True
ILI_dur = 30000
ILI_key = 'SPACE'

# make the stimulus pools
objectStimuli = 'images/object_stims'
#objectStimuliTxt = 'images/object_stims.txt'
objectBuffers = 'images/object_buffers'
#objectBuffersTxt = 'images/object_buffers.txt'
noiseStimuli = 'images/noise_stim'
#noiseStim = 'images/noise/noise1.png'
presentationType = 'image'  # image, sound, text
presentationAttribute = 'name'  # attribute to use to create the text
                                # description

# Trial text
# Beh
#trialBeginText = "Press any key for Trial #%d"
#testBeginText = "Press any key to begin test"
# EEG
sesBeginText = "Press any key for Session #%d."
trialBeginText = "Press any key for Trial #%d."
studyBeginText = "Blink now.\nPress space to begin Study #%d."
testBeginText = "Blink now.\nPress space to begin Test #%d."
studyPracBeginText = "Blink now.\nPress space to begin Study Practice."
testPracBeginText = "Blink now.\nPress space to begin Test Practice."
restEEGPrep = "Press any key to record resting data."
restEEGText = "Recording resting data. Please sit still..."
blinkRestText_study = "Blink now.\nPress any key to continue study period."
blinkRestText_test = "Blink now.\nPress any key to continue test period."
#confidenceText = "Sure | Probably | Guess | Guess | Probably | Sure"

# Set up the beeps
hiBeepFreq = 800
hiBeepDur = 500
hiBeepRiseFall = 100
loBeepFreq = 400
loBeepDur = 500
loBeepRiseFall = 100

# Instructions text file
instruct_getready = 'text/instruct_getready.txt'
# BEH
#instruct_intro = 'text/beh/instruct_intro.txt'
#instruct_study_practice = 'text/beh/instruct_study_practice.txt'
#instruct_test_practice = 'text/beh/instruct_test_practice.txt'
#instruct_study = 'text/beh/instruct_study.txt'
#instruct_test = 'text/beh/instruct_test.txt'
#midSessionBreak = 'text/beh/midSessionBreak.txt'
# EEG
instruct_intro = 'text/eeg/instruct_intro_eeg.txt'
instruct_study_practice = 'text/eeg/instruct_study_practice_eeg.txt'
instruct_test_practice = 'text/eeg/instruct_test_practice_eeg.txt'
instruct_study = 'text/eeg/instruct_study_eeg.txt'
instruct_test = 'text/eeg/instruct_test_eeg.txt'
midSessionBreak = 'text/eeg/midSessionBreak.txt'

# Default font
defaultFont = 'fonts/Verdana.ttf'
