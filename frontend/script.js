async function sendRequest() {
  const type = document.getElementById("type").value;
  const content = document.getElementById("content").value;

  const res = await fetch("http://localhost:8000/ai-email", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ type, content }),
  });

  const data = await res.json();

  document.getElementById("result").innerText = data.result;
}