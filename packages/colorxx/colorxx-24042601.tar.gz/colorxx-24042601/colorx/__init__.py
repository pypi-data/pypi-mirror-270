__version__ = "24042601"
__author_email__ ="xiaotech@163.com"
__author__ = "xiaotech"
__release_name__ = "colorxx"
__url__ = "https://github.com/xiaotech/colorx"

class Style:
    def __init__(self,msg:str,fore:str="white",back:str="black",style:str="default"):
        self.__fore_colors = {
            "black": 30,
            "red": 31,
            "green": 32,
            "yellow": 33,
            "blue": 34,
            "purple": 35,
            "turquoise": 36,
            "white": 37,
        }
        self.__back_colors = {
            "black": 40,
            "red": 41,
            "green": 42,
            "yellow": 43,
            "blue": 44,
            "purple": 45,
            "turquoise": 46,
            "white": 47,
        }
        self.__styles = {
            "default": 0,
            "bold": 1,
            "underline": 4,
            "blink": 5,
            "reverse": 7,
            "hidder": 8,
        }
        colors = ["black","red","green","yellow","purple","turquoise","white"]
        styles = ["default","bold","underline","blink","reverse","hidder"]
        assert fore in colors,f'fore must be {colors}'
        assert back in colors,f'back must be {colors}'
        assert style in styles,f'style must be {styles}'
        self.fore = self.__fore_colors.get(fore.lower(),37)
        self.back = self.__back_colors.get(back.lower(),40)
        self.style = self.__styles.get(style.lower(),0)
        self.msg = f"\033[{self.style};{self.fore};{self.back}m{msg}\033[0m"

    def __str__(self) -> str:
        return self.msg