// console.log(1);
// setTimeout(
//         function () {
//                 console.log(3);
//         },
//         2000
// )

// setInterval(
//         function () {
//                 console.log(3);
//         },
//         2000
// )
// console.log(2);

const URL = 'https://jsonplaceholder.typicode.com';
// GET
// POST
// PUT
// DELETE
const usersURL = URL + '/users';
fetch(usersURL);

// const getUsers = () => {
//     const getUsersReq = fetch(usersURL);
//     getUsersReq
//     .then((res) => {
//         res.json()
//         .then(
//             (parsedRes) => {
//             console.log(parsedRes)
//         })
//     })
// }

let users = [];
const getUsers = async () => {
    const getUsersReq = await fetch(usersURL);
    const data = await getUsersReq.json()
    users = data;
}

const userListElem = document.getElementById('user-list');

const start = async () => {
    await getUsers();

    showUsers(users);
    addNewUserButtonHandler();

    // const element = document.getElementById('test-id');
    // const spanElements = document.getElementsByClassName('text');
    // console.log(element);
    // console.log(spanElements);
}

// function getNumber() {
//     let number = 0;

//     return () => {
//         return ++number;
//     }
// }

// const newFunction = getUser();
// let newNumber = newFunction();

// console.log(newNumber); // 1
// newNumber = newFunction();
// console.log(newNumber); // 2

start();







