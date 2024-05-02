# 0x15. JavaScript - Web jQuery

## Front-end

## JavaScript

## Concepts

- For this project, we expect you to look at these concepts:

	- [JavaScript in the browser](#javascript-in-the-browser)
	- [Dealing with data statically versus dynamically](#dealing-with-data-statically-versus-dynamically)

![JQUERRY](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/305/4724718.jpg)

## Resources

- Read or watch:

- [What is JavaScript?](#what-is-javascript)
- [Selector](#selector)
- [Get and set content](#get-and-set-content)
- [Manipulate CSS classes](#manipulate-css-classes)
- [Manipulate DOM elements](#manipulate-dom-elements)
- [API](#api)
- [Introduction](#introduction)
- [GET & POST request](#get-&-post-request)
- [JQuery Ajax Tutorial](#jquery-ajax-tutorial)
- [What went wrong? Troubleshooting JavaScript](#what-went-wrong?-troubleshooting-javascript)
- [JQuery](#jquery)
- [JQuery API](#jquery-api)
- [JQuery Ajax](#jquery-ajax)

## Requirements

## General

- Allowed editors: vi, vim, emacs
- All your files will be interpreted on Chrome (version 57.0)
- All your files should end with a new line
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should be semistandard compliant with the flag --global $: semistandard *.js --global $
- You must use JQuery version 3.x
- You are not allowed to use var
- HTML should not reload for each action: DOM manipulation, update values, fetch data…

## More Info

## Import JQuery

<head>

    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>

</head>


![GETTRR](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/305/1f1ihd.jpg)

## TASKS

## 0. No JQuery

mandatory

Write a JavaScript script that updates the text color of the <header> element to red (#FF0000):

- You must use document.querySelector to select the HTML tag
- You can’t use the JQuery API

## 1. With JQuery

mandatory

Write a JavaScript script that updates the text color of the <header> element to red (#FF0000):

- You can’t use document.querySelector to select the HTML tag
- You must use the JQuery API

## 2. Click and turn red

mandatory

Write a JavaScript script that updates the text color of the <header> element to red (#FF0000) when the user clicks on the tag DIV#red_header:

- You can’t use document.querySelector to select the HTML tag
- You must use the JQuery API

## 3. Add `.red` class

mandatory

Write a JavaScript script that adds the class red to the <header> element when the user clicks on the tag DIV#red_header

- You can’t use document.querySelector to select the HTML tag
- You must use the JQuery API

## 4. Toggle classes

mandatory

Write a JavaScript script that toggles the class of the <header> element when the user clicks on the tag DIV#toggle_header:

- The <header> element must always have one class: red or green, never both in the same time and never empty.
- If the current class is red, when the user click on DIV#toggle_header, the class must be updated to green ; and the reverse.
- You can’t use document.querySelector to select the HTML tag
- You must use the JQuery API

## 5. List of elements

mandatory

Write a JavaScript script that adds a <li> element to a list when the user clicks on the tag DIV#add_item:

- The new element must be: <li>Item</li>
- The new element must be added to UL.my_list
- You can’t use document.querySelector to select the HTML tag
- You must use the JQuery API

## 6. Change the text

mandatory

Write a JavaScript script that updates the text of the <header> element to New Header!!! when the user clicks on DIV#update_header

- You can’t use document.querySelector to select the HTML tag
- You must use the JQuery API

## 7. Star wars character

mandatory

Write a JavaScript script that fetches the character name from this URL: https://swapi-api.alx-tools.com/api/people/5/?format=json

- The name must be displayed in the HTML tag DIV#character
- You can’t use document.querySelector to select the HTML tag
- You must use the JQuery API

## 8. Star Wars movies

mandatory

Write a JavaScript script that fetches and lists the title for all movies by using this URL: https://swapi-api.alx-tools.com/api/films/?format=json

- All movie titles must be list in the HTML tag UL#list_movies
- You can’t use document.querySelector to select the HTML tag
- You must use the JQuery API

## 9. Say Hello!

mandatory

Write a JavaScript script that fetches from https://hellosalut.stefanbohacek.dev/?lang=fr and displays the value of hello from that fetch in the HTML tag DIV#hello.

- The translation of “hello” must be displayed in the HTML tag DIV#hello
- You can’t use document.querySelector to select the HTML tag
- You must use the JQuery API
- Your script must work when it is imported from the <head> tag

## 10. No jQuery - document loaded


Write a JavaScript script that updates the text color of the <header> element to red (#FF0000):

- You must use document.querySelector to select the HTML tag
- You can’t use the jQuery API
- Note: Your script must be imported from the <head> tag, not at the end of the HTML

## 11. List, add, remove

Write a JavaScript script that adds, removes and clears LI elements from a list when the user clicks:

- The new element must be: <li>Item</li>
- The new element must be added to UL.my_list
- When the user clicks on DIV#add_item: a new element is added to the list
- When the user clicks on DIV#remove_item: the last element is removed from the list
- When the user clicks on DIV#clear_list: all elements of the list are removed
- You can’t use document.querySelector to select the HTML tag
- You must use the JQuery API
- You script must work when it imported from the HEAD tag

## 12. Say hello to everybody!

Write a JavaScript script that fetches and prints how to say “Hello” depending on the language

- You should use this API service: https://www.fourtonfish.com/hellosalut/hello/
- The language code will be the value entered in the tag INPUT#language_code (ex: es, fr, en etc.)
- The translation must be fetched when the user clicks on INPUT#btn_translate
- The translation of “Hello” must be displayed in the HTML tag DIV#hello
- You can’t use document.querySelector to select the HTML tag
- You must use the JQuery API
- You script must work when imported from the <head> tag12. Say hello to everybody!

## 13. And press ENTER

Write a JavaScript script that fetches and prints how to say “Hello” depending on the language

- You should use this API service: https://www.fourtonfish.com/hellosalut/hello/
- The language code will be the value entered in the tag INPUT#language_code (ex: es, fr, en etc.)
- The translation must be fetched when the user clicks on INPUT#btn_translate OR presses ENTER when the focus is on INPUT#language_code
- The translation of “Hello” must be displayed in the HTML tag DIV#hello
- You can’t use document.querySelector to select the HTML tag
- You must use the JQuery API
- You script must work when imported from the <head> tag

