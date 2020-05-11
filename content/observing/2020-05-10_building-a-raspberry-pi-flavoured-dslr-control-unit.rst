Building a Raspberry Pi Flavoured DSLR Control Unit
---------------------------------------------------

:title: Building a Raspberry Pi Flavoured DSLR Control Unit
:slug: building-a-raspberry-pi-flavoured-dslr-control-unit
:date: 2020-05-10
:tags: astronomy, astrophotograpy, observing, equipment, raspberrypi
:author: 53° Astro
:status: Published

.. |nbsp| unicode:: 0xA0
  :trim:

.. contents::

Introduction
++++++++++++

.. PELICAN_BEGIN_SUMMARY

As well as the telescope pier I like to have a DSLR (an astro-modified Canon EOS
450D) on a Skywatcher Star Adventurer mount around in the garden. It makes for a
nice little mobile arrangement that can be set up at a moment's notice. Usually
the set up consists of the camera, a lens warmer, power for the mount and an
intervalometer for controlling the timing of pictures being captured.

Having really enjoyed setting up a `Raspberry Pi 4`_ running `KStars`_, `EKOS`_
and `INDI`_ for the pier based telescope I thought that putting a 'one stop'
solution together, able to do the same as the above plus a few extras, for the
DSLR would be a great little side project.

.. PELICAN_END_SUMMARY

There are a few little limitations that I like to be able to overcome with the
current DSLR set up.

Battery life on the DSLR is pretty short usually, and getting shorter as the
battery ages. I am currently getting about three to three and a half hours. To
do longer star trails and so on, ideally I would like that limitation to go
altogether.

The mount and heater are powered with a portable battery, and again diminishing
battery life proves to be a bit of an issue.

Lastly, a minor point; messing about with SD cards or plugging the camera into
a laptop to get the images. It would be nice to be able to do that remotely
without wires or carrying cards about.

Requirements
++++++++++++

I decided that the the control box would have to be able to complete the
following requirements:

- Provide power for the DSLR, lens warmer and Skywatcher mount
- Download image data from the DSLR to local storage
- Be able to send data over my local network (WiFi or ethernet) via a shared
  drive or something similar
- Be powered from a 12 V power supply
- Perform the above tasks reliably and ideally in a single package

With the above in mind I built up a list of things that would have to be
purchased to start the project, namely:

- Raspberry Pi Model 4B
- 32 Gig SD Card
- IP66 Project Box
- 1 x short USB C lead (Pi power supply)
- 2 x Mini USB leads
- 1 x USB to 7.1 V Canon power pack
- 1 x 5 V / 5 A 4 port USB power supply, stepping down from 12 V + (sold in
  pairs)
- 5 V 40mm cooling fan

Construction
++++++++++++

Use of sending power down 4 redundant lines in Ethernet.

LED for power and activity - no, go for a simple acrylic light pipe arrangement.

.. raw:: html

    <a data-flickr-embed="true" href="https://www.flickr.com/photos/53-degrees-astro/49881847736/in/dateposted-public/" title="astropi-dslr_closeup"><img src="https://live.staticflickr.com/65535/49881847736_18682eacf1_c.jpg" width="800" height="533" alt="astropi-dslr_closeup"></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>

*The control unit boxed up and tested*

Testing
+++++++

Network issues where the Pi won't connect. Aha, /boot/

.. code-block:: bash

    sudo ethtool -s eth0 speed 100 duplex full autoneg off

So it goes awry here when I start to connect all the bits. Low voltage causing
the Pi to reset.

Result
++++++

Here it is

.. raw:: html

    <a data-flickr-embed="true" href="https://www.flickr.com/photos/53-degrees-astro/49881847716/in/dateposted-public/" title="astropi-dslr_outside-setup"><img src="https://live.staticflickr.com/65535/49881847716_3edb7ee208_c.jpg" width="533" height="800" alt="astropi-dslr_outside-setup"></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>

*Up and running in the garden*


.. links

.. _`Raspberry Pi 4`: https://www.raspberrypi.org/products/raspberry-pi-4-model-b/
.. _`KStars`: https://edu.kde.org/kstars/
.. _`EKOS`:  https://www.indilib.org/about/ekos.html
.. _`INDI`: https://indilib.org/
