from tdf_tool.tools.cli.project_cli import ProjectCLI
from tdf_tool.tools.cmd import Cmd
from tdf_tool.tools.config.config import CLIJsonConfig
from tdf_tool.tools.shell_dir import ProjectType, ShellDir
from tdf_tool.tools.vscode.vscode import VsCodeManager


class Module:
    """
    模块相关工具： tl module -h 查看详情
    """

    def __init__(self):
        ShellDir.goInShellDir()
        self.__cli = ProjectCLI()
        self.__vscodeManager = VsCodeManager()

    def init(self):
        """
        项目初始化
        """
        ShellDir.goInShellDir()
        self.__cli.initial()

    def deps(self):
        """
        修改initial_config.json文件后，执行该命令，更新依赖
        """
        ShellDir.goInShellDir()
        projectType = ShellDir.getProjectType()
        if projectType == ProjectType.FLUTTER:
            self.__cli.cliDeps()
        elif projectType == ProjectType.IOS:
            ios_arg = ["bundle", "exec", "pod", "bin", "batch", "clone"]
            Cmd.runAndPrint(ios_arg, shell=False)
    
    def depsUnSync(self):
        """
        修改initial_config.json文件后，执行该命令，更新依赖
        """
        ShellDir.goInShellDir()
        projectType = ShellDir.getProjectType()
        if projectType == ProjectType.FLUTTER:
            self.__cli.depsUnSync()
        elif projectType == ProjectType.IOS:
            ios_arg = ["bundle", "exec", "pod", "bin", "batch", "clone"]
            Cmd.runAndPrint(ios_arg, shell=False)

    def open(self):
        """
        打开vscode，同时将所有模块添加入vscode中
        """
        ShellDir.goInShellDir()
        self.__vscodeManager.openFlutterProject()

    def module_update(self):
        """
        更新存储项目git信息的json文件
        """
        ShellDir.goInShellDir()
        CLIJsonConfig.updateModuleConfig()
