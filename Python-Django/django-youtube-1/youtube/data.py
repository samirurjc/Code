"""Data to keep between HTTP requests (app state)

* selected: list of selected videos
* selectable: list of selectable videos
"""

selected = []
selectable = []

PAGE = """
<!DOCTYPE html>
<html lang="en">
  <body>
    <h1>Django YouTube (version 1)</h1>
    <h2>Selected</h2>
      <ul>
      {selected}
      </ul>
    <h2>Selectable</h2>
      <ul>
      {selectable}
      </ul>
  </body>
</html>
"""

VIDEO = """
      <li>
        <form action='/' method='post'>
          <a href='{link}'>{title}</a>
          <input type='hidden' name='id' value='{id}'>
          <input type='hidden' name='csrfmiddlewaretoken' value='{token}'>
          <input type='hidden' name='{name}' value='True'> 
          <input type='submit' value='{action}'>
        </form>
      </li>
"""
