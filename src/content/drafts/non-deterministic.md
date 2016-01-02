title: Non-deterministic Computing in Python
author: Chris Penner
date: December 4th 2015
tags: programming python
description: Experimenting with non-deterministic computing in Python

I 'm taking a class right now about finite automata. If you're not familiar with the term, it's basically a field that 
studies really stupid machines that take instructions and move from one state to another. Anyways, there's a type of 
this machine that acts "Non-deterministically" which basically means that in cases where the machine is faced with more 
than one valid choice, it takes BOTH. However, the way most computers work these days it's very hard to do two things at
once. We can theorize about a machine that, having taken every possible path through the machine (which in general for n 
different choices produces 2^n paths... which is a lot fo big problems), but until quantum computers become viable for 
consumers, it's tough to compute these sorts of things.

I decided it would be a fun experiment to come up with a way to emulate this behaviour in Python, even if it wouldn't 
be terribly fast, to see not only what nondeterministic programming looks like, but also to see how I could leverage 
metaprogramming in Python to make it as clean to work with as possible.

With the disclaimer that this is definitely experimental, and that things get a little messy, let's dive in!

## Syntax

Any time I approach an interesting programming language problem I like to first think about how I would like the 
solution to look. That is, if I could do almost anything

