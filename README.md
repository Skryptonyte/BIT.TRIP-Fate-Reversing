# Background

BIT.TRIP FATE is the fifth of the main six installations of the BIT.TRIP series developed by Choice Provisions ( formerly Gaijin games ). It is available on both PC and Wii and runs on their proprietary Atrophy engine. The PC port of the engine internally uses DirectX 9.

# Progress

Very much work in progress. I will probably upload some additional scripts along the way.

# Internal stuff I have found

* Each level is loaded in two separate parts. The level model itself is loaded from an aescn file ( which is basically a 3D model file used by the atrophy engine afaik ), which I speculate has the actual 3D background as well as the "thread" that Commander Video can move in. However the entity spawning positions such as enemies, bosses etc and positioning of certain effects like floating in game text, music transition etc are entirely hardcoded. For this purpose, there are six massive functions each for six respective levels. I will consider these functions to be related to entity data of each level. Entities appaear to spawn at set time lapses which I was partly able to figure this out from the weird behaviour I was observing when I used breakpoints and ended up figuring out that many of the game elements seem to be time based rather than position based.
* Bunch of mundane stuff related to config loading and saving. Nothing too remarkable here.

# Unused stuff
* Lots of leftover resources from the Wii BIT.TRIP collection. You can find a bunch of leftover text related to disc errors, NAND errors etc which aren't used in the PC version for obvious reasons.
* There is in fact an unused level which is not accessible by normal means. I found this when I found a function not associated with any of the six main levels. Moreover, it does not appear to have any assosiated aescn files of its own. The level goes by the name "Rise up". If you have played BIT.TRIP complete, you would know each installation had a bunch of mini challenges alongside the main levels which was not present in the original standalone Wii versions. So essentially, what we have is an inaccessible mini challenge. I was able to access this unused by breakpointing at a switch case area and changing a register to the unused level data. With a debugger, you can shift the control flow so that the entity data of this unused level gets loaded on top of whatever level you select in the menu. I ended up playing Rise up on top of the "DETERMINATION" map which is a somewhat fun sight. You even get to see the somewhat iconic exiting challenge graphic which is again not accessibly by normal means. This may have been used as a test level I suppose.


You can load entity data of another level on top of a selected level, say you want to play the FRUSTRATION enemy layout on top of the DETERMINATION map by making a breakpoint at 0xC7857A in IDA and changing the eax register to a value between 0-6. 0-5 are the entity loading functions of the main levels in order and 6 is for the unused level. Note that this method I am suggesting will not change the level map, only the entities aka where and what enemies spawn, what text appears etc etc so expect to see some crazy stuff! You can actually load the unused level data on any selected level and just cheese a perfect on all 6 levels really.

# TODO
* Reverse AETEX, AESCN, AEMENU, AESHADER files
