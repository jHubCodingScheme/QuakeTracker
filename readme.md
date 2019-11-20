# QuakeTracker

A small application to allow you to see earthquakes, their strength, and how they relate to your AOR.

## Deployment

[![asciicast](https://asciinema.org/a/TMFe9MR4cmN4CVizTC6T2LX8s.svg)](https://asciinema.org/a/TMFe9MR4cmN4CVizTC6T2LX8s)

Connect to the docker host and download a copy of the project
```shell
pollux: ~ ⌚ 14:11:17
$ ssh docker
[ec2-user@ip-172-31-13-187 ~]$ cd development
[ec2-user@ip-172-31-13-187 development]$ git clone git@github.com:jHubCodingScheme/QuakeTracker.git
```

Build a docker image and run it as a new container
```shell
[ec2-user@ip-172-31-13-187 development]$ cd QuakeTracker
[ec2-user@ip-172-31-13-187 QuakeTracker]$ ls

# build a new image called "quake", tag it "demonstrator", with the Dockerfile in the current directory
[ec2-user@ip-172-31-13-187 QuakeTracker]$ docker build -t quake:demonstrator .

# Run a container, connect host port 8000 to container port 80, and run it in the background
# Name the new container "quake_demo" and use the quake:demonstrator image.
[ec2-user@ip-172-31-13-187 QuakeTracker]$ docker run --publish 8000:80 --detach --name quake_demo quake:demonstrator
[ec2-user@ip-172-31-13-187 QuakeTracker]$ docker container ls
```

The application is now running - http://docker.pulham.info:8000/

## Configuration

Add the locations and names by lat/long in app/main.py

## Development

1. Create a development environment: `virtualenv -p python3 venv`
2. Enable it and install the dependencies: `. venv/bin/activate`, `pip install -r requirements.txt`
3. Test the current state runs: `FLASK_APP=main flask run`
4. You're good to hack on main.py
5. When you're done, `deactivate` to turn the development environment off again

## Screenshot

![QuakeRep Screenshot](https://i.imgur.com/XdkJVNY.png)
