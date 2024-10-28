/**
* Screen Console
* 2022, Guilherme Ranoya
*
* Just repeat the information at the browser console in a
* <div>, whose id is "ScreenConsole"
*
* Use:
* 
* Insert this line in your <head>

<script src="https://www.ranoya.com/Assets/JSLibs/ScreenConsole/startpanel.js"></script>

* OR 
*
* Insert this entire code inside a <script> tag in your <head>
* 
*
* That's it.
*
*/
 
console.defaultLog = console.log.bind(console);
console.logs = [];
 
let screen_console_wrap = document.createElement('div');
screen_console_wrap.setAttribute('id', 'ScreenConsoleWrap');
document.lastChild.appendChild(screen_console_wrap);
document.getElementById('ScreenConsoleWrap').style.position = 'fixed';
document.getElementById('ScreenConsoleWrap').style.bottom = '0';
document.getElementById('ScreenConsoleWrap').style.width = '100%';
document.getElementById('ScreenConsoleWrap').style.height = '200px';
document.getElementById('ScreenConsoleWrap').style.zIndex = '1000';
document.getElementById('ScreenConsoleWrap').style.backgroundColor = '#FFFFFF';
 
let console_output_title = document.createElement('div');
console_output_title.setAttribute('id', 'ScreenConsoleTitle');
screen_console_wrap.appendChild(console_output_title);
document.getElementById('ScreenConsoleTitle').innerHTML = 'Console';
document.getElementById('ScreenConsoleTitle').style.border = '1px solid grey';
document.getElementById('ScreenConsoleTitle').style.margin = '8px';
document.getElementById('ScreenConsoleTitle').style.marginBottom = 0;
document.getElementById('ScreenConsoleTitle').style.padding = '8px';
document.getElementById('ScreenConsoleTitle').style.display = 'inline-block';
document.getElementById('ScreenConsoleTitle').style.color = 'white';
document.getElementById('ScreenConsoleTitle').style.backgroundColor = 'grey';
document.getElementById('ScreenConsoleTitle').style.fontFamily = 'monospace';
 
let console_output = document.createElement('div');
console_output.setAttribute('id', 'ScreenConsole');
screen_console_wrap.appendChild(console_output);
document.getElementById('ScreenConsole').style.border = '1px solid grey';
document.getElementById('ScreenConsole').style.margin = '8px';
document.getElementById('ScreenConsole').style.marginTop = 0;
document.getElementById('ScreenConsole').style.padding = '8px';
document.getElementById('ScreenConsole').style.width = 'calc(100% - 32px)';
document.getElementById('ScreenConsole').style.height = '130px';
document.getElementById('ScreenConsole').style.overflowY = 'scroll';
document.getElementById('ScreenConsole').style.fontFamily = 'monospace';
 
console.log = function () {
    console.defaultLog.apply(console, arguments);
    console.logs.push(Array.from(arguments));
    document.getElementById('ScreenConsole').innerHTML += arguments[0] + '<br>';
}
window.onerror = function (msg, url, line) {
    document.getElementById('ScreenConsole').innerHTML += 'Line: ' + line + '<br>' + msg + '<br>';
}