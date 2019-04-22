---
layout: post
title:  "Change heap size in neo4j docker image"
categories: "database"
tags: ["neo4j", "docker"]
---
I am running neo4j using docker image. An Java heap memory error occurred. I checked default heap size is 512m.
So I googled how to change heap size setting in neo4j docker image.

[Neo4j Docker Configuration](https://neo4j.com/docs/operations-manual/current/docker/configuration/#docker-environment-variables)

The first and simplest way is to use environment variable. However, it should be noted that name of the variable changes according to the following rules.

- Prefix with `NEO4J_`.
- Underscores must be written twice: `_` is written as `__`.
- Periods are converted to underscores: `.` is written as `_`.

Especially the second rule. I wasted my time not knowing this. For example, ```dbms.memory.heap.max_size``` is should be ```NEO4J_dbms_memory_heap_max__size```.

Below is my neo4j docker run command applied custom java heap memory setting
```
docker run \
    --detach \
    --publish 7474:7474 --publish 7687:7687 \
    --volume $HOME/neo4j/data:/data \
    --env NEO4J_dbms_memory_pagecache_size=16G \
    --env NEO4J_dbms_memory_heap_max__size=16G \
    --env NEO4J_dbms_memory_heap_initial__size=16G \
    neo4j
```
