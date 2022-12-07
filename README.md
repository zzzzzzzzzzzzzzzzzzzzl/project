
My biggest weakness is probably organisation, appologies if this is a jumble.


# idea

Initialy i had the idea of Generating Random 3d meshes, They wouldnt have been creatures, that would be way out of my skillset.I was more thinking of generating
abstract Shapes.  there would have been a random set of rules that would have described the generation of the shapes. but the way of generating them seems kind of boring.

https://www.youtube.com/watch?v=VWivmi9j608, this way of generating "creatures" seems much more exciting to me, so I started thinking of a way where I could implement a genetic algorithom like this.

# project

I started developing an enginge in pygame for this.I could have used a prebuilt engine for this like unity, which would have been a much smarter idea, since I only wanted to create a genetic algorithom for creatures,but I started making one in python ive started about a week ago and its clear to me now that this will be 75% of the work for the project. creating a world for creatures to inhabit.I know that python is not the best when it comes to speed but its the laungauge that im most comfortable with. and if we are clever with how we design the creatures we can probably run this at a resonable speed

for the program the creatures will be made of several classes.I drew a diagram of the class hierachy .
https://github.com/zzzzzzzzzzzzzzzzzzzzl/project/blob/main/creature%20class%20hierachy.png
this was my first time using classes as the main part of one of my programs, before this I didnt really have a deep understanding of them but know I feel much more comfortable using them, before this I would have used a bunch of lists instead, but I could always get away with it because the programs would contain much fewer variables than this one. 

# components of a creature
https://github.com/zzzzzzzzzzzzzzzzzzzzl/project/blob/main/classes.png example of what each class will controll

a point is just a x,y coodernate that exists as the corner of a limb

a hinge is just a point that exists inside of a limb

The limb class will create the limbs of the creature.
these "limbs" will just be regular pollygons and iregular pollygons, each polygon will be made of 1 or for each corner.
and can contain hinges inside them 

the bone class will connect 2 points on a limb. it will always maintain the same distance between the 2 points.

the muscle class will connect 2 points on a limb. It will expand and contract. 

The creature class will contain all of the other classes.

# engine
this is going to be the part that consumes the most amount of time on this project. Its going to be difficult to create a physics engine. I dont really know much about
physics but ive got some ideas of how I want it to function. so far ive made a pendulum which works, If i can make 2 points that are connected by a bone fall with acurate physics Im confident I will be able to complete this project but until I can get that working Im not entirely sure if this is within my skill set.

# velocity 
each point or limb will contain a total velocity variable, Im not sure if i will give it to each point or to each limb, because I know having it on every point might slow down the program, but on every point would make it more acurate so idk. total velocity would then be converted to x,y velocity with a vector for the direction.
i still dont really know exactly how this will work. There will need to be a way to transfer total velocity between points.
# acceloration
gravity will be a constant force accelerating the y velocity. and the limbs being pushed and pulled by each other limbs. there will also be a form of resitance. i think that every frame there will a loss to total velocity.
# weight
I had an idea to give each point a weight of 1 that way we could have total weight of a limb and we could also create differnt points with differnt weight, like light points and heavy points, just an idea though not sure if this is useful. but weight will be a useful idea for distributing velocity 

# genetic agorithom and creature generation
I will need to reasearch different genetic algorithoms.
Figuring out how im going to feed the creature into an algorthom is going to be tricky

at this point this is about everything that ive considerd for this project. 

# python koans 

so I did some of the python koans. some of the early questions where confusing, because of the functions to check if the answers where correct.

I got through them ok once I understood what the functions where that would check the answers.

I gave a link to the source to where I found the explanations on some of the questions though I wasnt very thorough, 
some of the question I left a brief explanation on too.












