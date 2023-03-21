function submitForm() {
    const text = document.getElementById("text").value;
    const maxTokens = document.getElementById("max-tokens").value;
    
    const data = {
      "text": text,
      "max_tokens": maxTokens
    };
    
    fetch("/submit", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(result => {
      document.getElementById("result").value = result.result;
      document.getElementById("length").value = result.length;
    })
    .catch(error => console.error(error));
  }
  