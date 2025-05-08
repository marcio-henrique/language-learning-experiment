const API_BASE = "http://64.23.138.141:8000";  // ou o endereço real do seu backend

export async function getEducationalText() {
  const response = await fetch(`${API_BASE}/texts/`);
  if (!response.ok) {
    throw new Error("Erro ao buscar texto educacional");
  }
  return await response.json();
}

export async function registerTextRead(userId, textId) {
  const response = await fetch(`${API_BASE}/texts/read/`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ user_id: userId, educational_text_id: textId })
  });
  if (!response.ok) {
    throw new Error("Erro ao registrar leitura do texto");
  }
  return await response.json();
}
