# Lottery Generator

一个简单的彩票号码生成器，支持大乐透和双色球。

## 使用方法
使用 PyInstaller 打包跨平台可执行文件
以下是如何使用 PyInstaller 为不同平台创建可执行文件的步骤。

1. 安装 PyInstaller
首先，确保安装了 PyInstaller：

bash
复制代码
pip install pyinstaller
2. 编写打包脚本（main.py）
使用你的主代码文件 lottery/main.py。无需额外修改，只需将现有的 Python 脚本准备好打包即可。

3. 使用 PyInstaller 打包
在每个平台上（Windows、macOS、Linux），运行以下命令打包成适合该平台的可执行文件。

```bash
复制代码
pyinstaller --onefile lottery/main.py --name lottery-generator
此命令的参数说明：

--onefile：将所有文件打包成一个独立的可执行文件。
--name：定义生成的可执行文件名称，这里是 lottery-generator。
运行该命令后，PyInstaller 会在项目根目录下创建一个 dist 文件夹，包含生成的可执行文件。
```
4. 为每个平台生成文件
在每个平台上，运行 PyInstaller 来生成相应的文件：

Windows：会生成 lottery-generator.exe
macOS 和 Linux：会生成 lottery-generator（无扩展名）
注意：要在每个平台上生成适合它的文件，需要在相应的平台上运行 PyInstaller。例如，要生成 macOS 的可执行文件，需要在 macOS 上运行此命令。

5. 生成的可执行文件位置
运行完毕后，dist 文件夹中将会包含每个平台相应的可执行文件：

```bash
dist/
└── lottery-generator  # Mac 和 Linux
└── lottery-generator.exe  # Windows
```
6. 可选的优化配置
如果需要图形界面，可以在 PyInstaller 命令中添加 --noconsole 参数，这样在执行时不会弹出控制台窗口：

```bash
pyinstaller --onefile --noconsole lottery/main.py --name lottery-generator
```
## 图形界面
```bash
 pyinstaller --onefile --windowed lottery\lottery_gui.py --name lottery-generator
```