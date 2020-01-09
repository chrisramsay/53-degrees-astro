# 53-degrees-astro
53-degrees-astro Content

## Directories

Config file
`/media/data_1/web/sites/53-degrees-astro/pelicanconf.py`

Site itself
`/media/data_1/web/sites/53-degrees-astro/`

Content directory
`/media/data_1/web/sites/53-degrees-astro/content/`

Output directory
`/media/data_1/web/sites/53-degrees-astro/output/`

Theme directory (git repo), (chosen theme)
`/media/data_1/web/pelican-themes/my-chosen-theme`

Plugins directory (git repo)
`/media/data_1/web/pelican-plugins/`

## Command

```
docker run \
    --rm \
    --user $(UID):$(GID) \
    --volume /media/data_1/web/sites/53-degrees-astro:/site \
    --volume /media/data_1/web/sites/53-degrees-astro/content:/input \
    --volume /media/data_1/web/sites/53-degrees-astro/output:/output \
    --volume /media/data_1/web/pelican-themes/my-chosen-theme:/theme \
    --volume /media/data_1/web/pelican-plugins:/plugins \
    vorakl/alpine-pelican \
        pelican /input -o /output -t /theme -s /site/pelicanconf.py
```

There!        
