import requests

init = requests.get('https://raw.githubusercontent.com/NandemoStudios/SwyftEngine/master/Engine/__init__.py')
initcontent = init.text
maths = requests.get('https://raw.githubusercontent.com/NandemoStudios/SwyftEngine/master/Engine/maths.py')
mathscontent = maths.text

shouldContinue = input("Updating this package may result in code on your end breaking, continue? (Y/N) ")

if shouldContinue.lower() == 'n':
    print("update aborted")
    quit()

if initcontent != open('__init__.py', 'r'):
    initfile = open('__init__.py', 'w').write(initcontent)
else:
    print("there seems to be no changes to be made to __init__.py")

if mathscontent != open('maths.py', 'r'):
    open("maths.py", 'w').write(mathscontent)
else:
    print("there seems to be no changes to be made to maths.py")

