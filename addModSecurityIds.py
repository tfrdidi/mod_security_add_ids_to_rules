import sys
import os.path

# Mod_security decided to make IDs on rules mandatory with a certain update.
# This script is ment to solve the problem by assigning all rules of a file
# an ID starting with a certain value that is specified by the user.
#
# Call this script with "addModSecurityIDs.py <pathToRuleFile> <firstIDToAssing>.


uninitialized = "uninitialized"

if len(sys.argv) < 2:
	print "Call this script with 'python addModSecurityIDs.py <pathToRuleFile> <firstIDToAssing>'."
	exit()


ruleFileName = sys.argv[1]

if not os.path.isfile(ruleFileName):
	print ruleFileName + " is not a file."
	exit()

startId = int(sys.argv[2])


print "try to update rule file " + ruleFileName
ruleFile = open(ruleFileName, 'r')
content = ruleFile.readlines()
ruleFile.close()

result = open("result.conf", "w")

previousLine = uninitialized

ruleId = startId
for line in content:
	if not previousLine == uninitialized:
		if "SecRule" in line and "chain" not in previousLine \
				and "id:" not in line:
			tmp = line.split()
			print previousLine
			print line
			newLine = line[:len(line)-2] + ",id:" + str(ruleId) + line[len(line)-2:]
			print newLine
			result.write(newLine)
			ruleId+=1
		else:
			result.write(line)
	else:
		result.write(line)

	previousLine = line
	
