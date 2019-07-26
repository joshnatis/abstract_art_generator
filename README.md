# Abstract Art Generator
https://corduroy.trinket.io/sites/random-abstract-art-generator

### What?

As per the description, this is a funky program that generates a multitude of random, colorful shapes. I'm using the term 'abstract art' loosely here, as the 'algorithm' used to generate it is completely random at best. It seems, though, that a lot of generative art (the term used for artful images created with code) follows this pattern.

### When?

I wrote this code many moons ago when I was first experimenting with a programming language that wasn't Java. I forgot about it shortly thereafter, but recently re-discovered it and realized it had somehow stopped working despite the fact that I hadn't touched it since. It turns out that the module I'd used silently changed the arguments accepted for one of its functions -- shame on you, Turtle >:(. Either way, I've now fixed that 'bug' and returned the program to its original glory.

### How?

This code heavily relies upon the Turtle module. "Turtle graphics is a popular way for introducing programming to kids. It was part of the original Logo programming language developed by Wally Feurzig and Seymour Papert in 1966." I know, impressive. The general idea is this: a turtle with colored ink on its tail moves a random distance in a random direction. If the magnitude of its distance exceeds the size of the screen (which I found to be around 165 of some unit, presumably pixels), the turtle crawls back to the center, creating a cool shape or pattern. Additionally, whenever the turtle reaches an edge of the screen, a random collection of letters is printed on the screen at that location. Since each drawn shape is filled with a transparent color, a few minutes of overlaying drawings results in a intricate, cool looking pattern.

### Example output:
![An example: ](https://github.com/joshnatis/abstract_art_generator/raw/master/7.png)
