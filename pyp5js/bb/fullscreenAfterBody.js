document.getElementById("returnBtn").addEventListener("click", () => {
  const currentSketchParam = new URLSearchParams(window.location.search);
  const pathname = window.location.pathname.replace(/fullscreen.html/g, "");
  const baseUrl = new URL(window.location.origin + pathname);
  const sketchValue = currentSketchParam.get("sketch");

  // Validate and sanitize the sketch parameter
  const validSketchPattern = /^[a-zA-Z0-9_-]+$/; // Example pattern, adjust as needed
  if (sketchValue && validSketchPattern.test(sketchValue)) {
    window.location = `${baseUrl}?sketch=${sketchValue}`;
  } else {
    console.error("Invalid sketch parameter");
  }
});
