Equipment Setup Thoughts Part One
---------------------------------

:title: Equipment Setup Thoughts - Part One
:slug: equipment-setup-thoughts-part-one
:date: 2020-04-03
:tags: astronomy, hardware, engineering
:author: 53° Astro
:status: Published

.. |nbsp| unicode:: 0xA0
  :trim:

.. contents::

Introduction
++++++++++++

.. PELICAN_BEGIN_SUMMARY

Setting up a new telescope is not an easy task. It takes some planning and
thought to get the set up right first time. I have made an attempt to plan out
everything that I will need before getting started. Using a handy copy of Visio
I had lying about I have put together a handful of block level diagrams to help
me out. This process gives me an overview of what is needed to make sure that
the system is complete and that everything has been thought of, as far as
possible. Following is a run through of my plans and my thoughts regarding what
issues they raised.

.. PELICAN_END_SUMMARY

The basic idea has always been that the telescope should be automated as much as
possible. The extent of the automation will that I will be able to put together
an imaging session or two and set it running, all from the comfort of a warm
room, via a remote desktop connection to an on board computer. In this case I
consider an imaging session to be: target (re)acquisition, focus, capture a set
of lights via a combination of filters, occasionally re-focus depending on
temperature variation, take care of meridian flips if necessary, and finally
shut down when the session is complete.

For the (computing) brains behind the operation, a `Raspberry Pi 4`_ has
always been the goal, being that they are small, have reasonably low power
requirements and run on Linux, an operating system I am truly comfortable with.

Block Level Diagrams
++++++++++++++++++++

As can be seen, I started by preparing some block level diagrams to assist in
mapping out the entire telescope set up. The set up has been divided into
multiple blocks based on what the modules are transmitting from block to
block. The imaging train transmits photons between blocks, so that seemed like
a pretty obvious place to start:

Imaging Train
~~~~~~~~~~~~~

So this is how the image capture part of the set up currently looks. The photo
below was taken whilst I was checking the back focus from the Skywatcher field
flattener; it has to be 75 mm from a particular point on the flattener to the
CCD chip surface, give or take a small amount to account for the refractive
index of the filters.

.. image:: https://live.staticflickr.com/65535/49733936051_21ebfacfbc_c.jpg
   :width: 800
   :height: 601
   :scale: 100
   :alt: Imaging train in real life

*Imaging train in real life*

As is apparent in the photo above, I have not yet added the off axis guide
camera (OAG) to the set up. That will happen once I have the main imaging camera
properly focused. From right to left, the image shows the Skywatcher field
flattener, a custom made 15 mm spacer, a Starlight Xpress Loadstar 2 camera
mounted onto an off axis guider assembly, 7 position filter wheel and finally
the Starlight Xpress CCD imaging camera. The interfaces between the rear face of
the field flattener and the front face of the OAG / filter wheel are a male M62
thread and a male T-thread (42 mm) respectively, necessitating a custom made
15 mm spacer beautifully engineered by John at `J-Tech Design`_.

Once everything was together it was time to get drawing. Below is a plan of just
the imaging train as above with the light path show with blue arrows. Not much
in itself, but it makes sense once it is part of the rest of the plan.

.. image:: https://live.staticflickr.com/65535/49733170848_db10b2584c_z.jpg
   :width: 800
   :height: 577
   :scale: 100
   :alt: Block level imaging train plan

*Block level imaging train plan*

Overall Block Plan
~~~~~~~~~~~~~~~~~~~

Next was to try and understand just how many cables will be needed, what type
and what sort of lengths. Also, each piece of the puzzle has different types of
USB connections. Thankfully everything that requires 12 V has the same, centre
positive 5.5 mm by 2.1 mm connectors. That definitely makes life easier!

Additionally, the plan below has helped me to make sense of what was needed for
both power distribution and USB connections. Once everything is laid out, it
starts to become obvious where things are missing, such as: I need to think
about getting a powered USB hub, or, do I have enough USB A to USB B leads?

.. image:: https://live.staticflickr.com/65535/49733715706_a59272f456_c.jpg
   :width: 800
   :height: 560
   :scale: 100
   :alt: Block level physical connections

*Block level physical connections*

The block plan has also made sure that I have not forgotten about getting power
to the Raspberry Pi 4; these latest models are now powered via a USB C
connector. The initial plan for this was a step down converter from 12 V to 5 V
and then somehow butcher a USB-C lead to provide the power to the Pi. Other
options I have considered are, for example, sending a 5 volt supply via the
header pins on the Raspberry Pi circuit board; unfortunately this bypasses some
current protection devices in the process, so probably not the best idea.

USB Connections
~~~~~~~~~~~~~~~

From the overall plan I subsequently extracted the devices with a USB connection
and any associated USB cable. This leads me to my first thought with the USB
layout... I need a powered USB hub, and therefore power to run the hub itself. I
will ideally need to find a hub that will run from a 12 V supply (and in a
really ideal world, having a 5.5 x 2.1 centre positive power feed!) to try and
keep the amount of adaptations down to a minimum.

.. image:: https://live.staticflickr.com/65535/49733170253_b8c821283b_c.jpg
   :width: 800
   :height: 569
   :scale: 100
   :alt: Block level USB connections

*Block level USB connections*

Regarding cables, I am going to need a mix of different types. A number of mini
to mini and mini to USB B cables to connect to the in-built hub on the SX 814 to
provide power and control for the off axis guide camera, the filter wheel and
the focus cube. The in-built hub on the imaging camera will then be connected to
a theoretical standalone powered USB hub, and from there communicate with the
Raspberry Pi. Control of the EQ6R Pro mount will be achieved via a Lynx Astro
USB to EQ direct lead from this standalone hub also.

Thankfully I have a habit of hoarding old cables and connectors that come with
electrical items purchased over the years. This has come in useful as I have
been able to find all the leads as required for the cable layout on the
telescope.

Power and Network
~~~~~~~~~~~~~~~~~

Once I was happy with the USB layout, it was time to turn to looking at the
power and network layer. Again, the plan only has items that require power from
12 V cables and the cable runs themselves.

From the plan, it appears that I am going to need to find a neat way of
distributing 12 volts to a number of different bits of equipment on the
telescope. I have spent quite some time on the astronomy forums researching how
people achieve this. There does not really seem to be a single standard - no
surprises there. Some systems seem to be based on automotive type connectors
with blade fuses and so on, others utilise "Anderson Power Pole" connectors as
used by the Ham Radio community. This is something that definitely needs more
thought.

.. image:: https://live.staticflickr.com/65535/49734039312_c46bc7e2bb_c.jpg
   :width: 800
   :height: 564
   :scale: 100
   :alt: Block level USB connections

*Block level power and network connections*

Some thought needs to be put towards handling dew that will no doubt build up on
the objective lens on the telescope. Currently, I have a home built dew
prevention system that requires a 12 volt supply (not a problem then) but it is
very bulky; finding some space to mount it might be quite tricky.

The gold standard (perfect) solution for all this would be a combined USB hub
and 12 V power supply complete with a dew heater controller system. I wonder if
such a thing exists?

.. links

.. _`J-Tech Design`: https://j-techdesign.com/
.. _`Raspberry Pi 4`: https://www.raspberrypi.org/products/raspberry-pi-4-model-b/
