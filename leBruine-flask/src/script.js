const lista = [];

document.getElementById('cadastroCliente').addEventListener('click', function() {
    const getEmail = document.getElementById('emailUsuario').value;
    const getName = document.getElementById('nomeUsuario').value;
    const getPhone = document.getElementById('numeroUsuario').value;
    const getSenha = document.getElementById('senhaUsuario').value;

    console.log(getEmail);
    console.log(getName);
    console.log(getPhone);
    console.log(getSenha);

    const dados = {getEmail, getName, getPhone, getSenha};
    lista.push(dados.json);

    document.getElementById('cadastroCliente').addEventListener('click', function() {
        const json = JSON.stringify
        });

});
