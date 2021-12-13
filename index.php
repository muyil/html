<?php
if(isset($_POST['sent'])){
	$code = escapeshellcmd("sudo python3 /var/www/html/willemdafoe.py");
	$ergebnis = shell_exec($code);
	echo $code;
	echo $ergebnis;
	echo "test";
}

$servername = "localhost";

$user = "root";

$pw = "Samy0110";

$DB = "WillenDafoeDb";

define('DB','Datenbankname');

//Jetzt kommt die "Logik", du nutzt den prozedualen Stil (Versuch mal bei Gelegenheit den objektorientierten)

$con = mysqli_connect($servername,$user,$pw,$DB);

$query = "SELECT * FROM Temperatures ORDER BY id DESC Limit 1";

$res = mysqli_query($con,$query);

$fetch = mysqli_fetch_assoc($res); //Mit $fetch hast du nun ein Array


$query1 = "SELECT * FROM Humidities ORDER BY id DESC Limit 1";

$res1 = mysqli_query($con,$query1);

$fetch1 = mysqli_fetch_assoc($res1);

//Ausgabe von einem Wert mit echo


//Jetzt nutze ich mal dein Assoziatives Array $fetch, beachte die Anführungszeichen und wie sich die Variablen verhalten

//Jetzt das ganze mal umgesetz in HTML in deiner Art

?>
<!<!DOCTYPE html>
<html lang="de">
  <head>
    <meta charset="utf-8">
    <title>LuHeiKo</title>
    <link rel = "stylesheet" type="text/css" href="./bootstrap/css/bootstrap.css">
  </head>
  <body style="background-color: #e3f2fd;">
    <div>
      <h1>Dein LuHeiKo System</h1>
      <nav class="navbar navbar-light" style="background-color: #e3f2fd;">
        <nav class="navbar navbar-expand-lg navbar-light bg-light">
  <div class="container-fluid">
    <div class="collapse navbar-collapse" id="navbarNavDropdown">
      <ul class="navbar-nav">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="index.php">Dashboard</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="temperatur.php">Temperatur Anzeige</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="humidity.php">Luftfeuchtigkeit Anzeige</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="dooracces.php">Türkartensteuerung</a>
        </li>
      </ul>
    </div>
  </div>
</nav>
      </nav>
      <p> Hier findest du alle wichtigen Informationen zu den Gemessenen Werten und du Kannst Türkarten anlegen und Löschen. Außerdem kannst du dir die User Anlegen, die auf deine Daten Zugreifen Dürfen.</p>
    </div>
    <div>
      <h3>Temperatur Aktuell:</h3>
      <table class ="table">
				<tr>
          <th>ID</th>
					<th>Temperatur</th>
					<th>Zeitpunkt</th>
					<th>Beschreibung</th>
			</tr>
			<tr>
				<?php foreach($fetch as $Bezeichnung => $Wert)
        {?>
          <td><?php echo $Wert;?></td>
			<?php } ?>
			</tr>
      </table>
    </div>

    <div>
      <h3>Luftfeuchtigkeit Aktuell:</h3>
			<table class ="table">
				<tr>
					<th>ID</th>
					<th>Luftfeuchtigkeit</th>
					<th>Zeitpunkt</th>
					<th>Beschreibung</th>
			</tr>
			<tr>
				<?php foreach($fetch1 as $Bezeichnung => $Wert)
        {?>
          <td><?php echo $Wert;?></td>
			<?php } ?>
			</tr>
      </table>
			<form method="post" action="index.php">
				<input type="submit" name="sent" value="Messdaten Aktualisieren">
			</form>
    </div>
  </body>
</html>
