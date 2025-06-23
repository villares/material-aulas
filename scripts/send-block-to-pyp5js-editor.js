// To add the buttons that send code blocks to a pyp5js py5-mode editor
const EDITOR_BASE_URL = "https://abav.lugaralgum.com/material-aulas/pyp5js/py5mode/";

function encodeForEditor(code) {
  return btoa(encodeURIComponent(code));
}
/**
 * @param {string} code - The code to include in the URL
 * @param {boolean} fullScreen - Whether to load in fullscreen mode
 * @returns {string} - The complete editor URL
 */
function createEditorUrl(code, fullScreen = false) {
  let baseUrl = EDITOR_BASE_URL;
  if (fullScreen) {
    baseUrl = baseUrl + "fullscreen.html";
  }
  const encodedCode = encodeForEditor(code);
  const editorUrl = new URL(baseUrl);
  editorUrl.searchParams.append("sketch", encodedCode);

  return editorUrl.toString();
}

/**
 * @param {string} code - The code to send to the editor
 * @returns {HTMLElement} - The button element
 */
function createEditorButton(code) {
  const button = document.createElement("button");
  button.textContent = "Open in Editor";
  button.className = "editor-link-button";
  button.style.cssText = `
    background-color: #4CAF50;
    border: none;
    color: white;
    padding: 5px 10px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 12px;
    margin: 2px;
    cursor: pointer;
    border-radius: 4px;
  `;

  button.addEventListener("click", function() {
    const editorUrl = createEditorUrl(code);
    window.open(editorUrl, "_blank");
  });

  // Add a tooltip
  button.title = "Open on editor";
  
  return button;
}

/**
 * Create a "Copy URL" button that copies the editor URL to clipboard
 * @param {string} code - The code to include in the URL
 * @returns {HTMLElement} - The button element
 */
function createCopyUrlButton(code) {
  const button = document.createElement("button");
  button.textContent = "Copy URL";
  button.className = "copy-url-button";
  button.style.cssText = `
    background-color: #2196F3;
    border: none;
    color: white;
    padding: 5px 10px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 12px;
    margin: 2px;
    cursor: pointer;
    border-radius: 4px;
  `;

  button.addEventListener("click", function() {
    const editorUrl = createEditorUrl(code);
    copyTextToClipboard(editorUrl);
    
    // Visual feedback for copy action
    const originalText = button.textContent;
    button.textContent = "Copied!";
    button.style.backgroundColor = "#45a049";
    
    setTimeout(() => {
      button.textContent = originalText;
      button.style.backgroundColor = "#2196F3";
    }, 1500);
  });

  button.title = "Copy editor URL to clipboard";
  
  return button;
}

/**
 * Copy text to clipboard
 * @param {string} text - Text to copy to clipboard
 */
function copyTextToClipboard(text) {
  if (navigator.clipboard) {
    navigator.clipboard.writeText(text).catch(err => {
      console.error("Could not copy URL: ", err);
      fallbackCopyTextToClipboard(text);
    });
  } else {
    fallbackCopyTextToClipboard(text);
  }
}

/**
 * Fallback method for copying to clipboard
 * @param {string} text - Text to copy to clipboard
 */
function fallbackCopyTextToClipboard(text) {
  const textArea = document.createElement("textarea");
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
    console.error("Fallback: Unable to copy URL", err);
  }

  document.body.removeChild(textArea);
}

/**
 * Process code blocks in the document to add editor buttons
 */
function processCodeBlocks() {
  // GitHub Pages renders markdown code blocks in different ways depending on the theme
  // This selector tries to cover most common patterns
  
  // First attempt: Look for code blocks with the interactive class
  // When using ```python-interactive in markdown, GitHub Pages typically adds a class
  const interactiveBlocks = document.querySelectorAll([
    '.language-python-interactive pre code',
    '.language-javascript-interactive pre code',
    '.language-js-interactive pre code',
    '.highlighter-rouge.language-python-interactive .highlight pre.highlight code',
    '.highlighter-rouge.language-javascript-interactive .highlight pre.highlight code',
    '.highlighter-rouge.language-js-interactive .highlight pre.highlight code',
    'pre.highlight-interactive code',
    'div[class*="-interactive"] pre code'
  ].join(', '));
  
  if (interactiveBlocks.length > 0) {
    // Process the blocks marked as interactive
    interactiveBlocks.forEach(addButtonsToCodeBlock);
    console.log(`Added buttons to ${interactiveBlocks.length} interactive code blocks`);
  } else {
    // Fallback: If no interactive blocks found, look for classes with specific patterns
    const alternativeSelector = [
      // Common patterns for code blocks with interactive in the class name
      '[class*="-interactive"]',
      // If there are parent elements with -interactive in the class
      'div[class*="-interactive"] pre',
      'div[class*="-interactive"] code'
    ].join(', ');
    
    const alternativeBlocks = document.querySelectorAll(alternativeSelector);
    if (alternativeBlocks.length > 0) {
      alternativeBlocks.forEach(element => {
        // Find the actual code element
        const codeElement = element.tagName === 'CODE' ? element : element.querySelector('code');
        if (codeElement) {
          addButtonsToCodeBlock(codeElement);
        }
      });
      console.log(`Added buttons to ${alternativeBlocks.length} alternative interactive code blocks`);
    } else {
      console.log('No interactive code blocks found on this page');
    }
  }
}

/**
 * Add editor buttons to a code block
 * @param {HTMLElement} codeBlock
 */
function addButtonsToCodeBlock(codeBlock) {
  const code = codeBlock.textContent;
  
  // Create a container for our buttons
  const buttonContainer = document.createElement('div');
  buttonContainer.className = 'editor-button-container';
  buttonContainer.style.cssText = `
    display: flex;
    justify-content: flex-end;
    margin-top: 5px;
  `;
  
  // Add the buttons
  buttonContainer.appendChild(createEditorButton(code));
  buttonContainer.appendChild(createCopyUrlButton(code));
  
  // Find the parent element to attach the buttons after
  // Start with direct parent and move up until a block-level element is found
  let parentElement = codeBlock.parentElement;
  while (parentElement && 
         (window.getComputedStyle(parentElement).display === 'inline' || 
          window.getComputedStyle(parentElement).display === 'inline-block')) {
    parentElement = parentElement.parentElement;
  }
  
  if (parentElement) {
    parentElement.style.position = 'relative';
    parentElement.insertAdjacentElement('afterend', buttonContainer);
  } else {
    // Fallback to direct parent if couldn't find a block level parent
    const directParent = codeBlock.parentElement;
    if (directParent) {
      directParent.style.position = 'relative';
      directParent.insertAdjacentElement('afterend', buttonContainer);
    }
  }
}

/**
 * Initialize script once DOM is fully loaded
 */
function initCodeBlockEnhancer() {
  processCodeBlocks();
  console.log("Code Block Encoder initialized");
}
// Run initialization when DOM is fully loaded
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initCodeBlockEnhancer);
} else {
  initCodeBlockEnhancer();
}
