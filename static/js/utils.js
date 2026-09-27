// Error message extraction from API responses
export function getErrorMessage(error) {
  if (typeof error.detail === "string") {
    return error.detail;
  } else if (Array.isArray(error.detail)) {
    return error.detail.map((err) => err.msg).join(". ");
  }
  return "An error occurred. Please try again.";
}

// Show a Bootstrap modal by ID
export function showModal(modalId) {
  const modal = bootstrap.Modal.getOrCreateInstance(
    document.getElementById(modalId),
  );
  modal.show();
  return modal;
}

// Hide a Bootstrap modal by ID
export function hideModal(modalId) {
  const modal = bootstrap.Modal.getInstance(document.getElementById(modalId));
  if (modal) modal.hide();
}


// the first batch of posts are rendered by jinja 2 which takes care of escape html and date formating itself but scince adding paggination we will construct the comming posts when the user clicks load more ourselves using javascript thats why we need to manually escape html and format date

// XSS prevention for dynamic content insertion
export function escapeHtml(text) {
  const div = document.createElement("div");
  div.textContent = text;
  return div.innerHTML;
}

// Date formatting to match server's strftime("%B %d, %Y")
export function formatDate(dateString) {
  const date = new Date(dateString);
  return date.toLocaleDateString("en-US", {
    year: "numeric",
    month: "long",
    day: "2-digit",
  });
}