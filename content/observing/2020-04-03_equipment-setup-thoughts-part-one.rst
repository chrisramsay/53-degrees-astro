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
============

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

Block Level Diagrams
====================

As can be seen, I started by preparing some block level diagrams to assist in
thinking out the entire telescope set up. The system was divided into multiple
systems and blocks divided on what the modules are transmitting from block to
block. The imaging train transmits photons between blocks, so that seemed like
a pretty obvious place to start:

Imaging Train
+++++++++++++

So this is how the set up currently looks. The photo below was taken whilst I
was checking the back focus from the Skywatcher field flattener; it has to be
75 mm from the flattener to the CCD chip surface, give or take a small amount to
account for the refractive index of the filters.

.. image:: https://live.staticflickr.com/65535/49733936051_21ebfacfbc_c.jpg
   :width: 800
   :height: 601
   :scale: 100
   :alt: Block level imaging train in real life

*Block level imaging train in real life*

As is apparent in the photo above, I'd not yet added the off axis guide camera
(OAG) to the set up yet. That will happen once I have the main imaging camera
properly focused. From right to left, the image shows the Skywatcher field
flattener, a custom made 15 mm spacer, a Starlight Xpress off axis guider and
7 position filter wheel, and finally, the Starlight Xpress CCD imaging camera.
The interfaces between the rear face of the field flattener and the front face of
the OAG / filter wheel are male M62 thread and male T-thread (42 mm)
respectively, necessitating a custom made spacer beautifully created by John
at `JTech Design`_.

Once everything was together it was time to get drawing. Below is a plan of just
the imaging train as above with the light path show with blue arrows. Not much
in itself, but makes sense once it's part of the rest of the plan.

.. image:: https://live.staticflickr.com/65535/49733170848_db10b2584c_z.jpg
   :width: 800
   :height: 577
   :scale: 100
   :alt: Block level imaging train plan

*Block level imaging train plan*

Overall Block Plan
+++++++++++++++++++

Next was to try and understand just how many cables would be needed, what type
and what sort of lengths. Also, each piece of the puzzle has different types of
USB connections. Thankfully everything that requires 12 V has the same, centre
positive 5.5 mm by 2.1 mm connectors. That definitely made life easier!

Additionally, the plan below helped me to make sense of what was needed for both
power distribution and USB connections. Once everything is laid out, it starts
to become obvious where things are missing, such as: I need to think about
getting a powered USB hub, or, do I have enough USB A to USB B leads?

.. image:: https://live.staticflickr.com/65535/49733715706_a59272f456_c.jpg
   :width: 800
   :height: 560
   :scale: 100
   :alt: Block level physical connections

*Block level physical connections*

The block plan also made sure that I did not forget about getting power to the
Raspberry Pi 4; these latest models are now powered via a USB C connector.

USB Connections
+++++++++++++++

From the overall plan I subsequently extracted the devices with a USB connection
and any associated USB cable.

.. image:: https://live.staticflickr.com/65535/49733170253_b8c821283b_c.jpg
   :width: 800
   :height: 569
   :scale: 100
   :alt: Block level USB connections

*Block level USB connections*

Power and Network
+++++++++++++++++

Power and network mapped out next

.. image:: https://live.staticflickr.com/65535/49734039312_c46bc7e2bb_c.jpg
   :width: 800
   :height: 564
   :scale: 100
   :alt: Block level USB connections

*Block level power and network connections*
