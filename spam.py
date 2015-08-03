import os, time, sys
print 'message'
msg = raw_input('> ')
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
print cmd
i = 0
#times = 17
try:
    while i < times:
        os.system(cmd)
        #time.sleep(0.1)
        print 'I said ' + msg + " and I have " + str(times - i) + " repitition(s) to go."
        print i
        i = i + 1
except KeyboardInterrupt:
    sys.exit()
