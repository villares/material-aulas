// To add the buttons that send code blocks to a pyp5js py5-mode editor
// looks for <!-- interactive --> comment before the code blocks
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
  button.textContent = "Abrir no Editor Online";
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
  // button.title = "Open on editor";
  
  return button;
}

/**
 * Create a "Copy URL" button that copies the editor URL to clipboard
 * @param {string} code - The code to include in the URL
 * @returns {HTMLElement} - The button element
 */
function createCopyUrlButton(code) {
  const button = document.createElement("button");
  button.textContent = "Copiar URL do Editor";
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

  button.title = "Copy URL";
  
  return button;
}

/**
 * Copy text to clipboard
 * @param {string} text
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
 * Check if an element has an interactive comment before it
 * @param {HTMLElement} codeContainer - The code container element
 * @returns {boolean} - True if interactive comment is found before the element
 */
function hasInteractiveComment(codeContainer) {
  let currentElement = codeContainer.previousSibling;
  
  // Check up to 3 previous siblings to find the comment
  for (let i = 0; i < 3 && currentElement; i++) {
    // Check if it's a comment node
    if (currentElement.nodeType === Node.COMMENT_NODE) {
      const commentText = currentElement.textContent.trim();
      if (commentText === 'interactive') {
        return true;
      }
    }
    
    // Move to previous sibling
    currentElement = currentElement.previousSibling;
  }
  
  return false;
}

/**
 * Process code blocks in the document to add editor buttons
 */
function processCodeBlocks() {
  const allCodeBlocks = document.querySelectorAll('pre code');
  
  allCodeBlocks.forEach(codeBlock => {
    const codeContainer = codeBlock.closest('pre');
    
    if (codeContainer && hasInteractiveComment(codeContainer)) {
      addButtonsToCodeBlock(codeBlock);
    }
  });
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
}

// Run initialization when DOM is fully loaded
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initCodeBlockEnhancer);
} else {
  initCodeBlockEnhancer();
}