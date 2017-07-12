---
layout: post
title: "在linux下为 git socks5 proxy"
date: 2014-11-09 16:01
tags: 
  - 从csdn导出
  - 项目工程管理
categories: 
  - 项目工程管理
---

1\. sudo apt-get install connect-proxy

  

2\. sudo vim /usr/bin/git-proxy

#!/bin/sh

SOCKS5_PASSWD=connect-proxy -T [IP Address]:[PORT]

  

3\. sudo chmod +x git-proxy

  

4\. git config --global core.proxy "git-proxy"

  

