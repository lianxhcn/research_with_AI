
## nbstata 插件安装常见问题

### 确认是否已经成功安装 nbstata kernel

在 VScode 终端 (快捷键：`Ctrl + ~`) 执行如下命令：

```bash
jupyter kernelspec list
```

如果看到 `nbstata`，说明已经成功安装，例如：

```bash
PS D:\Github_lianxh> jupyter kernelspec list
Available kernels:
  nbstata    C:\Users\Administrator\AppData\Roaming\jupyter\kernels\nbstata
  python3    C:\Users\Administrator\AppData\Roaming\Python\share\jupyter\kernels\python3
```


### 无法关联？缺少 Stata 许可证文件

请确认你的 Stata 安装目录 (可以在 Stata 中输入 `sysdir` 查看你的安装目录) 下是否包含 `STATA.LIC` 文件。该文件是 Stata 的许可证文件，缺失可能导致无法在 .ipynb 文档中执行 Stata 命令。

如果你目前安装的 Stata 版本中确实了该文件，可以尝试重新安装或安装一个包含有效许可证的版本。

### 错误关联：确保选择 nbstata 作为 kernel

有些用户在安装 `nbstata` 之前，可能还安装了 `stata_kernel` 等插件 (一个比较陈旧的插件)。建议卸载之，或删除所有与 `stata_kernel` 相关的文件夹 (可以使用 [Everything](https://www.voidtools.com/) 软件查找 `Everything` 关键词，然后删除相应的文件夹或文件)。

最终，你在 VScode 中关联 kernel 时，看到的应该是 `nbstata`，而不是 `stata_kernel` 或 `stata`。

VScode 的右上角应该显示如下图标：

![20250803032205](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20250803032205.png)

点击右上角的

![20250803032342](https://fig-lianxh.oss-cn-shenzhen.aliyuncs.com/20250803032342.png)


### 虚拟环境问题



> 以下都是错误的

如果 nbstata 表现异常，比如 nbstata.conf 文件没有别识别，通常都是因为安装了虚拟环境导致的。

到 「C:\Users\Administrator\AppData\Roaming\jupyter\kernels」文件夹下把那些旧的，和 nbstata 相关的文件夹删除掉。仅保留一个 nbstata 的文件夹。
然后重启 Jupyter Notebook 或 Jupyter Lab 即可。

- 另外，可以用 everything 搜索 `nbstata.json`，这些都是缓存文件，但里面可能有些错误设定。将这些文件全部删除，然后重启 VScode 。