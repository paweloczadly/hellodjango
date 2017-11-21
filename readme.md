# hellodjango

![Django](https://www.bet.com/topics/d/django-unchained/_jcr_content/image.custom0x0.dimg/__1369349267451/121412-video-django-unchained-jamie-foxx-2.jpg)

## Usage

Prerequisites:
* Docker
* docker-compose

Run locally:

```
$ cd hellodjango
$ docker-compose up
```

## API

* /hello - lists all users from Cache (or DB if Cache is not available)
* /hello/create/Pawel - creates user Pawel
* /hello/delete/Pawel - delete all users with name Pawel
