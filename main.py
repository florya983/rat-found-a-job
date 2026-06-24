
# This project is in progress

matrix=[
    ["pig pen","sewer rat","supermarket"],
    ["job","stable","cow"],
    ["roof","restaurant","bull"],
]
attempts=0
print("Hello! welcome to RAT GOT A JOB GAME")
print("You must find the rat in the sewer then go to the job in a grid, you have six attempts to win the game, good luck!\n let’s go! the rat is in one cell and its job is in another cell\n[x x x] \n [x x x]\n [x x x]\n positions: 00,01,02\n 10,11,12\n 20,21,22\n  ")
ratposition=input("Where do you think the sewer rat is?")
jobposition=input("Where is the rat job?")
ratresult=resultverification(ratposition)
jobresult=resultverification(jobposition)