---
title: Introduction to Max Schoening
source_url: https://www.youtube.com/watch?v=mCO-D3pkviM
topic: AI Product Leadership, Agency in AI Era
date: 2026
---

Chapter 1: Introduction to Max Schoening
0:00Before it was very easy to always say,
0:022 secondswell, I will never be able to do this because insert skill issue. We're realizing that even if you have the skills at your fingertips, the thing
0:099 secondsthat matters is agency. I don't think agency is very evenly distributed in the world.
0:1414 secondsDo you have a piece of advice for someone that wants to develop this within themselves?
0:1818 secondsI tell this to myself. Could you drive notion like it's stolen? One day you wake up and you realize the world is made up by people no smarter than you.
0:2525 secondsIt just really awakens you to the idea that you can just change things. If you think about your job a couple years ago, what's most changed?
0:3232 secondsThe first 10% of every project are now free. It takes almost no effort to now build the first version of a startup. Taste comes up a lot now.
0:4040 secondsTaste actually means you're able to run a virtual machine in your head where given an idea, you can predict for a certain inroup whether they're going to
0:4848 secondslike it or not. You just have to do reps. It's almost like training a model.
0:5151 secondsWhat do you think matters to building a successful product?
0:5454 secondsAll the great products have something tiny that is a superpower. one tiny core that is so exceptionally good. One of the biggest pitfalls is if you get into
1:031 minute, 3 secondsthe loop of if I just add one more thing to the product, it will be finally great. That never works.
1:081 minute, 8 secondsGive this hot take on universal basic income. We already have universal basic income. It's called knowledge work.
1:151 minute, 15 secondsToday my guest is Max Shying. Max is a hard person to describe. He was a product manager at Google. He ran the
1:221 minute, 22 secondsdesign team at Heroku. He was a design leader and an engineer at GitHub under Natt Freriedman. He's also a two-time founder and is now head of product at
1:301 minute, 30 secondsNotion. He is one of the most successful AI forward product leaders out there and as you'll soon see, one of the deepest
1:371 minute, 37 secondsthinkers on how AI impacts how we build and how we use software. Before we get into it, don't forget to check out lennisproass.com
1:451 minute, 45 secondsfor an insane set of deals available exclusively to Lenny's newsletter subscribers. With that, I bring you Max Shing.
Chapter 2: The origin story of designers coding at Notion
1:551 minute, 55 secondsMax, welcome to the podcast. Thank you for having me.
1:581 minute, 58 secondsI am so excited to have you here. I feel like there's this quote I think about when I think about you uh and you being on this podcast. It comes from the
2:062 minutes, 6 secondsBible. And just paraphrasing, the quote is, "I was made for such a time as this." I feel like there's this all this
2:132 minutes, 13 secondstalk about roles merging, designers becoming PMs, engineers, everyone's the same. The ven diagrams collapsing.
2:182 minutes, 18 secondsYou've been that for a long time. It's like hard to even describe what you are and what you've done. You've done all the things. So, I feel like you have such a unique insight into where things
2:262 minutes, 26 secondsare heading. I want to start with just kind of this broad question. What have you seen about where things are going for product teams, for product building,
2:362 minutes, 36 secondsas AI becomes more powerful, as we integrate it more into our workflows?
2:392 minutes, 39 secondsAnd I ask you this because I've heard from so many people at Notion that you are the reason that designers are shipping code, PMs are shipping code.
2:472 minutes, 47 secondsYou're not just living in the future,
2:492 minutes, 49 secondsyou're like pushing the whole team and company to live in the future. And so,
2:532 minutes, 53 secondsso coming back to the question just like what are you seeing about where things are going? What will change? What will people realize in the next few months, years that you're already seeing?
3:003 minutesWell, first of all, when you said a quote from the Bible, I was I was very curious where this was going to It's the first time I've coded the Bible
3:093 minutes, 9 secondson this podcast. I think I wouldn't take credit for the designers at notion and PMs at notion now code. I think that would have probably happened anyways.
3:213 minutes, 21 secondsBut I can tell you the origin story of it which is when I joined notion we were building a lot of chat interfaces and we
3:283 minutes, 28 secondswere designing the chat interfaces in Figma and my there's this great talk by Brett
3:343 minutes, 34 secondsVictor uh stop drawing dead fish which essentially is I I mean the the
3:423 minutes, 42 secondsstatic image of a chat is basically the dead fish here. uh you have to feel the the AI to some degree. And so, uh, two
3:523 minutes, 52 secondsdesigners, myself, just put together the worst possible playground you could think of of a small codebase that is
4:004 minutesvery LLM friendly, used the tools that LLMs are very good at using. And then we moved all of our prototyping for the specifically the chat interfaces to
4:084 minutes, 8 secondsthat. And just to understand this playground concept, uh, essentially this is an idea of people work within this separate kind of area with AI tools
4:164 minutes, 16 secondsversus like their whole notion code base making it really easy to get started and try stuff.
4:214 minutes, 21 secondsYes. And that was the first version. It sort of aligned with model capabilities at the time. We don't always use maybe
4:294 minutes, 29 secondsat notion sort of the the main codebase is not always the most agent uh friendly because uh iterations and a decade of of
4:374 minutes, 37 secondsof patterns. And so we optimized for okay how can we make this the least scary and most oneshotable so that people would just have to overcome this
4:454 minutes, 45 secondssort of oh I the fear of the terminal but then it just becomes chatting and uh we recreated a bunch of the patterns and
4:534 minutes, 53 secondsUIs that exist in that playground now the good news is that's just to get people on the treadmill because as model
4:594 minutes, 59 secondscapabilities get better now we have the same designers npms also just contributing to the production codebase
5:085 minutes, 8 secondsto a lesser degree of course, but like you can see where the trend is headed as model capabilities get better. The the
5:145 minutes, 14 secondsthe amount of work that you can do is uh obviously going to increase exponentially. This episode is brought
5:225 minutes, 22 secondsto you by our season's presenting sponsor work OS. What do OpenAI, Anthropic, Cursor, Versell, Replet,
5:305 minutes, 30 secondsSierra, Clay, and hundreds of other winning companies all have in common?
5:345 minutes, 34 secondsThey are all powered by work OS. If you're building a product for the enterprise, you've felt the pain of integrating single signon, skim, arback,
5:425 minutes, 42 secondsaudit logs, and other features required by large companies. Work OS turns those deal blockers into drop-in APIs with a
5:495 minutes, 49 secondsmodern developer platform built specifically for B2B SAS. Literally,
5:545 minutes, 54 secondsevery startup that I'm an investor in that starts to expand upmarket ends up working with work OS. And that's because they are the best. Whether you are a
6:026 minutes, 2 secondsseedstage startup trying to land your first enterprise customer or a unicorn expanding globally, work OS is the fastest path to becoming enterprise
6:096 minutes, 9 secondsready and unblocking growth. It's essentially Stripe for enterprise features. Visit workos.com to get started or just hit up their Slack where
6:186 minutes, 18 secondsthey have actual engineers waiting to answer your questions. Workos allows you to build faster with delightful APIs,
6:246 minutes, 24 secondscomprehensive docs, and a smooth developer experience. go to works.com to make your app enterprise ready today.
Chapter 3: How much designers and PMs are shipping today
6:316 minutes, 31 secondsMaybe give us a sense of where things are today like how much are designers shipping stuff PMs and then just what do you see about where things might be
6:386 minutes, 38 secondsheading seeing all this actually happening in at a company like notion? I I feel so uncomfortable predicting the future in terms of where things are
6:466 minutes, 46 secondsheading because well predicting exponentials is really hard. But I'll take the stab at it is very very useful
6:556 minutes, 55 secondsfor designers to move from manipulating Figma documents into code.
7:017 minutes, 1 secondThat has always been useful. I've always been camp designers should code. uh at a in a previous life I I led design and product at GitHub and GitHub designers
7:107 minutes, 10 secondsbefore LLMs contributed to to GitHub I think in the top contributors to to GitHub itself like 10% were designers
7:197 minutes, 19 secondsright now processes are sort of breaking uh one is we have designers who now
7:267 minutes, 26 secondsmostly code and prototype in in code and then they are asked by other teams uh in marketing and so on to reverse engineer
7:357 minutes, 35 secondsthat in Figma because they use that to create assets for videos and so on and so obviously that is kind of silly right that seems like busy work on the pushing
7:437 minutes, 43 secondsto production I think it's a spectrum obviously small changes styling tweaks and so on it's a given that you can just
7:507 minutes, 50 secondsdo that now I do have a general sort of maybe issue with vibe coding uh in the
7:587 minutes, 58 secondssense of I I don't feel like the quality of software has increased all that much in the last 12 months I think the maybe
8:058 minutes, 5 secondsthe amount of software has, but it's very very hard to find software that is is reliable. And so the way we see it is it's not so much about pushing to production and having designers deploy.
8:178 minutes, 17 secondsIt's about them thinking and designing in the medium that will actually end up being the real thing once engineering takes it over.
Chapter 4: The balance between shipping code and strategic work
8:258 minutes, 25 secondsThere's all this talk about designers should be shipping code, PM should be shipping code. And then there's the flip side of because engineers can move so fast. There's so much more happening.
8:338 minutes, 33 secondsThings are moving all the time,
8:358 minutes, 35 secondsdesigners and PMs are squeezed more and more because it's hard to stay on top of all these things that are constantly shipping. And so maybe it doesn't actually make sense for designers and
8:438 minutes, 43 secondsPMs to be spending time coding and instead their time is better spent making sure things are moving in a direction that makes sense for the business. It's cohesive. What's your
8:518 minutes, 51 secondsthoughts on just that balance? I actually don't care at all whether designers write code that lands in
8:588 minutes, 58 secondsproduction. The reason I like thinking in code is because it forces you to consider the
9:079 minutes, 7 secondsmedium. If then all of that gets thrown out, great. So, for example, I think the two extremes would be if a PM or a
9:159 minutes, 15 secondsdesigner knows how to tweak with pick your favorite, they're all the same,
9:219 minutes, 21 secondscodeex, cloud code, whatever. If they know how to tweak small details of the UI, but they don't understand how an agent loop works, I would much rather
9:299 minutes, 29 secondstake the designer or PM that deeply has an affinity for understanding how agent loops work and can design those than someone who can sort of write
9:379 minutes, 37 secondstraditional software uh and and tweak styles. And that's really hard because I think the only way that you can actually
9:449 minutes, 44 secondsget to understanding agent loops is if you build them in the material that they're made of, which is currently code, and increasingly so if you look at
9:539 minutes, 53 secondsall the coding harnesses, basically the operating systems of the '90s, right?
9:579 minutes, 57 secondsUm, and so I think that's why I care that people code, not because of the utility of shipping to production, but because it forces you to really
10:0510 minutes, 5 secondsinterrogate the material that you're designing with. So, it's more the prototyping use cases than we're just going to be shipping more features
10:1310 minutes, 13 secondsbecause because we can. It tends to be that once you awaken someone to a new material that at some point they also blur the lines and then write production
10:2110 minutes, 21 secondscode. But I think it's really important not to forget that the reason why is to to become a master of the material, not
10:2910 minutes, 29 secondsa sort of cog in the delivery mechanism for the idea.
Chapter 5: Why agency will help you thrive in the AI era
10:3310 minutes, 33 secondsThat is really interesting. What do you find is key to people being successful in this new world? Like, you know,
10:4110 minutes, 41 secondsthere's a lot of designers, a lot of PMs at Notion. What do you find is separating the ones that are thriving and will do well in this coming future
10:4810 minutes, 48 secondsversus ones that may fall behind? I suspect that this is also something that has always been the case and we would just categorize this as founder versus
10:5710 minutes, 57 secondsnot and do you start a startup versus not, which is agency. I think before it was very easy to always say well I
11:0611 minutes, 6 secondswill never be able to do this because insert skill issue and I think we're realizing that even if you have the
11:1411 minutes, 14 secondsskills at your fingertips because now I don't know an AGI adjacent model helps you uh the thing that matters is agency
11:2211 minutes, 22 secondsand I don't think agency is very evenly distributed in the world and uh I think people who have true agency and they
11:3111 minutes, 31 secondsunderstand that the world around them is malleable will do great and the folks who stick to what tell me really what
11:3911 minutes, 39 secondsdoes it mean to be a PM what does it mean to be a designer and like what's my job as an engineer I think that will be much harder and yeah cultivate agency I
Chapter 6: Examples of high agency at Notion
11:4911 minutes, 49 secondsthink that's the that's the thing is there an example of someone using agency some a good example at notion of someone just leaning into that and doing and
11:5711 minutes, 57 secondsmaybe shipping something changing the way something was happening at notion just to give us a like, oh wow, I see what you're talking about.
12:0312 minutes, 3 secondsNinos are, this was surprising to me,
12:0612 minutes, 6 secondsespecially on the design team, way above average agency compared to other places that that I've worked at.
12:1312 minutes, 13 secondsAnd Ninos, by the way, are notion employees.
12:1512 minutes, 15 secondsYes. Sorry. Once you're boil I would say one example would be someone like Brian Leven, who you should probably have on the podcast at some point.
12:2412 minutes, 24 secondsHe was on uh our sister podcast, How I AI. We'll link to that episode.
12:2712 minutes, 27 secondsAh, there we go. Yeah, you should cut this one short and have him on. Um, I think the way I would describe it is, and I I I tell this to myself as well,
12:3512 minutes, 35 secondswhich is like, okay, do you drive notion like it's stolen, which is, you know, we're not the founders where, you know,
12:4112 minutes, 41 secondscoming in after there was already insane product market fit, but you can still contribute to the company in a way that
12:4912 minutes, 49 secondsyou feel agency and you're not sort of just like it's what's your role. And so Brian obviously already blurs engineering and design, but he also is
12:5712 minutes, 57 secondsprobably our number one recruiter uh in terms of hey, this is what the org needs. I'm going to go out and talk to people and find someone. And I think
13:0613 minutes, 6 secondsthat is a thing that sort of just demonstrates it's it's out of the day-to-day and it demonstrates that, you know, I want to just affect change. I don't care how it happens, right?
13:1413 minutes, 14 secondsUm Eric Lou is another one. the fact that he went from sort of writing a lot of strategy docs to he asked me at some point he's like hey look at some point
13:2213 minutes, 22 secondsin the future if you started a startup would you hire me and I said well not in the first 10 I don't need a product manager he's like oh okay I'm going to
13:3113 minutes, 31 secondswork on the skills so that you would hire me in the first five and that led to first spending more time in Figma instead of you know writing long PRDs
13:3913 minutes, 39 secondsand now it's just why do I have to do the Figma thing can can't I just build the prototype and at least show you what I think and do the thinking in there right So that those are just sort of
13:4813 minutes, 48 secondssigns of high agency of I'm going to change the role to to to how I think it should be.
Chapter 7: What we might lose as roles merge
13:5313 minutes, 53 secondsSomething you mentioned earlier which I love this idea of just rethinking what is what is this role of engineer and what might it what should it be if if we
14:0014 minutesdidn't have this kind of meme already for it. I wonder what we lose as these roles start to merge. We used to have this clear engineer, product manager,
14:0914 minutes, 9 secondsdesigner. And as people start to, you know, as you talk about malleable software, we'll come back to this, but like malleable roles almost, there's
14:1714 minutes, 17 secondssomething we lose like clear career paths and design consistency, things like that. I think if we're not careful,
14:2414 minutes, 24 secondswe will lose specialists. And so the way I would describe this is I sometimes like to think about software in terms of
14:3214 minutes, 32 secondsphysical metaphors, right? And physical metaphors somehow make it so much clearer what a prototype is versus what
14:3914 minutes, 39 secondsan engineered thing is. And if you and I were to build a hardware startup, well,
14:4414 minutes, 44 secondswe would make the first enclosures and prototypes with 3D printing. And you would see all the layer lines. It would be very very obvious to you that this is not a thing that you should just give to
14:5314 minutes, 53 secondsto to people to pay for. And then there's a long windy road all the way to the end where at some point if you're very lucky you get to manufacture that
15:0115 minutes, 1 secondproduct for I don't know 100 million people. And so then the engineering is actually the how do I optimize the factory so that we have enough yield and
15:1015 minutes, 10 secondsso that we have enough precision. And that to me I think is very absent right now from most of the discourse in
15:1815 minutes, 18 secondssoftware which is it's all about how many tokens can we spend and how many features can we ship. I'm like okay but where's the engineering part and the
15:2515 minutes, 25 secondsengineering part is the you make sure that this thing works for 100 million people for a billion people and on the design side I think there is the yes
15:3515 minutes, 35 secondsanyone can now very quickly take a design system off the shelf build a very usable user interface get to the core of
15:4215 minutes, 42 secondswhat's really important but where is the delight in craft and so I think we have to make sure that we in this sort of merging of roles don't lose the
15:4915 minutes, 49 secondsspecialists on the on the edges and Yeah, I I would say that's something we could it would potentially be be be sad if we lost it.
Chapter 8: Advice for developing agency
15:5715 minutes, 57 secondsI want to come back to this agency piece because I feel like people hear this word a lot on this podcast. Yes, agency.
16:0316 minutes, 3 secondsFor someone that wants to build this within themselves or even just understand, do I have agency? I don't know. I think I do. I imagine everyone
16:1016 minutes, 10 secondslistening is like, yes, I am huge. I have huge agency. I'm such an agent. I can do I I'll do what needs to be done.
16:1716 minutes, 17 secondsDo you have a piece of advice for someone that wants to develop this within themselves?
16:2316 minutes, 23 secondsPartially the reason why I'm in software is the thing that I care most about is
16:3016 minutes, 30 secondsthe Steve Jobs quote. One day you wake up and you realize the world is made up by people no smarter than you. And there are basically people who realize this by
16:3816 minutes, 38 secondsthemselves or they have an amazing teacher early on in their life that encourages this. And the the biggest
16:4616 minutes, 46 secondsthroughine I've found is making. I think if you tinker and if you make things,
16:5216 minutes, 52 secondsthen you are now on this treadmill of just um creating and then you're like, "Oh,
16:5916 minutes, 59 secondsit's actually not that hard to learn how to make that chair in my office or let me tweak it a little bit or maybe I don't know. It's like a home-cooked meal is a form of tinkering, ironically,
17:0717 minutes, 7 secondsright?" Uh and I think the more you can do that in life, I think actually sort of making things is the innately human
17:1517 minutes, 15 secondslike sort of tool making, creating art and so on. So just do that versus I think when a lot of people hear agency,
17:2217 minutes, 22 secondsthey think of themselves as they're in this big machine and they're like, "Oh,
17:2617 minutes, 26 secondsokay. I'm going to circumvent my terrible boss or manager or whatever so that I get X, Y, and Z." It's like, no,
17:3217 minutes, 32 secondsno, just start by making things. And usually when you get better at making things, at some point people pay attention and it just really awakens you
17:4017 minutes, 40 secondsto the idea that you can just change things. I love this. Uh there's this meme on Twitter, you could just do things. Uh like there's all I I love
Chapter 9: Malleable software explained
17:4817 minutes, 48 secondsthis version of it. You could just change things. Um which is a is a good segue to something you've been a big I don't know advocate of and uh proponent of this idea of malleable software.
17:5817 minutes, 58 secondsSomething you mentioned earlier. It feels like something that wasn't actually possible and now is like, okay,
18:0418 minutes, 4 secondsI could see exactly what you're talking about now. Like you've been on on this from before the AI revolution. Talk about just this idea. Malleable
18:1218 minutes, 12 secondssoftware, why you think it's so important, what you think people need to be thinking about here.
18:1618 minutes, 16 secondsMalleable software is the idea that software works closer to the interest of the people that use it
18:2418 minutes, 24 secondsthan the interest of the corporation that makes it. Maybe that's how I'd frame it. And in particular, like I don't want to use software that is
18:3318 minutes, 33 secondsspecifically just designed by the ivory tower in Certino. And I say this as a huge Apple fanboy, but
18:4118 minutes, 41 secondsimagine you lived in an environment where you do not get to rearrange your living room and the kitchen has to be
18:4818 minutes, 48 secondsexactly set up the way that someone else decided. We would not take that, right?
18:5318 minutes, 53 secondsBut that is kind of the world that we have in software right now where we have this world of apps and apps are like this very every layer is glued together
19:0219 minutes, 2 secondsof like the user interface, the data ownership and so on. It's like this little square on your phone and the moment you're like okay this is a really
19:1119 minutes, 11 secondsgreat app but I just want to change a little bit that is usually not possible right the behavior. uh you have the flip side which is you could run your own
19:1919 minutes, 19 secondsLinux distribution and go that way and I think then what happens is you realize oh okay I like the malleability but I
19:2619 minutes, 26 secondsalso have other things to do and I don't always want to start from scratch and and figure out why the the trackpad doesn't work and so to me it just comes
19:3419 minutes, 34 secondsback down to do you have ownership over your computing life and I think increasingly we don't
19:4219 minutes, 42 secondsnow you brought this up presumably because I think you may have sort of not thought about malleable software too much before I but now you're like making
19:5019 minutes, 50 secondsyour own tools maybe for podcast recording for prepping for shows or or I don't know whatever um there's a myriad examples and people are awakening to
19:5919 minutes, 59 secondsthis idea of like oh I can just make tools and that is a form of malleable software but it has to be built on top
20:0720 minutes, 7 secondsof a platform or an operating system that encourages this because otherwise we're just doing individual like
20:1520 minutes, 15 secondseverybody has their own individual little tool and um I don't know I I like working with people and I like communal tools and I don't know this is a thing
20:2420 minutes, 24 secondsthat the folks at Incan Switch are are obviously as sort of at the forefront I get to work with Jeffrey Lit every single day now that uh spend a lot of
20:3120 minutes, 31 secondstime thinking about how would we make software more malleable so that we feel more ownership over it without going
20:3920 minutes, 39 secondsback a long time and not having real-time collaboration and sort of the security aspects and so on. I really love and I just want to make sure we
Chapter 10: The Dieter Rams video and design philosophy
20:4720 minutes, 47 secondshighlight this idea you're sharing. It's something that I learned also from Brian Chesky at Airbnb. This idea that just you can change things that the things
20:5620 minutes, 56 secondsaround you are just made by other people that may not actually be smarter than you. And it's just this really empowering thing to always think about
21:0421 minutes, 4 secondsthat things can change. This isn't the way things have to be forever. people humans made this thing like humans made this uh this phone and and you could and
21:1321 minutes, 13 secondsthere there are better approaches that other humans that you can that you can come up with other people will come up with. What I think about as I think about this is there's a video that you
21:2221 minutes, 22 secondsuh pinned to your Twitter profile that will link to which I think is DA Roms. Is that who that who the person is?
21:2821 minutes, 28 secondsOkay. So, he's walking around. He's just criticizing all these designed chairs.
21:3321 minutes, 33 secondsuh talk about what that video is trying to why why you pin that to your your profile.
21:3821 minutes, 38 secondsUh there's many reasons. One is um I think maybe the only thing that I have in common with this very accomplished
21:4621 minutes, 46 secondsperson is that we're both German. And so sometimes I joke that I also aspire to disapprovingly just point at things with
21:5221 minutes, 52 secondsmy walking stick and say, "This isn't good enough. This isn't good enough."
21:5621 minutes, 56 secondsUm, the reason why is because I think if you speak German, this is one of the funniest uh clips that I've ever I just die laughing every single time. I'm
22:0622 minutes, 6 secondsactually curious how you think about how it ties to malleable software because the main
22:1322 minutes, 13 secondsreason why I use that as a clip of reference is I'm very much in the camp of design should be first useful and
22:2222 minutes, 22 secondsthen beautiful. And I think a lot of the pieces there are predominantly things that you put in a museum for display and
22:3022 minutes, 30 secondsif you try to sit on them you'd be like what is this nonsense?
22:3322 minutes, 33 secondsWhat I felt there is just like you see all like you would think it was Frank Giri and like all these famous designers pieces put up in a museum and I think to
22:4122 minutes, 41 secondsmo to most people be like wow this is so incredible and beautiful. Like you see somebody that has a status and a reputation and you assume this is great.
22:4922 minutes, 49 secondsAnd I love that he breaks that veil of like no this is so stupid. What is this?
22:5322 minutes, 53 secondsWhat is this bunch of cabinets tied together? Doesn't make any sense.
22:5722 minutes, 57 secondsYeah, he said that's for that cabinet. I think he says something like it is neither orderly nor properly chaotic.
23:0523 minutes, 5 secondsUm I understand the connection. Now the timeless way of building and Stuart Bran's uh sort of how buildings learn I
23:1423 minutes, 14 secondsthink idea is also that it's very likely that the best homes for you are not actually built by an architect. They are
23:2123 minutes, 21 secondsthe thing that over a long time adapt to exactly how you would love to lead your life and they learn over time versus you
23:3123 minutes, 31 secondsknow immediately. And so then that is obviously a very costly version of malleability right if you have to rip out a wall or whatever. But um I I think
23:4023 minutes, 40 secondsthe main thing that deer Rams points out there is it should be a thing that's
23:4723 minutes, 47 secondsuseful. And a good way to figure out how something is useful is if you can change it and tweak it. Makes sense. It all connects. It all connects.
23:5523 minutes, 55 secondsI get it now.
23:5623 minutes, 56 secondsThere we go. I won't link to it. It's really funny to watch. I wish I wish I understood the German. I want to come back to this idea of uh malleable
Chapter 11: The SaaS apocalypse debate
24:0324 minutes, 3 secondssoftware from a perspective of SAS and the SAS apocalypse. There's all this talk about we will not need SAS tools any longer. We will build all our own
24:1024 minutes, 10 secondstools. We don't need Salesforce. You know, I imagine some people are like, we don't need notion. I'm going to build my own notion. You have a hot take there.
24:1824 minutes, 18 secondsTalk about what you think is going to happen. If you just think about what SAS, the problem is the moment you have an an acronym, it it means a lot of very
24:2624 minutes, 26 secondsspecific things. And if you're going to say, hey, is this type of SAS that we've built in the 2010s just as relevant as it was in the 2010s?
24:3624 minutes, 36 secondsThe answer would be it would be silly to say, no, nothing's going to change.
24:4024 minutes, 40 secondsIt'll be the same because I think you can sort of say a lot of SAS in the 2010s was a very very fancy form around a spreadsheet or something more generic.
24:5124 minutes, 51 secondsAnd the thing it did is it just guided people in the right direction to fill out that form as in it is less malleable than a spreadsheet. And that sort of is
24:5924 minutes, 59 secondsthe value. The as a service part is I think the thing that actually matters which is I don't think most people actually want to maintain the full stack
25:0825 minutes, 8 secondsof software. And so whenever I see someone and I am I am someone here uh say oh I just rebuilt this piece of software. I've tried rebuilding notion
25:1525 minutes, 15 secondsin a weekend for myself uh just to you know push at the edges of frustration uh frustrating things. I don't think people want that. I think for the most part
25:2425 minutes, 24 secondsit's nice if you can just People don't want to go hunting either. They just want to go to Costco and have the the the the steak in in a styrofoam
25:3125 minutes, 31 secondspackaging and pretend that the that it wasn't uh hunting or or you know an animal in the first place. I think with software it's like it's a it's like a um
25:3925 minutes, 39 secondsBrett Taylor says this too. Software is like a garden. you need to tend to it and the the the thing you pay for in the as a service is the maintenance and a
25:4825 minutes, 48 secondsbunch of specialists thinking really hard about a problem and so I don't think that's going away. What I would probably say is that tools will become more general. I mean I'm obviously
25:5725 minutes, 57 secondsbiased. I work at Notion. I'd like notion and I consider notion to be fairly malleable. Not enough. I'm I think it should become more malleable.
26:0626 minutes, 6 secondsWe we internally joked Joanna Stern um a journalist recently tweeted something along the lines of oh thanks to notionai
26:1426 minutes, 14 secondsI finally understand and use notion. I don't know what that says about notion.
26:1826 minutes, 18 secondsAnd to me this is a great example of notion wasn't SAS in the traditional way. It's kind of hard to get started
26:2526 minutes, 25 secondsbut because of AI now people can sort of they have a a tutor essentially and can build more things. And so my I suspect
26:3326 minutes, 33 secondsthat software will go more back into the '9s of general tools, word processor,
26:3826 minutes, 38 secondsspreadsheet, FileMaker Pro, uh that kind of thing, but those will still be as a service. And then you'll still have specialized tools around security and
26:4726 minutes, 47 secondsand so on of just people who go the extra mile to really solve a user problem. So I think to some degree the SAS apocalypse is greatly exaggerated.
26:5526 minutes, 55 secondsAt the same time, are things going to stay the same? Of course not. Like why would they?
27:0027 minutesI completely agree. I think people think about just the okay I'll create something that's pretty cool and close and then they don't think about exactly as described like I have to maintain
27:0927 minutes, 9 secondsthis thing forever and I have to keep adding features taking people's feedback. One of the funniest things that I see again and again uh uh I just
27:1627 minutes, 16 secondshad the head of product for cloud code on the podcast Catwoo and she talks about how Slack is basically the OS for anthropic. Everything runs through Slack
27:2427 minutes, 24 secondsand you think of all companies that would just like we don't we'll just build our own what are we doing with Slack? like no they're just they're they're using Slack like crazy and I
27:3227 minutes, 32 secondsthink that's just one example of like nobody wants to rebuild a tool like Slack and Workday I think is another example. I I don't know I think it's
27:3927 minutes, 39 secondsmaybe even more unique in the US but one of the uh great things about the US is actually specialization. It's that I get
27:4627 minutes, 46 secondsto spend dollars on something like notion because it's not that expensive compared to me building it and then uh
27:5427 minutes, 54 secondswhy would I waste my time? I I want to do other things with my life, right? So I don't know that's not going to go away.
27:5927 minutes, 59 secondsYeah. Uh I agree like people anthropic there their time is better spent building AGI than trying to build better Slack.
28:0628 minutes, 6 secondsI also love the Slack example because uh I mean this is a there's this graphic of what it takes to deliver a notification in Slack the sort of decision flowchart.
28:1828 minutes, 18 secondsAnd that is just something that you only get to when you have real users, real scale and decades of just yep we understand the customer. I want to come
Chapter 12: How product building has changed in the past two years
28:2728 minutes, 27 secondsback to how product building is changing and how it's different. I know you've done a lot of different jobs but like your job I don't know a couple years
28:3528 minutes, 35 secondsago. What's most changed like what part is most not something you don't do anymore or you do
28:4228 minutes, 42 secondsa lot more of now with AI emerging as a big part of your process? I think the first 10% of every project are now free.
28:5028 minutes, 50 secondsThat's how I would describe it. So there is no point for most things to for example write a I don't know I the thing
28:5828 minutes, 58 secondsis has changed. I've never really been great at this. Uh but like there's no point in writing a PRD if you can just do the janky version and and sort of you
29:0629 minutes, 6 secondsknow do the uh here's the demo of like what I think we should build. So the first 10% that's so interesting just that that's such an interesting way to
29:1329 minutes, 13 secondsframe it idea there's just like the thinking through of it you can go a lot further really quickly. Uh yes and in if you look at uh a lot of the the it takes
29:2229 minutes, 22 secondsalmost no effort to now build sort of the first version of a startup right or like the first Z version 0.8 and then I
29:3229 minutes, 32 secondsthink the last or or maybe maybe even if you're generous and say the first 90%
29:3729 minutes, 37 secondsare now done the last 10% are still actually 90%. That's always the hardest.
29:4229 minutes, 42 secondsSo I think uh it's cheaper to just explore a lot of paths. You can now afford to say I'm going to send off 10
29:4929 minutes, 49 secondsagents to explore 10 different things and then see if I was right. We used to say this at at GitHub in in our product
29:5729 minutes, 57 secondsreviews a lot which is demos not memos and then we would say give me something to react to which is okay if you're
30:0530 minutes, 5 secondsgoing to write a PR just write the change log or the blog post that a user would have would read. Now it's much easier to give people something to react
30:1330 minutes, 13 secondsto as in yeah here's the version of the product and it's like okay what if we did it this other way oh yeah here's that version and so I think that is just
30:2030 minutes, 20 secondsamazing it it sort of builds in iter iteration uh into the product much earlier right like waterfall is sort of
Chapter 13: What’s next in how we build products
30:2730 minutes, 27 secondswhy why bother what do you think is the next kind of leap or shift in how we build what do you what are you seeing is like okay this is now the new thing
30:3530 minutes, 35 secondsthat's emerging that is going to change how we operate I'm very conflicted on this because On one hand, I do want to like I believe the never bet against plain text. So, a
30:4530 minutes, 45 secondsfamous forum post at some point. Plain text markdown. Like it's just such a durable thing. Code is such a durable
30:5130 minutes, 51 secondsthing. I think that expressing your thoughts in code is probably a a really good thing. We can talk about why. Uh but at the same time,
31:0231 minutes, 2 secondsI'm like, are we really going to just be chatting back and forth? And so what is the future of Figma for example is like a really interesting example to me
31:1031 minutes, 10 secondsbecause uh on one hand I do see like sort of a drop in usage of of Figma in some designers at notion and then others
31:1931 minutes, 19 secondsare like nope these AI tools are wonderful. I it's very hard for me to predict of like is direct manipulation going away because the agent is doing
31:2631 minutes, 26 secondsthe direct manipulation. Um the other thing that I'm curious about is there is this
31:3431 minutes, 34 secondsautomation versus augmentation fork. If I look at the really really fast models like spark and I forget what the
31:4131 minutes, 41 secondsanthropic variant is where haiku uh no sorry it's it's you still get a smart one. It's opus but like opus fast
31:5031 minutes, 50 secondsor something just yeah like you very quickly run up a bill of like $3,000 a day. Uh but um the speed of
31:5931 minutes, 59 secondsinference really changes things. If the inference is slow, then you're queuing up a bunch of jobs and then you're walking around the building thinking
32:0632 minutes, 6 secondsabout other things and then come back and review versus if it's nearly instant. Are you still going to do this?
32:1132 minutes, 11 secondsIs this sort of multitasking the frenetic kind of thing that we currently have going on actually the thing that is sort of you know gives us flow state?
32:1932 minutes, 19 secondsWell, no. But if the inference becomes instant, do we get back to direct manipulation? Right? Do you do you instantly sort of like mold the clay
32:2832 minutes, 28 secondsthat is the code? Right? Um I I I don't know. I think it depends on model capabilities, which is do people is
32:3632 minutes, 36 secondsthere a saturation on intelligence or not? Uh the analogy I like to give is a retina display, which is after I can't see the pixels, I can't see the pixels.
32:4732 minutes, 47 secondsI don't need you to make them smaller.
32:4932 minutes, 49 secondsIs it not the same for a lot of cognitive tasks which is at some sort of level of intelligence I don't need more and I instead I want a different
32:5732 minutes, 57 secondsmodality and faster. So I don't know those things I'm excited about.
33:0033 minutesInteresting. So that last point you're making is it's like smarter models will not significantly impact how teams operate because they've gotten so good
33:0833 minutes, 8 secondsand it's other blockers now like like UX essentially.
33:1333 minutes, 13 secondsYeah. I think in general I'm actually very curious. uh the labs sort of operate I feel like they operate uh
33:2033 minutes, 20 secondsunder the assumption that people will always want the smartest model like you want the frontier model and I think for certain domains that is probably true I
33:2833 minutes, 28 secondsthink if we're going to do cancer research and so on and if we're going to spend millions of dollars on something that's likely true but that's not how we run companies either right like we don't
33:3733 minutes, 37 secondshave a PhD for everything and so I I I think for a lot of knowledge work tasks probably sometime we'll get to good
33:4633 minutes, 46 secondsAnd once you get to good enough, then you can optimize other things like they run locally, they're cheaper, they're faster. And I don't know why the
33:5433 minutes, 54 secondsabsolute intelligence thing doesn't interest me very much. I I think society is largely not capped by intelligence.
34:0034 minutesUh I think Tyler Cowan says something similar. I don't want to put words in his mouth. Um, and so I'm much more interested in the exoskeleton
34:0934 minutes, 9 secondsversus the I have a god in a box in some data center center somewhere and we're all sort of, you know, twiddling our thumbs.
Chapter 14: Token spend and ROI conversations
34:1734 minutes, 17 secondsMhm. I have I have a bunch of questions along these lines. So interesting. You talked about how this 1pm is the highest token spender. This is across all of Notion.
34:2534 minutes, 25 secondsUh, I would assume this may not include our automatic security uh, vulnerability scanning and like bug triaging is like when Yeah. human kicks off and jobs. Yeah.
34:3634 minutes, 36 secondsYeah.
34:3634 minutes, 36 secondsWhat's your policy on token spent? Is it spend as much you want here's a limit everyone? Do you keep track of given that I don't know what the policy
34:4334 minutes, 43 secondsis? I think it is unlimited. Uh I mean you can imagine at some point there would be but uh right now I think it's just the wrong thing to optimize for.
34:5134 minutes, 51 secondsIt's like when something new comes along it's worth letting people explore.
34:5834 minutes, 58 secondsI do suspect in six to 12 months from now a lot of companies are going to actually start asking questions around RARI
35:0635 minutes, 6 secondsand I think that will be an uncomfortable conversation for for a lot of folks in terms of span what are like the numbers for say Eric or broadly in terms
35:1535 minutes, 15 secondsI am the wrong person to ask okay it's just a lot that is just the I don't I would assume they pale in comparison to the folks at
35:2335 minutes, 23 secondsopen eye and anthropic just by the nature of the work they do and so on but It is definitely for an individual in
35:3035 minutes, 30 secondsthe you know I don't even want to put numbers in but like thousands for sure but like maybe tens of thousands I don't know depends yeah
35:3835 minutes, 38 secondsI think just the fact that you're has had a product or not on top of that means that it's just let's not worry about this let's just see what we can do
35:4535 minutes, 45 secondsand then we'll we'll you know in six months as you said we'll figure out if this is ROI positive.
35:5035 minutes, 50 secondsYes that I have the luxury to right now not care.
35:5435 minutes, 54 secondsYeah I'm sure you know someone's looking at it. It's not going to be out of control. Correct. I think there's like this big, I don't know, milestone of when does token spend exceed someone's
36:0236 minutes, 2 secondssalary. That's something people talk about now more and more just like should that be higher than your salary, should that be lower? How does that all connect? Yeah, I think there's a real
36:0936 minutes, 9 secondsdanger in sort of making the token spend the the metric to like
36:1636 minutes, 16 secondsboast about, which is the same as when people boast about how many lines of code they've written in a day.
36:2236 minutes, 22 secondsYeah. And I'm like, I why do you have so many lines of code?
36:2736 minutes, 27 secondsUh you have I don't know the largest software projects in the world have uh not that many millions of lines of code.
36:3736 minutes, 37 secondsLike why are we why are we bragging about that? I I don't actually care about how many tokens someone spends. Um yeah,
36:4536 minutes, 45 secondsit's not a metric that's useful.
36:4636 minutes, 46 secondsYeah, such a good point. I know Meta got got some flack for this recently where they're trying to create a leaderboard who's doing the most.
36:5236 minutes, 52 secondsTo be fair, I do understand why companies do that which is I am surprised by how much work it takes to
37:0037 minutesget people to identify the outer loop of their work and enlist an agent and build sort of the I don't know the the term
37:0937 minutes, 9 secondsright now is like factory, right? Like the software factory for the work that they do. Uh it is surprising to me how
37:1637 minutes, 16 secondsmuch proddding you need to do to get people out of their the way they're used to working. And so if you're dealing
37:2437 minutes, 24 secondswith tens of thousands of people at the scale of meta, I have some sympathy for okay, a good way to do this is just
37:3137 minutes, 31 secondsstart a leaderboard and encourage people to do it. They will find good things and useful things to do with that as they as they learn, right? So it's a Yeah,
Chapter 15: Getting people to change how they work
37:4037 minutes, 40 secondsit's such a good point. like you have to over overindex to change people's default easy behavior. I'm just going to do things. I'm just gonna write these PRDs the way I've always done it. I'm
37:4837 minutes, 48 secondsgonna run the meetings the same the same way I've done it. I think that makes a lot of sense. What have you seen actually work within notion to get people to significantly change the way
37:5637 minutes, 56 secondsthey work? Depends on the role. So roles that are perhaps further away from engineering
38:0438 minutes, 4 secondsactually you don't have to convince them all that much because they're like whoa I have superpowers now. look at this amazing thing I've just built because
38:1238 minutes, 12 secondsthe the capability gap of what they were able to do before versus after is so huge that it it's intoxicating. And then you have to actually almost do the
38:1938 minutes, 19 secondsopposite which is like yes but do you understand why we can't merge this PR? I think on the engineering side something
38:2738 minutes, 27 secondsthat uh Simon last talks about a lot is sort of any manual intervention in code
38:3538 minutes, 35 secondsis kind of bad. you probably did something wrong in the verifiability loop and in sort of the software
38:4238 minutes, 42 secondsfactory. Uh this excludes obviously reviewing code, right? Like I am still very much in camp. You should probably
38:4938 minutes, 49 secondsreview more code than put more effort into reviewing code than you do. Um but at least on the writing side, every time
38:5638 minutes, 56 secondsthere is an intervention, a human intervention, it should feel a little bit like a bug. I think that's a good litmus test for uh how I don't know
Chapter 16: Max’s AI stack
39:0439 minutes, 4 secondsagentfilled you are. I want to come back to the tools that you use. You mentioned um Figma is kind of trending down within the design org, which is really interesting. Is there anything that's
39:1339 minutes, 13 secondstrending up? Anything else that's trending down in terms of tools in the tool stack of your team? So, I'm actually not positive that Figma is
39:2039 minutes, 20 secondstrending down. I think it's more that there is a there's two camps. Uh I could totally believe the Jevans paradox,
39:3039 minutes, 30 secondswhich is Figma is actually going up and then of course vibe coding is going up.
39:3439 minutes, 34 secondslike I don't want to create in general I really really dislike the the rivalry discourse that exists in in Silicon
39:4139 minutes, 41 secondsValley which is for anthropic to win OpenAI needs to lose and vice versa and like that kind of thing. So I I I don't
39:4839 minutes, 48 secondswant to um perpetuate that with sort of the Figma versus versus coding. I think uh the terminal is actually surprising
39:5639 minutes, 56 secondswhich is it's initially kind of scary for people and you could do so much but now PMs are slowly the once they're in
40:0440 minutes, 4 secondscloud code or codeex everything is fine right and I generally encourage them to not use the guies I I I I encourage them to use the the the twe because I just
40:1240 minutes, 12 secondsknow that over time they're going to be curious and like pull at other threads and one day they wake up and they're like oh I understand more of the substrate of what how how computers work.
40:2140 minutes, 21 secondsThat is so interesting. So the designers are using the terminal.
40:2440 minutes, 24 secondsYes. Yeah. And then um I I don't know conductor is another one. They they're basically just mostly using developer tools. It's not that different from what uh developers use.
40:3440 minutes, 34 secondsI am so excited to tell you about this season's supporting sponsor, Vanta.
40:3940 minutes, 39 secondsVanta helps over 15,000 companies like Cursor, Ramp, Dualingo, Snowflake, and Atlassian earn and prove trust with
40:4840 minutes, 48 secondstheir customers. Teams are building and shipping products faster than ever.
40:5140 minutes, 51 secondsthanks to AI. But as a result, the amount of risk being introduced into your product and your business is higher than it's ever been. Every security
41:0041 minutesleader that I talk to is feeling the increasing weight of protecting their organization, their business, and not to mention their customer data. Because
41:0841 minutes, 8 secondsthings are moving so fast, they are constantly reacting, having to guess at priorities, and having to make do with outdated solutions. Vanta automates
41:1641 minutes, 16 secondscompliance and risk management with over 35 security and privacy frameworks including SOCK 2, ISO 27,0001 and HIPPA.
41:2541 minutes, 25 secondsThis helps companies get compliant fast and stay compliant more than ever before. Trust has the power to make or break your business. Learn more at vanta.com/lenny.
41:3641 minutes, 36 secondsAnd as a listener of this podcast, you get $1,000 off Vanta. That's vanta.com/lenny.
Chapter 17: Which roles AI will transform next
41:4341 minutes, 43 secondsAI has completely transformed the work of a software engineer. Like two years ago versus today, it's completely different. Like almost all your code is
41:5241 minutes, 52 secondsnow AI. It and we've been talking about like when will 50% of engineers in the world be writing 100% AI code? It's
41:5941 minutes, 59 secondsprobably like in a year, which is insane how much that job has changed. Which role do you think AI transforms
42:0742 minutes, 7 secondsnext? Is it marketing? Is it growth? Is it sales? Is it design? Do you have a sense of like where things are starting to really change other than engineering?
42:1542 minutes, 15 secondsOkay, this is maybe a hot take and I actually don't have enough um I I it's very likely that the labs are like haha
42:2242 minutes, 22 secondslook at this guy. Um my take it's very clear at least empirically that models are getting better at coding at some
42:3042 minutes, 30 secondsexponential rate right and I don't think that's changing now. I'm not that impressed with the
42:3742 minutes, 37 secondsprogress in the any other domain. it tends to be like I don't think they've gotten significantly better at writing.
42:4342 minutes, 43 secondsI still very much hate reading uh sort of AI slop writing but the thing
42:5042 minutes, 50 secondsis software we we uh Andre right like software is eating the world well if the cost of software and creating software
42:5842 minutes, 58 secondsand encoding business practices in code and like I just literally mean the old like software 1.0 no kind of code then
43:0543 minutes, 5 secondsif that cost is very much going to zero we will just have a lot more of it and so I think then in that case it's more
43:1243 minutes, 12 secondsthat software engineering will go into all the other domains not necessarily that there is sort of some sort of yeah
43:1943 minutes, 19 secondslike um I don't know our folks in HR are automating a lot of things because now they don't have to bug an engineering
43:2743 minutes, 27 secondsteam to write that code uh and so I think that's how it's it's going and like if you look at when the model companies say, "Oh, we've made great
43:3543 minutes, 35 secondsprogress in this other non-coding domain." I was like, "You just applied coding principles to this domain, which
43:4343 minutes, 43 secondsis wonderful, but that's what it's getting better at, right?" And so I think um I I just think software is eating the world is going to accelerate.
43:5043 minutes, 50 secondsThat is a really interesting take. So it's basically software just the acceleration of software eating the world uh versus it's like it's going to now do a different kind of job. This
43:5943 minutes, 59 secondsmakes me think about the um had a product for codec said the same thing that every agent there's all these different kinds of agents and his take is every agent that will win is going to
44:0744 minutes, 7 secondsbe a coding agent that builds the thing it needs versus like it's come it has like certain number of capabilities.
44:1344 minutes, 13 secondsOpen class is such a good example. It's just like I will build a skill for myself and now I know how to do this thing.
44:1844 minutes, 18 secondsYes, all agents are also like if you look at all the harnesses whether it's the open source ones or the ones from the model companies uh ours as well uh
44:2544 minutes, 25 secondsthey all resemble a coding agent. I'm going to come back to the ROI piece. I think this is really interesting as you said there's just like okay we're going
Chapter 18: When companies will start caring about ROI
44:3244 minutes, 32 secondsto spend spend spend just see what happens learn accelerate lean into all this stuff you're uh saying that in maybe 6 months something like that you
44:4144 minutes, 41 secondsthink a lot of companies are going to start really looking at the cost here what do you I know you said you don't like to predict things but what do you predict is going to start happening I
44:4944 minutes, 49 secondsprobably spend too much time than I should because I have literally zero impact on any of this as sort of how it plays out but you can imagine a world
44:5744 minutes, 57 secondswhere the labs the delta between the labs and open weight models and so on uh
45:0445 minutes, 4 secondswidens. That is a world that I very much don't like because I I hate centralization of power. Um but in that
45:1245 minutes, 12 secondsworld uh I think the labs just kind of get to decide uh what the world looks like. I
45:1945 minutes, 19 secondsthink if that gap doesn't widen then you will just see a diffusion and people will get very comfortable running their
45:2745 minutes, 27 secondsown models rlinging their own models right like you see this with cursor you see this with intercom notion is uh dabbling in it as well he's dabbling
45:3545 minutes, 35 secondsright now but uh obviously at some point we might become more serious about it and then you have like it's not going it may not be the frontier but for a lot of
45:4345 minutes, 43 secondstasks it'll be good enough and so I think in that case that is just an ROI calculation that is the is it cheaper
45:5045 minutes, 50 secondsfor me to send this task to a smaller model that is cheaper to run where I remove the lab sort of profit margin kind of thing. I think that may happen
45:5945 minutes, 59 secondsbut it only happens if there isn't a fast sort of like you know oh yeah the gap is now so big. The other one is that's interesting is right now I think
46:0746 minutes, 7 secondswe're actually in a one of the luckiest possible timelines which is we have at least in the US three competent labs
46:1546 minutes, 15 secondsthat are all sort of duking it out at the and like who knows maybe meta now.
46:1946 minutes, 19 secondsSo four maybe we can make it six at some point. I think like I would love a world where we have like a dozen sort of frontier models in the US versus having
46:2846 minutes, 28 secondsto always rely on on on um uh other places in the world to do this. Uh but like that's sort of pretty good. If that
46:3646 minutes, 36 secondschoose stopped I would be somewhat worried. Um uh and then it's hard to predict right like what would happen. Uh
46:4546 minutes, 45 secondsbut if that doesn't then I think it's going to look similar to the cloud wars which is some point layers commoditize.
46:5246 minutes, 52 secondsBusinesses are not going to want to lock in into one single provider. uh I don't know in a past life I worked at Heroku and like Kubernetes was much more
47:0047 minutessuccessful than than Heroku even though I think from a user experience perspective it was much worse but the delta was Heroku was saying hey we're
47:0847 minutes, 8 secondsgoing to uh uh replace your ops team and Kubernetes was we're going to make your ops team superheroes and also we're not
47:1647 minutes, 16 secondsgoing to lock you into a cloud you can choose and obviously that's what businesses want right like businesses want uh choice and so I don't know it
47:2347 minutes, 23 secondsit's really hard to predict because It depends. So, it's so as asymmetric in terms of model progress.
47:2947 minutes, 29 secondsWhen you say the products that win often are the ones that make you feel like superheroes, I always think about Kathy Sierra. Do you remember that at all as the thing?
47:3647 minutes, 36 secondsUh, it rings a bell. Okay. This just like it's like from from the olden days at this point. Shows how old I am. She was just something that really stuck
47:4547 minutes, 45 secondswith me and I think it's informed a lot of how people think about product at least in the past is just her whole pitch was uh instead of making talking about your product and how amazing it
47:5347 minutes, 53 secondsis, it's about we will make you a superhero. Like it's like Mario getting the little flower and having superpowers now versus look at our incredible
48:0148 minutes, 1 secondproduct. Uh I think it's actually a thing that uh the coding companies had to learn when they tried to move to like why do code review tools automatic code
48:0948 minutes, 9 secondsreview tools not work that well? I think this is actually a subtle thing which is you push your code publicly to or publicly within your organization or
48:1848 minutes, 18 secondsyour team and then a thing roasts your code and tells you how terrible of a developer you are versus if you think
48:2548 minutes, 25 secondsabout what claude code and codeex does is you're coding and then you publish the work of you plus Claude and you get
48:3448 minutes, 34 secondsbragging rights of how good of a developer you are, right? And so I think the superhero stuff is is definitely true. Speaking of superhero, I wasn't planning to talk about this, but I've
Chapter 19: Why Notion AI is so successful
48:4248 minutes, 42 secondsbeen hearing a lot about how much people love your agent, the notion AI agent that you all released. Just like it's just coming up a lot of just like, wow,
48:5148 minutes, 51 secondsthis is actually really useful with like a lot of different people. It'd be interesting to hear what you think made it so successful. I know it was like a long time before you guys launched it.
49:0149 minutes, 1 secondJust like what do you think is helping it be this useful and successful as a product out in the world? I would like
49:0849 minutes, 8 secondsit to be even better. So, I I'm like my own worst critic, I guess. Uh I've spent most of my day thinking about where it
49:1649 minutes, 16 secondsfalls short, not how great it is. But I agree with you that um I'm actually surprised at how this sounds so weird. I'm surprised how
49:2449 minutes, 24 secondsgood it is, if that makes sense. Um Notion has always been fairly at the forefront of AI. Like I think the first
49:3249 minutes, 32 secondsnotion assistant was actually launched before Chat GPT. And so it's not that like I think both Ivan and uh Simon had
49:3949 minutes, 39 secondsthe intuition of hey this is going to change a lot of things and so that's a huge sort of reason why but there every company wants to become AI native now
49:4849 minutes, 48 secondswhatever that means I it's kind of like cloud native I'm like if you have to say it then are you really do you have a chance but uh I'm surprised how fast
49:5649 minutes, 56 secondsthat happened for notion and I I'll take almost no credit in this um I think what's good about it is agents need
50:0350 minutes, 3 secondscontext to operate agents don't really like walls of like oh I I have to go through this narrow
50:1150 minutes, 11 secondsorifice to talk to this other data repository and um I think for the first time it is kind of obvious to people why
50:2050 minutes, 20 secondsa connected workspace is actually valuable because it's great I can have agents roam around and do that and it touches on malleable software I think I
50:2850 minutes, 28 secondsthink of notion as an operating system more so and then in that case it resembles the environment that coding agents are in with Unix much more than
50:3650 minutes, 36 secondsone might maybe intuitively think. So I think those all contribute and then sometimes it's just we're just dumb enough to try hard things. Uh and so I
50:4550 minutes, 45 secondsthink our enterprise search is sort of like this this thing where we do a lot of automatic permission handling and so on that others don't. Uh I don't know
50:5250 minutes, 52 secondsit's it's you have to care. I'm going to come back to my quote from the Bible. I feel like that actually is an answer to this question that it was made for such
51:0151 minutes, 1 seconda time as this. the fact that notion basically has all the things about everything in your company is the perfect source of context for using AI
51:1051 minutes, 10 secondsand helping you work. So, it's just like just being around long enough for Wow.
51:1451 minutes, 14 secondsOkay, this is exactly what we've been meant to be. It's nice job. Nice job. It's the same as uh malleable software,
51:2151 minutes, 21 secondsright? Like I I love that people are waking up to malleable software now, but it's been around for a long time. It was just always slightly too hard and slightly too like why would I do this?
51:3151 minutes, 31 secondsAnd so I think yeah I like I'm going to use this quote from the Bible. Thank you.
51:3451 minutes, 34 secondsThere it is. It's like shorter. The original quote is for such a time as this and interpretation is this. You're like destined to do this thing. This is
51:4451 minutes, 44 secondsvery Bible heavy episode. Oh man. Um going back to the way your team operates because I think this is something that a lot of people are thinking about right
Chapter 20: How to ship more quickly while maintaining quality
51:5251 minutes, 52 secondsnow. There's all this talk of productivity pace getting things out like Anthropics launching a a massive product every day. Basically,
51:5951 minutes, 59 secondsyour job is at a product, help people ship consistently, regularly, often,
52:0452 minutes, 4 secondsship great stuff. What has worked in allowing you guys to ship more quickly if you are and and stuff that you're
52:1252 minutes, 12 secondsproud of, stuff that works? I think this answer is so specific to companies like internal culture where if you I've I've
52:2152 minutes, 21 secondsbeen at this in this situation sort of twice in my career. one is uh when I joined GitHub which is obviously I think
52:2852 minutes, 28 secondsI don't know insane product market fit uh it just so happened that at the time that I had joined there was a little bit of a I don't know identity crisis or
52:3752 minutes, 37 secondslike oh what's our next act what do we do and like lots of debates about what to ship because it's such a tough act to follow if your first act was just
52:4552 minutes, 45 secondsincredible right and I don't know I would put notion in the same bucket and so a lot in this case it's just like reminding people that hey you can just
52:5352 minutes, 53 secondsdo stuff we don't have to be that precious. I think there's this preciousness that develops over time.
52:5752 minutes, 57 secondsIt's like, oh, what do we do? And our users are going to be upset. Well, our users are going to be upset if we don't innovate more so than if we accidentally
53:0553 minutes, 5 secondsbreak a thing. So, it's obviously a balance. Um, but I think just reminding people that the same group of people that was able to do the first act is
53:1353 minutes, 13 secondsvery likely going to be able to do the second one, but you have to try. Shots on goal is a thing that we say internally a lot, which is like great,
53:1953 minutes, 19 secondshow do you increase shots on goal? which of course if if we go back to it's easier to experiment now you're increasing the shots of goal on goal
53:2753 minutes, 27 secondsright um so I think that has worked really well just shipping feature after feature doesn't I we have been a little
53:3553 minutes, 35 secondsbit on a roll in terms of shipping new functionality maybe in the last like I don't know 6 months or so but at the end of the day feature count is the same
53:4353 minutes, 43 secondssilly metric as lines of code or tokens consumed or whatever um I would rather have fewer features
53:5153 minutes, 51 secondsthat are really really good and where the combinatorics let you do everything.
53:5653 minutes, 56 secondsAnd so I think something that I'm still very much uh struggling with is software quality. And I will also say I don't
54:0554 minutes, 5 secondsthink the labs are exempt from this. Uh like I I love their tools. It's great.
54:0954 minutes, 9 secondslike I love I live in the CLI but a regression like every two weeks of like a thing that was fixed like three weeks
54:1654 minutes, 16 secondsbefore and they still can't render a TUI at I don't know a frame rate that's ex reasonable and so I think yeah quality
54:2554 minutes, 25 secondsis a thing that's missing like this Appleesque machined unibody aluminum kind of engineering I I I would like us to to figure out how to get back to that
54:3454 minutes, 34 secondsas an industry. Is there something you've done to help improve that? So,
54:3954 minutes, 39 secondsthere's code quality and then there's actual software quality. If you're shipping, you know, shots on goal, there's always this balance of, okay,
54:4554 minutes, 45 secondsbut wait for it to be awesome. I know this is just like very hard question to answer, but just how do you what's your kind of communication to the team of
54:5254 minutes, 52 secondshere's how we're going to here's where we're going to find that balance? And this is a very frustrating thing for people, but uh I actually I can't show you because I'm using my laptop, but we
55:0055 minuteshave a obviously good stickers, which is let's just only make obviously good stuff. the origin, which is like, okay, wait, what does that mean? And I'm like, ah,
55:0855 minutes, 8 secondsyou know it when you see it. Like, I don't think anyone argued when they saw the first iPhone that it's obviously good. I don't think anyone argued that when Chat GPT first came out that it's
55:1655 minutes, 16 secondsobviously good. And so, I think that's the bar, like just make obviously good stuff. I think the mistake that maybe a lot of companies then make is great,
55:2455 minutes, 24 secondswe're going to be in this cave in isolation until we have it sort of be obviously good. Um, one of my core values is incremental correctness, which is sort of, uh, iterate, get really,
55:3455 minutes, 34 secondsreally good at iterating. And so, uh, I don't know, it's probably a union of, okay, increase shots on goal. Like,
55:4055 minutes, 40 secondshere's a great example. We get roasted from our customers all the time, which I love about we have like six automation primitives inside of notion, right? Like if you include all the agents and so on.
55:5055 minutes, 50 secondsI'm like, yep, we let like a bunch of sort of different ideas sort of grow. we look at how they work, but then you do
55:5755 minutes, 57 secondshave to do the hard work at consolidating it back into like the the naked robotic core of that idea and that's hard, right? Because you have to
56:0556 minutes, 5 secondssort of be okay with perhaps then shipping the next thing slightly delayed as you reconcile. Um I don't know. I think we have work to do there like at
56:1356 minutes, 13 secondsnotion but um at an as an industry too like somebody was joking like why does claude the desktop app have three tabs
56:2156 minutes, 21 secondsof co-work and I don't know what the first chat or whatever um why do we have six automation primitives well because
56:2856 minutes, 28 secondssomeone has to sit down and reconcile them and like figure out what's actually the core simple thing that should
56:3556 minutes, 35 secondsoutlive the other uh sort of evolutionary branches uh of that same idea. this idea of knowing when things
Chapter 21: Building taste through iterations
56:4256 minutes, 42 secondsare obviously good. There's a element of having taste and there's this word taste that comes up a lot now and this is like what we will need more and more because
56:5056 minutes, 50 secondsAI is building the thing now our job is taste is this great is this good I feel like you're someone that has really great taste a question people always ask
56:5856 minutes, 58 secondshow do I build taste do I have taste do you have any advice for someone that's like I want to develop my taste I first I don't know if I have great taste like
57:0657 minutes, 6 secondsI I I look at others and I look at how they exercise taste and I think that The
57:1357 minutes, 13 secondscommon thing I think is iterations with feedback.
57:1957 minutes, 19 secondsSo it takes a really long time to build up taste in a specific domain. Then you maybe often can extrapolate into other
57:2857 minutes, 28 secondsdomains with that taste. But if I had to describe what taste actually means, it's you're able to run, this is such a nerdy
57:3557 minutes, 35 secondsway of describing it. You're able to run a virtual machine in your head where given an idea, you can predict for a
57:4357 minutes, 43 secondscertain inroup whether they're going to like it or not. Right? Um the extremes are is if you are the only person on the
57:5257 minutes, 52 secondsplanet that thinks something is good, is it good? No. But maybe you also don't need to build a product for 8 billion people. I've never built consumer
57:5957 minutes, 59 secondssoftware. I I would probably be terrible at it. But you decide what your in-group is and then how good do you get at emulating
58:0858 minutes, 8 secondsuh how they will react to it. And to do that you just have to do reps.
58:1458 minutes, 14 secondsIt's almost like training a model which is also why I'm not super you know the whole um the one thing that we have left is is taste. I'm not so sure. Like I if
58:2358 minutes, 23 secondsyou think about the loop it's input idea. How do people react? That seems very uh back propagation. I don't know
58:3258 minutes, 32 secondslike it seems very much how we train models too.
58:3458 minutes, 34 secondsSo I what I love that it's basically you built taste by just doing the thing getting feedback iterating.
58:3958 minutes, 39 secondsLook at Japan like Japanese crafts people right they've just been I don't know painting the bowl for however long uh and it just takes a while and so I
58:4858 minutes, 48 secondsthink the more reps they the increase the frequency of reps that's that's what I would say. It's so funny. That's exactly how um you know agents learn and
58:5658 minutes, 56 secondsand develop how how as you said a models learn just like doing the thing seeing was this good was this correct no okay learn. So it's just yeah it's just doing
59:0459 minutes, 4 secondsthe thing learning getting feedback and there's no way to uh speedrun this. This is why often people with the best taste have been doing this for a long time.
59:1359 minutes, 13 secondsThe one thing I will say that I've noticed is specifically for designers,
59:1859 minutes, 18 secondsthe designers that I think have at least in software design high taste are the ones that both have side projects that
59:2559 minutes, 25 secondsthey build where they're responsible of the full thing in end and they're also always tinkering with some new app. Like
59:3359 minutes, 33 secondsthey're the annoying person that is like, "Hey, what if we tried this in our team?" I'm like, "Really? This is the 49th time that you suggested a new tool.
59:4059 minutes, 40 secondsDo we really need this?" It's exposure to other people's ideas. I I think that is the u it's also really important to
59:4759 minutes, 47 secondssurround yourself with tasteful things so that you feel like the thing you're making is lacking, right? Like one of the things we do at Notion is uh all of
59:5559 minutes, 55 secondsour conference rooms are named after uh famous objects like the first typewriter, the Macintosh, a Porsche 911 and so on. And so inevitably when I'm
1:00:041 hour, 4 secondssitting in one of the rooms and I pay attention to the room like nothing I'm doing amounts to this like uh I got to do better. You've built so many successful great loved products.
Chapter 22: What matters most in building successful products
1:00:171 hour, 17 secondsWhat do you think matters in the end to building a successful product? If you had to just kind of boil it down.
1:00:241 hour, 24 secondsYes. Here's the one trick that I'll sell a course next week.
1:00:271 hour, 27 secondsUm please I'll sign First of all, I think I would actually say that I have contributed to some really great products, not built them. Because I
1:00:351 hour, 35 secondsthink uh I did not I think I did not used to believe this early on in my career, but like the longer I'm in this,
1:00:421 hour, 42 secondsthe more I care about what's the team that's building the thing. I used to think that was such like a I don't know,
1:00:481 hour, 48 secondsnot important thing. Uh and now I'm like, it's the only thing. Um, I don't think that there is a through line out
1:00:551 hour, 55 secondsof the things that I've contributed to where I can pinpoint it. Um, I think that you can't say that the best design always wins. I think there's many
1:01:031 hour, 1 minute, 3 secondsproducts where just design doesn't matter and like I think then as a designer you can have this identity crisis of like why am I doing this? I think you can't even say that the way
1:01:111 hour, 1 minute, 11 secondsit's built always like the best engineering always wins.
1:01:151 hour, 1 minute, 15 secondsUh I think one of the biggest pitfalls is if you get into the loop of if I just add one more thing to the product it'll
1:01:231 hour, 1 minute, 23 secondsbe finally great. Like if I really look at the the truly great products they all have one tiny core that is so
1:01:311 hour, 1 minute, 31 secondsexceptionally good. And uh that is both a combination of you stumbled upon it by luck uh and then the market agreed but I
1:01:401 hour, 1 minute, 40 secondsthink it's the what's the tiny core? I don't know multi-touch on the phone. uh GitHub is probably the poll request,
1:01:461 hour, 1 minute, 46 secondsright? Like this idea that anyone can suggest something to you and and sort of you see it. Um I do think that at notion it's the blocks and like the slash
1:01:541 hour, 1 minute, 54 secondscommands like uh Figma. It's sort of the seamless blend between uh uh real-time collaboration and and and and not like
1:02:041 hour, 2 minutes, 4 secondsall the great products have something tiny that is a superpower. Like that's sort of like uh uh versus oh yeah if we have this suite of things and like we
1:02:121 hour, 2 minutes, 12 secondsadd one more thing it'll finally be useful that never works and for GitHub interesting it was the PR um other examples of that at other
1:02:191 hour, 2 minutes, 19 secondsplaces you worked because this is really interesting just like what's the tiny core that makes everything else work? Um at Heroku for sure I think it was the
1:02:271 hour, 2 minutes, 27 secondsthe git push Heroku master of like uh at the time it was really hard to deploy apps right like this is like nobody it's
1:02:341 hour, 2 minutes, 34 secondssad because people don't remember Heroku they but like I have to explain it as it's the versel it's the first versel did it get bought by Salesforce who
1:02:431 hour, 2 minutes, 43 secondsyes yeah okay um yeah get push master was just like this very simple oneliner that went from the thing on my computer now I have a
1:02:521 hour, 2 minutes, 52 secondsURL and that's so intoxicating that everything else sort of flows from there.
1:02:561 hour, 2 minutes, 56 secondsUh, Dropbox is a great one, right? Like I think Dropbox is like such an interesting study where it was the little menu bar icon that was so good at
1:03:061 hour, 3 minutes, 6 secondssyncing that you could even use it as a symbol for do I have internet or not because it was better at figuring out whether you had an internet connection
1:03:131 hour, 3 minutes, 13 secondsthan your Mac itself. And it was it just that's the job. Get out of the way and just all my files are always there. And
1:03:201 hour, 3 minutes, 20 secondsthen for years they tried to increase the surface area and I kept thinking no no no no push it back. I don't want more like this is the only job I want from
1:03:291 hour, 3 minutes, 29 secondsyou. Right. And so I think the tiny core like is is is the thing that makes great products.
1:03:341 hour, 3 minutes, 34 secondsAnd Snapchat obviously just like the disappearing photo concept is so interesting. I hear I heard you've also talk about just like being first doesn't matter that much either.
1:03:441 hour, 3 minutes, 44 secondsYou have to be right. Not first. Uh I don't know. Like I think um uh I mean there are probably there are elements of
1:03:521 hour, 3 minutes, 52 secondslike if you talk about network effects and like perhaps now with like training models it does make sense if you have sort of a a a head start but I think
1:04:001 hour, 4 minutesit's overrated. Um I don't know like my favorite example is like Bluetooth headphones were kind of crappy and then you have the AirPods and like oh they
1:04:081 hour, 4 minutes, 8 secondsconnect and so on and they weren't the first like I don't know they weren't the first MP3 player they weren't the f like you just got to do it right. Uh, I don't think being first is all that that
1:04:161 hour, 4 minutes, 16 secondsuseful. I think we're currently because it's so hard to keep people's attention.
1:04:221 hour, 4 minutes, 22 secondsWe try to like we're like, "Oh, how do I become how how do I go viral, right? How do I do the Clo thing?" And I'm like, "Yep, I don't durability matters,
1:04:301 hour, 4 minutes, 30 secondsright?" Like, uh, think of how would you build IKEA like a generational company that is not concerning itself with whatever is trending on Twitter today. I
1:04:391 hour, 4 minutes, 39 secondsthink speaking of models, a good example is Anthropic, which was way behind, started after OpenAI, got less funding,
1:04:451 hour, 4 minutes, 45 secondsand now is just killing it and dominating. And the thing that I find the most impressive about uh I don't know who to
1:04:541 hour, 4 minutes, 54 secondsgive credit, but like obviously you give the CEO a bunch of credit, but like Dario is that he wasn't Oh, he wasn't
1:05:011 hour, 5 minutes, 1 secondjust lucky once at OpenAI. He did the same thing twice and it was successful twice. And like I think that's like that's actually really cool. I know you're also a believer in jobs to be
Chapter 23: Using the jobs-to-be-done framework
1:05:091 hour, 5 minutes, 9 secondsdone as a way of thinking about product which is kind of this it's been a long time controversial topic on this podcast mostly because of Shiram who's very
1:05:161 hour, 5 minutes, 16 secondsanti- jobs to be done. Uh what's your kind of framing of how you find this framework useful in thinking about product?
1:05:221 hour, 5 minutes, 22 secondsI bet that if I read reread all of the Clayton Christensen stuff I would also
1:05:311 hour, 5 minutes, 31 secondsnot identify super strongly with it. I use it mostly as have you thought holistically about what the user wants
1:05:391 hour, 5 minutes, 39 secondsto hire your product for and are you honest about what the user wants versus what you want the user to want. And then
1:05:491 hour, 5 minutes, 49 secondsthe other thing that I find happens very frequently in larger organizations is that people sort of turn off the brain
1:05:581 hour, 5 minutes, 58 secondswhen they're reviewing their own products uh from a I'm a user. Is this a good experience? And they're more like
1:06:061 hour, 6 minutes, 6 secondsI'm a employee of this company and I made a thing. And so I think jobs to be done might encourage people to zoom out
1:06:151 hour, 6 minutes, 15 secondsand sort of not get lost in the the sauce of like making the thing. That's why I like the framework. It's a good reminder of like no no no the user hires you for a thing.
1:06:261 hour, 6 minutes, 26 secondsBe that user for a second. Would you even buy the thing that you just made?
1:06:301 hour, 6 minutes, 30 secondsAnd the answer often is like oh uh I hadn't thought about that. Right? Like and so that's that's how I use Is there an example of this from some of the products you worked on just to make this
1:06:381 hour, 6 minutes, 38 secondsreal for people other than like milkshake example? Obviously,
1:06:411 hour, 6 minutes, 41 secondsthere's a very recent one which is more about communication. We're launching a new feature soon and we're working on this landing page to describe the
1:06:481 hour, 6 minutes, 48 secondsfeature. And I found that when people make landing pages, first of all, their writing skills just like deteriorate
1:06:551 hour, 6 minutes, 55 secondsimmediately because they want to sound clever and like marketing speak comes out of their mouth. And I'm like, wait,
1:07:001 hour, 7 minutesthat's not how you would explain it to a friend. And then if I'm communicating this product to you, just pretend you're standing in front of a whiteboard.
1:07:081 hour, 7 minutes, 8 secondsWhat's the manic thing that you're drawing on the whiteboard to to to to communicate this versus, okay, now go back to the thing you just designed,
1:07:161 hour, 7 minutes, 16 secondslook at it. Are you telling me that those are the same thing? Are you telling me that you understand what this thing does and like that zoom out? So, I
1:07:231 hour, 7 minutes, 23 secondsdon't know. Um, yeah, I don't know. I don't want to pick on on individual uh recent things, though.
Chapter 24: Hot take on universal basic income
1:07:291 hour, 7 minutes, 29 secondsOkay. Uh, as we close out this conversation, there's something I want to get your you have this hot take on on universal basic income. This completely out of the blue, but I think it's
1:07:371 hour, 7 minutes, 37 secondsinteresting to hear. There's this idea that, you know, with AI emerging, we may not need to work. We'll all just get some UBI and enjoy our life. And you
1:07:461 hour, 7 minutes, 46 secondshave this uh hot take that maybe we already have universal basic income. What's what's going on?
1:07:511 hour, 7 minutes, 51 secondsYeah. So please extend me some grace here because I both mean it as a joke and maybe somewhat real like just depends on which altitude of human
1:07:581 hour, 7 minutes, 58 secondsnature you look at. Um my my take is that we already have universal basic income. It's called knowledge work. Uh
1:08:051 hour, 8 minutes, 5 secondsand I don't exclude my job from it. But if you really look about at what do we actually need to live and like to be
1:08:141 hour, 8 minutes, 14 secondscontent, it is a lot less. and we've built this hierarchy and this sort of all these jobs and all these things that are absolutely necessary. Uh and so to
1:08:231 hour, 8 minutes, 23 secondsto me it's like yeah, we already have it. It's UBI and we'll come up with other ways in which we as humans because we're the most important species in the
1:08:311 hour, 8 minutes, 31 secondsuniverse insert ourselves into the conversation around agents. Um will it look the same? I don't know. But uh
1:08:381 hour, 8 minutes, 38 secondsyeah, I don't know. We are so inventive and we come up with new reasons of why we absolutely must be in that loop. Um, and so I think that's my my my hot take.
1:08:461 hour, 8 minutes, 46 secondsPeople have always joked like we get paid so much just to sit in front of a computer and put the right sorts of words and letters into the into this thing and we get paid a lot of money to
1:08:541 hour, 8 minutes, 54 secondsdo it and now it's like oh maybe I won't be paid this much in the future because AI is going to be taken over and so your take there is just like this a
1:09:021 hour, 9 minutes, 2 secondspretty sweet gig we already got. Enjoy enjoy the CBI. Yes. I I think I think all things considered how lucky are we?
1:09:111 hour, 9 minutes, 11 secondsLike I don't know. I'm sitting in an air conditioned room right now talking to you, having a good time. Uh I don't know like yeah I just to be clear not
1:09:201 hour, 9 minutes, 20 secondseverybody has that luck but I think that's the folks that I find discussing this the most are the ones that are in the bucket of luck. Say we have AGI you
Chapter 25: What Max would do with AGI
1:09:281 hour, 9 minutes, 28 secondsdon't have to work you could just do anything. What would you be spending your time doing?
1:09:311 hour, 9 minutes, 31 secondsI actually ask this to almost everybody that we hire. Um I would be doing the exact same thing.
1:09:381 hour, 9 minutes, 38 secondsUh I would uh probably spend less time um having meetings and managing. One of the sad things about my job is that uh I
1:09:481 hour, 9 minutes, 48 secondshave yet to replace uh 80% of it with agentic loops. Um uh I I I envy our engineers and designers who get to to do
1:09:571 hour, 9 minutes, 57 secondsthis. So um hopefully at some point I won't like I won't have a job. Uh um but yeah, I would do the same thing. I think
1:10:041 hour, 10 minutes, 4 secondsI am someone who I don't code because of a utility. I code because it's also an intellectual challenge. So I think of it as playing chess and go. Um I'm very sad
1:10:131 hour, 10 minutes, 13 secondsthat Lee Sodel uh after losing against I think I I don't know if it's alpha go or zero but one of the two sort of like it
1:10:211 hour, 10 minutes, 21 secondsseems like he gave up on go and I'm like who cares if some machine is better at it like uh it's the human stuff like
1:10:291 hour, 10 minutes, 29 secondsjust you know keep going at it. And so I think I would do the same thing. I would tinker. I would build stuff. Uh I would try and make the world around me more malleable. I just got an email this morning from someone who asked me about,
1:10:411 hour, 10 minutes, 41 secondsoh, you think a lot about malleable software. Have you ever thought about what robotics might do? And it just blew my mind because I had not because it's so far from the skills that I have.
1:10:501 hour, 10 minutes, 50 secondsUh, but yeah, I don't know, something like that. Just I would do the same thing.
Chapter 26: Contrarian corner
1:10:541 hour, 10 minutes, 54 secondsAmazing. Okay, I'm going to take us to two recurring corners of the podcast to see what we find there. Uh, the first
1:11:011 hour, 11 minutes, 1 secondcorner is contrarian corner. Is there something that you have a you have a lot of these already. I'm curious if there's anything else. Is there something you have a contrarian opinion about?
1:11:091 hour, 11 minutes, 9 secondsSomething you believe that a lot of people don't? It's becoming so hard to have contrarian views because I think the algorithms just uh try and get
1:11:171 hour, 11 minutes, 17 secondscontrarian views out of people sort of you know at like a insane uh with an
1:11:231 hour, 11 minutes, 23 secondsinsane force. um depending on the era uh like this may not be contrarian but I think that inclusivity isn't always all
1:11:321 hour, 11 minutes, 32 secondsthat great um um I think I I very much believe in small group theory like I think the world is run by group chats of
1:11:401 hour, 11 minutes, 40 secondseight people or fewer uh and so sometimes it's great to be exclusive and what I mean by that is I even think
1:11:481 hour, 11 minutes, 48 secondsabout this in terms of notion notion could have the ambition to say we are going to have 8 billion users so every single person on the planet use this
1:11:561 hour, 11 minutes, 56 secondsnotion. And I think if we did that, we would very much upset the first call it 500 million because uh
1:12:051 hour, 12 minutes, 5 secondsthe top of the class wants different things than everybody and everybody is in the top of the class at something.
1:12:111 hour, 12 minutes, 11 secondsAnd so I think being okay with being exclusive sometimes is is okay. Um, I I will have to caveat
1:12:201 hour, 12 minutes, 20 secondsthis with if you are if you're McDonald's and you have exclusive hiring practices and it's the only job in a
1:12:291 hour, 12 minutes, 29 secondslocation, that is not what I'm talking about. But like going back to comfy air conditioned like job kind of thing. It's like great, just work with and for the
1:12:371 hour, 12 minutes, 37 secondstop of the class is sometimes a winning winning thing and just build a really really good product for them which by definition means you're going to exclude others. The TBPN guys have a really good
1:12:461 hour, 12 minutes, 46 secondsway of describing this exact concept which is you know they had like I don't know 8,000 listeners and like a conversation they got acquired for
1:12:541 hour, 12 minutes, 54 secondshundreds of millions of dollars just like what's going on there and the way they pitch it is you know like if we have if we have millions of people listening to this thing this we've done
1:13:021 hour, 13 minutes, 2 secondssomething wrong. This is specifically designed for like the people and power of tech to influence them to teach them
1:13:091 hour, 13 minutes, 9 secondswhat's going on. Um and it worked out it worked out great for them. So it's exactly what you're describing. Okay,
Chapter 27: Failure corner
1:13:161 hour, 13 minutes, 16 secondsI'm going to take us now to fail corner.
1:13:191 hour, 13 minutes, 19 secondsSo you people like you come on this podcast, they're like, "Okay, look at all these wonderful things he's done. He's just killing it all the time.
1:13:251 hour, 13 minutes, 25 secondsEverything's working." In reality, I'm sure not everything has worked in your the course of your career. What's one one example where things didn't work out
1:13:331 hour, 13 minutes, 33 secondsand what did you learn from that experience?
1:13:351 hour, 13 minutes, 35 secondsOh my god, like this is a it's such a weird I don't think about win versus fail. I kind of feel like every day I fail a lot.
1:13:431 hour, 13 minutes, 43 secondsUh what are big ones that annoy me culturally? I think like sort of in running teams I think a mistake that I
1:13:501 hour, 13 minutes, 50 secondsmade is at some point because hiring at this now it's easy but at the time hiring designers that can code was was
1:13:571 hour, 13 minutes, 57 secondsquite challenging and so then if you loosen that requirement I did not sort of predict how quickly that becomes like
1:14:061 hour, 14 minutes, 6 secondsa slippery slope and I would rather have had fewer designers that are more polymath. Um, so I think that's one on organizational side on product. Oh my
1:14:161 hour, 14 minutes, 16 secondsgod. I mean, GitHub actions and their uh the um uh I don't know like it's very technical, but the fact that we also
1:14:231 hour, 14 minutes, 23 secondsthought we didn't need good package management for the actions like I I don't know. I think the world would be better off if we had thought about that
1:14:301 hour, 14 minutes, 30 secondsslightly harder. This is maybe like I I I had a started a a competitor to notion
1:14:371 hour, 14 minutes, 37 secondsin 2014 and uh I didn't think of it as in fact it wasn't a competitor of notion because the week that we were going to get a term sheet from True Ventures,
1:14:461 hour, 14 minutes, 46 secondsNotion pivoted from website building to document collaboration and so True Ventures was like hey sorry we have a conflict and we're like yep no worries.
1:14:541 hour, 14 minutes, 54 secondsUm, and we spent so much time polishing the editing experience. We did markdown
1:15:011 hour, 15 minutes, 1 secondfolding, all the stuff that you now have in Obsidian. Like we sort of did that back in 2014. And we thought that's the thing that really matters. And then
1:15:091 hour, 15 minutes, 9 secondsNotion by comparison, the first version of the Notion editor was terrible. Like there was like no, it was all blocks.
1:15:151 hour, 15 minutes, 15 secondsYou couldn't even select between two blocks. But it turns out it didn't matter. And so I think that is like just working diligently on the wrong thing for way too long. Huge fail.
1:15:241 hour, 15 minutes, 24 secondsThat's so interesting. Just coming back to your insight of when a product works,
1:15:291 hour, 15 minutes, 29 secondsthere's just this tiny core thing that is the thing that makes it amazing and what people want to come back to no matter how bad everything else is. Uh I
1:15:371 hour, 15 minutes, 37 secondsthink that's a really interesting takeaway. We actually kept adding new feature. At some point you go down the death spiral. So we kept adding yet another feature of like okay is it good now? Is it good now? Uh, and it's just,
1:15:471 hour, 15 minutes, 47 secondsyou know, nope. The core wasn't good.
1:15:481 hour, 15 minutes, 48 secondsThat's interesting. And is in your experience, you can tell pretty quickly,
1:15:511 hour, 15 minutes, 51 secondsokay, wow, this is really taking off. We we found something really powerful here. I think you can tell. I think you could.
1:15:561 hour, 15 minutes, 56 secondsYeah, I think it's the the obviously good thing. I think you're like, yep, I this is good. And then it may be good in a way that you give it to users and
1:16:041 hour, 16 minutes, 4 secondsevery single user study that you do or whatever like just it falls flat and they don't know how to use it. I think the important thing is actually to not give up on the core idea. And so it's
1:16:131 hour, 16 minutes, 13 secondsthat's 80% but then the 20% is like relentlessly iterate until it actually clicks with with the folks that you're the that you're working for.
Chapter 28: Advice for young people in Silicon Valley
1:16:221 hour, 16 minutes, 22 secondsMax, is there anything else that you wanted to share with folks? Anything else you want to leave listeners with before we get to our very exciting
1:16:301 hour, 16 minutes, 30 secondslightning round? when I talk to like young I it's so funny to say that but like when younger people in in Silicon
1:16:371 hour, 16 minutes, 37 secondsValley um right now I think that Silicon Valley is uncharacteristically full of
1:16:451 hour, 16 minutes, 45 secondspeople who don't actually love computers. What I mean by that is like it's like sort of like oh I want to make money and of course everybody does I
1:16:521 hour, 16 minutes, 52 secondslike making money too. I think there is this idea of this is the last train or like what do we call like the permanent
1:17:001 hour, 17 minutesunderclass kind of stuff and it it is so detrimental to thinking about how you
1:17:081 hour, 17 minutes, 8 secondswant to spend your heartbeats in life and so I don't know except like the advice I would give is like just don't
1:17:141 hour, 17 minutes, 14 secondslet the rush or the f frenzy sort of distract you from the things that you
1:17:221 hour, 17 minutes, 22 secondsactually care about and are passionate in life, I think it'll find a way. And that is not to mean that you shouldn't work hard. I think you're actually way
1:17:291 hour, 17 minutes, 29 secondsbetter off if you work incredibly hard by until from like 18 to 25 or whatever.
1:17:351 hour, 17 minutes, 35 secondsLike that's the way to go. Like you should work a lot, right? And then later you can work a little less. But um so it's more about the frenetic nature like
1:17:421 hour, 17 minutes, 42 secondsyou're so so worried that if you if you don't win, if you don't like take that last train out like you're going to be screwed. And I just it doesn't seem
1:17:511 hour, 17 minutes, 51 secondsright to me. And I think it seems like a very hollow way of leading life. So I would encourage people to to zoom out and and not think about it that way.
1:17:591 hour, 17 minutes, 59 secondsRead history. Read computer science history. Maybe it's easy to hear that and feel like, okay, I'll be all right.
1:18:041 hour, 18 minutes, 4 secondsI'm just going to work on things that I'm excited about and and then like,
1:18:081 hour, 18 minutes, 8 secondsokay, but how will I actually have a job in the future? I love the sentiment like don't be so stressed about missing out on things and being in the permanent
1:18:161 hour, 18 minutes, 16 secondsunderclass. anything there that you think is important for people to do while not being overly stressed and worried about missing that train?
1:18:241 hour, 18 minutes, 24 secondsI think I don't think I don't I don't know if it's Chris Rock, but like there's a comedian that has this joke that is like it's great to follow your passion and then he has this pause and
1:18:321 hour, 18 minutes, 32 secondslike if it pays u and so obviously there is a little bit to that. I'm not suggesting that um you don't worry about
1:18:401 hour, 18 minutes, 40 secondsthis uh at all. I think it's more that just tune down the amplitude of how much worry there is and then just sort of
1:18:481 hour, 18 minutes, 48 secondsrealizing that history repeats itself more so than it is completely novel and new. Uh and then of course yeah if you tie it to agency and if you're not so
1:18:561 hour, 18 minutes, 56 secondsstuck in oh I need certainty of how the world is going to unfold you're probably going to be fine. And in the extreme this is the other side of things which
1:19:041 hour, 19 minutes, 4 secondsis often if I then talk to people who are like yeah but you know everything's going to change like okay great. So, how is a move that you are going to make
1:19:131 hour, 19 minutes, 13 secondsreally going to shield you from it? And do you want to live in a society where all of this like I don't know like it just seems so insular that mindset. With
Chapter 29: Lightning round and final thoughts
1:19:221 hour, 19 minutes, 22 secondsthat, we have reached our very exciting lightning round. I've got five questions for you. Are you ready? Uh, sure.
1:19:301 hour, 19 minutes, 30 secondsWhat are two or three books that you find yourself recommending most to other people?
1:19:341 hour, 19 minutes, 34 secondsIt depends on the person. Uh I would say so code
1:19:421 hour, 19 minutes, 42 secondsuh by uh Charles Pzled which is uh the secret language of hardware and software. It basically it's like do you
1:19:491 hour, 19 minutes, 49 secondsknow how computers actually work? Uh it is actually surprising to me how many professionally employed programmers don't know how computers work. Um that
1:19:571 hour, 19 minutes, 57 secondsone the funny thing is it does not have a line of code in it until like chapter 27. Uh so exceptionally good book. Um I
1:20:061 hour, 20 minutes, 6 secondshave a weird one uh which is tools of conviviiality by Ivan Illich. It's sort
1:20:121 hour, 20 minutes, 12 secondsof the contrast between like you look at the history of technology and tools that let users exercise human ingenuity and
1:20:221 hour, 20 minutes, 22 secondsautonomy versus tools that are more at industrial scale that almost um uh have become destructive to to human autonomy.
1:20:301 hour, 20 minutes, 30 secondsUh and then the last one that I give mostly to executives uh that I think are creating a lot of systems uh is uh
1:20:391 hour, 20 minutes, 39 secondsseeing like a state uh which I think there is a famous stack overflow that sort of um popularized this but it's the
1:20:481 hour, 20 minutes, 48 secondsidea of are you actually just designing a system so that you have legibility but the system the way that you've created
1:20:551 hour, 20 minutes, 55 secondsthat legibility completely neglects the reality of the system on the And so I think of it as great you you're the
1:21:031 hour, 21 minutes, 3 secondsexecutive and you have these status reports and you think you know exactly how your teams work. If you actually spend time with the teams you would realize that none of that is actually
1:21:111 hour, 21 minutes, 11 secondstrue. And so I think for for like executives love creating fake legibility for themselves because we don't like
1:21:181 hour, 21 minutes, 18 secondsnoise as humans right we want the signal but there's often less signal in it than you than than one might think. So favorite recent movie or TV show that
1:21:261 hour, 21 minutes, 26 secondsyou have recently enjoyed? Uh, I have purposeful terrible taste in movies,
1:21:321 hour, 21 minutes, 32 secondswhich is I want to watch movies that I never think about again after watching them. Um, and I just want to be entertained and I mostly just want to see things that I couldn't remotely
1:21:401 hour, 21 minutes, 40 secondsexperience in in real life. So, you should not ask me for for movie recommendations. I did like uh uh
1:21:471 hour, 21 minutes, 47 secondsProject Hail Mary uh a lot. I liked the book and I think the adaptation was was was really good. I think it also makes me super excited about any kind of
1:21:561 hour, 21 minutes, 56 secondsfuture of humanity which is I sometimes joke to uh our teams internally which is like okay if we're really really good at some point in notion OS will be the
1:22:051 hour, 22 minutes, 5 secondsthing that empowers like five to to to eight people like explore the galaxy somehow and everything will be organized for them in notion. I don't know like I
1:22:121 hour, 22 minutes, 12 secondslike this idea of of sort of pushing into space. Uh TV show I'm late to this
1:22:191 hour, 22 minutes, 19 secondsthe Handmaid's Tale. If you replace the concept of God with AI in that TV show
1:22:271 hour, 22 minutes, 27 secondsand then you don't actually have to squint that far to replace ice with ice in that TV show right now. It becomes a
1:22:341 hour, 22 minutes, 34 secondsvery um uh I don't know a heavy show to watch in a good way.
1:22:401 hour, 22 minutes, 40 secondsWow. I had not thought about that. Uh under his eye. Was that one of the things? Yeah. Under his AI.
1:22:491 hour, 22 minutes, 49 secondsWhoa. Oh, no. Okay. I'm afraid I used to watch it. I'm more afraid to watch it now. Okay. Uh, favorite product you've
1:22:581 hour, 22 minutes, 58 secondsrecently discovered that you really love. I know you put together a list of beautiful products that that people buy.
1:23:031 hour, 23 minutes, 3 secondsUh, what's something recent? Well, that list that I put together was for products that I think people should buy,
1:23:101 hour, 23 minutes, 10 secondsI think, or that I thought I actually did the taste emulation. I'm like, "Oh,
1:23:141 hour, 23 minutes, 14 secondsI think a lot of people are going to find this useful." Uh I have weird ones now for you which is Yes.
1:23:201 hour, 23 minutes, 20 secondsUh okay so this is not a you can just it's a product it's great. It's Ghosty terminal emulator. Like most people use terrible terminals. Don't do that to
1:23:281 hour, 23 minutes, 28 secondsyourself. Just use Ghosty. Huge fan of the work that uh Mitchell is doing. Uh and then there is a new one for the
1:23:351 hour, 23 minutes, 35 secondsphone called Moshi. M O S HI. That one's not free but it looks very well done.
1:23:411 hour, 23 minutes, 41 secondsI'm like currently exploring it. I mostly code on the phone now um because I don't have a real job. Uh there is an
1:23:481 hour, 23 minutes, 48 secondsopen source keyboard called uh I don't even know how to say it. Corny. C O R N E which is a split keyboard. It looks
1:23:551 hour, 23 minutes, 55 secondsvery weird. The reason I like that one is I'm trying to claw back as much agency in my compute life as possible.
1:24:021 hour, 24 minutes, 2 secondsThis one is very open source. If you really wanted to, you could like download all the schematics, send them off to China, and you have the PCB back and like you can just build it from
1:24:091 hour, 24 minutes, 9 secondsscratch. Um and then this one's silly, but uh I like tools. I like physical tools. A Cevivi pocket knife, uh, which is pretty high quality,
1:24:201 hour, 24 minutes, 20 secondsmaybe more expensive than what most people would spend on a pocket knife,
1:24:231 hour, 24 minutes, 23 secondsbut I think a good pocket knife is is is a good tool to have.
1:24:261 hour, 24 minutes, 26 secondsThese are awesome. Very, very legit products. Okay, we'll link to them all.
1:24:301 hour, 24 minutes, 30 secondsUh, two more questions. You have favorite life motto that you find yourself coming back to in work or in life?
1:24:351 hour, 24 minutes, 35 secondsIt is very hard to remind yourself of that day-to-day. Uh, but I try to. The universe is change and life is what you make it. Um, I think we love to cling to
1:24:441 hour, 24 minutes, 44 secondscertainty. Uh, and there is no certainty, you know. Um, I could walk out of this room and could be the end of
1:24:511 hour, 24 minutes, 51 secondsmy life and like live in the moment kind of thing. Um, and life is what you make it sort of I think it's a Marcus Aurelius quote I believe. Uh, but
1:24:591 hour, 24 minutes, 59 secondsum, yeah I I And then um, do you really want to know how it's going to end? Like no spoilers just like you know enjoy the ride. Final question. You speak German.
1:25:081 hour, 25 minutes, 8 secondsDo you have a favorite German word? Uh I do uh tuftla which is uh like tinker
1:25:171 hour, 25 minutes, 17 secondsbut it's to me it sounds like it has a less tinker can sometimes be a little bit derogatory and I think with the
1:25:251 hour, 25 minutes, 25 secondsGerman equivalent it's just not uh that harsh and then the other one is uh faba
1:25:321 hour, 25 minutes, 32 secondswhich is the word for user but it puts so much more emphasize on using up a
1:25:401 hour, 25 minutes, 40 secondsLike as in if you think about user is like you're using it but using it up like you've you've you and so then like you think a lot more about the um
1:25:491 hour, 25 minutes, 49 secondsimpermanence slash the wastefulness of products that you might build uh if you use that word.
1:25:541 hour, 25 minutes, 54 secondsI love it. I love that you had quick answers to this question. Max, this was amazing. Thank you so much for doing this. Two final questions. Where can
1:26:021 hour, 26 minutes, 2 secondsfolks find you online if they want to ping you about anything? And how can listeners be useful to you? I am unfortunately on X or Twitter. Um I I
1:26:101 hour, 26 minutes, 10 secondswould like to be less addicted to that thing. Uh max.dev.
1:26:141 hour, 26 minutes, 14 secondsUm is I don't even know if I linked to X, but I'll I'll put it on there for your listeners. How can listeners be
1:26:211 hour, 26 minutes, 21 secondshelpful to me? Go for a walk in whatever city you're in or forest, wherever you want to go. Uh actually, no, it's it's better if it's man-made uh or humanmade.
1:26:331 hour, 26 minutes, 33 secondsUm, and just carefully look at how everything around you is made up by people that are no smarter than you and
1:26:401 hour, 26 minutes, 40 secondsrealize that probably in the span of 6 to9 months, you can for most things around you figure out how to make it from scratch. And therefore, uh, you
1:26:491 hour, 26 minutes, 49 secondshave much more agency than than you think. And so, just exercise that. What a beautiful way to end it. Max, thank you so much for being here.
1:26:561 hour, 26 minutes, 56 secondsThank you for having me.
1:26:581 hour, 26 minutes, 58 secondsHi, everyone. Thank you so much for listening. If you found this valuable,
1:27:021 hour, 27 minutes, 2 secondsyou can subscribe to the show on Apple Podcasts, Spotify, or your favorite podcast app. Also, please consider giving us a rating or leaving a review
1:27:101 hour, 27 minutes, 10 secondsas that really helps other listeners find the podcast. You can find all past episodes or learn more about the show at lennispodcast.com.
1:27:191 hour, 27 minutes, 19 secondsSee you in the next episode.

Sync to video time