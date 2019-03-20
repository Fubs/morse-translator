import morsetranslator as mt
import sys
import re

msg = str(input("Input message: "))

morsemsg = mt.txt2morse(msg, "/")
print(morsemsg)

dotlen = 200 # in miliseconds

dashlen = 3*dotlen
lettergap = 3*dotlen
wordgap = -7*dotlen
lettergap = -3*dotlen
dotgap = -1*dotlen

timinglist = []

subbedmsg = re.sub(" ","l",morsemsg)
msgList = list(subbedmsg)


for i in range(len(msgList)):
    if (msgList[i] == "." or msgList[i] == "-") and (msgList[i+1] == "." or msgList[i+1] == "-"):
        msgList.insert(i+1,"c")

for i in range(len(msgList)+1):
    if (msgList[i] == "." or msgList[i] == "-") and (msgList[i+1] == "." or msgList[i+1] == "-"):
        msgList.insert(i+1,"c")

parsedmsg = "".join(msgList)

print(parsedmsg)

for c in parsedmsg:
    if c == ".":
        timinglist.append(int(dotlen))
    elif c == "-":
        timinglist.append(int(dashlen))
    elif c == "c":
        timinglist.append(int(dotgap))
    elif c == "l":
        timinglist.append(int(lettergap))
    else:
        timinglist.append(int(wordgap))

timinglist.append(-3000)
print(timinglist)


# Begin writing arduino code
f = open("morsemsg/morsemsg.ino","w")
f.write("void setup() {\n")
f.write("pinMode(LED_BUILTIN, OUTPUT);\n")
f.write("}\n")
f.write("\n")
f.write("void loop() {\n")

delayvar = 0

for t in timinglist:
    if t > 0:
        delayvar = int(t)
        f.write("digitalWrite(LED_BUILTIN, HIGH);\n")
        f.write("delay(" + str(delayvar) + ");\n")
    else:
        delayvar = -1*int(t)
        f.write("digitalWrite(LED_BUILTIN, LOW);\n")
        f.write("delay(" + str(delayvar) + ");\n")

f.write("}\n")


























