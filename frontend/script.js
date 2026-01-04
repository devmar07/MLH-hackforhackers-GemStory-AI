let currentStory = "";

async function createStory() {
  const genre = document.getElementById("genre").value;
  const character = document.getElementById("character").value;

  const response = await fetch("http://127.0.0.1:5000/story", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      genre: genre,
      character: character
    })
  });

  const data = await response.json();
  currentStory = data.story;

  document.getElementById("output").textContent = currentStory;
}

async function continueStory() {
  const response = await fetch("http://127.0.0.1:5000/story", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      history: currentStory
    })
  });

  const data = await response.json();
  currentStory += "\n\n" + data.story;

  document.getElementById("output").textContent = currentStory;
}
