from django.forms.widgets import ClearableFileInput


class CustomClearableFileInput(ClearableFileInput):
    allow_multiple_selected = True

    def value_from_datadict(self, data, files, name):
        if self.allow_multiple_selected:
            return files.getlist(name)
        return super().value_from_datadict(data, files, name)
