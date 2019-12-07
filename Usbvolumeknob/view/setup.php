<?php
/**
 Example Setup View File
 
 @Copyright 2014 Stefan Rick
 @author Stefan Rick
 Mail: stefan@rick-software.de
 Web: http://www.netzberater.de
 

 This program is free software; you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation; either version 2 of the License, or
 (at your option) any later version.
 
 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.
 
 You should have received a copy of the GNU General Public License along
 with this program; if not, write to the Free Software Foundation, Inc.,
 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
 */

/**
 * Put HTML and Javascript Content here
 */
?>


<h1 class="entry-header">
	<?php echo _t("USB rotary encoder knob") ?>
</h1>
<div class="entry-content">
	<?php if(isset($Usbvolumeknob->view->message[0])){ ?>
		<div class="ui-widget">
		<div class="ui-state-highlight ui-corner-all"
			style="margin-bottom: 10px; padding: 0.4em .7em;">
			<p>
				<span class="ui-icon ui-icon-info"
					style="float: left; margin-right: .3em;"></span>
					<?php echo implode('<br />', $Usbvolumeknob->view->message); ?>					
				</p>
		</div>
	</div>
	<?php } ?>
	
	<p class="ui-state-default ui-corner-all"
		style="padding: 4px; margin-bottom: 1em;">
		<span class="ui-icon ui-icon-wrench"
			style="float: left; margin: -2px 5px 0 0;"></span> <b><?php echo _("Control the volume and toggle play/pause on a squeezelite player") ?></b>
	</p>

	<form id="form1" action="" method="get">
		<input type="hidden" id="action" name="action" value="">
		<input type="hidden" id="server-ip" name="server-ip" value="">
		<input type="hidden" id="player-mac" name="player-mac" value="">
		<input type="hidden" id="hid-name" name="hid-name" value="">

	
	
<?php /* Thomas section begin */ ?>
	
	<br />
		<h3>Install Usbvolumeknob plugin</h3>
		<br>
		<div id="install-button">
			<p>
				server IP <input type="text" id="serverIP" name="serverIP" value="xxx.xxx.xx.xx:9000" /> (don't forget the port!!!) <br>
				player MAC <input type="text" id="playerMAC" name="playerMAC" value="xx:xx:xx:xx:xx:xx" /><br>
				HID device name <input type="text" id="HIDDeviceName" name="HIDDeviceName" value="Adafruit Trinket HID Combo" /><br>
				<br>
				<input
					type="button"
					value="<?php echo _t("Install") ?>"
					name="install1"
					onclick="document.getElementById('action').value='install';
							 document.getElementById('server-ip').value= document.getElementById('serverIP').value;
							 document.getElementById('player-mac').value= document.getElementById('playerMAC').value;
							 document.getElementById('hid-name').value= document.getElementById('HIDDeviceName').value;
							 submit();" 
				/>
				<br />
				<br />
			</p>
		</div>
	
<?php /* Thomas section end */ ?>
	
	
		
			<input type="button" id="save" name="<?php echo _("save") ?>"
				onclick="document.getElementById('action').value='save';submit();"
				value="<?php echo _("save") ?>" />
			</td>
		</div>
		<br />
		
		

	</form>

	<br />
	<br /> <a href="#javascript"
		onclick="document.getElementById('debug').style.display='';return false;"><?php echo _("DEBUG Informations") ?></a>
	<textarea id="debug" rows="30" cols="70" style="display: none;"><?php

foreach ($Usbvolumeknob->view->debug as $key => $debug) {
			echo "#### ". $key. " ####\n"; 
			 echo $debug." \n\n"; 
		 }?>
	</textarea>
</div>
