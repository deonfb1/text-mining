'''Write up is coming, a tad bit later than 12 am'''

import praw

reddit = praw.Reddit(
    client_id="P8EECF5Sr2WWELq-sg4joQ",
    client_secret="g5WDIhTv0sFtJLoxBZBKdO3DlMrTpg",
    user_agent="Deonagent",
    username="PopBlox",
    password="t8NoF*:P*ifX33G5.w",
)

teslad = dict()

#Change these to see word frequencies for different subreddits post and comments
sub = 'teslainvestorsclub'
submissions = reddit.subreddit(sub).top('month', limit=20)

def h_frequency():
    '''Headline frequency'''

    #teslad = dict.clear() <---- doesn't work for some reason
    top = [(submission.title, submission.selftext) for submission in submissions]
    for line in top:
        for line2 in line:
            words = line2.split()
            for word in words:
                if word not in teslad:
                    teslad[word] = 1
                else:
                    teslad[word] += 1
    #I got this line of code from stack overflow, it conveneiently
    #prints all the words and their frequencies in order
    sorttesla = sorted(teslad.items(), key=lambda x: x[1], reverse=False)
    for i in sorttesla:
        print(i[0], i[1])
                
def c_frequency():
    '''Comment frequency'''

    #teslad = dict.clear()
    for submission in submissions:
        for comment in submission.comments:
            body = comment.body 
            words = body.split()
            for word in words:
                if word not in teslad:
                        teslad[word] = 1
                else:
                        teslad[word] += 1
    sorttesla = sorted(teslad.items(), key=lambda x: x[1], reverse=False)
    for i in sorttesla:
        print(i[0], i[1])


#h_frequency()
c_frequency()
#May take a while to run

if __name__ == "__main__":
    main() 
#Not sure i did this right?