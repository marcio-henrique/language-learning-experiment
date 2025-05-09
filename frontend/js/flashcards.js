const userId = localStorage.getItem("user_id");
const container = document.getElementById("flashcards-container");
const colors = ["yellow", "blue", "green", "purple"];
import { API_BASE } from "./config.js";

async function loadFlashcards() {
  const res = await fetch(`${API_BASE}/flashcards/custom/?auto_flashcards=3&manual_flashcards=1`);
  const data = await res.json();

  data.flashcards.forEach((card, i) => {
    const div = document.createElement("div");
    div.className = "flashcard";
    div.dataset.color = colors[i % colors.length];

    const front = `
      <div class="front">
        <h3>${card.grammar_structure_value.toUpperCase()}</h3>
        <p>${card.description}</p>
        <p><strong>Aplicações em frase:</strong><br> - ${card.example_sentence}</p>
        <button class="flip-btn">Ver Verso</button>
      </div>
    `;

    const options = card.options.map(opt => `
      <label class="radio-option">
        <input type="radio" name="q-${card.id}" value="${opt}" />
        ${opt}
      </label>
    `).join("");

    const back = `
      <div class="back">
        <p><strong>${card.question}</strong></p>
        <form>${options}</form>
        <div class="feedback" style="margin-top: 8px;"></div>
        <button class="flip-btn">Ver Frente</button>
      </div>
    `;

    div.innerHTML = front + back;
    container.appendChild(div);

    // interatividade das respostas
    const form = div.querySelector("form");
    const feedback = div.querySelector(".feedback");

    form.querySelectorAll("input[type=radio]").forEach(input => {
      input.addEventListener("change", async () => {
        const resposta = input.value;
        const correta = card.correct_answer;

        // reset classes
        form.querySelectorAll("label").forEach(label => label.classList.remove("correct", "incorrect"));

        // aplicar classes visuais
        form.querySelectorAll("input").forEach(r => {
          const label = r.closest("label");
          if (r.value === correta) {
            label.classList.add("correct");
          }
          if (r.checked && r.value !== correta) {
            label.classList.add("incorrect");
          }
        });

        feedback.textContent = resposta === correta ? "✔️ Resposta correta!" : `❌ Resposta incorreta. Correta: ${correta}`;

        // salvar no backend
        await fetch(`http://localhost:8000/flashcards/answer/`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            user_id: userId,
            flashcard_id: card.id,
            answer: resposta,
            correct_answer: correta
          })
        });
      });
    });
  });

  setupFlipEvents();
}

function setupFlipEvents() {
  document.querySelectorAll(".flip-btn").forEach(btn => {
    btn.addEventListener("click", e => {
      const card = e.target.closest(".flashcard");
      card.classList.toggle("flipped");
    });
  });
}

document.getElementById("continue-to-quiz").addEventListener("click", () => {
  window.location.href = "quiz.html";
});

loadFlashcards();
