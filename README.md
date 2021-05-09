####  Git的简单使用方法

1. 在本地新建一个空的文件夹，任意命名

2. 打开终端程序，进入此文件夹目录

3. 在终端运行如下命令

   ```bash
   //创建git仓库
   $ git init 
   ```

   ```bash
   //添加基本信息
   $ git config --global user.email 邮箱 
   ```

   ```bash
   $ git config --global user.name 用户名
   ```

   ```bash
   //创建一个分支，避免直接提交到master
   $ git branch -m 你的分支的名字 e.g. git branch -m liuruixuan 
   ```

   ```bash
   //添加远程仓库
   $ git remote add origin https://github.com/2021-SPM/Forum.git
   ```

   ```bash
   //拉取仓库中master分支的内容
   $ git pull --rebase origin master
   ```

   等待下载完成...

4. 这样在本地就会有一个完整的git仓库了

5. 在本地进行修改之后运行如下命令

   ```bash
   //添加所有修改的文件
   $ git add .
   ```

   ```bash
   //干了点啥
   $ git commit -m "写点注释"
   ```

   ```bash
   //提交到github仓库
   $ git push origin 你的分支的名字
   ```

   完成提交

   

#### Forum - Release 3

##### 更新

1. 新增评论通知，现在可以在首页收到回帖的通知了
2. 增加文章目录
3. 优化页面
4. 支持搜索文章标题、正文和作者




#### Forum - Release 2

##### 更新

1. 首页增加了轮播图片，优化了顶栏按钮
2. 评论区更新
3. 分类目录优化，增加了返回按钮
4. 增加了帖子的阅读量、点赞数和评论数的显示
5. 帖子支持了markdown格式的创作
6. 赋予了管理员更多权限

##### 修复

1. 在首页点击帖子的分类可以正确地显示该分类下的所有帖子
2. 在首页点击帖子的作者可以正确地查看作者资料



#### Forum - Release 1

##### 第一版上线！🎉