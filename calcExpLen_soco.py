#########################
# study length
#########################

study_listLen = 100.0;
study_buffers = 4.0;
study_stimDuration = 1500.0;
study_stimJitter = 0.0;
study_ISI = 500.0;
study_ISIJitter = 250.0;
study_blinkBreaksPerList = 3.0;
study_blinkDuration = 15000.0;
study = (((study_listLen + study_buffers) * (study_stimDuration + study_ISI + (study_stimJitter/2.0) + (study_ISIJitter/2.0))) + (study_blinkBreaksPerList * study_blinkDuration)) / 1000.0 / 60.0;

#########################
# test length
#########################

test_lures = study_listLen/2.0;
test_preview = 750.0;
test_previewJitter = 0.0;
test_preRespOrientDelay = 1500.0;
test_preRespOrientJitter = 0.0;
test_stimDuration = 750.0;
test_stimJitter = 0.0;
test_respLen = 3000.0;
test_ISI = 500.0;
test_ISIJitter = 250.0;
test_blinkBreaksPerList = 10.0;
test_blinkDuration = 15000.0;
test = (((study_listLen + test_lures) * (test_preview + test_stimDuration + test_preRespOrientDelay + test_respLen + test_ISI + (test_previewJitter/2.0) + (test_preRespOrientJitter/2.0) + (test_stimJitter/2.0) + (test_ISIJitter/2.0))) + (test_blinkBreaksPerList * test_blinkDuration)) / 1000.0 / 60.0;

#########################
# exp length
#########################

numLists = 4.0;

numItems = numLists * (study_listLen + study_buffers + test_lures);
numTargs = numLists * study_listLen;
numLures = numLists * test_lures;
numTargsPerCond = numTargs / 2.0;
numLuresPerCond = numLures / 2.0;

initialNet = 30.0;
introPrac = 10.0;
impedanceBreaks = numLists - 1.0;
impedanceBreakDuration = 5.0;
totalMin = initialNet + introPrac + (numLists * (study + test)) + (impedanceBreaks * impedanceBreakDuration);

#study/numLists
#test/numLists
#totalMin
#numItems
#numTargs
#numLures
#numTargsPerCond
#numLuresPerCond

#####################################################################
# calculate when blink breaks occur for study and test
#
# you need to decide if the numbers seem reasonable
#####################################################################

#########################
# study - blink breaks
#########################

study_stims = range(study_listLen+study_buffers)

study_trialDuration = (study_stimDuration + study_ISI + (study_stimJitter/2.0) + (study_ISIJitter/2.0)) / 1000.0;
study_totalDuration = 0.0;

for n in study_stims:
    if (n+1) % (len(study_stims)/(study_blinkBreaksPerList+1)) == 0 and (n+1) != 1 and (n+1) != len(study_stims) and (len(study_stims) - (n+1)) > 6:
        study_totalDuration += study_trialDuration
        print n, study_totalDuration,'s break'
        study_totalDuration = study_trialDuration
    else:
        study_totalDuration += study_trialDuration
        print n, study_totalDuration,'s'


#########################
# test - blink breaks
#########################

test_stims = range(int(study_listLen*1.5))

test_preview = 750.0;
test_preRespOrientDelay = 1500.0;
test_stimDuration = 750.0;
test_respLen = 3000.0;
test_ISI = 750.0;

test_trialDuration = (test_preview + test_preRespOrientDelay + test_stimDuration + test_respLen + test_ISI + (test_previewJitter/2.0) + (test_preRespOrientJitter/2.0) + (test_stimJitter/2.0) + (test_ISIJitter/2.0)) / 1000.0;
test_totalDuration = 0.0;

for n in test_stims:
    if (n+1) % (len(test_stims)/(test_blinkBreaksPerList+1)) == 0 and (n+1) != 1 and (n+1) != len(test_stims) and (len(test_stims) - (n+1)) > 6:
        test_totalDuration += test_trialDuration
        print n, test_totalDuration,'s break'
        test_totalDuration = test_trialDuration
    else:
        test_totalDuration += test_trialDuration
        print n, test_totalDuration,'s'
