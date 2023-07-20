# Lisa IA

![alt text](static/img/lisa_photo.jpg "Photo generate by ia for represent Lisa")

## What is it ?

Lisa IA is a simple code to launch a small web server with Flask and a discord bot at the same time to be able to exchange with ChatGPT in a personalized way ( Prompt defined by you ) 

## Requirements

You can download everything you need in the "requirements.txt" file.

```
pip install -r requirements.txt
```

## Customization

To customize most of the code, you can base it on .env.example

Start by renaming it to ".env" or copying it under this name - everything is detailed in the comments.

As for promptsn ckeck directly the .env on part "Open IA / Prompts"

## How to launch Lisa AI

After installing the requirements and modifying the .env file, issue the following command: 

```
python launcher.py
```

## Bug known and being solved

>**July 18, 2023**
> 
> discord.py launches twice so Lisa responds twice
> 
> Status : **FIXED**
> ID : B-0-0-1-A

## Changelogs

>**July 19, 2023**
> 
> Updated V0.1.0 :
> - launcher.py: fixed the bug that launched main twice, added print to make it prettier 🥰
> - README.md : Adding the WIP part
> - lisa_bot / lisa_web : improved and optimized 
> - .env : added variable for lisa_bot and lisa_web to personify code directly in .env, no need to touch the code directly 😘


>**July 18, 2023**
> 
> Updated :
> - README.md: user information added
> - launcher.py: improved and optimized 

## Work In Progess

> Add : 
> 
> Give the user the option of resetting the AI's memory in the discord bot as in the web version, as well as setting a custom prompt. 
>
> Status : WIP

## Credits and acknowledgements

I would like to mention here the sources I used and the people who helped me.

>For the lisa_web GUI, I used @RuifMaxx's code.
>
>https://github.com/RuifMaxx/ChatGPT-API-WebUI

> Big Thanks : @XenorDoz 
> 
> He helps me to correct English mistakes and also helps me to correct :
> 
> - Bug id ID : B-0-0-1-A

