<!DOCTYPE html>
<html>
<head>
   <title>Alô mundo Zumbi</title>
</head>
<body>
<p>
   Bem Vindo {{username}}
<p>
<ul>
%for thing in things:
   <li>{{thing}}</li>
%end
</ul>
</body>
</html>
