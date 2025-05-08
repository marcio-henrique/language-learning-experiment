const userId = localStorage.getItem("user_id");
const container = document.getElementById("flashcards-container");
const colors = ["yellow", "blue", "green", "purple"];

async function loadFlashcards() {
  const res = await fetch(`https://language-learning-experiment.duckdns.org/flashcards/custom/?auto_flashcards=3&manual_flashcards=1`);
  const data = await res.json();

  data.flashcards.forEach((card, i) => {
    const div = document.createElement("div");
    div.className = "flashcard";
    div.dataset.color = colors[i % colors.length];

    div.innerHTML = `
      <div class="front">
        <h3>${card.grammar_structure_value.toUpperCase()}</h3>
        <p>${card.description}</p>
        <p><strong>Aplicações em frase:</strong><br> - ${card.example_sentence}</p>
        <button class="flip-btn">Ver Verso</button>
      </div>
      <div class="back">
        <p><strong>${card.question}</strong></p>
        <ul>
          ${card.options.map(opt => `<li>${opt}</li>`).join("")}
        </ul>
        <button class="flip-btn">Ver Frente</button>
      </div>
    `;

    container.appendChild(div);
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
