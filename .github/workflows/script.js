const form = document.getElementById("feedbackForm");
const averageEl = document.getElementById("average");
const countEl = document.getElementById("count");

let feedbackList = [];

form.addEventListener("submit", (e) => {
  e.preventDefault();

  const name = document.getElementById("name").value;
  const subject = document.getElementById("subject").value;
  const rating = parseInt(document.getElementById("rating").value);
  const comments = document.getElementById("comments").value;

  if (rating < 1 || rating > 5) {
    alert("Rating must be between 1 and 5");
    return;
  }

  const feedback = { name, subject, rating, comments };
  feedbackList.push(feedback);

  updateAverage();
  form.reset();
});

function updateAverage() {
  const total = feedbackList.reduce((sum, fb) => sum + fb.rating, 0);
  const avg = (total / feedbackList.length).toFixed(2);
  averageEl.textContent = avg;
  countEl.textContent = feedbackList.length;
}
