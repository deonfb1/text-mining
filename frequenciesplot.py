import praw
from PIL import Image
import matplotlib.pyplot as plt #This wouldn't import so I cant see the word cloud but hopefully you can
from wordcloud import WordCloud


reddit = praw.Reddit(
    client_id="P8EECF5Sr2WWELq-sg4joQ",
    client_secret="g5WDIhTv0sFtJLoxBZBKdO3DlMrTpg",
    user_agent="Deonagent",
    username="PopBlox",
    password="t8NoF*:P*ifX33G5.w",
)

teslad = dict()

#Change these to see a word cloud of word frequencies for different subreddits post and comments
sub = 'teslainvestorsclub'
submissions = reddit.subreddit(sub).top('month', limit=1000)

def h_frequency():
    '''Headline frequency word cloud'''

    #teslad = dict.clear()
    top5 = [(submission.title, submission.selftext) for submission in submissions]
    for line in top5:
        for line2 in line:
            words = line2.split()
            for word in words:
                if word not in teslad:
                    teslad[word] = 1
                else:
                    teslad[word] += 1
        sorttesla = sorted(teslad.items(), key=lambda x: x[1], reverse=True)
        for i in sorttesla:
            print(i[0], i[1])

def c_frequency():
    '''Comment frequency word cloud'''

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
    wc = WordCloud(background_color="white",width=1000,height=1000, max_words=100,relative_scaling=0.5,normalize_plurals=False).generate_from_frequencies(teslad)
    plt.imshow(wc)
    #An improvement I could make is getting rid of common words like "the"


#h_frequency()
c_frequency()

if __name__ == "__main__":
    main()