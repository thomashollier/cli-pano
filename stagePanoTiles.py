#!/Users/thomas/miniconda3/bin/python3


import os, sys, subprocess

srcDir = "pix"
images=os.listdir("./pix/")
images.sort()
images=[x for x in images if x.split(".")[-1:][0]=="jpg"]

def getTimeStamp(i):
	cmd = ('exiftool -d "%%s" -DateTimeOriginal -s -s -s pix/%s' % i)
	cmd = cmd.split()
	v = subprocess.run(cmd, capture_output=True, text=True)
	date = v.stdout.rstrip()
	date= int(eval(date))
	return(date)	

def linkImage(i, srcDir, dstDir):
	if os.path.exists("%s/%s"%(dstDir, i)):
		print("%s/%s exists and already linked to %s/%s - do nothing" % (dstDir, i, srcDir, i))
	else:
		print("%s/%s created and  linked to %s/%s" % (dstDir, i, srcDir, i))
		os.symlink("../%s/%s" % (srcDir,i), "%s/%s"%(dstDir, i))
	
print("start")

ii = images[0]
tt = getTimeStamp(ii)
g = 1

panoDir="pano_%02d" % g
os.makedirs(panoDir, exist_ok=True)

for i in [x for x in images if x.split(".")[-1:][0]=="jpg"]:
	t = getTimeStamp(i)
	tDelta =  t-tt
	if tDelta>20:
		print("time delta is %s, new group"%tDelta)
		g = g + 1
		panoDir="pano_%02d" % g
		os.makedirs(panoDir, exist_ok=True)
	linkImage(i, srcDir, panoDir)
	tt = t
	ii = i



