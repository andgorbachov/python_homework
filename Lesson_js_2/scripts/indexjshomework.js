
// Создайте пустой массив letters
// Создайте строку из нескольких слов, например "Backend As A Service"
// Напилите код, который разбивает эту строку на массив слов и пушит в массив letters первый символ каждого слова
// Выведите результат в консоль
// Объедините все элементы массива letters в одну строку и выведите ее в консоль

let letters = [];
let string = 'Backend As A Service';
let words = string.split(' ');

function getLetter (str){
	letters.push(str.slice(0,1))
}

words.forEach(getLetter);
console.log(letters);
console.log(letters.join(''));


//----------------------------------------------------------------------------------------------------------------
// Объявите функцию с одним формальным параметром, которая проверяет тип данных переданного аргумента и:
// если это число, возвращает текущую дату в формате "20.02.2019, 13:21:51"
// в противном случае возвращает строку "Неверный тип данных"
// Вызовите функцию

function getDate (item){
	if (typeof item === 'number'){
		var today = new Date();
		let date = ("00" + today.getDate()).slice(-2) + "." +
		  ("00" + today.getMonth() + 1).slice(-2) + "." +
		  today.getFullYear() + ", " +
		  ("00" + today.getHours()).slice(-2) + ":" +
		  ("00" + today.getMinutes()).slice(-2) + ":" +
		  ("00" + today.getSeconds()).slice(-2);
		console.log(date);
	}
}
getDate(5);

//----------------------------------------------------------------------------------------------------------------
// Обязательная часть ( 3 балла )
// Объявите функцию без формальных параметров, которая выводит в консоль сама себя и все переданные ей аргументы
// Вызовите эту функцию с аргументами 10, false, "google"

function printSelf() {
	console.log(printSelf.name);
	let args = [...arguments];
	args.forEach(console.log);
}

printSelf(10, false, "google");

//----------------------------------------------------------------------------------------------------------------
// Дополнительно ( 4 балла )
// Объявите функцию userInfo, которая выводит в консоль сообщение:
// "Дата регистрации: " + свойство data контекста вызова, если свойство registered имеет значение true
// "Незарегистрированный пользователь: " + свойство name в противном случае
// ( используйте переменные в литералах )
// Создайте два объекта с одинаковым набором свойств:
// name ( строка )
// registered ( логическое значение )
// data ( дата в формате "дд.мм.гг" )
// Добавьте каждому объекту метод getInfo, который будет ссылкой на функцию userInfo
// Вызовите каждый метод

let object1 = {
	name: "Andrii",
	registered: true,
	date: "22.01.2021",
	getInfo: userInfo,
}

let object2 = {
	name: "Roman",
	registered: false,
	date: "22.01.2021",
	getInfo: userInfo,
}

function userInfo (){	
	this.registered 
	? console.log('Дата регистрации: ' + this.date) 
	: console.log('Незарегистрированный пользователь: ' + this.name);
}

object1.getInfo();
object2.getInfo();

//----------------------------------------------------------------------------------------------------------------
// Дополнительно ( 5 баллов )
// Есть три объекта: users, posts и comments
// ( готовые объекты уже ждут вас по ссылке )
// Написать код функции getPostComments ( postId ),
// которая возвращает массив всех комментариев к посту
// с идентификатором postId
// ( с именем автора комментария и текстом комментария )
// Result:

var users = {
        14587: {
                name: "Ivan",
                email: "ivan78@gmail.com"
        },
        28419: {
                name: "Georg",
                email: "georg.klep@gmail.com"
        },
        41457: {
                name: "Stephan",
                email: "stephan.borg@gmail.com"
        }
}
var posts = {
        7891451: {
                author: 14587,
                text: "Imagine we can encapsulate these secondary responsibilities in functions"
        },
        7891452: {
                author: 28419,
                text: `В конструкторе ключевое слово super используется как функция, вызывающая родительский конструктор. 
                        Её необходимо вызвать до первого обращения к ключевому слову this в теле конструктора. 
                        Ключевое слово super также может быть использовано для вызова функций родительского объекта`
        },
        7891453: {
                author: 28419,
                text: `DOM не обрабатывает или не вынуждает проверять пространство имен как таковое. 
                        Префикс пространства имен, когда он связан с конкретным узлом, не может быть изменен`
        },
        7891454: {
                author: 14587,
                text: "Ключевое слово super используется для вызова функций, принадлежащих родителю объекта"
        }
}
var comments = {
        91078454: {
                postId: 7891451,
                author: 28419,
                text: `The static String.fromCharCode() method returns a string created 
                        from the specified sequence of UTF-16 code units`
        },
        91078455: {
                postId: 7891451,
                author: 41457,
                text: `HTML элемент <template> — это механизм для отложенного рендера клиентского контента, 
                        который не отображается во время загрузки, но может быть инициализирован при помощи JavaScript`
        },
        91078457: {
                postId: 7891452,
                author: 41457,
                text: "Глобальный объект String является конструктором строк, или, последовательностей символов"
        },
        91078458: {
                postId: 7891452,
                author: 14587,
                text: `The Element.namespaceURI read-only property returns the namespace URI of the element, 
                        or null if the element is not in a namespace`
        }
}

function getCurrentPostComments ( postId ) {
        var res = []
        let authorOutput = 'author check';
        let textOutput = 'check';
        for (const [key, value] of Object.entries(comments)) {
        	
			if (value.postId === postId) {
				for (const [kUser, vUser] of Object.entries(users)){
					if (kUser === String(value.author)){
						authorOutput = vUser.name
						textOutput = value.text
						break					
					}					
				};
				res.push(
				{
					author: authorOutput,
					text: textOutput,
				});
			}
		};
        return res
}

console.log ( getCurrentPostComments ( 7891451 ) )








