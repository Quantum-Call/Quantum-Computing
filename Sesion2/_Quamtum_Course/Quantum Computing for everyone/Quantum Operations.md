La computación cuántica nace d ela pregunta de un fenómeno no comprendido.
Es diferente a como los humanos entendemos el computar  o calcular. El computaro clásico está diseñado para esto, y resuelve bien un set de tareas.

La idea es basarse en unas propiedades únicas de estos sistemas cuánticos para poder calcular porblemas que antes eran intraqueables, como el [[Criptografía cuántica]] y las RSA.

Una perspectiva histórica:

Hello! Today, before we dive into quantum operations, I want to give you a little bit of a historical perspective.
it gives you insight into why we're teaching you to code in quantum computing much differently from how one would normally go about learning to code in a classical computing environment.
So let's look at the development of classical computers.
Classical computers were designed to mimic human operations. Calculations, in fact.
So, Pascal invented a calculator. And in World War II, the development was driven by the need to calculate firing tables that would look at the angle, and the distance you needed to fire, and weather conditions so that that we could have accurate firing during the war.
And it was actually other people, like Ada Lovelace, who envisioned other uses for this like composing music.
And it was Grace Hopper who took a step back and said, "Wait these are really hard to program. We should really use a programming language that has some English language features instead of writing all of our programs just so the machine can understand it."
And over decades, these languages have changed and developed so that they're quite easy to understand, especially the ones designed for children learning coding.
Development of quantum computing has been completely different.
This started with scientists observing phenomenon and not knowing what to do with it.
And eventually, there have been many uses. Only one of which is computing.
And so, someone said, "Oh, well, maybe we could harness these for for computation."
And only if we harness these unique features are we going to get something that gives us an advantage over classical computing, because we're looking at a technology that wasn't designed for that.
Right. Quantum computers were never designed to mimic how humans perform tasks.
We already have a technology that does that and does that well for certain tasks, certain tasks that humans do quickly.
And so these are the products of an observation of these unique features that can be harnessed.
And so the only way we're going to win is if we are able to do things that humans can't do quickly, in a way that somehow the quantum properties allow it to be faster.
So in some sense, quantum computing is a hammer in search of a nail.
What are those applications that are both very hard for classical computers, intractable in fact, and also able to be solved on quantum computers?
So really, the differences are at the most basic level and we don't yet have languages that hide those basic level details.
So, to understand how quantum computers perform computation, we really need to start with those basic quantum operations.
And we recognize that this is very different from how people learn to program classical computers today.
But that's how we go about it until someone figures out how to express those operations and features in a way that hides the detail and still retains the ability to get the benefit out of it.
We're stuck with this system and no one has thought exactly how to do that yet successfully.



Existen SDK para manipular algunos circuitos,
Pero aún estamos allí.
Existen proyectos ambiciosos para poder crear lenguajes de programación.



_____________________-

HADAMARD

1.  Hello! Today we're going to talk about the quantum H gate.
2.  It is a probabilistic gate and we'll go into what that means in a moment.  
3.  Now, let's look at how this gate works. We put in a black ball, maybe we get out a white ball.  
4.  We put in a black ball, sometimes we get out a black ball.
5.  So, if we were to give it lots of balls in sequence, lots of black balls, we would end up with the results being half black,  half white.
6.  Which means that 50% of the time when we apply an H gate, we end up with a black ball and half of the times when we apply the H gate we end up with a white ball. That seems very odd.
7.  Okay. Well, likewise, it won't be any surprise to you that if you give it a white ball and apply the H gate, then sometimes you get a white ball out and sometimes you get a black ball.
8.  And by out, I don't mean physically out of it. When we apply an H gate, our result is either a black ball or a white ball.
9.  And just like the black ball, if I were to do this many times then my results: 50% of the time would be white and 50% of the time would be black.
10.  You might be thinking this seems completely random!  
11.  Well, let's look at what happens. The observed outcome from a single gate is, in fact, random.
12.  So, we'll indicate this here. We need something else now, we need a measurement symbol.
13.  So that means that whatever H produces, if I apply H to a white ball and then measure the result, it's either black or white.
14.  But before I measure the result, it can be also either black or white; but I don't know what it is. I don't know the state of it until I measure it.
15.  And this is what all of this has been, we just haven't really talked about the role of measurement and we're actually going to talk about it a lot more in the next video.
16.  But for now, we'll look at the fact that this means that when I measure, I have a 50/50 chance of measuring a black value or a white value.
17.  But the probability itself is predictable -- it's not the case that 70% of the time I get a black ball and 30% of the time I get a white ball. It is 50/50.
18.  Okay, but in a single instance, I have no idea if I'm going to get a black or a white ball -- it could be either one. So we can depict this this way.
19.  Alright, so we're going to explore this H gate a little bit, because it ends up covering a lot of quantum concepts that are important.
20.  So what is going on with these  probabilistic gates? We'll look at some of their odd behavior and how to explain it, and then we need to figure out how to represent this probabilistic output visually in a way that we can have it be inputs and outputs to other gates.
21.  And then in this course, we're also going to start introducing the mathematics so that you can calculate the values and predict what's going to happen, and so we'll need a representation, a mathematical representation, and then we'll need to learn the operations to calculate them.
22.  We won't do this all right now, we'll do this over the course of several videos.
23.  So the first thing we want to ask is, is the H gate truly random and how would we know?
24.  It appears random right now and what I mean by random is that if I looked inside, no matter what I give it, there's a 50% probability that nothing will happen to that and a 50% probability that I will apply a NOT gate to that.
25.  That's what we'll describe as random. And so let's look at whether this is random. 
26.  So, if I had random gates and I gave it a set of black balls or a set of white balls, and I applied two random gates in a row -- what would happen?  
27.  Well, it would all be random, right? Because at the end of the first gate, I would have either something that's black or white and then I would have a 50/50 probability of flipping that back or keeping that value.
28.  And so it would look like once I get one random gate, it doesn't matter how many I apply in a row, the output will always be 50/50 probability of white versus black values measured at the end.
29.  Okay, but let's look at what happens with the H gate.
30.  If I give it a sequence of black balls and I don't just apply one H gate but I apply two in sequence, I actually get back black balls. Every time I measure, I will always get a black ball.
31.  And if I start with a white ball, every time I measure I will get a white ball.
32.  So that means that H is its own inverse. But if it were truly  random, we wouldn't be able to invert it because we wouldn't know if it had been flipped or not.
33.  So there must be something extra going on here. So, although it appears random when I only do one of them, it's not actually random.
34.  And so we need to explore what makes the H gate different from a purely random gate.
35.  Alright so what we know is that after two gates it's different from a random gate.  
36.  We also know that there's some state in the middle of those H gates that we haven't depicted, because measurement is not the same as the state.
37.  So, after an H gate but before measurement, the ball can't be just simply black or white -- it needs to be something more complex after an H gate.
38.  So what we need first is a visual representation and so we're going to represent it this way.  
39.  It turns out that an H gate we know has a 50/50 probability of measuring black or white.
40.  So this is something we've already observed and so we know  this to be true, so we're going to depict it this way -- with a rounded box, rounded rectangle, with black and white, which means equal probability of black and white.
41.  No matter how many things I have in this block, it means that they're equal probability of each of them.
42.  So, because there are two of them that means it's a 50/50 probability of the black or the white.
43.  But what you'll notice down here is that when the black ball gets applied the H gate there's a negative sign in front of that black ball.
44.  And this is indicating that even though the H gate had a probability of measuring black or white, the negative sign does not affect the probability of measuring black and white.
45.  It means there was something we were missing about the state; somehow, the state reflected the fact that the black ball had produced it versus the white ball produced it and so we're going to use the negative sign. In quantum, that actually has a physical property which is called phase.
46.  And so we'll get into that later, but right now what we need to know is that this is how we'll depict the output from an H gate. And we'll see how doing that allows us to calculate and actually figure out, “oh yes, it should go back to its original state if we apply the inverse.”
47.  So, what we've figured out is that in the H gate, the states are not identical between the black and the white, but they are 50/50 probability of being measured a black or white.
48.  And what we know: that for random, it's also 50/50 probability of measuring black or white. But even when we go through the random again, it ends up with a 50/50 probability of black or white.
49.  So that's what's different in our observations. We'll have to see mathematically what that would mean.