from django.http import HttpResponse

PAGE = """
<!DOCTYPE html>
<html lang="en">
  <body>
    <p>Countdown!</p>
    <p>Current count: {count}.</p>
  </body>
</html>
"""

count = 5

def index(request):

    global count

    htmlBody = PAGE.format(count=str(count))
    count = (count - 1) % 6
    return HttpResponse(htmlBody)