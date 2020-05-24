#! /bin/bash

sudo rm -rf ${BASE}/sites/53-degrees-astro/publish/*

BASE=${HOME}/web
sudo docker run \
    --rm \
    --volume ${BASE}/sites/53-degrees-astro/build:/site \
    --volume ${BASE}/sites/53-degrees-astro/build/content:/content \
    --volume ${BASE}/sites/53-degrees-astro/publish:/output \
    --volume ${BASE}/themes/pelican-bs-53:/theme \
    --volume ${BASE}/pelican-plugins:/plugins \
    chrisramsay/alpine-pelican \
        pelican -v /content -o /output -t /theme -s /site/configs/publish_conf.py

sudo chown -R raz: ${BASE}/sites/53-degrees-astro/publish
