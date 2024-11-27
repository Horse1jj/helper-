// Fetch bot status
fetch('/status')
  .then((response) => response.json())
  .then((data) => {
    document.getElementById('bot-status').textContent = `Bot is ${data.status} with prefix '${data.prefix}'.`;
  });

// Handle custom embed submission
document.getElementById('embed-form').addEventListener('submit', (e) => {
  e.preventDefault();
  const title = document.getElementById('embed-title').value;
  const description = document.getElementById('embed-description').value;
  const color = document.getElementById('embed-color').value;

  fetch('/embed', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ title, description, color }),
  })
    .then((response) => response.json())
    .then((data) => alert(data.message));
});

// Handle announcement submission
document.getElementById('announcement-form').addEventListener('submit', (e) => {
  e.preventDefault();
  const message = document.getElementById('announcement-message').value;
  const delay = document.getElementById('announcement-delay').value;

  fetch('/announcement', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ message, delay }),
  })
    .then((response) => response.json())
    .then((data) => alert(data.message));
});
