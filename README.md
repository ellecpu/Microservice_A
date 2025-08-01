# Microservice_A
This is the Score Management Microservice implemented by me for the main program of Argent.

Note: The Microservice must be kept in the same in the same directory as UserTopScores.txt and typingsessionresults.txt, if these files do not exist, they must be created first.

**How to request data:**

Data can be requested through 2 methods 
get_saved_top_score(username) and update_user_top_score(username), both of these methods take username (String) as the only parameter and both return the user top score, the difference is that update_user_top_score(username) recalculates the top score and saves it in the UserTopScore.txt before returning the data while get_saved_top_score(username) scans the UserTopScore.txt and returns the top score. before calling get_saved_top_score(username), the method update_user_top_score(username) must be called to ensure up to date high score.

example call:

user = "Guest2"
#Recalculate Top score.
update_user_top_score(user)

#Get Saved top score for a user
get_saved_top_score(user)

**How to receive data:**

After calling both the update_user_top_score(username) and get_saved_top_score(user) method, the user recives a JSON object, it can be received by capturing it in a variable.

example call:

user = "Guest2"

#Recalculate Top score after every session
new_top = update_user_top_score(user) 
print(new_top)

#Get Saved top score  for a user
saved_score = get_saved_top_score(user)
print(saved_score)


UML Diagram:
<img width="1602" height="1063" alt="Sequence diagram (1)" src="https://github.com/user-attachments/assets/13162812-9494-403c-ab0d-fedb820380a7" />


