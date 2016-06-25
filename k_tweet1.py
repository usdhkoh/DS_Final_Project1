class User:
    def __init__(self):
        self.name = "None"
        self.tweets = 0
        self.friends = 0
        self.next_tweet = None
        self.join_d = "None" # 가입날짜, 이 프로젝트에선 필요없는 데이터

class Tweet:
    def __init__(self):
        self.owner = "None"
        self.content = "None"
        self.next_tweet = None
        self.tweet_number = 0
        self.date = "None" # 트윗날짜, 이 프로젝트에선 필요없는 데이터


class Friend:
    def __init__(self):
        self.color


    def add(self, v):


class delete: #delete 통합수행

class Scc:
    def
class Spath:
    def aa(self):


def u_read(user):
    while
        a = user.readline()
        b = user.readline()
        c = user.readline()
        d = user.readline() # user의 매 4번째 줄은 공백임
        a = User()
        a.join_d = b
        a.name = c

def t_read(tweet):

def f_read(friend):


def zero(): # user는 이미 id에 따라 sorting 되어 있음, tweet과 friend는 한 사람 것이 모여있음
    user = open(input(("\nEnter USER file location\n")), encoding="cp949")
    tweet = open(input(("\nEnter TWEET file location\n")), encoding="cp949")
    friend = open(input(("\nEnter FRIEND file location\n")), encoding="cp949")

    u_read(user)
    t_read(tweet)
    f_read(friend)




def one():


def interface():
    print("""
0. Read data files
1. display statistics
2. Top 5 most tweeted words
3. Top 5 most tweeted users
4. Find users who tweeted a specific word
5. Find all people who are friends of the above users
6. Delete users who mentioned a specific word
7. Delete all users who mentioned a specific word
8. Find strongly connected components
9. Find shortest path from a given user
99. Quit
""")
    mselect = input("Select Menu: ")
    if mselect == 0: # 0. Read data files
        zero()
        #reading process
        print("""
Total users: %d
Total friendship records: %d
Total tweets: %d"""%())

    elif mselect == 1: # 1. display statistics
        one()
        #static process
        print("""
Average number of friends: %f
Minimum friends: %d
Maximum number of friends: %d

Average tweets per user: %f
Minimum tweets per user: %d
Maximum tweets per user: %d"""%())

    elif mselect == 2:# 2. Top 5 most tweeted words
        # count process(모든 tweet 순회)
        print("""
 rank(tweeted)    content
     1.(%d)        %s
     2.(%d)        %s
     3.(%d)        %s
     4.(%d)        %s
     5.(%d)        %s

        """%())

    elif mselect == 3: # 3. Top 5 most tweeted users
        # count process(모든 user 순회)
        print("""
  rank(tweeted)   id(user name)
     1.(%d)        %s(%s)
     2.(%d)        %s(%s)
     3.(%d)        %s(%s)
     4.(%d)        %s(%s)
     5.(%d)        %s(%s)

                """ % ())
    elif mselect == 4: # 4. Find users who tweeted a specific word
        # word finding process
        print("""
who tweeted "%s"(%d)

%s"""%())

    elif mselect == 5: # 5. Find all people who are friends of the above users
        # node checking process
        print("""
user: %s(%s)

%s's friends(%d)
%s"""%())

    elif mselect == 6: # 6. Delete users who mentioned a specific word
        # word finding process
        print("""
who tweeted "%s"(%d)

%s""" % ())
        print("Enter the index number of users you want delete")
        print("Number should separated by comma(,) - ex)1,3,5 ")
        #user deleting process
        print("""
%d users,

%s

are deleted."""%())

    elif mselect == 7: # 7. Delete all users who mentioned a specific word
        # deleting process
        print("""
who tweeted "%s"(%d)

%s

are all deleted""" % ())

    elif mselect == 8: # 8. Find strongly connected components
        # node traversal process
        print("""
Those groups are strongly connected components

%s"""%())

    elif mselect == 9: # 9. Find shortest path from a given user
        # path finding process
        print("""
The shortest path from "%s" to "%s" is

%s"""%())

    elif mselect == 99: # 99. Quit
        exit()
    else: #Other numbers
        print("Wrong order!")

    input("Press the Enter key to continue.")
    print("\n\n\n")
    interface()



