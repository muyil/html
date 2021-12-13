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

//Ausgabe von einem Wert mit echo


//Jetzt nutze ich mal dein Assoziatives Array $fetch, beachte die Anführungszeichen und wie sich die Variablen verhalten

//Jetzt das ganze mal umgesetz in HTML in deiner Art

?>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">

<head>
    <title>Werte</title>
    <meta http-equiv="content-type" content="text/html;charset=utf-8" />
    <meta name="generator" content="Geany 1.24" />
</head>

<body>


<!-- Jetzt ich -->
<table border="3"> <a href=temperatur.php title= Temperatur>Temperatur:</a>
    <?php foreach($fetch as $Bezeichnung => $Wert)
    {?>
        <tr>
        <th><?php echo $Bezeichnung; ?>:</th>
        <td><?php echo $Wert;?></td>
        </tr>


    <?php
    }
    ?>
</table>
<form method="post" action="index.php">
	<input type="submit" name="sent">
</form>
</body>

</html>

<?php

$con = mysqli_close();

?>
