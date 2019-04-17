---
layout: post
title:  "Dockerfile of Open AI universe"
categories: "container"
tags: "Dockerfile"
---
Recently I have tried to build a docker file of [Open AI's universe].
I found two interesting things in universe's Dockerfile.

# Cachebusting
{% highlight ruby %}
# Cachebusting
COPY ./setup.py ./
COPY ./tox.ini ./

RUN pip install -e .

# Upload our actual code
COPY . ./
{% endhighlight %}
In Dockerfile, the configuration files of package dependency are copied first.
And Dependent packages are installed, then all source code are copied.
I think it is for docker image layer and it can be applied to my python project as well.

In my project, I copied all source files and installed packages using `pipenv`.
I'm going to modify `Pipfile` and `Pipfile.lock` to copy first. 

[Open AI's universe]: https://github.com/cuspymd/universe

# py3clean
{% highlight ruby %}
# Just in case any python cache files were carried over from
# the source directory, remove them
RUN py3clean .
{% endhighlight %}
In universe Dockerfile, run the command `py3clean` at the end. I've never seen this command before.
It is said to delete python cache files. I compared the file size of docker image with this command or not.
The difference in file size was only 2bytes.

I think this small difference may be because the source codes have never been run at my local PC.
The command `py3clean` is installed for python installation in ubuntu, so it might not be bad to add it to Dockerfile. 
