Title: My Over-Engineered Blogging Setup
Tags: software, tutorial

A while ago, HTTP requests to my website stopped working for some reason. It was an error with my CDN (cloudflare). This, to me, was a sign from the gods that it was time to do something unnecessarily complex to fix the problem.

Seriously though; there were some things I wanted to fix for a long time that I hadn't gotten around to doing. The current CDN issue + a long weekend seemed like the right time to do this.

**tldr**:

- Created a [custom docker image](https://github.com/gDelgado14/personal-site/blob/master/Dockerfile-push) with (sass + python and all the pelican dependancies)
- Dockerized the whole project [using](https://github.com/gDelgado14/personal-site/blob/master/Dockerfile#L1) the aforementioned docker image
- Set up automated deploys (using [CircleCI](https://circleci.com/)) to deploy the blog to [Netlify](https://www.netlify.com/)

### Dependency Hell

There were some things that were bugging me about the way Pelican blogs are set up for local development. The [pelican docs](http://docs.getpelican.com/en/stable/install.html) suggest that you install [Virtualenv](https://virtualenv.pypa.io/en/stable/). That worked fine until I decided I wanted a better developer experience with CSS. I switched over to SASS for my CSS, but that meant that I had to install ruby since it's a ruby gem.

Ok so now I have python, virtualenv and Ruby globally installed just so that I may run the blog locally. This complicates automated deploys as well since you have to install these dependancies to ensure building the blog succeeds.


### Docker to the Rescue

I really do not like having dependancies globally installed. So I figured this would be a fun opportunity to play around with Docker.

I'll spare you all the intermediate versions of my docker setup and get to what you currently see in the repo.

There are three docker-related files: 

- `Dockerfile-push`
- `Dockerfile`
- `docker-compose.yml`

`Dockerfile-push` contains the instructions to create a reusable image (I reuse this image during the CI process. More on this later). This image lives at https://hub.docker.com/r/giorgio14/pelican/  ... The image is fairly large, I know. So what? Sue me.

Now that I have a base image to run pelican and all its dependencies, I can create a new image from it that runs a development server. That's where `Dockerfile` comes in. In it I: 

- Create an image `FROM` my custom giorgio14/pelican image
- `COPY` the relevant files and directories into the image
- Bind my OS's port 8080 onto the container's port 8080
- run a `make` script which runs a live-reloading server on port 8080

There's just one problem. If I were to create a container from this image, the container creates copies of my files, but it doesn't link back to them. In other words; the container has its own copies that are completely unrelated to the ones on my OS. This means that in spite of having a live-reloading server that listens to file changes, no files will actually change within the container.

We need [volumes](https://docs.docker.com/storage/volumes/). This is a mechanism that allows a container to have access to a host OS's files and directories. I use volumes so that I may edit anything inside the `theme` and `content` directories and have those changes propagate to the running docker container. Once the changes occur within the container, then the python server running inside the container can regenerate the blog and serve the updated files.

For this reason, I use the `docker-compose.yml` file. In it, there's a `volumes` key that describes which local directories I want to mount onto the running container.

Now that this is all done, I can simply run:

```
docker-compose up
```

And docker will:

- Pull and generate the required images
- Run `make devserver PORT=8080` (which comes from the `Dockerfile`) inside the container

Now I have a schnazzy dev setup that does not need python, virtualenv, ruby or anything :) ... Only Docker!

### Automated deploys

Now that I have a reusable docker image hosted on hub.docker.com, I can leverage it to make my CI steps super easy.

My goal was for my website to update on every new push to the master branch on my repo. I chose CircleCI for its brand, great documentation (took me less than a day to figure out how to use it), and free pricing 🙃.

I basically just followed the documentation to connect my github repo to circle and had the "[hello world](https://circleci.com/docs/2.0/hello-world/)" pipeline running shortly thereafter.

[Here](https://github.com/gDelgado14/personal-site/tree/master/.circleci) are the relevant files associated with circle. It took me a few tries and tweaks to get the pipeline running as I wanted, so I created a bash script that allowed me to run pipelines without pushing commits to github. [Here](https://circleci.com/docs/2.0/examples/)'s the relevant doc from circle.

I'll mention some high-level points about the `config.yml` file. Note that I use the custom image I made above. No need to install ruby, do apt-get, or anything. It's all just ready to go with the `pelican` cli installed as well.

Since I want to deploy to netlify, I have to install their cli. I chose their current stable cli (repo [here](https://github.com/netlify/netlifyctl)) instead of their node-based one since I was familiar with it already.

Then I generate a production build of the blog using `make publish`. 

For the sake of future debugging I figured I would save the output of the `make publish` command in case something strange ever occurred. Circle's UI allows me to access the zipped directory if I ever need to.

Finally I deploy to netlify.

I've set up a custom domain on netlify by creating a CNAME record that points to the randomly-generated netlify URL. More info here on [netlify](https://www.netlify.com/docs/custom-domains/) custom domains.

### Still to be figured out

I really want to have comments on my website, but I definitely don't want to use Disqus. When I get a chance I'll give [Staticman](https://staticman.net) a shot.

[Staticman + Pelican Tutorial](https://snipcart.com/blog/pelican-blog-tutorial-search-comments)



... and that's it! 
