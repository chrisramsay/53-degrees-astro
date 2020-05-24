#! /bin/bash

BASE=${HOME}/web
sudo docker run \
    --rm \
    --volume ${BASE}/sites/53-degrees-astro.com/build:/site \
    --volume ${BASE}/sites/53-degrees-astro.com/build/content:/content \
    --volume ${BASE}/sites/53-degrees-astro.com/local:/output \
    --volume ${BASE}/themes/pelican-bs-53:/theme \
    --volume ${BASE}/pelican-plugins:/plugins \
    chrisramsay/alpine-pelican:latest \
        pelican /content -o /output -t /theme -s /site/configs/local_conf.py

sudo chown -R raz: ${BASE}/sites/53-degrees-astro.com/local
