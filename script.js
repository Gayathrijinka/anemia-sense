document.getElementById("anemiaForm").addEventListener("submit", function(e){
    e.preventDefault();

    const data = {
        gender: parseInt(document.getElementById("gender").value),
        hemoglobin: parseFloat(document.getElementById("hemoglobin").value),
        mch: parseFloat(document.getElementById("mch").value),
        mchc: parseFloat(document.getElementById("mchc").value),
        mcv: parseFloat(document.getElementById("mcv").value)
    };

    fetch('/predict', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(result => {
        const output = `<p><strong>${result.result}</strong></p>`;
        document.getElementById("result").innerHTML = output;
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById("result").innerHTML = "<p style='color:red;'>Error occurred. Check console.</p>";
    });
});

function resetForm() {
    document.getElementById("anemiaForm").reset();
    document.getElementById("result").innerText = "";
}
