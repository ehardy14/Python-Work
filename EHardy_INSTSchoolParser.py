#URL to use for this question:
#   https://academiccatalog.umd.edu/undergraduate/approved-courses/inst/


#____FUNCTIONS_____
import urllib.request, urllib.parse, urllib.error
import re
import ssl

#takes URL,
#returns the list of the rows of the course block
#(<div class="courseblock">)
def getHTML(link):
    url = re.findall(r'(https?://[^\s]+)', link)[0]
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    html = urllib.request.urlopen(url, context = ctx).read()
    fullPage = str(html).split("\\t\\t")
    courseList = []
    for line in fullPage:
        if '<p class="courseblockdesc noindent">' in line:
            begin = line.find(">", 2) + 1
            end = line.find("<", begin)
            title = line[begin:end]
            courseList.append(title)
    return courseList#return the list created on the last line above


#takes list of rows of the rows of the course block,
#returns dict of course codes, titles and credits
def makeCourseDict(courseList):
    courseDict = {}

    for courses in courseList:
        courseCode = courses[0:7]
        courseTitleCredits = courses[7:].split('(')
        courseDict[courseCode] = courseTitleCredits
        
    return courseDict


#takes dictionary of courses,
#returns list of courses at given level
def atLevel(courseDict):
    levelDict = {}
    #create another empty course dictionary to hold course at given level
    userLevel = int(level)
    #cast user input level value passed to this function to int(), assign to variable
    #calculate highest possible number at given level, assign to variable (e.g., 399)
    level100 = range(100, 199)
    level200 = range(200, 299)
    level300 = range(300, 399)
    level400 = range(400, 499)
    for line in courseDict:
        theLevel = line[4:7]
        if theLevel == level100:
            levelDict[userLevel] = theLevel
        if theLevel == level200:
            levelDict[userLevel] = theLevel
        if theLevel == level300:
            levelDict[userLevel] = theLevel
        if theLevel == level400:
            levelDict[userLevel] = theLevel
    #traverse the course dictionary passed to this function
        #slice course number protion of the course code
        #check if the course number is between the start and end numbers at the given level
            #if above condition holds, append entry to the new dictionary
    
    return levelDict #return the new course dictionary created above

    

#____MAIN CODE_____

 #capture URL from user input, assign to variable
 #capture course level (100, 200, 300, 0r 400) from user input, assign to variable

 #pass URL string to getHTML() function, and assign return value to course block list
 #pass course block list to makeCourseDict() function, and assign return value to dictionary
 #pass course dictionary to atLevel() function, and assign return value to dictionary of courses at given level
 #print dictionary of courses at given level
url = input('Enter URL - ' )
level = input('Enter Level (100, 200, 300, 400) -' )
courseBlockList = getHTML(url)
courseDictionary = makeCourseDict(courseBlockList)
dictAtGivLevel = atLevel(courseDictionary)
print(dictAtGivLevel)
