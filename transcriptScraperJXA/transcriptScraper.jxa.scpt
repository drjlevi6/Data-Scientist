JsOsaDAS1.001.00bplist00�Vscript_
�/* Copy and reformat the transcript of a LinkedIn Learning lesson:
 * Copy the entire text of the lesson (as displayed in Firefox),
 * cut the text preceding the transcript and the second line 
 * ("Selecting transcript lines in this section..."),
 * fold the remaining text to lines of <= 80 chars and copy to
 * pasteboard.
 */
(() => {

/*-----Initialization---------------------------------------------------------*/
const app = Application.currentApplication();
app.includeStandardAdditions = true;

const se = Application('System Events');
const finder = Application('Finder');
const finderp = se.processes.byName('Finder');

const firefox = Application('Firefox');
const firefoxp = se.processes.byName('Firefox');

const bbedit = Application('BBEdit');

const cliclick = '/usr/local/bin/cliclick ';

/*-----Main-------------------------------------------------------------------*/
remindUserTranscriptSelected();
let allText = getTranscriptText();
formatTranscriptText(allText);
clickFirefoxScreenBottom();
notifyFormattedText();
bbedit.activate();

/*-----Functions--------------------------------------------------------------*/
function remindUserTranscriptSelected(){ // was the transcript selected?
	app.activate()
	app.displayDialog("Have you selected the Transcript text?",
		{withIcon: "caution"});
}

function notifyFormattedText(){
	app.activate();
	app.displayDialog(
		"The formatted text has been copied to the Clipboard.\r" +
		"You may need to click the page bottom to deselect remaining text.",
		{withTitle: "Done!", givingUpAfter: 2, withIcon: "caution"});	
}

function getTranscriptText(){
	firefox.activate();
	clickFirefoxScreenBottom();
	return firefoxGetAndCutAllText();
}

function formatTranscriptText(allText){	// With doShellScript() JXA appears to convert  
										// newlines to carriage returns, even after 
										// "tr '\r' '\n'. To get around this, we
										// just send the entire text to the clipboard and
										// from there to she shell script without any 
										// processing by JXA.
	theClipboard = allText;
	app.doShellScript("$HOME/bin/formatTranscript.bash");
}

function firefoxGetAndCutAllText(){ // get entire web page's text; cut pre-
									// transcript text and "Selecting..." line
	// We appear to need all three delays below
	firefox.activate();
	delay(0.25);
	se.keystroke('a', {using: 'command down'});
	delay(0.25);
	se.keystroke('c', {using: 'command down'});
	delay(0.25);
	return app.theClipboard();
}

function clickFirefoxScreenBottom(){
	delay(0.25);
	let w = firefox.windows[0];
	let wbounds = w.bounds();
	let w_xcenter = parseInt(wbounds['x'] + (2 * wbounds['width']/3) );
	let w_ybottom = wbounds['y'] + wbounds['height'] - 100;
	app.doShellScript( cliclick + 'dc:' + w_xcenter + ',' + w_ybottom);
}
})()                              jscr  ��ޭ