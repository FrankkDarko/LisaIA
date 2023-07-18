#Lisa IA

![alt text](static/img/lisa_photo.jpg "Photo generate by ia for represent Lisa")

##What is it ?

Lisa IA is a simple code to launch a small web server with Flask and a discord bot at the same time to be able to exchange with ChatGPT in a personalized way ( Prompt defined by you ) 

##Requirements

You can download everything you need in the "requirements.txt" file.

```
pip install -r requirements.txt
```

##Customization

To customize most of the code, you can base it on .env.example

Start by renaming it to ".env" or copying it under this name - everything is detailed in the comments.

As for prompts :

- in lisa_web.py: line 73,75,76

- in lisa_bot.py: line 17,20,21

##How to launch Lisa AI

After installing the requirements and modifying the .env file, issue the following command: 

```
python launcher.py
```

##Bug known and being solved

>**July 18, 2023**
> 
>discord.py launches twice so Lisa responds twice

##Changelogs

>**July 18, 2023**
> 
> updated from :
> - README.md: user information added
> - launcher.py: improved and optimized 

##Credits and acknowledgements

I would like to mention here the sources I used and the people who helped me.

>For the lisa_web GUI, I used @RuifMaxx's code.
>
>https://github.com/RuifMaxx/ChatGPT-API-WebUI