import sublime, sublime_plugin
import os

class OpenfolderCommand(sublime_plugin.TextCommand):
    """docstring for OpemFolderCommand"""
    def run(self,edit):
        currentfilename = self.view.file_name()
        os.system("explorer.exe /select ,%s" % currentfilename)




class CommentselCommand(sublime_plugin.TextCommand):
    def run(self,edit):
        currentfilename = self.view.file_name()
        fname, fextension=os.path.splitext(currentfilename)
        if fextension ==".xml":
            for region in self.view.sel():
                begin = region.begin()
                end = region.end()
                self.view.insert(edit,end,"-->")
                self.view.insert(edit,begin,"<!--")
        elif fextension == ".lua":
            for region in self.view.sel():
                lines = self.view.lines(region)
                lines.reverse()
                for lineregion in lines:
                    begin = lineregion.begin()
                    index = self.FindLineBegin(lineregion)
                    begin = index + begin
                    if begin > -1:
                        self.view.insert(edit,begin,"--")

    def FindLineBegin(self,region):
        lineStr = self.view.substr(region)
        index = -1
        for c in lineStr:
            csub = str(c)
            if not csub.isspace():
                index = lineStr.index(c)
                break
        return index


class UncommentselCommand(sublime_plugin.TextCommand):
    def run(self,edit):
        currentfilename = self.view.file_name()
        fname, fextension=os.path.splitext(currentfilename)
        if fextension ==".xml":
            for region in self.view.sel():
                beginRegion = sublime.Region(region.begin(),region.begin() + 4)
                endRegion = sublime.Region(region.end() - 3,region.end())
                blabel = self.view.substr(beginRegion)
                elabel = self.view.substr(endRegion)
                if elabel == "-->":
                    self.view.erase(edit,endRegion)
                if blabel == "<!--":
                    self.view.erase(edit,beginRegion)


        elif fextension == ".lua":
            for region in self.view.sel():
                lines = self.view.lines(region)
                lines.reverse()
                for lineregion in lines:
                    begin = lineregion.begin()
                    lineStr = self.view.substr(lineregion)
                    comRegion = self.FindCommentLabel(lineregion,edit)


                    if comRegion:
                        self.view.erase(edit,comRegion)

    def FindCommentLabel(self,region,edit):
        lineStr = self.view.substr(region)
        index = -1
        for c in lineStr:
            csub = str(c)
            if not csub.isspace():
                index = lineStr.index(c)
                break
        comRegion = sublime.Region(region.begin() + index,region.begin() + index+2)
        label = self.view.substr(comRegion)
        if label == "--":
            return comRegion
        return None


class OpenfileCommand(sublime_plugin.TextCommand):
    """xml与lua之间切换"""
    def run(self, edit):
        currentfilename = self.view.file_name()
        fname, fextension=os.path.splitext(currentfilename)
        if fextension ==".xml":
            luafilename = currentfilename + '.lua'
            if os.path.exists(luafilename):
                self.view.window().open_file(luafilename)
        elif fextension == ".lua":
            xmlfilename = fname
            if os.path.exists(xmlfilename):
                self.view.window().open_file(xmlfilename)





