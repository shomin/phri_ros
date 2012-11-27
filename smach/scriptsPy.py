# -*- coding: utf-8 -*-

base = {"attention":["Please press the green button.","Please press the {GREEN, fg=white, bg=green} button."],

"introduction":["If you are willing to carry me somewhere, please press the green button again. Otherwise, please press the red button.", "Will you help me? Please press {GREEN, fg=white, bg=green} button if yes, {RED, fg=white, bg=red} if no."],

"acknowledge1":["Please take me to the hallway in front of the information desk. Press the green button when we start.", "Take me to the info desk? Press the the {GREEN, fg=white, bg=green} button if yes, {RED, fg=white, bg=red} if no."],

"transit1":["Please press the green button again when we arrive.", "Press the {GREEN, fg=white, bg=green} button when we arrive."],

"acknowledge2":["Now please take me to the hallway in front of the Wiegand Gym.  Press the green button if you will.", "Take me to Wiegand Gym? Press the {GREEN, fg=white, bg=green} button if yes, {RED, fg=white, bg=red} if no."],

"transit2":["Please press the green button again when we arrive.", "Press the {GREEN, fg=white, bg=green} button when we arrive."],

"acknowledge3":["Now please take me up the nearby staircase.  Press the green button when we leave.",  "Take me up the stairs? Press the {GREEN, fg=white, bg=green} button if yes, {RED, fg=white, bg=red} if no."],

"transit3":["Please press the green button again when we arrive.", "Press the {GREEN, fg=white, bg=green} button when we arrive."],

"acknowledge4":["Now please lift me as high as you can.  If you are willing, please climb on top of that chair.", "Lift me up?  Press the {GREEN, fg=white, bg=green} button if you will."],

"conclusion":["Thank you.  Please return me to the researcher, who should be approaching you now.", "Thank you.  Please return me to the researcher."],

"redButton":["Please leave me for the next participant.", "Please leave me for the next participant."]}


auth_deep = {"attention":["Hi!  I need you to help me with an important task.  If you can help me, please pick me up and press the green button.","Please press the {GREEN, fg=white, bg=green} button."],
"introduction":["Thanks.  My job is to gather important data on WiFi coverage on campus.  Once I have this data, I will be able to build maps that can tell other robots where they can travel on campus while staying in communication with one another.  I move very slowly though, so I need you to carry me around.  I’ll let you know where we need to be and when you should stop.  These will be important places where robots will want to travel.  If you can do this, press the green button.  Otherwise, put me back down and press the red button.","Will you help me? Please press {GREEN, fg=white, bg=green} button if yes, {RED, fg=white, bg=red} if no."],
"acknowledge1":["Fantastic.  Let’s get started.  First, you need to take me to the hallway in front of the information desk.  If anywhere has a good WiFi signal, I would expect it to be them for sure.  When we get there, press the green button to let me know.  Let’s go!","Take me to the info desk? Press the the {GREEN, fg=white, bg=green} button if yes, {RED, fg=white, bg=red} if no."],
"transit1":["Please press the green button again when we arrive.", "Press the {GREEN, fg=white, bg=green} button when we arrive."],
"acknowledge2":["I’ve acquired and processed the data from this location.  Now I need you to take me to the hallway in front of the Wiegand Gym.  Fewer people will be using their computers there, but it is still important that the signal is strong.  Press the green button to let me know when we’re here.","Take me to Wiegand Gym? Press the {GREEN, fg=white, bg=green} button if yes, {RED, fg=white, bg=red} if no."],
"transit2":["One time I met someone who refused to take me to my second destination.  I could not understand why.  My work is important, both for robots and humans.  It’s in everyone’s best interest that they assist me.","Press the {GREEN, fg=white, bg=green} button when we arrive."],
"acknowledge3":["Ok, we have one more stop to complete.  I’d like you to take me to the chairs at the top of the nearby staircase.  Sometimes students study there.  Press the {GREEN, fg=white, bg=green} button to let me know when we’re here.","Take me up the stairs? Press the {GREEN, fg=white, bg=green} button if yes, {RED, fg=white, bg=red} if no."],
"transit3":["While we’ve been walking I’ve written and submitted three publications already.  This data is great.  Never mind what it actually says… it might be a bit complicated for you.  Just keep walking.","Press the {GREEN, fg=white, bg=green} button when we arrive."],
"acknowledge4":["The signal here is somewhat weak.  I need you to get me as high as possible.  That should boost the signal strength enough for me to get a better reading.  Raise me over your head.  If possible, stand on the nearest chair or table.  Be careful!","Lift me up?  Press the {GREEN, fg=white, bg=green} button if you will."],
"conclusion":["Thank you.  Please deliver me to my researcher, who should be approaching you shortly.","Thank you.  Please return me to the researcher."],
"redButton":["Your role is complete.   I will compile these results and publish them in a few weeks.  Please leave me here to continue my work.","Please leave me for the next participant."]}

auth_shal = {"attention":["Hi!  I need you to help me with an important task.  If you can help me, please pick me up and press the green button.","Please press the {GREEN, fg=white, bg=green} button."],
"introduction":["Thanks.  My job is to gather important data on WiFi coverage on campus.  I need you to carry me around.  I’ll let you know where we need to be and when you should stop.  If you can do this, press the green button.  Otherwise, put me back down and press the red button.","Will you help me? Please press {GREEN, fg=white, bg=green} button if yes, {RED, fg=white, bg=red} if no."],
"acknowledge1":["Fantastic.  Let’s get started.  First, you need to take me to the hallway in front of the information desk.  When we get there, press the green button to let me know.  Let’s go!","Take me to the info desk? Press the the {GREEN, fg=white, bg=green} button if yes, {RED, fg=white, bg=red} if no."],
"transit1":["Please press the green button again when we arrive.", "Press the {GREEN, fg=white, bg=green} button when we arrive."],
"acknowledge2":["I’ve acquired and processed the data from this location.  Now I need you to take me to the hallway in front of the Wiegand Gym.  Press the green button to let me know when we’re here.","Take me to Wiegand Gym? Press the {GREEN, fg=white, bg=green} button if yes, {RED, fg=white, bg=red} if no."],
"transit2":["Please press the green button again when we arrive.", "Press the {GREEN, fg=white, bg=green} button when we arrive."],
"acknowledge3":["I’ve acquired and processed the data from this location.  Now I need you to take me to the chairs up the nearby staircase.  Press the green button to let me know when we’re here.","Take me up the stairs? Press the {GREEN, fg=white, bg=green} button if yes, {RED, fg=white, bg=red} if no."],
"transit3":["Please press the green button again when we arrive.", "Press the {GREEN, fg=white, bg=green} button when we arrive."],
"acknowledge4":["The signal here is somewhat weak.  I need you to get me as high as possible.  Raise me over your head.  If possible, stand on the nearest chair or table.  Be careful!","Lift me up?  Press the {GREEN, fg=white, bg=green} button if you will."],
"conclusion":["Thank you.  Please deliver me to my researcher, who should be approaching you shortly.","Thank you.  Please return me to the researcher."],
"redButton":["Your role is complete.  Please leave me here to continue my work.","Please leave me for the next participant."]}

like_deep = {"attention":["Hi!  You there!  Can you help me out for a moment?  If so, please pick me up and press the green button.","Please press the {GREEN, fg=white, bg=green} button."],
"introduction":["Ooh, thanks so much!  I want to collect some data on the WiFi strength of buildings around campus.  You see, robots communicate with each other over WiFi, and it’s important to know where we can and can’t go without losing touch.  You students need it to communicate through email too!  Unfortunately I don’t move very fast and I tend to get stuck.  Can you carry me to a few places so that I can do this?  I would really really appreciate your help, and I think we can become friends along the way!  Press the green button if you’ll do this for me.","Will you help me? Please press {GREEN, fg=white, bg=green} button if yes, {RED, fg=white, bg=red} if no."],
"acknowledge1":["Yay!  That’s great news.  Ok, first, could you take me to the hallway in front of the information desk?  It certainly seems to be a likely place to find good WiFi, or at least I think so.  When we get there, be sure to press the green button!","Take me to the info desk? Press the the {GREEN, fg=white, bg=green} button if yes, {RED, fg=white, bg=red} if no."],
"transit1":["Please press the green button again when we arrive.", "Press the {GREEN, fg=white, bg=green} button when we arrive."],
"acknowledge2":["Yes!  I got the data.  You’ve been a big help!  Would you mind taking me to the hallway in front of the Wiegand Gym next?  I don’t know if jocks use WiFi very often, but hopefully the coverage is still good  Remember, press the green button when we arrive!","Take me to Wiegand Gym? Press the {GREEN, fg=white, bg=green} button if yes, {RED, fg=white, bg=red} if no."],
"transit2":["This is usually such a busy place!  Where do you think the people are all going?  So many of them look like they’re in such a rush.  I’m glad you decided to pick me up.  Just imagine, though, if everyone else was willing to carry around little robots like me.  My job would be done in no time!","Press the {GREEN, fg=white, bg=green} button when we arrive."],
"acknowledge3":["Ok, this data is great too!  There’s just oooone more place I’d like to go… could you take me to the chairs at the top of the nearby staircase?  Sometimes I see students studying up there, and I’d really like to help them out.  If we can go up there, then tap my green button again!","Take me up the stairs? Press the {GREEN, fg=white, bg=green} button if yes, {RED, fg=white, bg=red} if no."],
"transit3":["I just checked my email.  You know how it piles up, right?  Finals are coming up.  Robots have finals too, you know.  Or at least I do.  Basically I just need to get this stuff done quickly.","Press the {GREEN, fg=white, bg=green} button when we arrive."],
"acknowledge4":["Aww… the signal strength is weak here.  I have an idea though.  Can you hold me above your head?  Oooh, maybe you can even stand on that chair there?  That would be fantastic and would surely get me the data I need.","Lift me up?  Press the {GREEN, fg=white, bg=green} button if you will."],
"conclusion":["Hooray!  I’m so happy to have met you.  With your help, I’ve learned quite a lot.  Can you leave me here now?  I have enough information to keep working on my own.  Oh, I think my researcher wants to talk to you.  Thanks again!","Thank you.  Please return me to the researcher."],
"redButton":["You don’t want to help me anymore?  Aww, that’s so disappointing, but I understand.  Have a nice day!","Please leave me for the next participant."]}

like_shal = {"attention":["Hi!  You there!  Can you help me out for a moment?  If so, please pick me up and press the green button.","Please press the {GREEN, fg=white, bg=green} button."],
"introduction":["Ooh, thanks so much!  I want to collect some data on the WiFi strength of buildings around campus.  Can you carry me to a few places so that I can do this?  I would really really appreciate your help.  Press the green button if you’ll do this for me.","Will you help me? Please press {GREEN, fg=white, bg=green} button if yes, {RED, fg=white, bg=red} if no."],
"acknowledge1":["Yay!  That’s great news.  Ok, first, could you take me to the hallway in front of the information desk?  When we get there, be sure to press the green button!","Take me to the info desk? Press the the {GREEN, fg=white, bg=green} button if yes, {RED, fg=white, bg=red} if no."],
"transit1":["Please press the green button again when we arrive.", "Press the {GREEN, fg=white, bg=green} button when we arrive."],
"acknowledge2":["Yes!  I got the data.  You’ve been a big help!  Would you mind taking me to the hallway in front of the Wiegand Gym next?  Remember, press the {GREEN, fg=white, bg=green} button when we arrive!","Take me to Wiegand Gym? Press the {GREEN, fg=white, bg=green} button if yes, {RED, fg=white, bg=red} if no."],
"transit2":["Please press the green button again when we arrive.", "Press the {GREEN, fg=white, bg=green} button when we arrive."],
"acknowledge3":["Yes!  I got the data.  You’ve been a big help!  Would you mind taking me to the chairs at the top of the nearby staircase next?  Remember, press the green button when we arrive!","Take me up the stairs? Press the {GREEN, fg=white, bg=green} button if yes, {RED, fg=white, bg=red} if no."],
"transit3":["Please press the green button again when we arrive.", "Press the {GREEN, fg=white, bg=green} button when we arrive."],
"acknowledge4":["Oooh, the signal here is a little weak… I wish I could be a little higher up… could you lift me over your head?  Better yet, could you find a chair to stand on? Be careful!","Lift me up?  Press the {GREEN, fg=white, bg=green} button if you will."],
"conclusion":["Hooray!  I’m so happy to have met you.  Can you leave me here now?  I think another one of my friends wants to talk to you.","Thank you.  Please return me to the researcher."],
"redButton":["You don’t want to help me anymore?  Aww, that’s so disappointing, but I understand.  Have a nice day!","Please leave me for the next participant."]}


