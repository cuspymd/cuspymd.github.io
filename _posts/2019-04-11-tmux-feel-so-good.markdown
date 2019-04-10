---
layout: post
title:  "tmux, feel so good"
categories: "tools"
tags: "tmux"
---
[feudal_networks] is a repository that implements the RL research [FeUdal Networks for Hierarchical Reinforcement Learning]. I tried to run it today. But It's too difficult to install module dependancies. It depends on universe and go-vncdriver of Open AI. I felt these modues are tricky to install. After wasting half a day, I gave up. Sad? But I got one thing.

# tmux: terminal multiplexer
Upper repository used the tools [tmux] which I've never heard of before. So I googled it. It is said to be a terminal multiplexer. Terminal Multiplexer? What does it mean? I understood it may be able to run and manage many terminal sessions. But that's not the point for me. Upper repository used tmux as an alternative to 'nohup' command. I wondered if the terminal's session would continue in tmux after logging out it.

So I installed and tested it. The result was amazing. Using tmux, I was able to access the session before I logged in. It is Cool. I once said that I use [pm2] for convenience when I run an RL script. I think I can use tmux instead of pm2. Of course, pm2 is much easier to see the script's logs.

There are many similarities between tmux and pm2. The difference is that pm2 manages the process, but tmux manages the terminal session. It is important and why tmux is so appealing to me. I don't know if tmux will actually help my work, but I'll try it steadily from tomorrow.


[feudal_networks]: https://github.com/dmakian/feudal_networks
[FeUdal Networks for Hierarchical Reinforcement Learning]: https://arxiv.org/abs/1703.01161
[tmux]: https://github.com/tmux/tmux
[pm2]: http://pm2.keymetrics.io/
