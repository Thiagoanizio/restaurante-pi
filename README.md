This was my first website created using Python Flask, very proud of it.

Let's begin:

You will need python installed on your machine to run this app properly.
When you open this project on your VSCode (or your favourite IDE),
just open the integrated terminal and navigate to "labruine_flask" using the command: cd labruine_flask;
After that, just run the command: flask run;

Esse foi meu primeiro website usando Python com Flask, sou muito orgulhoso dele.
O projeto foi usado com uma template gratúita e eu alterei algumas informações no HTML e criei outras páginas usando do mesmo modelo.
O backend foi desenvolvido por mim com a ajuda de um amigo que já tem experiência na área do desenvolvimento;

Vamos começar:

Primeiramente, você precisa ter Python instalado na sua maquina para que o backend funcione, caso contrário você só irá ver o HTML sem nada funcionando por trás dos panos;
Quando abrir esse projeto no VSCode (ou na sua IDE favorita), abra o terminal integrado e navegue para "labruine_flask" usando o comando "cd labruine_flask",
Depois disso, rode o comando "flask run" e o aplicativo irá começar a rodar e te dará a porta local para abrir;

Descrição do projeto:

Basicamente, o intúito dessa aplicação é criar reserva de mesas no restaurante.
Ao entrar na página de reserva, o usuário irá inserir suas informações basicas: nome e sobrenome, telefone e email. Depois disso ele irá informar quantas pessoas vão estar presente para a reserva de 2 a 8 e escolher a data para sua reserva.
Depois que isso for feito, o usuário irá escolher qual mesa ele deseja reservar. Cada mesa possui um id e uma quantidade máxima de pessoas que ela comporta. Depois de criar a reserva, será redirecionado a uma página dizendo se a reserva foi concluída.
Se o usuário tentar criar uma outra reserva na mesma data, irá notar que a mesa com o id que foi previamente escolhida, não estará mais disponível, pois já tem uma reserva feita para ela.