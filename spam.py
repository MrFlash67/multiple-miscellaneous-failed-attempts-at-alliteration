try:
    import os, time, sys
    print 'message'
    msg = str(raw_input('> '))
    print 'times'
    times = int(raw_input('> '))
    print "You want to say " + msg + " " + str(times) + " times.\nPress enter to continue."
    raw_input()
    
    cmd = """
    osascript -e 'tell application "Skype" to activate
    tell application "System Events" to keystroke " """ + msg + """ "
    tell application "System Events" to keystroke return' 
    """.format(msg)
    
    #print 1
    i = 0
    #times = 17
    
    while i < times - 1:
        os.system(cmd)
        #time.sleep(0.1)
        print 'I said ' + msg + " and I have " + str(times - i) + " repitition(s) to go."
        print i
        i = i + 1
except KeyboardInterrupt:
    sys.exit()
except ValueError:
    print 'Ensure that all numbers are numbers.'
