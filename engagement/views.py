from instaloader.structures import Post
import requests
from django.shortcuts import render

# Create your views here.
def index(reqeust):
    return render(reqeust,'index.html')
def engagement(reqeust):
    target_profile = reqeust.GET['targetProfile']

    from instaloader import Instaloader, Profile
    import instaloader
    from instaloader.structures import Post
    loader = Instaloader()

    profile = Profile.from_username(loader.context, target_profile)

    num_followers = profile.followers
    total_num_likes = 0
    total_num_comments = 0
    total_num_posts = 0
    total_num_views = 0
    total_num_posts = 0
    total_numof_posts = 0

    for post in profile.get_posts():
        total_num_likes += post.likes
        total_num_comments += post.comments
        if post.is_video == True:
            total_num_views += post.video_view_count    
        total_num_posts += 1
    engagement = float(total_num_likes + total_num_comments + total_num_views) / (num_followers * total_num_posts)
    engagement = engagement * 100
    Avglikes = int(total_num_likes/total_num_posts)
    Avgcomments = int(total_num_comments/total_num_posts)
    for post in profile.get_posts():
        total_numof_posts += 1
    return render(reqeust,'index.html',{'engagement':engagement,'total_numof_posts':total_numof_posts,'Avglikes':Avglikes,'Avgcomments':Avgcomments})