Title: I Just Did What?
Tags: posts

In an effort to not burn myself out (again) I have placed little importance on
updating this blog. I've just been too busy with other things to stay sane and
manage all the things I had initially hoped to do. On a related note, WOW is
sleep ever good. I had totally forgotten what it felt like to get constant
sleep ever since placing such emphasis on doing too many things.







* * *



# On Creating a Marketable Product ...

I've been going out to bicycle stores and talking to cyclists to get a better
understanding of the cycling culture in this region and to see if whether
[BykMe](http://bykme.ca/register) is a viable idea. Another dilemma I'm
currently facing is the process by which I'll deliver a prototype to market.
There are essentially two alternatives.



##### 1 - Code a basic prototype myself:

This is not as hard as it sounds if you know basic web development (The true
test is making a web-application look the same on any web browser
**Cough**Internet Explorer**Cough**) and use resources available to you, of
which there are swaths. I've already got a basic template that I'd use if I
were to go this route (check [here](http://delgadogiorgio.com/steam/)).



##### 2 - Use a sub-par and costly marketplace system:

This option is slowly becoming the preferable one. The choice of marketplace
system boils down to either [Sharetribe](https://www.sharetribe.com/) or
[Near-Me](https://near-me.com/), both of which allow me to focus on [my other
goals](http://giorgiodelgado.ca/self-development-challenge/) for this winter
while still achieving the goal of having a marketable product. Sharetribe is
considerably cheaper, and since all I'm looking for is [a basic
prototype](https://en.wikipedia.org/wiki/Minimum_viable_product), it will
definitely do.







* * *



# On Becoming A Proficient Programmer ...

On another note. I've mentioned previously how I am aiming at becoming a
knowledgeable programmer and just last night I really noticed how far I've
come since my early days.

Below is a code snippet for an algorithm I wrote over the summer (in
[VBA](https://en.wikipedia.org/wiki/Visual_Basic_for_Applications)):



`Dim Mult3 As Long`

`Dim Mult5 As Long`

`Dim Tot As Long`

`Mult3 = 0`

`Mult5 = 0`

`For i = 3 To 999 Step 3`

`Mult3 = Mult3 + i`

`Next i`

`For i = 5 To 999 Step 5`

`If Int(i / 3) - i / 3 <> 0 Then 'prevent double counting`

`Mult5 = Mult5 + i`

`End If`

`Next i`

`Tot = Mult3 + Mult5`

`MsgBox ("Answer is: " & Tot)`

And below is another algorithm (if you can even call it that) that does the
exact same thing but in [Python](https://www.python.org/) (try and figure out
what it does!).



`print "answer is: ", sum([x for x in range(1,1000) if (x % 3 == 0) or (x % 5
== 0)])`

I've also finally finished Udemy's [Web Development
Course](https://www.udemy.com/complete-web-developer-
course/?dtcode=onKtD4P2sehJ) and I've got to say I have learned a lot of
practical skills which I may start monetizing soon.[
Here's](http://delgadogiorgio.com/) a link to some of my work.







* * *



# On Learning About Artificial Intelligence ...

In one of [ my last posts](http://giorgiodelgado.ca/restarting-for-
efficiencys-sake/) I mentioned how MIT's Artificial Intelligence class is not
for the faint of heart. With my knowledge of programming, I was not prepared
to tackle a senior-level Computer Science class on my own without the help of
an online community. That's why I started over and have been progressing along
with [UC Berkeley's](https://www.edx.org/course/artificial-intelligence-uc-
berkeleyx-cs188-1x-0) Artificial Intelligence class.

Below is a short video of what I managed to do with my new-found Artificial
Intelligence skills. This is an intelligent Pacman character that knows where
to go to find the ball (although not in the most efficient way, which is what
I'm working on next).

That's all folks. Adios.

