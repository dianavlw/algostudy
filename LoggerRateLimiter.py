
"""
359. Logger Rate Limiter :https://leetcode.com/problems/logger-rate-limiter/
Soure: https://www.youtube.com/watch?v=g8r59EosQhU

Design a logger system that receives a stream of messages along with their timestamps. 
Each unique message should only be printed at most every 10 seconds (i.e. a message printed at timestampt will prevent other
identical messages from being printed until timestamp t + 10).

All messages will come in chronological order. Several messages may arrive at the same timestamp.
Implement the Logger class:
Logger() Initializes the logger object.
bool shouldPrintMessage(int timestamp, string message) 
Returns true if the message should be printed in the given timestamp, otherwise returns false.
 
Example 1:

Input
["Logger", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage", 
"shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage"]
[[], [1, "foo"], [2, "bar"], [3, "foo"], [8, "bar"], [10, "foo"], [11, "foo"]]
Output [null, true, true, false, false, false, true]


Approach:
how to remember if we've seen the message before?
hashmap vs hashset

hashmap will cointain key, and values
key : message
value: timestamp

initialize hashmap()

criteria: 
[1, "foo"], 
[2, "bar"],
[3, "foo"], 
[8, "bar"], 
[10, "foo"], 
[11, "foo"]

1. is it unique?
2. has it been seen 10 sec since last seen

output:
(timestamp, message)
[1, "foo"], True 
[2, "bar"], True
[3, "foo"], False
[8, "bar"], False (last time seen was at 2, 6 secs ago it hasnt been 10 secs so its FALSE)
[10, "foo"], False
[11, "foo"], True (it has been 10 since the 1 sec the first time, then we update the time stamp in the hashmap to 11)

HashMap: 
"foo": 11
"bar": 2

"""

class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashMap = {}
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        if message not in self.hashMap:
            self.hashMap[message] = timestamp
            return True
        elif timestamp >= self.hashMap[message] + 10:
            self.hashMap[message] = timestamp
            return True
        else:
            return False
        
        
        
# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)

#         if timestamp < self.hashMap.get(message, 0):
#             return False
#         self.hashMap[message] = timestamp + 10
#         return True


