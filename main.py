
def check_position(position):
    if position<1 or position>9:
       print("invalid position😵")
       return None
    row=(position-1) // 3
    column=(position-1)%3            
    return matrix[row][column]
               
  

matrix=[
    ["pig pen","sewer rat","supermarket"],
    ["job","stable","cow"],
    ["gaming room","restaurant","bull"],
]
cellsewerrat="sewer rat"
celljob="job"

if __name__ == "__main__":

    attempts=0
    print("""Welcome to RAT GOT A JOB GAME\n
    You must find the sewer rat and then find its job on the grid.🏢\n
    You have six attempts to win the game.😱\n
    Good luck!\nThe rat is in one cell and its job is in another cell🤪 \n
    [🐀🐀🐀] \n
    [🐀🐀🐀 ]\n 
    [🐀🐀🐀]\n 
    positions:\n
    1,2,3\n 
    4,5,6\n 
    7,8,9\n""")

    while attempts<6:
        rat_position=int(input("Where do you think the sewer rat is?🐷\n"))
        rat_result=check_position(rat_position)
        if rat_result is None:
            continue
        if rat_result==cellsewerrat:    
            print(rat_result)
            print("The rat is here! Let's go to its job!🐀🏃\n")
            job_position=int(input("Where is the rat's job?🐷\n"))
            job_result=check_position(job_position)
            if job_result is None:
                continue
            if job_result==celljob:
                print("We arrived at the rat's job!!Congratulations You are the winner🎉🎉")
                break
            if job_result!=celljob:
                print("The job isn't here.Try again😨\n")
                attempts+=1
        if rat_result!=cellsewerrat:
            attempts+=1
            print(rat_result)
            print("The rat isn't here!Try again😨\n")
        
    print("Game Over 😭")
