Simple code for a slot machine game
===================================

:date: 2015-05-18
:author: Anne Jones


Basic knowledge in PHP is extremely useful for a computer
programmer. PHP is easy to understand and widely used by computer
programmers around the world. There are `plenty of tutorials on the
web`__ that you can check out in order to have basic knowledge of PHP
and if you’re interested in creating a very simple game using this
language, this article is for you.

Slot machines are one of the oldest and most popular games around the
world. According to figures, slot machine revenue in Macau – the new
mecca of gaming – reached `more than $1.70 billion last year`__, and
is predicted to become a $3 billion industry by the end of 2015.

Being in a lucrative business means cutthroat competition, which is
why a lot of casino providers today upgrade their services in order to
have the upper hand against competitors. Entertainment hub `Spin
Genie`__, along with the biggest gaming providers in the UK, are now
using HTML5 in order to be able to easily port and publish games on
many platforms. If you’re new to coding, use the code below as a
stepping-stone in furthering your programming knowledge.

Making a three-reeled slot machine game using PHP
-------------------------------------------------

The code we're going to use is from IBM's Developer Works page. If you
want to learn how to make other games apart from slot machines, you
can go on ahead and click `this link`__.

Let's begin. First, we must establish the user interface of the game:

.. sourcecode:: php

     $faces = array ('Figure1', 'Figure2', 'Figure3', 'Figure4', 'Figure5', 'Figure6');

You can substitute any image you want for the figures: fruits, flags,
your favorite cartoon hero, anything.  Then, you will have to declare
the combinations of winning reels. In a traditional slot machine, 3
images must match a payout line, so write the code like this:

.. sourcecode:: php

     $payouts = array (
         'Figure1|Figure1|Figure' => '10',
         'Figure2| Figure2|Figure2' => '20',
         'Figure3|Figure3|Figure3' => '25',
         'Figure4|Figure4|Figure4' => '35',
         'Figure5|Figure5|Figure5' => '50',
         'Figure6|Figure6|Figure6' => '200',
     );

     if (isset($payouts[$result1.'|'.$result2.'|'.$result3])) {
         // give the payout
     }

Let's make the reels spin like a real slot machine. Traditional slots
usually have the first and third reels spin in one direction, while
the second reel spins in the other.

.. sourcecode:: php

     $wheel1 = array();
     foreach ($faces as $face) {
         $wheel1[] = $face;
     }
     $wheel2 = array_reverse($wheel1);
     $wheel3 = $wheel1;

Done! With this, you will be able to create a game that has all the
elements (reel images, moving reels, and payout lines) of a classic
Vegas slot machine.

*This is a guest post*



__ http://www.homeandlearn.co.uk/php/php.html
__ http://www.macauhub.com.mo/en/2014/01/16/macau%E2%80%99s-gaming-and-gambling-revenues-total-us45-233-billion-in-2013
__ https://www.spingenie.com
__ http://www.ibm.com/developerworks/library/os-php-gamescripts3
