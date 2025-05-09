import { API_BASE } from "./config.js";

document.addEventListener("DOMContentLoaded", () => {
    const userId = localStorage.getItem("user_id");
    if (userId) {
        window.location.href = "index.html";
    }
});

document.getElementById("user-form").addEventListener("submit", async (e) => {
  e.preventDefault();

  const name = document.getElementById("name").value.trim();
  const email = document.getElementById("email").value.trim();

  if (!name || !email) {
    alert("Preencha todos os campos.");
    return;
  }

  try {
    const response = await fetch(`${API_BASE}/users/`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ name, email })
    });

    if (!response.ok) throw new Error("Erro ao registrar usuário");

    const user = await response.json();
    localStorage.setItem("user_id", user.id);
    localStorage.setItem("user_group", user.group);
    window.location.href = "index.html"; // leitura do texto

  } catch (err) {
    alert("Erro: " + err.message);
  }
});
