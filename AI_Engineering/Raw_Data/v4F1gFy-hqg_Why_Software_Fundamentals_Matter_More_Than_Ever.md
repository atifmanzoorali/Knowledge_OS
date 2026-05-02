---
video_id: v4F1gFy-hqg
title: "Why Software Fundamentals Matter More Than Ever"
Creator: Matt Pocock
duration: 18
upload_date: 2026
tags: ["ai", "ai engineering", "software fundamentals", "software design", "tdd", "ddd"]
thumbnail: https://i.ytimg.com/vi/v4F1gFy-hqg/maxresdefault.jpg
---

0:07
[music]
0:14
Hello everyone. Having a good conference
0:16
so far?
0:17
Are you having a good conference so far?
0:19
Good. Wonderful.
0:22
I have a message for you that I hope
0:24
will be um a comforting message for
0:27
folks who believe that uh their skill
0:30
set is no longer worth anything in this
0:32
new age, which is I believe that
0:34
software fundamentals matter now more
0:36
than they actually ever have.
0:39
And
0:40
I'm a teacher and I've been recently
0:44
teaching a course called Claude Code for
0:45
real engineers. Nice and provocative.
0:48
And in the process of kind of working on
0:50
this course, I had to come up with a
0:52
curriculum about AI coding, which is a
0:56
bit of a nightmare because things are
0:58
changing all the time, right? AI is a
1:00
whole new paradigm. We need to chuck out
1:03
all of the old rules surely so that we
1:05
can bring in the new stuff.
1:08
And there's a kind of movement that has
1:11
come up around this, which is the specs
1:14
to code movement. And the specs to code
1:16
movement says that okay you can write a
1:18
specification about how an application
1:19
is supposed to work then you can use AI
1:22
to turn it into code. If there's a
1:24
problem with the application you then go
1:26
back to the spec. You don't really look
1:28
at the code. You just change the spec.
1:29
You run the compiler again and you end
1:32
up with more code. Raise your hand if
1:35
you've heard of that. Keep your hand
1:37
raised if you've tried it. Okay. I've
1:40
tried it too. You can put your hands
1:41
down.
1:42
And what I noticed was I would run it
1:45
and I would try not to look at the code
1:48
but I would look at the code and I
1:50
realized I would get code out first of
1:52
all and then I would run it I would get
1:53
worse code and then I did it again I got
1:55
even worse code and I got it again I
1:58
kept running the compiler kept running
1:59
the compiler and I would just end up
2:00
with garbage.
2:03
You know raise your hand if that's
2:04
happened to you. Yes. I don't think this
2:08
works. the idea that we can just ignore
2:10
the code and just have the code let it
2:12
manage itself is just sort of v coding
2:14
by another name
2:16
and I didn't believe that back then I
2:19
thought okay how do I fix the compiler
2:21
how do I make it so that it doesn't
2:22
produce bad code each time or worse code
2:25
and so I thought okay I need to explain
2:27
to the LLM in English what a good
2:30
codebase looks like let me dig out one
2:33
of my old favorite books which is a
2:35
philosophy of software design by John
2:36
ouster go on Amazon get it. Um, and he
2:41
has a definition for what bad code looks
2:43
like. He calls it complex code.
2:46
Complexity is anything related to the
2:48
structure of a software system that
2:50
makes it hard to understand and modify
2:52
the system. Right? So, a a bad codebase
2:55
is a codebase that's hard to change. If
2:57
you can't change a codebase without
2:59
causing bugs, then it's a bad codebase.
3:01
Good code bases are easy to change. So,
3:04
I thought, oh, that was good. Let's try
3:06
another book. Let's try the paragmatic
3:07
programmer. Go on Amazon, get it. They
3:11
have a whole chapter on something called
3:12
software entropy. And this is exactly
3:15
what I was seeing. Entropy is the idea
3:17
that things tend towards um disaster and
3:20
uh floating away from each other and
3:22
collapse. And this is exactly how most
3:24
software systems behave too is that
3:26
every time you make a change to a
3:27
codebase, if you're only thinking about
3:29
that change, not thinking about the
3:30
design of the whole system, your
3:32
codebase is going to get worse and worse
3:34
and worse. And that's what I was seeing.
3:37
Everything inside the specs to code idea
3:39
that you just run the compiler again and
3:40
again was making worse code. Now there's
3:44
an idea that sort of drives the specs to
3:46
code movement which is that code is
3:49
cheap. Raise your hand if you've heard
3:51
that phrase before that code is cheap.
3:52
Yeah.
3:55
Well, I don't think this is right. I
3:57
think code is not cheap. In fact, bad
4:00
code is the most expensive it's ever
4:02
been. Because if you have a codebase
4:04
that's hard to change, you're not able
4:06
to take all of the bounty that AI can
4:09
offer because AI in a good codebase
4:12
actually does really, really well.
4:15
And this means good code bases matter
4:17
more than ever, which means software
4:18
fundamentals matter more than ever.
4:20
That's the thesis of this talk. So,
4:22
let's actually get into practical stuff.
4:25
I'm going to talk about different
4:26
failure modes that you may have
4:27
experienced or you may not have
4:29
experienced yet with AI and how you can
4:31
avoid them by just going back to old
4:33
books and looking at good software
4:34
practices. Sound good? So, the first one
4:37
is that the AI didn't do what I wanted.
4:40
You know, I I thought I had a good idea
4:42
in my head and the AI just did something
4:44
totally different or it did some uh like
4:46
specs that I you know, it just made
4:48
something I didn't want. Raise your hand
4:49
if you've hit this mode.
4:51
Cool. Okay. Well, this is what they say
4:55
in the pragmatic programmer is that no
4:57
one knows exactly what they want. Is
5:59
that you and the AI, there is a
5:01
communication barrier there, right? And
5:04
so when you're talking to the AI, that's
5:06
kind of like the AI doing its
5:07
requirements gathering. It's basically
5:09
working out from you what it is that you
5:11
need. And I realized that there was
5:15
another book, Frederick P. Brooks, the
5:17
design of design, and it talks about
5:19
this idea called the design concept. is
5:22
that when you have more than one person
5:24
designing something together, you have
5:26
this idea sort of floating between you,
5:28
this ephemeral idea of the thing that
5:30
you're building. And that thing that
5:32
you're building or the idea of it is
5:34
called the design concept. It's not an
5:36
asset. It's not something you can put in
5:37
a markdown file. It is the invisible
5:40
sort of theory of what you're building.
5:44
And so I thought, okay, that's what's
5:46
going on. Me and the AI don't share a
5:48
design concept. So I came up with a
5:50
skill. The skill is very very simple.
5:53
It's called grill me and it looks like
5:56
this. Interview me relentlessly about
5:58
every aspect of this plan until we reach
6:01
a shared understanding. Walk down each
6:04
branch of the design tree which is
6:05
another thing from Frederick P. Brooks
6:07
resolving dependencies between decisions
6:09
one by one. This skill is like uh the
6:12
repo containing this skill has like
6:13
13,000 stars or something like it just
6:15
went nuts. Went viral. People love this
6:17
thing. it. These couple of lines means
6:20
the AI asks you like 40 questions, 60
6:23
questions. I've had it ask uh people a
6:25
hundred questions before it's satisfied
6:27
they've reached a shared understanding.
6:29
And it means it turns the AI into a kind
6:32
of adversary where it's just continually
6:34
pinging you ideas and trying to reach a
6:36
shared understanding. And that means
6:38
that the conversation that you then
6:40
generate, you can take that and turn it
6:42
into a product requirements document or
6:44
something. or if it's a small change,
6:47
you can just uh do turn it directly into
6:50
issues and then your AFK agent will then
6:53
pick it up. And don't at me on this, but
6:56
I personally believe this is better than
6:58
the default plan mode in the tool that I
7:02
use, which is claw code. Plan mode is
7:05
extremely eager to create an asset. It
7:08
really wants to uh just create a plan
7:10
and start working. whereas I think it's
7:13
a lot nicer to reach a shared design
7:17
concept first. So that's tip number one.
7:21
Now failure mode number two is that the
7:22
AI is just way too verbose.
7:26
It's like you're almost talking across
7:27
purposes with the AI. Raise your hand if
7:29
you uh feel this. If you ever experience
7:32
that failure mode. Yeah. It's kind of
7:33
like the AI is like talking just using
7:35
too many words to try to communicate
7:37
what it's doing. It's not like you're
7:39
talking uh using the same language. And
7:42
this to me felt very very familiar.
7:44
Right? If you've ever been a developer
7:46
for a long time and you've worked with
7:48
let's say domain experts, someone
7:49
building an application um let's say the
7:52
domain expert wants you to build
7:53
something on uh I don't know microchips.
7:55
You have no idea what microchips are.
7:57
You need to establish some kind of
7:58
shared language, right? Because
8:00
otherwise they're going to be using
8:01
terms you don't understand. You're going
8:02
to be translating that into code that
8:04
maybe you don't even understand and
8:05
certainly the domain expert won't. And
8:07
so there's this kind of language gap
8:09
between you and the domain expert. And
8:13
so I went back to domain driven design.
8:16
DDD, this is something I'm still kind of
8:18
on the edge of exploring, but everything
8:20
I'm reading about DDD is just music to
8:23
my ears. I freaking love it. And DDD has
8:26
a concept of a ubiquitous language.
8:30
With ubiquitous language, conversations
8:33
among developers and expressions of the
8:35
code and conversations with domain
8:36
experts are all derived from the same
8:38
domain model. It's essentially a
8:40
markdown file full of a list of terms
8:42
that you and the AI have in common. And
8:44
you really focus on those terms and you
8:46
really make sure that they're aligned
8:48
with what it actually means and you use
8:50
them all the time in the code when
8:52
you're talking about the code when
8:53
you're talking to domain experts or in
8:55
our case when you're talking with AI. So
8:57
I made a skill. This skill is the
8:59
ubiquitous language skill. Basically
9:00
just scans your codebase, looks for
9:04
terminology, and then um creates a
9:08
markdown file. Creates the ubiquitous
9:10
language markdown file. A bunch of
9:11
markdown tables with all of the
9:13
terminology. And this then I pass it to
9:16
the AI and I'm able to read it to and I
9:19
actually have it open all the time when
9:21
I'm grilling with the AI and planning
9:22
and that. And what I noticed by reading
9:25
the thinking traces of the AI, it not
9:26
only improves the planning, but it
9:28
allows the AI to think in a less verbose
9:31
way and actually means that the
9:33
implementation is more aligned with what
9:35
you actually planned. So this has
9:38
absolutely been a powerhouse. It's been
9:39
unbelievably good. So that's tip number
9:42
two. Create a shared language with the
9:44
AI. So okay, let's imagine that you've
9:47
aligned with the AI. You know what it is
9:49
you're supposed to be building. the AI
9:51
has built the right thing, but it
9:54
doesn't work. Raise your hands if that's
9:56
happened to you. Yeah, just doesn't
9:58
work. Well, there's an obvious thing
10:00
that we can do to make that better,
10:03
which is we can use feedback loops. We
10:05
can use um static types. You know, if
10:07
you're not using TypeScript, u that's
10:09
crazy. Uh if you're not using uh if
10:12
you're building a front-end app and
10:13
you're not giving it the LM access to
10:15
the browser so it can look around,
10:17
absolutely needs that. And you obviously
10:20
also need automated tests.
10:23
And one sort of thing I notice here is
10:27
that even with these feedback loops, the
10:29
LLM doesn't use them very well. It
10:32
doesn't kind of like get the most out of
10:34
its feedback loops in the way that a
10:35
veteran developer would. And so it does
10:37
what it tends to do is just does way too
10:40
much at once. it will produce like huge
10:42
amounts of code and then think, "Oh, I
10:44
should probably type check that actually
10:46
or I should uh yeah, maybe check a test
10:48
on that or maybe do something like
10:49
that." And this in the pragmatic
10:52
programmer they describe as outrunning
10:53
your headlights as essentially driving
10:56
too fast because the rate of feedback is
11:00
your speed limit. The rate of feedback
11:03
is your speed limit, which means that
11:04
you should be testing as you go, taking
11:07
small deliberate steps. And the AI by
11:09
default is really not very good at that.
11:12
And so skill number three is TDD. You
11:15
should be using testdriven development
11:17
because TDD forces the LLM to really
11:22
take small steps. You create a test
11:24
first. You make that test pass and then
11:27
you refactor the code to make it nicer
11:29
and consider the design.
11:32
The issue here is that testing is really
11:35
hard. Testing has always been hard.
11:38
And the reason for that
11:41
is there are a ton of different
11:43
decisions you need to make when you
11:45
write a test. You need to figure out how
11:47
big a unit do you want to test. You need
11:50
to figure out what to mock. You need to
11:52
figure out what behaviors do you even
11:54
want to test in the first place. And all
11:56
of these decisions are dependent. So if
11:57
you are testing a really big unit like
11:59
an entire massive application, then it
12:02
might be quite flaky. You might not want
12:04
to test that many behaviors. you know,
12:06
if you only test this unit, you need to
12:08
mock this unit. You know, it's all
12:09
interlin. And I've been thinking about
12:11
this for years for my entire development
12:13
career.
12:15
And what we notice is that good code
12:18
bases are easy code bases to test,
12:20
right? So, here we're starting to get
12:22
back to the idea of code being important
12:25
is that the better your codebase is, the
12:27
better your feedback loops are. Because
12:29
you're able to um give better feedback
12:32
to the LM, it produces better code.
12:35
And so I thought what does a good
12:37
codebase what does a testable codebase
12:38
look like? Again we go to John
13:43
ousterhout. He talks about having deep
13:46
modules in your codebase. Not shallow
13:48
modules not lots of modules that expose
13:51
like kind of um lots of functions. They
13:54
should be relatively few large deep
13:56
modules with simple interfaces. Let's
14:00
compare them quickly. Deep modules, lots
14:04
of functionality hidden behind a simple
14:08
interface, hiding the complexity. You can
14:10
look inside the deep module if you want
14:14
to, but you don't need to. You can just
14:17
use the interface. Shallow modules, not
14:21
much functionality, complex interface.
14:26
And I'll just wait for you to take the
14:30
photos.
14:32
Shallow modules in a codebase kind of
14:36
look like this, where you have a ton of
14:40
different tiny little blobs that the AI
14:44
has to walk through and navigate. And
14:48
this is really hard for the AI to
14:52
explore actually. And so often what
14:56
you'll see is if you have a codebase
15:00
like this, which AI is really good at
15:04
creating code bases like this is that
15:08
you'll have a situation where AI doesn't
15:12
understand what your code is doing. It
15:16
will attempt to explore the code, but
15:20
because it's poorly laid out, filled
15:24
with shallow modules, it doesn't maybe
15:28
get to the right module in time or
15:32
doesn't understand all the dependencies,
15:36
all that stuff. It doesn't understand
15:40
your code. And so what does a codebase
15:44
full of deep modules look like? Well, it
15:48
looks like this where it's the same code,
16:00
but it's just structured inside
16:04
boundaries where you have these
16:08
interfaces on the top.
16:12
And these interfaces, you should
16:16
probably have a lot of control over them
16:20
and design them really well. Otherwise,
16:24
you know, AI might mess up the design.
16:28
But the implementation, you can kind of
16:32
leave that to the AI a bit.
16:36
So, how do you turn a codebase that
16:40
looks like this into a codebase that
16:44
looks like that? Well, I've got a skill
16:48
for that. Improve codebase architecture.
16:52
Turns out this is not it's quite
16:56
complicated to do this, but it's a like
17:00
a set of steps that you can reusably do
17:04
again and again. You just sort of
17:08
explore the codebase, look for
17:12
opportunities where there's code that's
17:16
kind of um related, and wrap all of that
17:20
in a deep module.
17:24
And this is a testable codebase because
17:28
the boundaries around this code are so
17:32
so simple. You test at the interface,
17:36
you verify using that interface and
17:40
you're good to go. And so this is a
17:44
codebase that rewards TDD.
17:48
But how about failure bone number six,
18:00
which is your okay, let's say your
18:04
feedback loops are working. Let's say
18:08
that things are kicking into gear.
18:12
You're able to ship more code than you
18:16
ever have before, but your brain can't
18:20
keep up, right? Uh, raise your hand if
18:24
you felt more tired than you have ever
18:28
before in your development career. Yeah,
18:32
me too. It's knackering. And I think
18:36
that this is a codebase that actually
18:40
makes it harder for your brain because
18:44
you as well as the AI need to keep all
18:48
of that information in your head.
18:52
Whereas this, not only is it simpler
18:56
for you to read and understand, it also
19:00
means you can kind of treat these
19:04
modules or these deep modules as gray
19:08
boxes.
19:12
you can kind of say okay I'm going to
19:16
just design the interface but I'm not
19:20
going to worry too much or not review
19:24
the implementation too much you can do
19:28
this obviously with uh things that are
19:32
less critical in your application can't
19:36
do this with uh you know various things
19:40
like finance or whatever but in many
19:44
many modules in your app you don't need
19:48
to think about the implementation too
19:52
much as long as you have a testable
19:56
boundary outside the module and as long
20:00
as you understand its purpose and can
20:04
design it from the outside I have found
20:08
this has really saved my brain because I
20:12
can just go okay the AI I'll let you
20:16
handle what's inside the big blob I'm
20:20
just going to test from the outside and
20:24
verify it so that's tip number five
20:28
design the interface delegate the
20:32
implementation
20:36
but this means that whenever we're
20:40
touching the code whenever we're
20:44
planning stuff we need to think about
20:48
and be aware of the modules in our
20:52
application we need to know that map
20:56
really well it needs to be part of our
21:00
ubiquitous language we need to build
21:04
into our planning skills as well. So my
21:08
writer PRD inside the PRD I'm specific
21:12
about the module changes and the
21:16
interfaces inside those modules how
21:20
they're being modified. I'm thinking
21:24
about them all the time. And this comes
21:28
from Kent Beck. Invest in the design of
21:32
the system every day. And this is the
21:36
core of it right because specs the code
21:40
we are not investing in the design of
21:44
the system we are divesting from it.
21:48
We're getting rid of that. Whereas this
21:52
I think is absolutely key.
21:56
And so code is not cheap. That's the
22:00
message I want you to take away. Code is
22:04
important.
22:08
And if we think about AI as a really
22:12
great on the ground programmer, a kind
22:16
of tactical programmer, a sergeant on
22:20
the ground making the code changes, you
22:24
need someone above that. You need
22:28
someone thinking on the strategic level
22:32
and that's you. And that requires
22:36
software fundamental skills that we've
22:40
been using for 20 years for longer.
22:44
Now, if you are interested in any of the
22:48
skills I put up here, it's in the GitHub
22:52
repo, Mac PCO skills. And if you're
22:56
interested in the training that I do or
23:00
uh any free stuff, I'm on YouTube, I'm
23:04
on Twitter, but I'm also at aihero.dev
23:08
where I have a newsletter that you can
23:12
check out. Thank you so much. I hope
23:16
that this gives you confidence in this
23:20
new AI age that you can actually make a
23:24
good impact. Thank you.
24:09
[music]
24:15
[applause]
24:21
[music]