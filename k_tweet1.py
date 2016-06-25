
class User:
    def __init__(self):
        self.n =

    def u_add(self):

class Tweet:
    def __init__(self):

    def t_add():

    def t_delete(): # tweet delete는 별개로 수행

    def t_find

class Friend:
    def __init(self):

    def f_add():

    def f_delete(): # friend delete는 별개로 수행

class Scc:
    def

class Spath:




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
        location1 = input(("\nEnter USER file location\n"))
        location2 = input(("\nEnter TWEET file location\n"))
        location3 = input(("\nEnter FRIEND file location\n"))
        #reading process
        print("""
Total users: %d
Total friendship records: %d
Total tweets: %d"""%())

    elif mselect == 1: # 1. display statistics
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
        input("Number should separated by comma(,) - ex)1,3,5 ")
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



