"""

468. Validate IP Address:https://leetcode.com/problems/validate-ip-address/

Given a string IP, return "IPv4" if IP is a valid IPv4 address, "IPv6" if IP is a valid IPv6 address or "Neither" if IP is not a correct IP of any type.

A valid IPv4 address is an IP in the form "x1.x2.x3.x4" where 0 <= xi <= 255 and xi 
cannot contain leading zeros. For example, "192.168.1.1" and "192.168.1.0" are valid 
IPv4 addresses but "192.168.01.1", while "192.168.1.00" and "192.168@1.1" are invalid IPv4 addresses.

A valid IPv6 address is an IP in the form "x1:x2:x3:x4:x5:x6:x7:x8" where:

1 <= xi.length <= 4
xi is a hexadecimal string which may contain digits, lower-case English letter ('a' to 'f') 
and upper-case English letters ('A' to 'F').
Leading zeros are allowed in xi.
For example, "2001:0db8:85a3:0000:0000:8a2e:0370:7334" and "2001:db8:85a3:0:0:8A2E:0370:7334" 
are valid IPv6 addresses, while "2001:0db8:85a3::8A2E:037j:7334" 
and "02001:0db8:85a3:0000:0000:8a2e:0370:7334" are invalid IPv6 addresses.


"""


class Solution:
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        a = self.IPv4(IP)
        b = self.IPv6(IP)
        if a:
            return "IPv4"
        if b:
            return "IPv6"
        return "Neither"
    
    def IPv4(self, IP):
        if IP.count('.') == 3:
            res = IP.split('.')
            for string in res:
                if len(string) > 0 and len(string) <= 4:
                    for s in string:
                        if s not in "0123456789":
                            return False
                    if len(string) > 1 and string[0] == '0' or int(string) >= 256:
                        return False
                else:
                    return False
                
            return True
        else:
            return False
    
    def IPv6(self, IP):
        if IP.count(':') == 7:
            res = IP.split(':')
            for string in res:
                if len(string) > 0 and len(string) <= 4:
                    for s in string:
                        if s not in "0123456789abcdefABCDEF":
                            return False
                else:
                    return False
            return True
        else:
            return False
            

        
         
"""        
0-9 a-f A-F ...22 characters 
10:a/A, 11: b/B, 12: c/C .... 
.1 vs .01
invalid: 172.16.256.1 256 exceeds the max of 255
invalid: 172.16.256. we are missing one more

ipv6: leading zeros 
::0 not valid

algo:
check if the len is 0 or more than 3  return neither
for each token, if len(t) == 0 || len(t) > 3 return "neither"
if t[0] == '0' return "neither"

for c in t: if != isDigit[c] return "neither"
if int[t] > 255 return 'neither'
return ipv4

cases for ipv6:
for each t :
if len(t) == '0' or len(t) > 4 return 'neither'
for c in t:
if c not in hexdigit return 'neither'
after loop return ipv6

io is a string
if ip contai
""""""


        
