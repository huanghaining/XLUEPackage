import sublime, sublime_plugin
import os

MAX_VIEWS = 2000

class CompleteCommand(sublime_plugin.TextCommand):
    """docstring for OpemFolderCommand"""
    def run(self,edit):
        folders = self.view.window().folders()
        for f in folders:
            self.view.insert(edit, 0, f+"\n")
        # self.view.insert(edit, 0, self.view.file_name())
        # other_views = sublime.active_window().views()
        # other_views = {}
        # windows = sublime.windows()
        # self.view.insert(edit, 0, "1\n")
        # for w in windows:
        #     self.view.insert(edit, 0, "2\n")
        #     # other_views.append(w.views())
        #     w_views = w.views()
        #     for v in w_views:
        #         self.view.insert(edit, 0, v.file_name()+"\n")
            # other_views.append(w_views)
        # views =  other_views
        # views = views[0:MAX_VIEWS]
        # for v in views:
        #     self.view.insert(edit, 0, v.file_name()+"\n")
        #     # self.view.insert(edit, 0, v.file_name())
