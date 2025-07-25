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
    `;

  const currentUrl = new URLSearchParams(window.location.search);

  if (currentUrl.has("sketch")) {
    initialSketch = decodeSketchUrl(currentUrl.get("sketch"));
  }

  return initialSketch;
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
