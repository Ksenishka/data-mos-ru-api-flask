<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<h1>Welcome to this site!</h1>
<ul>
    {% for row in data %}
    <li>
        <a href="{{ url_for('show_table',
n = loop.index0) }}">
           {{ row['Cells']['Name'] }}
        </a>
    </li>
    {% endfor %}
</ul>
</body>
</html>