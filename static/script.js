document.getElementById('prediction-form').addEventListener('submit', async function (e) {
    e.preventDefault();

    const formData = {
        hours_studied: document.getElementById('hours_studied').value,
        attendance: document.getElementById('attendance').value,
        previous_scores: document.getElementById('previous_scores').value,
        sleep_hours: document.getElementById('sleep_hours').value,
        extracurricular: document.getElementById('extracurricular').value
    };

    try {
        const response = await fetch('/predict', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(formData)
        });

        const result = await response.json();

        if (result.status === 'success') {
            const resultBox = document.getElementById('result-box');
            const scoreDisplay = document.getElementById('score-display');
            const categoryDisplay = document.getElementById('category-display');
            const resultTitle = document.getElementById('result-title');

            resultBox.classList.remove('hidden', 'result-best', 'result-good', 'result-dull');
            scoreDisplay.textContent = `${result.score} / 100`;

            // Dynamic Styling Based on Score
            if (result.score >= 85) {
                resultBox.classList.add('result-best');
                resultTitle.textContent = "🏆 LEGENDARY ACADEMIC STATUS! 🌟";
                categoryDisplay.textContent = `Outstanding achievement! You are mastering the multiverse! (${result.category})`;
            } else if (result.score >= 70) {
                resultBox.classList.add('result-good');
                resultTitle.textContent = "⚡ Solid Performance!";
                categoryDisplay.textContent = `Great effort! Keep pushing further! (${result.category})`;
            } else {
                resultBox.classList.add('result-dull');
                resultTitle.textContent = "⚠️ Low Energy Output...";
                categoryDisplay.textContent = `Needs improvement. Time to power up your routine! (${result.category})`;
            }
        } else {
            alert('Error: ' + result.message);
        }
    } catch (err) {
        console.error(err);
        alert('Failed to connect to backend server.');
    }
});