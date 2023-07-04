# Harry-Potter-Short-Video-Creator
 This is A Tool To Create Short Videos With Audio About Spells From The Harry Potter World 

- Here I Used The https://hp-api.onrender.com API To Get Information About The Spells To Be Used In The Videos And Stored Them In A Local Database

# What Does This Tool DO
- Each Time It Runs It Creates A Single Episode With 3 Spells And Their Description
- It Uses A Text To Speech Library To Read The Video's Content
- It Creates A Ready To Use Video, As It Creates Its Own Video Intro, Sounds And Images

# How To Use It
- Install The Requirements Using 
```
pip install -r requirements.txt
```
- Make Sure You Have ffmpeg
- Just Run The "main.py" File And It Will Create A Single Episode Each Time
- Each Episode And Its Contents Will Be Saved Inside The EPisodes Folder In A Folder With The Episode's Name
- To Reset Everything Just Run The "reset_episodes.py" File
- You Can Change The Images In The Backgrounds Folder To Change The Video's Background

# How Does it Work
- The Tool Chooses 3 Random Spells From The Database And Marks Them With The Episode Number They Were Chosen In
- It Converts The Spells Information To Audio
- Then Picks A Random Background From The backgrounds Folder
- Then it adds Spells Names And Description To It
- Then Create A Video For Each Spell Of them
- With Each Step the Intro Is Being Created Too
- Then it Merges All The Videos Together With The Intro Video To Make The Final Video
- Everything Is Placed In The Episodes Folder

# Extras
- I Left The Spells json And Text Files So It's Easier To See What Is Being Used
- I Also Left The Code That I Used To Gather The Data From The API in The 'api.py' File

