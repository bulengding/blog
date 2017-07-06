---
layout: post
title: "GIT使用之版本分支图解析"
date: 2016-09-13 00:00:00 +0000
tags: 
  - GIT
  - 版本分支图
categories:
  - 工程管理
---

  GIT的版本分支图。如下图所示

![](/images/git_branch.png)

1. 不同的颜色表示的是不同的分支。
2. 上下表示时间线。
3. 注意当前选中的是分支合并点，该提交有父节点1，父节点2，
4. 父节点1差异表示跟红色分支的差异，父节点2差异，表示跟合并源分支的差异