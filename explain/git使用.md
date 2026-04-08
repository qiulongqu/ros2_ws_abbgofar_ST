# 如何使用git克隆仓库

## 1\. 初始化 Git 仓库

`cd \~/ros2\_ws\_gazebo`
`git init`

## 2\. 配置 .gitignore 文件

`touch.gitignore`

将以下内容添加到.gitignore 文件中：

`build/`
`install/`
`log/`

这些文件都是编译生成的临时文件和环境缓存，不应该被纳入版本管理。

## 3\. 保存本地仓库

`git status` <!-- # 查看当前仓库状态 -->
`git add .` <!-- # 添加所有文件到暂存区 -->
`git commit -m "Initial commit" `<!-- # 提交本地仓库 -->

## 3.1 更改主分支名称

由于现在 GitHub 默认主分支叫 main，而本地 Git 可能默认叫 master，为了避免以后的麻烦，建议现在就把本地分支重命名为 main：

`git branch -m main`



注意：以上命令是在本地仓库进行的操作，并没有与远程仓库进行交互。

## 4\. 克隆远程仓库

### 第一步，先在github上创建一个空仓库。

### 第二步，在本地仓库中执行以下命令：

`git remote add origin https://github.com/你的用户名/你的新项目名.git`

# 注意：origin 是远程仓库的别名，可以自定义。



### 第三步，执行以下命令：

`git push -u origin master` <!-- # 推送本地仓库到远程仓库 -->

后面只需要在终端输入：`git push` 即可将代码推送到远程仓库。



\# 5. 如何查看git的旧版本和恢复旧版本

\## 5.1 查看版本

使用`git log`可以查看完整的提交历史

使用`git log --oneline`可以查看简短的提交历史

使用`git show <commit-hash>`可以在使用git log找到对应版本的哈希值之后查看该版本的详细信息

使用`git show <commit-hash-1> git show <commit-hash-2>`可以比较两个版本之间的差异

\## 5.2 回退版本

使用`git revert` 它不会修改历史，而是创建一个新的提交来“撤销”更改

使用`git revert HEAD` 撤消最近一次修改

使用`git reset` 直接更改历史，直接删除指定版本之后的所有提交

使用`git checkout` 用于临时查看版本

## 6.如何解决改名冲突

当你更改了本地文件夹的名称，通常不会直接破坏 Git 与 GitHub 远程库的连接。但如果你在 GitHub 网页端 更改了仓库名称，或者在本地进行了某些涉及 .git 配置的改动，就会出现“找不到远程库”的情况。

要解决这个问题，你需要完成两个步骤：同步仓库名称 和 更新远程连接地址。

### 6.1 在 GitHub 网页端改名

如果你还没有在 GitHub 上改名，请先执行这一步：

登录 GitHub，进入你的项目页面。

点击顶部的 Settings（设置）选项卡。

在 Repository name 输入框中输入新名字。

点击 Rename。

### 6.2 更新本地的远程连接 (Remote URL)

因为你改了 GitHub 上的仓库名，旧的 URL 已经失效了。你需要告诉本地 Git 新的地址。

1. 查看当前远程库状态
在本地项目根目录下打开终端，输入：

```bash
git remote -v
```

你会看到类似 origin  https://github.com/用户名/旧项目名.git 的输出。

2. 设置新的远程库地址
使用以下命令将远程地址更新为新名字：

```bash
git remote set-url origin https://github.com/用户名/新项目名.git
```

注意：如果你使用的是 SSH 连接，地址格式应为 git@github.com:用户名/新项目名.git。

3. 测试推送

现在尝试拉取或推送代码以确保连接恢复：

```bash
git pull origin main
# 或者推送
git push -u origin main
```
