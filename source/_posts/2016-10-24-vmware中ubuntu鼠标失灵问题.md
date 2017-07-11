---
layout: post
title: "vmware中ubuntu鼠标失灵问题"
date: 2016-09-13 00:00:00 +0000
tags: 
  - vmware
  - ubuntu
  - 鼠标失灵
categories:
  - 电脑与服务器维护
---

几次遇到vmware里面ubuntu界面卡死的情况，对此系统不熟，
无法诊断，打开 ctrl , f1 的console 发现总是冒出vmmouse的消息，猜测
是不是鼠标卡死，键盘还能用，实验一下果然如此。

执行 sudo apt-get remove xserver-xorg-input-vmmouse， 卸载 vmmouse. 搞定。
