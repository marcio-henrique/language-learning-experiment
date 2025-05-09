import { API_BASE } from "./config.js";
const userId = localStorage.getItem("user_id");

function sendLog(eventType, element, context = {}) {
  const id = element.id || element.className || element.tagName;
  const screen = window.location.pathname.split("/").pop().replace(".html", "");

  const log = {
    user_id: userId,
    timestamp_begin: new Date().toISOString(),
    timestamp_end: new Date().toISOString(),
    event_type: eventType,
    screen,
    html_element_id: id,
    context
  };

  console.log('bora ver');
  console.log(log);

  fetch(`${API_BASE}/logs/`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(log)
  });
}

["click", "mouseover", "mouseout"].forEach(evt => {
  document.addEventListener(evt, e => {
    if (!userId) return;
    const context = {
      value: e.target.innerText?.substring(0, 100),
      page_url: window.location.pathname
    };
    sendLog(evt, e.target, context);
  });
});

document.addEventListener("selectionchange", () => {
  const selection = document.getSelection();
  if (!selection || selection.toString().trim().length < 1) return;

  const context = {
    selected_text: selection.toString().substring(0, 100),
    page_url: window.location.pathname
  };

  sendLog("text_selection", selection.anchorNode?.parentElement || document.body, context);
});

window.addEventListener("beforeunload", () => {
  sendLog("leave_page", document.body);
});

window.addEventListener("pageshow", e => {
  if (e.persisted) sendLog("return_to_page", document.body);
});
