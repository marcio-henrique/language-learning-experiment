// import { getEducationalText, registerTextRead } from "./api.js";

document.addEventListener("DOMContentLoaded", async () => {
  const userId = localStorage.getItem("user_id");
  if (!userId) {
    // alert("Usuário não identificado.");
    localStorage.removeItem("user_id");
    window.location.href = "basic_login.html";
    return;
  }

  const userGroup = localStorage.getItem("user_group");
  const titleElement = document.getElementById("text-title");
  const continueBtn = document.getElementById("continue-btn");

  if (userGroup === "B") {
    titleElement.innerText = "Estude atentamente o texto abaixo, para responder as questões:";
    continueBtn.innerText = "Responder Questões";
    continueBtn.addEventListener("click", () => {
      window.location.href = "quiz.html";
    });
  } else {
    continueBtn.addEventListener("click", () => {
      window.location.href = "flashcards.html";
    });
  }




});


// document.getElementById("continue-btn").addEventListener("click", () => {
//     // Salvar evento no backend (opcional)
//     // Redirecionar para a próxima etapa (ex: flashcards.html)
//     window.location.href = "flashcards.html";
//   });
  
document.getElementById("logout-btn")?.addEventListener("click", () => {
  localStorage.removeItem("user_id");
  window.location.href = "basic_login.html";
});
  