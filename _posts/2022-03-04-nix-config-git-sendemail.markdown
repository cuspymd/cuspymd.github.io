---
layout: post
title: "Nixos configuration for git sendemail"
tag: ["nixos", "configuration", "git", "sendemail", "gmail"]
---
It is a configuration to use `git sendemail` with gmail in NixOS.

## configuration.nix
```
...

  home-manager.users.userid = {
    programs.git = {
      enable = true;
      package = pkgs.gitAndTools.gitFull;
      userName  = "Your Name";
      userEmail = "your@gmail.com";
      extraConfig = {
        sendemail = {
          smtpserver = "smtp.gmail.com";
          smtpuser = "your@gmail.com";
          smtpencryption = "tls";
          smtpserverport = 587;
          smtpPass = "yourpassword";
        };
      };
    };
  };
  
...
```
