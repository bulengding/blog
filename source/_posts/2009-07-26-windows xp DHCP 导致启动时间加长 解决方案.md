---
layout: post
title: "windows xp DHCP 导致启动时间加长 解决方案"
date: 2009-07-26 17:48
tags: 
  - 技巧
categories: 
  - 学生时代
---

    logon.bat: netsh interface ip set address name="本地连接" source=dhcp
    logoff.bat: netsh interface ip set address name="本地连接" source=static
    addr=192.168.0.118 mask=255.255.255.0

gpedit.msc，设置开机启动脚本，试试吧，很管用，如果你也遇到这种烦恼

