const API_BASE = "http://64.23.138.141:8000";
const userId = localStorage.getItem("user_id");

if (!userId) {
  window.location.href = "basic_login.html";
}

let correctAnswers = {};

document.addEventListener("DOMContentLoaded", async () => {
  try {
    const res = await fetch(`${API_BASE}/questionnaires/latest?type=evaluation`);
    const questionnaire = await res.json();

    const form = document.getElementById("quiz-form");
    form.dataset.qid = questionnaire.id;

    questionnaire.questions.forEach((q, index) => {
      const qid = index + 1;
      correctAnswers[qid] = q.correct;  // assumindo que há campo "correct"

      const fieldset = document.createElement("fieldset");
      const legend = document.createElement("legend");
      legend.innerText = `${qid}. ${q.q}`;
      fieldset.appendChild(legend);

      q.options.forEach((opt, idx) => {
        const label = document.createElement("label");
        const radio = document.createElement("input");
        radio.type = "radio";
        radio.name = `q${qid}`;
        radio.value = opt;

        label.appendChild(radio);
        label.appendChild(document.createTextNode(opt));
        label.classList.add("option-label");
        fieldset.appendChild(label);
      });

      form.appendChild(fieldset);
    });

  } catch (err) {
    alert("Erro ao carregar questionário.");
    console.error(err);
  }
});

document.getElementById("submit-quiz").addEventListener("click", async (e) => {
  e.preventDefault();

  const form = document.getElementById("quiz-form");
  const qid = form.dataset.qid;
  const answers = {};

  let allAnswered = true;

  Object.keys(correctAnswers).forEach(qnum => {
    const selected = form.querySelector(`input[name="q${qnum}"]:checked`);
    if (!selected) {
      allAnswered = false;
      return;
    }

    const userAnswer = selected.value;
    answers[qnum] = userAnswer;

    const labels = form.querySelectorAll(`input[name="q${qnum}"]`);
    labels.forEach(radio => {
      const label = radio.parentElement;
      label.classList.remove("correct", "wrong");

      if (radio.value === correctAnswers[qnum]) {
        label.classList.add("correct");
      }

      if (radio.checked && radio.value !== correctAnswers[qnum]) {
        label.classList.add("wrong");
      }
    });
  });

  if (!allAnswered) {
    alert("Por favor, responda todas as questões antes de enviar.");
    return;
  }

  await fetch(`${API_BASE}/questionnaires/answer/`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      user_id: userId,
      questionnaire_id: qid,
      answers: answers
    })
  });

  setTimeout(() => {
    window.location.href = "thanks.html";
  }, 3000); // mostra as respostas por 3 segundos
});

document.getElementById("logout-btn")?.addEventListener("click", () => {
  localStorage.removeItem("user_id");
  window.location.href = "basic_login";
});
