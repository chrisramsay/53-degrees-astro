#! /bin/bash

BASE=${HOME}/web
sudo docker run \
    --rm \
    --volume ${BASE}/sites/53-degrees-astro/build:/site \
    --volume ${BASE}/sites/53-degrees-astro/build/content:/content \
    --volume ${BASE}/sites/53-degrees-astro/local:/output \
    --volume ${BASE}/pelican-themes/pelican-bootstrap3:/theme \
    --volume ${BASE}/pelican-plugins:/plugins \
    chrisramsay/alpine-pelican:latest \
        pelican -v /content -o /output -t /theme -s /site/configs/local_conf.py
