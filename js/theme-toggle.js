// Theme Toggle Script
(function() {
  'use strict';
  
  const STORAGE_KEY = 'color-scheme';
  const ATTR_NAME = 'data-color-scheme';
  
  // Get saved theme or system preference
  function getInitialTheme() {
    const saved = localStorage.getItem(STORAGE_KEY);
    if (saved) return saved;
    
    // Check system preference
    if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
      return 'dark';
    }
    return 'light';
  }
  
  // Apply theme immediately to prevent flash
  function applyTheme(theme) {
    document.documentElement.setAttribute(ATTR_NAME, theme);
  }
  
  // Toggle between themes
  function toggleTheme() {
    const current = document.documentElement.getAttribute(ATTR_NAME) || 'light';
    const next = current === 'light' ? 'dark' : 'light';
    applyTheme(next);
    localStorage.setItem(STORAGE_KEY, next);
    updateButton(next);
  }
  
  // Update button icon only
  function updateButton(theme) {
    const button = document.getElementById('theme-toggle');
    if (button) {
      button.textContent = theme === 'light' ? '🌙' : '☀️';
      button.setAttribute('aria-label', `Switch to ${theme === 'light' ? 'dark' : 'light'} mode`);
    }
  }
  
  // Initialize on page load
  function init() {
    const theme = getInitialTheme();
    applyTheme(theme);
    
    // Wait for DOM to be ready
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', () => {
        updateButton(theme);
        attachListeners();
      });
    } else {
      updateButton(theme);
      attachListeners();
    }
  }
  
  // Attach event listeners
  function attachListeners() {
    const button = document.getElementById('theme-toggle');
    if (button) {
      button.addEventListener('click', toggleTheme);
    }
    
    // Listen for system theme changes
    if (window.matchMedia) {
      window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
        // Only auto-switch if user hasn't set a preference
        if (!localStorage.getItem(STORAGE_KEY)) {
          const theme = e.matches ? 'dark' : 'light';
          applyTheme(theme);
          updateButton(theme);
        }
      });
    }
  }
  
  // Run immediately
  init();
})();
