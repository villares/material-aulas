function createSketchUrl(fullScreen = false) {
  let baseUrl = window.location.origin + window.location.pathname;
  if (fullScreen) {
    baseUrl = baseUrl + "fullscreen.html";
  }
  const userCode = editor.getSession().getValue();

  const encodedUserCode = btoa(encodeURIComponent(userCode));

  const sketchUrl = new URL(baseUrl);
  sketchUrl.searchParams.append("sketch", encodedUserCode);

  return sketchUrl;
}

function decodeSketchUrl(encodedSketch) {
  const decodedSketch = decodeURIComponent(atob(encodedSketch));

  return decodedSketch;
}

function checkForSketch() {
  let initialSketch = `def setup():
    size(400, 400)

def draw():
    background(200)
    diameter = sin(frame_count / 60) * 50 + width / 2
    fill("blue")
    ellipse(width / 2, height / 2, diameter, diameter)
    `;

  const currentUrl = new URLSearchParams(window.location.search);

  if (currentUrl.has("sketch")) {
    initialSketch = decodeSketchUrl(currentUrl.get("sketch"));
  }

  return preprocessCode(initialSketch);
}

function preprocessCode(code) {
  // Check if the code contains a def setup(): definition
  if (code.indexOf('def setup') === -1) {
    // If not, check if the code contains a size() function
    if (code.indexOf('size(') === -1) {
      // If not, wrap the entire code inside a new setup() function and add size(100, 100)
      const lines = code.trim().split('\n');
      const indentedLines = lines.map(function(line) {
        return '  ' + line;
      });
      code = 'def setup():\n  size(100, 100)\n' + indentedLines.join('\n');
    } else {
      // If size() is present, wrap the entire code inside a new setup() function
      const lines = code.trim().split('\n');
      const indentedLines = lines.map(function(line) {
        return '  ' + line;
      });
      code = 'def setup():\n' + indentedLines.join('\n');
    }
  }


// Made by user Dean Taylor in
// https://stackoverflow.com/questions/400212/how-do-i-copy-to-the-clipboard-in-javascript

function fallbackCopyTextToClipboard(text) {
  var textArea = document.createElement("textarea");
  textArea.value = text;

  // Avoid scrolling to bottom
  textArea.style.top = "0";
  textArea.style.left = "0";
  textArea.style.position = "fixed";

  document.body.appendChild(textArea);
  textArea.focus();
  textArea.select();

  try {
    document.execCommand("copy");
  } catch (err) {
    console.error("Fallback: Oops, unable to copy URL", err);
  }

  document.body.removeChild(textArea);
}

function copyTextToClipboard(text) {
  if (!navigator.clipboard) {
    fallbackCopyTextToClipboard(text);
    return;
  }
  navigator.clipboard.writeText(text).then(
    function () {
      return;
    },
    function (err) {
      console.error("Async: Could not copy URL: ", err);
    }
  );
}
