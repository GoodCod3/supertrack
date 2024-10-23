from django.forms.utils import ErrorList


class DivErrorList(ErrorList):
    def __str__(self):
        return self.as_divs()

    def as_divs(self):
        if not self:
            return ""
        return f"""
            <div class="p-4 my-4 border border-red-600 border-solid rounded-md bg-red-50">
              <div class="flex">
                <div class="ml-3 text-sm text-red-700">
                      {''.join(['<p>%s</p>' % e for e in self])}
                </div>
              </div>
            </div>
         """