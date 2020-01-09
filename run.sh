#! /bin/bash

BASE=/media/data_1/web
sudo docker run \
    --rm \
    --volume ${BASE}/sites/53-degrees-astro/build:/site \
    --volume ${BASE}/sites/53-degrees-astro/content:/content \
    --volume ${BASE}/sites/53-degrees-astro/output:/output \
    --volume ${BASE}/pelican-themes/pelican-bootstrap3:/theme \
    --volume ${BASE}/pelican-plugins:/plugins \
    chrisramsay/alpine-pelican \
        pelican /content -o /output -t /theme -s /site/pelicanconf.py
