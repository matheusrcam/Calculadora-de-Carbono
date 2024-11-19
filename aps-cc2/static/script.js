document.getElementById('emissao-form').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const dados = {
        energia: parseFloat(document.getElementById('energia').value),
        gasolina: parseFloat(document.getElementById('gasolina').value),
        diesel: parseFloat(document.getElementById('diesel').value),
        voo: parseFloat(document.getElementById('voo').value)
    };

    fetch('/calcular', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(dados)
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('resultado').innerText = 
            `Total de Emissões: ${data.total_emissoes.toFixed(2)} kg CO2\n` +
            `Créditos de Carbono Necessários: ${data.creditos.toFixed(2)} toneladas`;
    });
});

document.getElementById('calcular-custo').addEventListener('click', function() {
    // Extraindo a quantidade de créditos de carbono
    const creditos = parseFloat(document.getElementById('resultado').innerText.split(' ')[3]);
    const projeto = document.getElementById('projeto').value;

    fetch('/custo', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ creditos: creditos, projeto: projeto })
    })
    .then(response => response.json())
    .then(data => {
        if (data.custo) {
            document.getElementById('custo').innerText = `Custo para compensar: R$ ${data.custo.toFixed(2)}`;
        } else {
            document.getElementById('custo').innerText = `Erro: ${data.erro}`;
        }
    });
});
