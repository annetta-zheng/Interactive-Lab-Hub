# Interactive Prototyping: The Clock of Pi

## Overview
For this assignment, you are going to 

A) [Connect to your Pi](#part-a)  

B) [Try out cli_clock.py](#part-b) 

C) [Set up your RGB display](#part-c)

D) [Try out clock_display_demo](#part-d) 

E) [Modify the code to make the display your own](#part-e)
- [The Sensory Time Capsule Clock, ClockIn](#The-Sensory-Time-Capsule-Clock-ClockIn)
- [Baseline. Mirroring the changing emotions](#Baseline-Mirroring-the-changing-emotions)
- [Interactions 1. Reflection Reminder](#Interactions-1-Reflection-Reminder)
- [Interactions 2. Emotion Checker](#Interactions-2-Emotion-Checker)
- [Interactions 3. Tour with Sustainability Awareness](#Interactions-3-Tour-with-Sustainability-Awareness)
- [Interactions 4. Chinese Divination](#Interactions-4-Chinese-Divination)
- [Interactions 5. Memory Collector](#Interactions-5-Memory-Collector)

F) [Make a short video of your modified barebones PiClock](#part-f)

G) [Sketch and brainstorm further interactions and features you would like for your clock for Part 2.](#part-g)


Does it feel like time is moving strangely during this semester?

For our first Pi project, we will pay homage to the [timekeeping devices of old](https://en.wikipedia.org/wiki/History_of_timekeeping_devices) by making simple clocks.

It is worth spending a little time thinking about how you mark time, and what would be useful in a clock of your own design.

**Please indicate anyone you collaborated with on this Lab here.**
Be generous in acknowledging their contributions! And also recognizing any other influences (e.g. from YouTube, Github, Twitter) that informed your design. 

## Prep

Lab Prep is extra long this week. Make sure to start this early for lab on Thursday.

1. ### Set up your Lab 2 Github

Before the start of lab Thursday, [pull changes from the Interactive Lab Hub](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2021Fall/readings/Submitting%20Labs.md#to-pull-lab-updates) so that you have your own copy of Lab 2 on your own lab hub.


  If you are organizing your Lab Hub through folder in local machine, go to terminal, cd into your Interactive-Lab-Hub folder and run:

  ```
  Interactive-Lab-Hub $ git remote add upstream https://github.com/FAR-Lab/Interactive-Lab-Hub.git
  Interactive-Lab-Hub $ git pull upstream Fall2023
  ```
  
  The reason why we are adding a upstream with **course lab-hub** instead of yours is because the local Interactive-Lab-Hub folder is linked with your own git repo already. Try typing ``git remote -v`` and you should see there is the origin branch with your own git repo. We here add the upstream to get latest updates from the teaching team by pulling the **course lab-hub** to your local machine. After your local folder got the latest updates, push them to your remote git repo by running:
  
  ```
  Interactive-Lab-Hub $ git add .
  Interactive-Lab-Hub $ git commit -m "message"
  Interactive-Lab-Hub $ git push
  ```
  Your local and remote should now be up to date with the most recent files.

The new GitHub.com UI makes this step easy from the webbrowser:
![image](https://github.com/FAR-Lab/Interactive-Lab-Hub/assets/90477986/91d0fbc8-2eba-401f-a5a7-66640910cb62)


2. ### Get Kit and Inventory Parts
Prior to the lab session on Thursday, taken inventory of the kit parts that you have, and note anything that is missing:

***Update your [parts list inventory](partslist.md)***

3. ### Prepare your Pi for lab this week
[Follow these instructions](prep.md) to download and burn the image for your Raspberry Pi before lab Thursday.


## The Report
This readme.md page in your own repository should be edited to include the work you have done. You can delete everything but the headers and the sections between the \*\*\***stars**\*\*\*. Write the answers to the questions under the starred sentences. Include any material that explains what you did in this lab hub folder, and link it in the readme.

Labs are due on Mondays. Make sure this page is linked to on your main class hub page.

## Part A. 
### Connect to your Pi
Just like you did in the lab prep, ssh on to your pi. Once you get there, create a Python environment (named venv) by typing the following commands.

```
ssh pi@<your Pi's IP address>
...
pi@raspberrypi:~ $ python -m venv venv
pi@raspberrypi:~ $ source venv/bin/activate
(venv) pi@raspberrypi:~ $ 

```
### Setup Personal Access Tokens on GitHub
Set your git name and email so that commits appear under your name.
```
git config --global user.name "Your Name"
git config --global user.email "yourNetID@cornell.edu"
```

The support for password authentication of GitHub was removed on August 13, 2021. That is, in order to link and sync your own lab-hub repo with your Pi, you will have to set up a "Personal Access Tokens" to act as the password for your GitHub account on your Pi when using git command, such as `git clone` and `git push`.

Following the steps listed [here](https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token) from GitHub to set up a token. Depends on your preference, you can set up and select the scopes, or permissions, you would like to grant the token. This token will act as your GitHub password later when you use the terminal on your Pi to sync files with your lab-hub repo.


## Part B. 
### Try out the Command Line Clock
Clone your own lab-hub repo for this assignment to your Pi and change the directory to Lab 2 folder (remember to replace the following command line with your own GitHub ID):

```
(venv) pi@raspberrypi:~$ git clone https://github.com/<YOURGITID>/Interactive-Lab-Hub.git
(venv) pi@raspberrypi:~$ cd Interactive-Lab-Hub/Lab\ 2/
```
Depends on the setting, you might be asked to provide your GitHub user name and password. Remember to use the "Personal Access Tokens" you just set up as the password instead of your account one!


Install the packages from the requirements.txt and run the example script `cli_clock.py`:

```
(venv) pi@raspberrypi:~/Interactive-Lab-Hub/Lab 2 $ pip install -r requirements.txt
(venv) pi@raspberrypi:~/Interactive-Lab-Hub/Lab 2 $ python cli_clock.py 
02/24/2021 11:20:49
```

The terminal should show the time, you can press `ctrl-c` to exit the script.
If you are unfamiliar with the Python code in `cli_clock.py`, have a look at [this Python refresher](https://hackernoon.com/intermediate-python-refresher-tutorial-project-ideas-and-tips-i28s320p). If you are still concerned, please reach out to the teaching staff!


## Part C. 
### Set up your RGB Display
We have asked you to equip the [Adafruit MiniPiTFT](https://www.adafruit.com/product/4393) on your Pi in the Lab 2 prep already. Here, we will introduce you to the MiniPiTFT and Python scripts on the Pi with more details.

<img src="https://cdn-learn.adafruit.com/assets/assets/000/082/842/large1024/adafruit_products_4393_iso_ORIG_2019_10.jpg" height="200" />

The Raspberry Pi 4 has a variety of interfacing options. When you plug the pi in the red power LED turns on. Any time the SD card is accessed the green LED flashes. It has standard USB ports and HDMI ports. Less familiar it has a set of 20x2 pin headers that allow you to connect a various peripherals.

<img src="https://maker.pro/storage/g9KLAxU/g9KLAxUiJb9e4Zp1xcxrMhbCDyc3QWPdSunYAoew.png" height="400" />

To learn more about any individual pin and what it is for go to [pinout.xyz](https://pinout.xyz/pinout/3v3_power) and click on the pin. Some terms may be unfamiliar but we will go over the relevant ones as they come up.

### Hardware (you have already done this in the prep)

From your kit take out the display and the [Raspberry Pi 4](https://cdn-shop.adafruit.com/970x728/3775-07.jpg)

Line up the screen and press it on the headers. The hole in the screen should match up with the hole on the raspberry pi.

<p float="left">
<img src="https://cdn-learn.adafruit.com/assets/assets/000/087/539/medium640/adafruit_products_4393_quarter_ORIG_2019_10.jpg?1579991932" height="200" />
<img src="https://cdn-learn.adafruit.com/assets/assets/000/082/861/original/adafruit_products_image.png" height="200">
</p>

### Testing your Screen

The display uses a communication protocol called [SPI](https://www.circuitbasics.com/basics-of-the-spi-communication-protocol/) to speak with the raspberry pi. We won't go in depth in this course over how SPI works. The port on the bottom of the display connects to the SDA and SCL pins used for the I2C communication protocol which we will cover later. GPIO (General Purpose Input/Output) pins 23 and 24 are connected to the two buttons on the left. GPIO 22 controls the display backlight.

To show you the IP and Mac address of the Pi to allow connecting remotely we created a service that launches a python script that runs on boot. For the following steps stop the service by typing ``` sudo systemctl stop mini-screen.service```. Othwerise two scripts will try to use the screen at once. 

We can test it by typing 
```
(venv) pi@raspberrypi:~/Interactive-Lab-Hub/Lab 2 $ python screen_test.py
```

You can type the name of a color then press either of the buttons on the MiniPiTFT to see what happens on the display! You can press `ctrl-c` to exit the script. Take a look at the code with
```
(venv) pi@raspberrypi:~/Interactive-Lab-Hub/Lab 2 $ cat screen_test.py
```

#### Displaying Info with Texts
You can look in `screen_boot_script.py` and `stats.py` for how to display text on the screen!

#### Displaying an image

You can look in `image.py` for an example of how to display an image on the screen. Can you make it switch to another image when you push one of the buttons?



## Part D. 
### Set up the Display Clock Demo
Work on `screen_clock.py`, try to show the time by filling in the while loop (at the bottom of the script where we noted "TODO" for you). You can use the code in `cli_clock.py` and `stats.py` to figure this out.

### How to Edit Scripts on Pi
Option 1. One of the ways for you to edit scripts on Pi through terminal is using [`nano`](https://linuxize.com/post/how-to-use-nano-text-editor/) command. You can go into the `screen_clock.py` by typing the follow command line:
```
(venv) pi@raspberrypi:~/Interactive-Lab-Hub/Lab 2 $ nano screen_clock.py
```
You can make changes to the script this way, remember to save the changes by pressing `ctrl-o` and press enter again. You can press `ctrl-x` to exit the nano mode. There are more options listed down in the terminal you can use in nano.

Option 2. Another way for you to edit scripts is to use VNC on your laptop to remotely connect your Pi. Try to open the files directly like what you will do with your laptop and edit them. Since the default OS we have for you does not come up a python programmer, you will have to install one yourself otherwise you will have to edit the codes with text editor. [Thonny IDE](https://thonny.org/) is a good option for you to install, try run the following command lines in your Pi's ternimal:

  ```
  pi@raspberrypi:~ $ sudo apt install thonny
  pi@raspberrypi:~ $ sudo apt update && sudo apt upgrade -y
  ```

Now you should be able to edit python scripts with Thonny on your Pi.

Option 3. A nowadays often preferred method is to use Microsoft [VS code to remote connect to the Pi](https://www.raspberrypi.com/news/coding-on-raspberry-pi-remotely-with-visual-studio-code/). This gives you access to a fullly equipped and responsive code editor with terminal and file browser.  

Pro Tip: Using tools like [code-server](https://coder.com/docs/code-server/latest) you can even setup a VS Code coding environment hosted on your raspberry pi and code through a web browser on your tablet or smartphone! 

## Part E.

<details>
  
  <summary>Click to expand the requiremnts</summary>
Does time have to be linear?  How do you measure a year? [In daylights? In midnights? In cups of coffee?](https://www.youtube.com/watch?v=wsj15wPpjLY)

Can you make time interactive? You can look in `screen_test.py` for examples for how to use the buttons.

Please sketch/diagram your clock idea. (Try using a [Verplank digram](http://www.billverplank.com/IxDSketchBook.pdf)!
**We strongly discourage and will reject the results of literal digital or analog clock display.**

</details>

## The Sensory Time Capsule Clock. ClockIn

### ClockIn as an Emotion Checker and Memory Collector 
The "Sensory Time Capsule" clock is designed to make time a multisensory and interactive experience. It focuses on measuring time in personal and meaningful ways, incorporating elements like background color change, background image change, text display, and interactive buttons. Instead of displaying hours and minutes conventionally, this clock encourages users to engage with time through their senses and emotions.
- \*\*\***Please see the file ```clockin.py``` for my code for ClockIn.**\*\*\*  

#### Baseline. Mirroring the changing emotions
The clock wil change its display and background color based on time as a reminding of time and avoking different energy or emotions to the users. (Please see video).

  _after coding I found that the backgroud image changes need some intereactions, so the image change becomes interaction #1 when both A and B are pressed._
![Alt text](diagram0.jpg)

#### Interactions 1. Reflection Reminder
Instead of showing numerical time, the clock displays inspirational quotes, personal affirmations, or thought-provoking messages related to the time of day or the month of year. These messages are designed to stimulate reflection and mindfulness as well. (Please see video).

#### Interactions 2. Emotion Checker

The clock triggers a brief mindfulness exercise base on time, prompting users to reflect on their emotions and well-being. It might suggest a deep breath, a moment of gratitude, or a mindfulness exercise. (Please see video).

![Alt text](diagram1.jpg)


```
suggestions = {
  'morning' : ['Good Morning~~~~~',
                      'Time for a coffee!',
                      'Do some morning mediation!',
                      'Stretching Time.',
                      'Do some light exercises.',
                      "Plan for the day ahead."],
  'noon': ['Stay hydrated!',
            "Grab a snack to keep up energy.",
            'Check your emails',
            'Prioritize tasks.',
            "Take a short break :D",
            "Do a mindfulness exercise.",
            'Get some fresh air.'],
  "afternoon": ["Wind down and review your day's progress.",
                "Spend time with family or friends.",
                "Have a relaxing evening routine.",
                "Take a walk for a mental break.",
                'Time for some exercise!','(°∀°)ﾉ',
                'Live in the moment.'] ,
  'night' : ['Goodnight~~~~~','ʕ•ᴥ•ʔ',
              "Limit screen time for better sleep.",
              "Practice deep breathing to unwind.",'_(:3」∠)____',
              "Reflect on the positive moments.",
              "Prepare for tomorrow and set goals.",'ƪ(˘⌣˘)ʃ']}
```



#### Interactions 3. Tour with Sustainability Awareness 
The Clock will allow you take a brief break to another world at different altitude. After the tour it will display a enviormental issue 

The current demo version is the Marine World, from 600 meters in the sky to -1000 meters in the water.
It allows you to go to different levels of altitude or different views at the same sea level. 
After the tour, it will tell you how many marine animals have died because of the plastic during your touring time length. (Please see video).

Folder `aqua` contains different photos for the tour, and here are a few examples:
1. 60 meter example

   ![60_3](https://github.com/annetta-zheng/Interactive-Lab-Hub/assets/67286396/43a96764-566d-459b-8bb5-a0ddc27ab863)
  
2. 0 meter sea level example
   
   ![0_3](https://github.com/annetta-zheng/Interactive-Lab-Hub/assets/67286396/e404e4ef-4546-4b03-aa86-23766bb108ea)
   
3. -1000 meters underwater exaple

   ![-100_1](https://github.com/annetta-zheng/Interactive-Lab-Hub/assets/67286396/8dd49c90-b93c-4fc5-9027-94bf7419955a)

Diagrams:

![171694909092_ pic](https://github.com/annetta-zheng/Interactive-Lab-Hub/assets/67286396/4aa7866d-86af-4879-b908-e642d052f8b3)

![201694912466_ pic](https://github.com/annetta-zheng/Interactive-Lab-Hub/assets/67286396/dddb1f74-9e13-4b22-8e9a-448736e88c3e)

![211694912591_ pic](https://github.com/annetta-zheng/Interactive-Lab-Hub/assets/67286396/ae381e54-403e-4377-aee9-1391d6fcd6ba)

![221694912716_ pic_hd](https://github.com/annetta-zheng/Interactive-Lab-Hub/assets/67286396/a6801d45-2129-4961-a114-256ae8003c5b)

#### Interactions #4: Chinese Divination
The clock will generate a divination based on Chinese Lunar Calender. 梅花易数 is a tradition Chinese divination method like tarot.
However, I couldn't figure out how the code would work properly. The [link](https://www.cnblogs.com/luoxian1011/p/15732754.html) contains the code I found for converting time to a divination.

ideally I would display time in the format in the picture:

<img width="292" alt="image" src="https://github.com/annetta-zheng/Interactive-Lab-Hub/assets/67286396/14a6f6f2-d43e-48a3-a014-4cfb46eeb712">

Then if the player wants to do a divination, the display will show the result like:

<img width="482" alt="image" src="https://github.com/annetta-zheng/Interactive-Lab-Hub/assets/67286396/f054e06f-e3a9-4593-a54d-c3aed02f5a7e">


With further connections / explaintions to the nature element like fire / wind / water / metal / soil.

<img width="434" alt="image" src="https://github.com/annetta-zheng/Interactive-Lab-Hub/assets/67286396/46abaa17-1aa5-4040-b1e2-05920f9774fe">

#### Interactions 5. Memory Collector
The Clock will generate a random task on the right side, and display the time remaining to complete the task on the left side. The color blocks representing the time will decrease as time passes by. After the task is finished, the clock saves a snap with the current sensory experience in a digital journal for later reflection. (I'm still trying to figure out for the code so there is no video for this interaction.)
![Alt text](diagram2.jpg)


## Part F. 
## Make a short video of your modified barebones PiClock
- if any video fails, please see the folder: https://drive.google.com/drive/folders/1kv7lCBnJk674OqSsMxS0a3OFfw85_XtE?usp=share_link

1. **Baseline: Mirroring the changing emotions**

- As time differs 12PM ('noon') and 2AM ('night'), the background color shifts gradually and dynamically, reflect the changing scenes of nature or life events.
  
https://github.com/annetta-zheng/Interactive-Lab-Hub/assets/67286396/da2f63ca-d1d0-4ab5-b787-ccc313e78dd9

https://github.com/annetta-zheng/Interactive-Lab-Hub/assets/67286396/7fc741b5-d88e-44f5-bb72-b265239a864e


 
2. **Interactions #1: Reflection Reminder**


- When taking the video, it's autumn and 12PM ('noon'). When click both A and B buttons, the clock will display cheering reminders.

https://github.com/annetta-zheng/Interactive-Lab-Hub/assets/67286396/ae15f66d-200f-46a7-8cfa-985f2db3661b

- When taking the video, it's autumn and 2AM ('night'). When click both A and B buttons, the clock will display smoothing reminders.
  
https://github.com/annetta-zheng/Interactive-Lab-Hub/assets/67286396/ffb916fa-6401-4451-8d52-4c0c02dcdca7

  

3. **Interactions #2: Emotion Checker**

- When taking the video, it's 12PM ('noon'). It might suggest a work quote, an encouragement, or a task reminder.
  
https://github.com/annetta-zheng/Interactive-Lab-Hub/assets/67286396/4dd66868-4acc-42bc-8db3-c3568f18f561

- When taking the video, it's 2AM ('night'). It might suggest a deep breath, a moment of gratitude, or a mindfulness exercise.
  
https://github.com/annetta-zheng/Interactive-Lab-Hub/assets/67286396/6811117a-97aa-4250-a3dd-d602004ea246


4. **Interactions #3: Tour with Sustainability Awareness**

- Step in the tour
- Interact with hand gestures up / down / left / right
- End the tour if reach the bottom of sea / the top of the sky / click button A to exit
- Show the number of marine animals died due to plastic since the player stepped in the tour.

https://github.com/annetta-zheng/Interactive-Lab-Hub/assets/67286396/88dae20b-cdcb-4ace-a5f8-0dfe4327f26d



  
## Part G. 
## Sketch and brainstorm further interactions and features you would like for your clock for Part 2.

1. Interactions: Mood Tracker
   
Include a mood tracker that prompts users to rate their mood periodically. Over time, the clock can create a mood history chart, helping users identify patterns in their emotional well-being.

2. Interactions: Music and Soundscapes
   
Allow users to select background music or soundscapes that match the sensory experience. For example, during a "Beach Day" theme, users can choose to play ocean waves in the background.

3. Interactions: Mindful Breathing Exercises
   
Expand the "Emotion Checker" interaction to include guided mindful breathing exercises. Users can follow along with on-screen animations and instructions for relaxation and stress reduction.

4. Interactions: Goal Setting
   
Enable users to set daily or weekly goals through the clock. The clock can remind users of their goals and provide motivational messages to help them stay on track.

5. Interactions: Daily Challenges
   
Present users with daily challenges related to well-being, creativity, or personal growth. Completing these challenges can lead to rewards or additional sensory experiences.

6. Feature: Weather
   
Integrate weather information and adjust the clock's sensory elements based on the current weather conditions. For instance, on a rainy day, the clock could display soothing raindrop animations and calming messages.

7. Feature: Themed Days
   
Introduce themed days or weeks where the clock aligns its sensory elements with a particular theme chosen by the user. For example, a "Nature Week" could feature natural background images, colors, and messages related to the outdoors.

_____________

After you edit and work on the scripts for Lab 2, the files should be upload back to your own GitHub repo! You can push to your personal github repo by adding the files here, commiting and pushing.

```
(venv) pi@raspberrypi:~/Interactive-Lab-Hub/Lab 2 $ git add .
(venv) pi@raspberrypi:~/Interactive-Lab-Hub/Lab 2 $ git commit -m 'your commit message here'
(venv) pi@raspberrypi:~/Interactive-Lab-Hub/Lab 2 $ git push
```

After that, Git will ask you to login to your GitHub account to push the updates online, you will be asked to provide your GitHub user name and password. Remember to use the "Personal Access Tokens" you set up in Part A as the password instead of your account one! Go on your GitHub repo with your laptop, you should be able to see the updated files from your Pi!


# Prep for Part 2

1. Pick up remaining parts for kit on Thursday lab class. Check the updated [parts list inventory](partslist.md) and let the TA know if there is any part missing.
  
2. Look at and give feedback on the Part G. for at least 2 other people in the class (and get 2 people to comment on your Part G!)

# Lab 2 Part 2

Pull Interactive Lab Hub updates to your repo.

Modify the code from last week's lab to make a new visual interface for your new clock. You may [extend the Pi](Extending%20the%20Pi.md) by adding sensors or buttons, but this is not required.

As always, make sure you document contributions and ideas from others explicitly in your writeup.

i have some ideas about the Chinese Lunar Calender and make divination based on that. However, I couldn't figure out how the code would work properly. The link below contains the code I found for converting time to a divination
-  https://www.cnblogs.com/luoxian1011/p/15732754.html


You are permitted (but not required) to work in groups and share a turn in; you are expected to make equal contribution on any group work you do, and N people's group project should look like N times the work of a single person's lab. What each person did should be explicitly documented. Make sure the page for the group turn in is linked to your Interactive Lab Hub page. 


