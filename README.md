# 53-degrees-astro
53-degrees-astro Content

## Directories

Config file
`/volume/sites/53-degrees-astro/pelicanconf.py`

Site itself - mounted to `/site` in container
`/volume/sites/53-degrees-astro/build/`

Content directory - mounted to `/content` in container
`/volume/sites/53-degrees-astro/content/`

Output directory mounted to `/output` in container
`/volume/sites/53-degrees-astro/output/`

Theme directory (git repo), (chosen theme)- mounted to `/theme` in container
`/volume/pelican-themes/chosen-theme/`

Plugins directory (git repo) - mounted to `/plugins` in container
`/volume/pelican-plugins/`

## Command

```
BASE=/volume
sudo docker run \
    --rm \
    --volume ${BASE}/sites/53-degrees-astro/build:/site \
    --volume ${BASE}/sites/53-degrees-astro/content:/content \
    --volume ${BASE}/sites/53-degrees-astro/output:/output \
    --volume ${BASE}/pelican-themes/chosen-theme:/theme \
    --volume ${BASE}/pelican-plugins:/plugins \
    chrisramsay/alpine-pelican \
        pelican /content -o /output -t /theme -s /site/pelicanconf.py
```

There!        
