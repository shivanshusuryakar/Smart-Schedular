#---------------------------------------------------------------------------------------------------
#   @Author: Shivanshu Anant Suryakar
#   github : https://www.github.io/jiminnpark
#   email  : shivanshusurya192@gmail.com
#   Task Schedular Algorithm
#---------------------------------------------------------------------------------------------------


# Please go through the steps to use this schedular
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 1.Firstly you need to know how many tasks do you have to complete.
# 2. You also need to know how many fixed tasks do you have.
#      (Fix tasks includes tasks that need to be done in the exact time only) ex-Lunch ,Dinner,Gym
# 3.Assign rating (out of 5) to each task based on their weightage.
#      (The one which has more weightage should be given value close  to 5).
# 4.Please use 24 hour format to input the timings.
# 5.Suppose you want to say 3:30 PM then input as 15.50.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




n = int(input('Enter total tasks: '))
task = list()  # stores names of tasks
tasktime = list()  #
mintask = list()
minfree = list()
minfix = list()
userfractime = 0
fixtime = 0
fixname = []
fix = []
timings = []
timingname = []


# stores names of the task
for x in range(n):
    temp = input("Task name {}: ".format(x + 1))
    task.append(temp)

# stores weightage of the task
for x in range(n):
    temp = int(input("Task {} (out of 5): ".format(x + 1)))   # dont exceed the limit
    tasktime.append(temp)
    userfractime += temp

totalfractime = 5 * n  # total fraction time
freefractime = totalfractime - userfractime  # total free time in fraction
scaledtime = list()
for x in tasktime:
    scaledtime.append(x / (userfractime))  # task time scaled (under 1)

start = float(input("Start of day: "))
end = float(input("End of day: "))


# deals with storing of fixed tasks
n = int(input("Number of Fixed Tasks:"))
for x in range(0, n):
    tn = input("Your Fixed Task name: ")
    fixname.append(tn)
    st = float(input("Start of {}: ".format(tn)))
    en = float(input("End of {}: ".format(tn)))
    fix.append([st, en])

for x in fix:
    minfix.append([round(x[0] * 12), round(x[1] * 12)])
    fixtime += x[1] - x[0]

temp = end - start - fixtime
timefortask = (userfractime / totalfractime) * temp
timefree = temp - timefortask


remtasktime = list()
remfreetime = list()
for i in range(len(scaledtime)):
    remtasktime.append(timefortask * scaledtime[i] * 12)
    remfreetime.append(timefree * scaledtime[i] * 12)

count = 0
i = 0
fxflag = 0

# Initially it checks if the task one can be performed without being divided by some fixtime
if count == 0:
    stt = start * 12
    ent = (start * 12 + round(remtasktime[i]))
    for j in range(0, len(minfix)):
        if int(minfix[j][0]) in range(int(stt), round(ent) + 1):
            if stt != minfix[j][0]:
                timings.extend([[stt, (minfix[j][0])]])
                timingname.extend([task[i]])
                workdone = minfix[j][0] - stt
                remtasktime[i] = round(round(remtasktime[i]) - round(workdone))
            if (minfix[j][0]) != (minfix[j][1]):
                timings.extend([[(minfix[j][0]), (minfix[j][1])]])
                timingname.extend([fixname[j]])

            fxflag = 1
    # if the task is completed
    if remtasktime[i] <= 0:
        count += 1

    # if task can be processed into whole without segments
    if fxflag == 0:
        timings.extend([[stt, ent]])
        timingname.extend([task[i]])
        remtasktime[i] = round(round(remtasktime[i]) - round(ent - stt))
        count = 1
        i = 0

fxflag = 0
while (count < (2 * len(task))):
    fxflag = 0
    workdone = 0
    if i == 0:
        if count % 2 == 0:  # for tasks
            stt = timings[-1][1]
            ent = timings[-1][1] + round(remtasktime[i])
            for j in range(0, len(minfix)):
                stt = timings[-1][1]
                ent = timings[-1][1] + round(remtasktime[i])
                if int(minfix[j][0]) in range(int(stt), round(ent) + 1):  # checks if any fixtime is coming between
                    if stt != minfix[j][0]:
                        timings.extend([[stt, (minfix[j][0])]])
                        timingname.extend([task[i]])
                        workdone = minfix[j][0] - stt  # indicated the work progress done
                        remtasktime[i] = round(round(remtasktime[i]) - round(workdone))  # stores remaining time
                    if (minfix[j][0]) != (minfix[j][1]):
                        timings.extend([[(minfix[j][0]), (minfix[j][1])]])
                        timingname.extend([fixname[j]])

                    fxflag = 1
            if remtasktime[i] <= 0:
                count += 1
            # this means that the work is done in one go and no fixtime was in between
            if fxflag == 0:
                timings.extend([[stt, ent]])
                timingname.extend([task[i]])
                remtasktime[i] = round(round(remtasktime[i]) - round(ent - stt))
                count += 1

        else:  # for freetime
            stt = timings[-1][1]
            ent = timings[-1][1] + round(remfreetime[i])
            for j in range(0, len(minfix)):
                stt = timings[-1][1]
                ent = timings[-1][1] + round(remfreetime[i])
                if int(minfix[j][0]) in range(int(stt), round(ent) + 1):  # checks if any fixtime comes between freetime
                    if stt != minfix[j][0]:
                        timings.extend([[stt, (minfix[j][0])]])
                        timingname.extend(["Freetime:" + str(i + 1)])
                        workdone = minfix[j][0] - stt  # total amount of work done from assigned time
                        remfreetime[i] = round(round(remfreetime[i]) - round(workdone))  # remaining work is stored
                    if (minfix[j][0]) != (minfix[j][1]):
                        timings.extend([[(minfix[j][0]), (minfix[j][1])]])
                        timingname.extend([fixname[j]])

                    fxflag = 1
            if remfreetime[i] <= 0:
                count += 1
                i += 1

            # freetime is assigned without segmentation
            if fxflag == 0:
                timings.extend([[stt, ent]])
                timingname.extend(["Freetime:" + str(i + 1)])
                remfreetime[i] = (round(remfreetime[i]) - round(ent - stt))
                count += 1
                i += 1


    else:
        if count % 2 == 0:
            stt = timings[-1][1]
            ent = timings[-1][1] + round(remtasktime[i])
            for j in range(0, len(minfix)):
                stt = timings[-1][1]
                ent = timings[-1][1] + round(remtasktime[i])
                if int(minfix[j][0]) in range(int(stt), round(ent) + 1):
                    if stt != minfix[j][0]:
                        timings.extend([[stt, (minfix[j][0])]])
                        timingname.extend([task[i]])
                        workdone = minfix[j][0] - stt
                        remtasktime[i] = (round(remtasktime[i]) - round(workdone))
                    if (minfix[j][0]) != (minfix[j][1]):
                        timings.extend([[(minfix[j][0]), (minfix[j][1])]])
                        timingname.extend([fixname[j]])

                    fxflag = 1
            if remtasktime[i] <= 0:
                count += 1

            if fxflag == 0:
                timings.extend([[stt, ent]])
                timingname.extend([task[i]])
                remtasktime[i] = (round(remtasktime[i]) - round(ent - stt))
                count += 1
        else:
            stt = timings[-1][1]
            ent = timings[-1][1] + round(remfreetime[i])
            for j in range(0, len(minfix)):
                stt = timings[-1][1]
                ent = timings[-1][1] + round(remfreetime[i])
                if int(minfix[j][0]) in range(int(stt), round(ent) + 1):
                    if stt != minfix[j][0]:
                        timings.extend([[stt, (minfix[j][0])]])
                        timingname.extend(["Freetime:" + str(i + 1)])
                        workdone = minfix[j][0] - stt
                        remfreetime[i] = (round(remfreetime[i]) - round(workdone))
                    if (minfix[j][0]) != (minfix[j][1]):
                        timings.extend([[(minfix[j][0]), (minfix[j][1])]])
                        timingname.extend([fixname[j]])

                    fxflag = 1
            if remfreetime[i] <= 0:
                count += 1
                i += 1
            if fxflag == 0:
                timings.extend([[stt, ent]])
                timingname.extend(["Freetime:" + str(i + 1)])
                remfreetime[i] = (round(remfreetime[i]) - round(ent - stt))
                count += 1
                i += 1

newtime = []

# this converts 5 min group  in hours  (1 group= 5 minutes)
for x in timings:
    newtime.append(["%.2f" % (x1 / 12) for x1 in x])

# this code adjusts floating point values into minutes out of 60
finaltimings = [[str(int(float(x[0]))) + ":" + str(int((float(x[0]) - int(float(x[0]))) * 60)),
                 str(int(float(x[1]))) + ":" + str(int((float(x[1]) - int(float(x[1]))) * 60))] for x in newtime]

for i in range(len(finaltimings)):
    # if int(finaltimings[i][0])>12:
    #     finaltimings[i][0]-=12
    # if int(finaltimings[i][1])>12:
    #     finaltimings[i][0]-=12
    print(str(i + 1) + ": {} => {} to {}".format(timingname[i], finaltimings[i][0], finaltimings[i][1]))


''' 
---------------FIXED BUG---------------------

Enter total tasks: 3
Task name 1: Compiler Design
Task name 2: DAA Huffman
Task name 3: WPL
Task 1 (out of 5): 5
Task 2 (out of 5): 4
Task 3 (out of 5): 2
Start of day: 8
End of day: 22
Number of Fixed Tasks:4
Your Fixed Task name: Lunch
Start of Lunch: 13
End of Lunch: 13.50
Your Fixed Task name: Dinner
Start of Dinner: 20
End of Dinner: 20.50
Your Fixed Task name: Empath-Meet
Start of Empath-Meet: 21
End of Empath-Meet: 22
Your Fixed Task name: Entertainment
Start of Entertainment: 16
End of Entertainment: 17
1: Compiler Design => 8.0 to 11.40
2: Freetime:1 => 11.40 to 13.0
3: Lunch => 13.0 to 13.30
4: DAA Huffman => 13.30 to 16.0
5: Entertainment => 16.0 to 17.0
6: DAA Huffman => 17.0 to 17.25
7: Freetime:2 => 17.25 to 18.30
8: WPL => 18.30 to 20.0
9: Dinner => 20.0 to 20.30
10: Freetime:3 => 20.30 to 21.0
11: Empath-Meet => 21.0 to 22.0





'''
