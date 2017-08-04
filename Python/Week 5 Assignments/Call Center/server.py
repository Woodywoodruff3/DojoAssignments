class Call(object):
    def __init__(self, uniqueID, callerName, callerNum, time, reason):
        self.uniqueID = uniqueID
        self.callerName = callerName
        self.callerNum = callerNum
        self.time = time
        self.reason = reason

    def display(self):
        print "ID: {}, Name: {}, Number: {}, Time: {}, Reason: {}".format(self.uniqueID, self.callerName, self.callerNum, self.time, self.reason)
    
class CallCenter(Call):
    def __init__(self, uniqueID, callerName, callerNum, time, reason):
        super(CallCenter, self).__init__(uniqueID, callerName, callerNum, time, reason)


caller1 = CallCenter(1, "Robert", 555-555-5555, "8:00", "sick" )

caller1.display()