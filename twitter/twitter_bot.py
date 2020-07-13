#!/user/bin/python
import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("CONSUMER_KEY", "CONSUMER_SECRET")
auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")

# Create API object
api = tweepy.API(auth)


# 1. LOg on to twitter
# 2. Find new tweets
# 3. Like new tweets
# 4. Follow the user
# 5. Store their name, save it soewhere we can look back at it
# 6. unfollow the user that dont follow back after 1 hour
# 7. Save the names of those who followed us back
# 8. write the lists to a file in case of a error
