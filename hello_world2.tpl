<!DOCTYPE html>
<html>
<head>
<title>Alô mundo Zumbi!</title>
</head>
<body>
<p>
  Bem Vindo {{username}}
<p>
<ul>
%for thing in things:
<li>{{thing}}</li>
%end
</ul><p>
<form action="/favorita" method="POST">
Qual é a sua linguagem preferida?
  <input type="text" name="lang" size="40" value=""><br>
  <input type="submit" value="Submit">
</form>
</body>
</html>
