

// Нарисуйте блок-схему алгоритма, который проверяет значение входного параметра x, и если это значение больше или равно 0, то возвращает в качестве результата строку "Число положительное", в противном случае - строку "Число отрицательное"
console.log("Task #1.");
let x = 15;
if (x >= 0) {
	console.log("The number is positive.")
} else {
	console.log("The number is negative.")
};

x = -3;
if (x >= 0) {
	console.log("The number is positive.")
} else {
	console.log("The number is negative.")
};



// Нарисуте блок-схему алгоритма суммирования 10 чисел, кратных 5 ( начиная с 0 )
console.log("Task #2.");
let number = 500;
let sum = 0;
let counter = 0;

for (let i = 0; i <= number; i++) {
	if (i % 5 == 0 & counter <= 10) {
		sum += i;
		counter++;
	}
}

console.log(sum);


// Напилите кодец, который работает с массивом произвольных целых чисел
// var numbers = [ 254, 115, 78, 25, 91, 45, 37 ]
// Ваш скрипт должен вывести в консоль все числа больше 50
// Посказка: используйте оператор цикла и условный оператор

console.log("Task #3.");
var numbers = [ 254, 115, 78, 25, 91, 45, 37 ];
for (let i = 0; i <= numbers.length; i++) {
	if (numbers[i] > 50) {
		console.log(numbers[i])
	}
};



