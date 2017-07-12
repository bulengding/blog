---
layout: post
title: "TortoiseGit, TrotoiseSVN 网络代理设置"
date: 2014-11-03 10:44
tags: 
  - 从csdn导出
  - 项目工程管理
categories: 
  - 项目工程管理
---

#  自己总结： 使用socks5代理的话就加 socks5 的 协议前缀， 比如 socks5://127.0.0.1

  

以下文章转载自: [ http://www.cnblogs.com/over140/archive/2011/09/21/2183325.html
](http://www.cnblogs.com/over140/archive/2011/09/21/2183325.html)

#  

#  [ TortoiseGit设置代理问题
](http://www.cnblogs.com/over140/archive/2011/09/21/2183325.html)

  

** 前言 **

帮朋友下载一个Google Code上的项目，装了一个Git的Windows版客户端TortoiseGit，发现总是连不上，设置hosts文件也很容易中断，
这里把搜到的解决办法分享一下。

声明

欢迎转载，但请保留文章原始出处:)  

博客园：http://www.cnblogs.com

农民伯伯： http://over140.cnblogs.com

** 正文 **

一、错误信息

error: Unknown SSL protocol error in connection to code.google.com:443

二、错误设置代理

右键 -> TortoiseGit -> Settings -> Network

Server address : 127.0.0.1

Port : 1988

三、正确设置代理

右键 -> TortoiseGit -> Settings -> Network

Server address :  http://  127.0.0.1

Port : 1988

四、本文参考讨论帖

[ http://code.google.com/p/tortoisegit/issues/detail?id=137
](http://code.google.com/p/tortoisegit/issues/detail?id=137)

