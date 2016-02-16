# Given a day of the week encoded as 0=Sun,
# 1=Mon, 2=Tue, ...6=Sat, and a boolean
# indicating if we are on vacation, return
# a string of the form "7:00" indicating
# when the alarm clock should ring.
# Weekdays, the alarm should be "7:00"
# and on the weekend it should be "10:00".
# Unless we are on vacation -- then on
# weekdays it should be "10:00" and weekends
# it should be "off"

def alarm_clock(day, vacation):
    if day is 0 or day is 6: # it's the weekend
        if vacation: # on vacation
            return "off"
        else: # not on vacation
            return "10:00"
    else: #it's a weekday
        if vacation:
            return "10:00"
        else:
            return "7:00"
        
def tester(actual, expected):
    if actual == expected:
        print "OK."
    else:
        print "Incorrect."

tester(alarm_clock(1, False), '7:00')  
tester(alarm_clock(5, False), '7:00')
tester(alarm_clock(0, False), '10:00')
tester(alarm_clock(6, False), '10:00')    
tester(alarm_clock(0, True), 'off')  
tester(alarm_clock(6, True), 'off')   
tester(alarm_clock(1, True), '10:00')
tester(alarm_clock(3, True), '10:00')   
tester(alarm_clock(5, True), '10:00')
