<?php
require_once('../db.php');
$sql = "SELECT * FROM Keycards ORDER BY Id";
$anzahleintraege;
if ($erg = $db->query($sql)) {
 	if ($erg->num_rows) {
		$ds_gesamt = $erg->num_rows;
		$erg->free();
	}
	if ($erg = $db->query($sql)) {
		while ($datensatz = $erg->fetch_object()) {
			$daten[] = $datensatz;
		}
	}
}
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
          <a class="nav-link" aria-current="page" href="index.php">Dashboard</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="temperatur.php">Temperatur Anzeige</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="humidity.php">Luftfeuchtigkeit Anzeige</a>
        </li>
        <li class="nav-item">
          <a class="nav-link active" href="dooracces.php">Türkartensteuerung</a>
        </li>
      </ul>
    </div>
  </div>
</nav>
      </nav>
      <h3>Registrierte Türkarten</h3>
      <p>
         Hier findest du alle deine Gespeicherten Türkarten und kannst neue Karten Anlegen: <?php print($ds_gesamt); ?>
         <form method="post" action="index.php">
   				<input type="submit" name="sent" value="Neue Karte Anlegen">
   			</form>
      </p>
    </div>
    <div>
<div data-role="main" class="ui-content">
  <table id="meineTabelle" data-role="table" class="table"
         data-mode="columntoggle" data-column-btn-text="Spalten" >
    <thead>
      <tr>
        <th data-priority="4">ID</th>
        <th data-priority="1">Kartennummer</th>
        <th data-priority="3">Löschen</th>
      </tr>
    </thead>
    <tbody>
  <?php
  foreach ($daten as $inhalt) {
  ?>
      <tr>
          <td>
              <?php echo $inhalt->Id; ?>
          </td>
          <td>
              <?php echo $inhalt->KeyCode; ?>
          </td>
          <td>
            <form method="post" action="index.php">
              <input type="submit" name="sent" value="Löschen">
            </form>
          </td>
        </tr>
  <?php
  }
  ?>
    </tbody>
  </table>
