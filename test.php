<?php
require_once('../db.php');
echo "<h1>Datenbank auslesen um ". date("H:i:s") . "</h1>";
$sql = "SELECT * FROM Temperature ORDER BY Id";
if ($erg = $db->query($sql)) {
 	if ($erg->num_rows) {
		print_r($erg->num_rows);
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
<div data-role="main" class="ui-content">
  <h1>TemperaturDaten</h1>
  <table id="meineTabelle" data-role="table" class="ui-responsive"
         data-mode="columntoggle" data-column-btn-text="Spalten" >
    <thead>
      <tr>
        <th data-priority="4">ID</th>
        <th data-priority="1">Temperatur</th>
        <th data-priority="1">Zeitpunkt</th>
        <th data-priority="3">Beschreibung</th>
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
              <?php echo $inhalt->Temperature; ?>
          </td>
          <td>
              <?php echo $inhalt->MessuredDay; ?>
          </td>
          <td>
              <?php echo $inhalt->Description; ?>
          </td>
        </tr>
  <?php
  }
  ?>
    </tbody>
  </table>
